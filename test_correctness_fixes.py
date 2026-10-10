import ast
import asyncio
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
from types import ModuleType
import unittest
from unittest.mock import patch

from developer_docs import call_template, collect_apis, caller_parameters, write_api_page
from package_discovery import main, runtime_object, static_api, fence
import test_package_discovery as helpers


SOURCE = '''
def configure(self, cls):
    return self + cls

async def fetch(value):
    return value + 1

class Client:
    def __init__(receiver, value=1):
        receiver.value = value

    def run(receiver, cls):
        return receiver.value + cls

    async def fetch(receiver, value):
        return receiver.value + value

    @classmethod
    async def create(owner, value):
        return value + 2

    @staticmethod
    async def static_fetch(self, cls):
        return self + cls
'''


class TemplateExecutionTests(unittest.TestCase):
    def setUp(self):
        self.module = ModuleType('binding_fixture')
        exec(SOURCE, self.module.__dict__)
        self.patch = patch.dict(sys.modules, {'binding_fixture': self.module})
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def rows(self, runtime):
        module = {'module': 'binding_fixture', 'source': 'binding_fixture.py', 'exports': None}
        if runtime:
            members = [runtime_object(name, value) for name, value in vars(self.module).items() if not name.startswith('_')]
            return collect_apis({'modules': [], 'runtime_modules': [dict(module, members=members)]})
        return collect_apis({'modules': [dict(module, members=static_api(ast.parse(SOURCE)))]})

    def execute(self, item, values, expected):
        template = call_template(item)
        for name, value in values.items():
            template = template.replace(f'{name} = ...', f'{name} = {value}')
        template = template.replace('instance = ...', 'instance = m.Client(10)')
        ast.parse(template)
        namespace = {}
        with contextlib.redirect_stdout(io.StringIO()):
            exec(template, namespace)
        if item['kind'] == 'async function':
            self.assertIn('await ', template)
            result = asyncio.run(namespace['practice']())
        else:
            result = namespace['result']
        self.assertEqual(result, expected)

    def test_source_and_runtime_templates_execute(self):
        scenarios = [('configure', {'self': '2', 'cls': '3'}, 5),
                     ('fetch', {'value': '3'}, 4),
                     ('Client.run', {'cls': '4'}, 14),
                     ('Client.fetch', {'value': '4'}, 14),
                     ('Client.create', {'value': '4'}, 6),
                     ('Client.static_fetch', {'self': '2', 'cls': '3'}, 5)]
        for runtime in (False, True):
            rows = {r['path']: r for r in self.rows(runtime)}
            for name, values, expected in scenarios:
                with self.subTest(runtime=runtime, api=name):
                    self.execute(rows[name], values, expected)

    def test_input_tables_preserve_ordinary_parameters(self):
        rows = {r['path']: r for r in self.rows(True)}
        for name in ('configure', 'Client.static_fetch'):
            with self.subTest(api=name):
                self.assertEqual([p['name'] for p in caller_parameters(rows[name])], ['self', 'cls'])
                page = write_api_page(rows[name], fence)
                self.assertIn('| self |', page)
                self.assertIn('| cls |', page)
        self.assertEqual([p['name'] for p in caller_parameters(rows['Client.run'])], ['cls'])
        self.assertEqual([p['name'] for p in caller_parameters(rows['Client.create'])], ['value'])

    def test_constructor_receiver_removed_by_position(self):
        rows = {r['path']: r for r in self.rows(False)}
        self.assertEqual([p['name'] for p in rows['Client']['parameters']], ['value'])
        self.assertEqual(rows['Client']['signature'], 'Client(value=1)')


class StandardLibraryCoverageTests(unittest.TestCase):
    def test_delegated_modules_and_dotted_alias(self):
        targets = {'decimal': ['decimal.Decimal'], 'datetime': ['datetime.datetime', 'datetime.date'],
                   'os.path': ['os.path.join', 'os.path.basename']}
        for name, expected in targets.items():
            with self.subTest(module=name), tempfile.TemporaryDirectory() as temp:
                with patch('sys.argv', ['package_discovery.py', name, '--output', temp]), patch('package_discovery.install_and_run') as install, contextlib.redirect_stdout(io.StringIO()):
                    main()
                    install.assert_not_called()
                output = next(Path(temp).glob(f'{name}-python-*'))
                report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
                self.assertEqual(report['errors'], [])
                self.assertTrue(report['runtime_modules'])
                self.assertIn('automatic_runtime_reason', report)
                index = json.loads((output / 'api_index.json').read_text(encoding='utf-8'))
                names = {r['qualified'] for r in index}
                for api in expected:
                    self.assertIn(api, names)
                helpers.IntegrationTests().check_markdown(output)
                if name == 'os.path':
                    item = next(r for r in index if r['qualified'] == 'os.path.basename')
                    from developer_docs import inspection_code
                    code = inspection_code({'module': 'os.path', 'path': 'basename'})
                    with contextlib.redirect_stdout(io.StringIO()):
                        exec(code, {})


if __name__ == '__main__':
    unittest.main()
