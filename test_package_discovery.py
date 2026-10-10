"""Offline unit checks for source fidelity and Markdown safety."""
import ast
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace
from developer_docs import call_template, collect_apis, doc_details, examples_from_doc, inspection_code, write_api_page

from package_discovery import create_output, fence, install_and_run, module_name, remove_created_environment, static_api
from package_discovery import main


class StandardLibraryTests(unittest.TestCase):
    def test_json_skips_installation_and_creates_useful_docs(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch('package_discovery.sys.argv', ['package_discovery.py', 'json', '--output', temp]), patch('package_discovery.install_and_run') as install:
                main()
                install.assert_not_called()
            output = next(Path(temp).glob('json-python-*'))
            report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
            self.assertEqual(report['package_type'], 'standard-library')
            self.assertEqual(report['version_selection'], 'python-interpreter')
            self.assertEqual(report['errors'], [])
            self.assertFalse((Path(temp) / '.venvs').exists())
            names = [r['qualified'] for r in json.loads((output / 'api_index.json').read_text(encoding='utf-8'))]
            self.assertIn('json.dumps', names)
            self.assertIn('json.loads', names)
            self.assertNotIn('pip install', (output / 'QUICKSTART.md').read_text(encoding='utf-8'))
            self.assertNotIn('metadata.distribution', (output / 'REFERENCE.md').read_text(encoding='utf-8'))
            IntegrationTests().check_markdown(output)

    def test_builtin_math_runtime_without_installation(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch('package_discovery.sys.argv', ['package_discovery.py', 'math', '--output', temp]), patch('package_discovery.install_and_run') as install:
                main()
                install.assert_not_called()
            output = next(Path(temp).glob('math-python-*'))
            report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
            self.assertEqual(report['errors'], [])
            self.assertTrue(report['runtime_modules'])
            names = [r['qualified'] for r in json.loads((output / 'api_index.json').read_text(encoding='utf-8'))]
            self.assertIn('math.sqrt', names)
            IntegrationTests().check_markdown(output)

    def test_standard_library_version_rejected_before_output(self):
        with tempfile.TemporaryDirectory() as temp, patch('package_discovery.sys.argv', ['package_discovery.py', 'json', '1.0', '--output', temp]):
            with self.assertRaises(SystemExit) as exc:
                main()
            self.assertEqual(exc.exception.code, 2)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_standard_library_cleanup_flag_does_not_delete_environment(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch('package_discovery.sys.argv', ['package_discovery.py', 'json.decoder', '--cleanup-venv', '--output', temp]), patch('package_discovery.remove_created_environment') as cleanup:
                main()
                cleanup.assert_not_called()
            output = next(Path(temp).glob('json.decoder-python-*'))
            IntegrationTests().check_markdown(output)


class DiscoveryTests(unittest.TestCase):
    def test_signature_and_class_members(self):
        tree = ast.parse('''
class Example(Base):
    """Class documentation."""
    @property
    def value(self) -> int:
        """Property documentation."""
        return 1

async def query(x: int, /, y="a", *, limit: int = 2) -> str:
    """Query documentation."""
    return y
''')
        items = static_api(tree)
        self.assertEqual(items[0]['bases'], ['Base'])
        self.assertEqual(items[0]['members'][0]['decorators'], ['property'])
        self.assertEqual(items[1]['docstring'], 'Query documentation.')
        signature = items[1]['signature']
        self.assertIn('x: int, /', signature)
        self.assertIn('*,limit:int=2', signature.replace(' ', ''))
        self.assertTrue(signature.endswith(' -> str'))

    def test_distribution_paths(self):
        self.assertEqual(module_name('foo/__init__.py'), 'foo')
        self.assertEqual(module_name('foo/core.pyi'), 'foo.core')
        self.assertEqual(module_name('foo/native.cp310-win_amd64.pyd'), 'foo.native')
        self.assertIsNone(module_name('foo-1.0.dist-info/METADATA'))
        self.assertIsNone(module_name('../bin/script.py'))

    def test_conditional_definitions_are_labeled(self):
        items = static_api(ast.parse('if True:\n    def available():\n        pass\n'))
        self.assertTrue(items[0]['conditional'])

    def test_embedded_fences_are_preserved(self):
        rendered = fence('example\n```python\npass\n```')
        self.assertTrue(rendered.startswith('````text\n'))
        self.assertTrue(rendered.endswith('````\n'))


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.site = self.root / 'site'
        package = self.site / 'discovery_fixture'
        package.mkdir(parents=True)
        (package / '__init__.py').write_text('''"""Fixture module: café and ``` fences."""
from pathlib import Path
Path(__file__).with_name('imported.marker').write_text('imported')
def query(x: int, /, *, limit: int = 2) -> str:
    """Return documented results.

    Args:
        x (int): Number to convert to text.
        limit (int): Optional result limit.

    Returns:
        str: Text representing x.

    Examples:
        >>> from discovery_fixture import query
        >>> query(2)
        '2'
    """
    return str(x)
class Client:
    """A documented client."""
    @property
    def value(self) -> int:
        """Property docs."""
        return 1
''', encoding='utf-8')
        (package / 'broken.py').write_text("raise ImportError('optional dependency absent')\n", encoding='utf-8')
        (package / 'guide.md').write_text('# Guide\n```python\nquery(1)\n```\n', encoding='utf-8')
        info = self.site / 'discovery_fixture-1.0.dist-info'
        info.mkdir()
        (info / 'METADATA').write_text('Metadata-Version: 2.1\nName: discovery-fixture\nVersion: 1.0\nSummary: Local fixture\nRequires-Dist: optional-dep; extra == "test"\n\nFixture description.\n', encoding='utf-8')
        (info / 'entry_points.txt').write_text('[console_scripts]\nfixture = discovery_fixture:query\n', encoding='utf-8')
        (info / 'RECORD').write_text('\n'.join(f'{p.relative_to(self.site).as_posix()},,' for p in self.site.rglob('*') if p.is_file()) + '\ndiscovery_fixture-1.0.dist-info/RECORD,,\n', encoding='utf-8')
        self.env = dict(os.environ, PYTHONPATH=str(self.site), PYTHONIOENCODING='utf-8')
        self.script = Path(__file__).with_name('package_discovery.py')

    def run_cli(self, *extra, version='1.0', name='discovery-fixture'):
        versions = [version] if version is not None else []
        return subprocess.run([sys.executable, str(self.script), name, *versions, '--installed', '--output', str(self.root / 'output'), *extra], env=self.env, capture_output=True, text=True, encoding='utf-8', timeout=30)

    def test_omitted_version_uses_installed_version_offline(self):
        result = self.run_cli(version=None)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Resolved package: discovery-fixture==1.0', result.stdout)
        output = self.root / 'output' / 'discovery-fixture-1.0'
        report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
        self.assertEqual(report['version'], '1.0')
        self.assertIsNone(report['requested_version'])
        self.assertEqual(report['version_selection'], 'installed')
        self.assertFalse((self.root / 'output' / '.venvs').exists())
        self.check_markdown(output)

    def test_default_output_and_repeat(self):
        command = [sys.executable, str(self.script), 'discovery-fixture', '1.0', '--installed']
        for suffix in ('', '-2'):
            result = subprocess.run(command, cwd=self.root, env=self.env, capture_output=True, text=True, encoding='utf-8', timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            output = self.root / 'package_docs' / f'discovery-fixture-1.0{suffix}'
            self.assertTrue((output / 'README.md').is_file())
            self.check_markdown(output)

    def test_invalid_requirement_rejected_before_setup(self):
        for name, version in [('https://example.com/pkg.whl', '1.0'), ('valid', '>=1'), ('valid', '1.*')]:
            with self.subTest(name=name, version=version):
                self.assertEqual(self.run_cli(name=name, version=version).returncode, 2)
        self.assertFalse((self.root / 'output').exists())

    def test_cleanup_with_installed_rejected(self):
        result = self.run_cli('--cleanup-venv')
        self.assertEqual(result.returncode, 2)
        self.assertIn('cannot be combined', result.stderr)

    def check_markdown(self, output):
        for page in ([output] if output.is_file() else output.rglob('*.md')):
            content = page.read_text(encoding='utf-8')
            active = None
            language = None
            body = []
            for line in content.splitlines():
                match = re.match(r'^(`{3,})(\w*)$', line)
                if active is None and match:
                    active, language, body = match[1], match[2], []
                elif active and line == active:
                    if language == 'python':
                        ast.parse('\n'.join(body))
                    if language == 'json':
                        json.loads('\n'.join(body))
                    active = None
                elif active:
                    body.append(line)
                else:
                    for link in re.findall(r'\]\(([^)]+)\)', line):
                        if '://' not in link:
                            self.assertTrue((page.parent / link).is_file(), f'Broken link: {page}: {link}')
            self.assertIsNone(active, f'Unclosed fence: {page}')

    def test_static_markdown_and_no_import(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.root / 'output' / 'discovery-fixture-1.0'
        report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
        self.assertEqual(report['errors'], [])
        self.assertEqual(report['entry_points'][0]['value'], 'discovery_fixture:query')
        self.assertIn('optional-dep', report['requirements'][0])
        self.assertEqual(len(report['modules']), 2)
        self.assertFalse((self.site / 'discovery_fixture' / 'imported.marker').exists())
        content = '\n'.join(p.read_text(encoding='utf-8') for p in (output / 'modules').glob('*.md'))
        for expected in ('Return documented results.', 'Property docs.', 'limit: int=2', 'café'):
            self.assertIn(expected, content)
        self.check_markdown(output)

    def test_developer_navigation_search_and_inputs(self):
        self.assertEqual(self.run_cli().returncode, 0)
        output = self.root / 'output' / 'discovery-fixture-1.0'
        index = json.loads((output / 'api_index.json').read_text(encoding='utf-8'))
        query = next(item for item in index if item['qualified'] == 'discovery_fixture.query')
        page = (output / query['page']).read_text(encoding='utf-8')
        self.assertIn('Number to convert to text.', page)
        self.assertIn('positional-only | Yes | int', page)
        self.assertIn('keyword-only | No | int | 2', page)
        self.assertIn('Text representing x.', page)
        self.assertIn('Expected output recorded', page)
        self.assertIn('edit before running', page)
        self.assertIn('obj = inspect.getattr_static(obj, \'query\')', page)
        self.assertLess(len((output / 'README.md').read_text(encoding='utf-8')), 6000)
        self.assertNotIn('"Metadata-Version"', (output / 'README.md').read_text(encoding='utf-8'))
        self.assertTrue((output / 'REFERENCE.md').is_file())
        result = subprocess.run([sys.executable, str(output / 'search_api.py'), 'convert'], capture_output=True, text=True, encoding='utf-8', timeout=10)
        # Search covers summary, signature and name, not full parameter descriptions.
        self.assertIn('0 matches', result.stdout)
        result = subprocess.run([sys.executable, str(output / 'search_api.py'), 'query'], capture_output=True, text=True, encoding='utf-8', timeout=10)
        self.assertIn('discovery_fixture.query', result.stdout)
        self.assertEqual(result.returncode, 0)
        self.check_markdown(output)

    def test_extracted_fixture_examples_execute(self):
        self.assertEqual(self.run_cli().returncode, 0)
        output = self.root / 'output' / 'discovery-fixture-1.0'
        report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
        module = next(m for m in report['modules'] if m['module'] == 'discovery_fixture')
        query = next(m for m in module['members'] if m['name'] == 'query')
        examples = examples_from_doc(query['docstring'])
        self.assertEqual(examples[-1]['expected'], "'2'")
        tree = ast.parse(examples[-1]['code'])
        self.assertIsInstance(tree.body[-1], ast.Expr)
        expression = ast.unparse(tree.body.pop().value)
        code = ast.unparse(tree) + '\nprint(repr(' + expression + '))'
        result = subprocess.run([sys.executable, '-c', code], env=self.env, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), examples[-1]['expected'])

    def test_exact_api_inspection_executes(self):
        code = inspection_code({'module': 'discovery_fixture', 'path': 'query'})
        result = subprocess.run([sys.executable, '-c', code], env=self.env, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('limit: int = 2', result.stdout)
        self.assertIn('Return documented results.', result.stdout)

    def test_runtime_success_and_import_failure(self):
        result = self.run_cli('--runtime')
        self.assertEqual(result.returncode, 0, result.stderr)
        output = self.root / 'output' / 'discovery-fixture-1.0'
        report = json.loads((output / 'report.json').read_text(encoding='utf-8'))
        self.assertTrue(any('optional dependency absent' in e for e in report['errors']))
        self.assertTrue((self.site / 'discovery_fixture' / 'imported.marker').exists())
        data = json.loads((output / 'runtime-00000.json').read_text(encoding='utf-8'))
        query = next(m for m in data['members'] if m['name'] == 'query')
        self.assertIn('limit: int = 2', query['signature'])
        self.check_markdown(output)

    def test_wrong_version_no_output(self):
        result = self.run_cli(version='9.9')
        self.assertEqual(result.returncode, 2)
        self.assertIn('installed 1.0', result.stderr)
        self.assertFalse((self.root / 'output').exists())

    def test_missing_package(self):
        result = self.run_cli(name='nonexistent-discovery-fixture-xyz')
        self.assertEqual(result.returncode, 2)
        self.assertIn('not installed', result.stderr)

    def test_invalid_timeout(self):
        for value in ('0', '-1', 'nan', 'inf'):
            with self.subTest(value=value):
                self.assertEqual(self.run_cli('--timeout', value).returncode, 2)

    def test_existing_output_is_preserved(self):
        self.assertEqual(self.run_cli().returncode, 0)
        page = self.root / 'output' / 'discovery-fixture-1.0' / 'README.md'
        before = page.read_bytes()
        result = self.run_cli()
        self.assertEqual(result.returncode, 2)
        self.assertIn('Output already exists', result.stderr)
        self.assertEqual(page.read_bytes(), before)

    def test_missing_file_inventory_is_reported(self):
        (self.site / 'discovery_fixture-1.0.dist-info' / 'RECORD').unlink()
        self.assertEqual(self.run_cli().returncode, 0)
        report = json.loads((self.root / 'output' / 'discovery-fixture-1.0' / 'report.json').read_text(encoding='utf-8'))
        self.assertTrue(any('inventory is unavailable' in e for e in report['errors']))

    def test_runtime_timeout_is_recorded(self):
        (self.site / 'discovery_fixture' / 'slow.py').write_text('import time\ntime.sleep(10)\n', encoding='utf-8')
        record = self.site / 'discovery_fixture-1.0.dist-info' / 'RECORD'
        with record.open('a', encoding='utf-8') as stream:
            stream.write('discovery_fixture/slow.py,,\n')
        result = self.run_cli('--runtime', '--timeout', '0.5')
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads((self.root / 'output' / 'discovery-fixture-1.0' / 'report.json').read_text(encoding='utf-8'))
        self.assertTrue(any('TimeoutExpired' in e for e in report['errors']))


class DeveloperDocsTests(unittest.TestCase):
    def test_documented_kwargs_options_are_not_lost(self):
        page = write_api_page({'qualified': 'demo.fetch', 'module': 'demo', 'path': 'fetch', 'kind': 'function', 'evidence': 'source', 'export_basis': 'name heuristic',
                               'parameters': [{'name': 'kwargs', 'kind': 'variadic keyword', 'required': False}],
                               'docstring': ':param timeout: Maximum wait in seconds.\n:param headers: Custom headers.'}, fence)
        self.assertIn('Additional inputs documented', page)
        self.assertIn('timeout | Not provided | Maximum wait', page)

    def test_public_exports_and_local_reexports(self):
        report = {'modules': [
            {'module': 'demo', 'source': 'demo/__init__.py', 'exports': ['fetch'], 'members': [
                {'name': 'from .core import fetch', 'kind': 'import', 'from_module': 'core', 'level': 1, 'bindings': [{'local': 'fetch', 'imported': 'fetch'}]},
                {'name': 'helper', 'kind': 'function', 'signature': 'helper()'}]},
            {'module': 'demo.core', 'source': 'demo/core.py', 'exports': None, 'members': [
                {'name': 'fetch', 'kind': 'function', 'signature': 'fetch(x)', 'docstring': 'Fetch a result.'},
                {'name': '_private', 'kind': 'function'}]},
            {'module': 'demo._internal', 'members': [{'name': 'hidden', 'kind': 'function'}]}
        ]}
        rows = collect_apis(report)
        names = [r['qualified'] for r in rows]
        self.assertIn('demo.fetch', names)
        self.assertNotIn('demo.helper', names)
        self.assertNotIn('demo.core._private', names)
        self.assertNotIn('demo._internal.hidden', names)
        fetch = next(r for r in rows if r['qualified'] == 'demo.fetch')
        self.assertEqual(fetch['alias_of'], 'demo.core.fetch')

    def test_google_numpy_sphinx_fields(self):
        google = doc_details('Args:\n    value (int): Input number.\nReturns:\n    str: Encoded number.\nRaises:\n    ValueError: Invalid number.')
        self.assertEqual(google['parameters']['value']['type'], 'int')
        self.assertIn('ValueError', google['raises'][0])
        numpy = doc_details('Parameters\n----------\nvalue : int\n    Input number.\nReturns\n-------\nstr\n    Encoded number.')
        self.assertEqual(numpy['parameters']['value']['type'], 'int')
        self.assertEqual(numpy['parameters']['value']['description'], 'Input number.')
        sphinx = doc_details(':param value: Input number.\n:type value: int\n:returns: Encoded number.\n:raises ValueError: Invalid number.')
        self.assertEqual(sphinx['parameters']['value']['type'], 'int')
        self.assertEqual(sphinx['returns'], ['Encoded number.'])
        stars = doc_details(':param params: Query values.\n:param \\*\\*kwargs: Extra options.\n:rtype: Response')
        self.assertEqual(stars['parameters']['kwargs']['description'], 'Extra options.')
        self.assertEqual(stars['parameters']['params']['description'], 'Query values.')

    def test_signature_based_template_argument_styles(self):
        item = {'module': 'demo', 'path': 'fetch', 'kind': 'function', 'parameters': [
            {'name': 'value', 'kind': 'positional-only', 'required': True},
            {'name': 'limit', 'kind': 'keyword-only', 'required': True},
            {'name': 'optional', 'kind': 'positional or keyword', 'required': False}]}
        template = call_template(item)
        ast.parse(template)
        self.assertIn('m.fetch(value, limit=limit)', template)
        self.assertNotIn('optional=', template)
        self.assertIn('TODO', template)


class SetupTests(unittest.TestCase):
    def test_omitted_version_installs_unpinned_with_upgrade(self):
        with tempfile.TemporaryDirectory() as temp:
            args = SimpleNamespace(package='six', version=None, output=Path(temp))
            with patch('package_discovery.venv.EnvBuilder') as builder, patch('package_discovery.subprocess.run', return_value=SimpleNamespace(returncode=0)) as run, patch('package_discovery.sys.argv', ['package_discovery.py', 'six']):
                self.assertEqual(install_and_run(args, SimpleNamespace()), 0)
                command = run.call_args_list[0].args[0]
                self.assertEqual(command[-1], 'six')
                self.assertIn('--upgrade', command)
                self.assertTrue(builder.return_value.create.call_args.args[0].name.startswith('six-latest-'))
                self.assertEqual(run.call_args_list[0].kwargs['env']['PACKAGE_DISCOVERY_VERSION_SELECTION'], 'latest-compatible')
                child = run.call_args_list[1].args[0]
                self.assertNotIn('None', child)
                self.assertEqual(child[-2:], ['six', '--installed'])
    def test_cleanup_removes_only_created_environment(self):
        with tempfile.TemporaryDirectory() as temp:
            parent = Path(temp) / '.venvs'
            target = parent / 'new'
            other = parent / 'existing'
            target.mkdir(parents=True)
            other.mkdir()
            (target / 'pyvenv.cfg').write_text('home = python')
            docs = Path(temp) / 'README.md'
            docs.write_text('Generated documentation')
            remove_created_environment(target, parent)
            self.assertFalse(target.exists())
            self.assertTrue(other.exists())
            self.assertTrue(docs.exists())

    def test_cleanup_rejects_outside_or_nonvenv_targets(self):
        with tempfile.TemporaryDirectory() as temp:
            parent = Path(temp) / '.venvs'
            parent.mkdir()
            outside = Path(temp) / 'outside'
            outside.mkdir()
            (outside / 'pyvenv.cfg').write_text('home = python')
            notvenv = parent / 'notvenv'
            notvenv.mkdir()
            for target in (outside, notvenv, parent):
                with self.subTest(target=target), self.assertRaises(ValueError):
                    remove_created_environment(target, parent)
                self.assertTrue(target.exists())

    def test_cleanup_runs_only_after_success(self):
        for generation_code in (0, 5):
            with self.subTest(generation_code=generation_code), tempfile.TemporaryDirectory() as temp:
                args = SimpleNamespace(package='six', version='1.17.0', output=Path(temp), cleanup_venv=True)
                with patch('package_discovery.venv.EnvBuilder'), patch('package_discovery.subprocess.run') as run, patch('package_discovery.remove_created_environment') as cleanup, patch('package_discovery.sys.argv', ['package_discovery.py', 'six', '1.17.0', '--cleanup-venv']):
                    run.side_effect = [SimpleNamespace(returncode=0), SimpleNamespace(returncode=generation_code)]
                    self.assertEqual(install_and_run(args, SimpleNamespace()), generation_code)
                    self.assertNotIn('--cleanup-venv', run.call_args_list[1].args[0])
                    if generation_code == 0:
                        cleanup.assert_called_once()
                    else:
                        cleanup.assert_not_called()

    def test_cleanup_failure_returns_error(self):
        with tempfile.TemporaryDirectory() as temp:
            args = SimpleNamespace(package='six', version='1.17.0', output=Path(temp), cleanup_venv=True)
            with patch('package_discovery.venv.EnvBuilder'), patch('package_discovery.subprocess.run', return_value=SimpleNamespace(returncode=0)), patch('package_discovery.remove_created_environment', side_effect=PermissionError('file locked')):
                self.assertEqual(install_and_run(args, SimpleNamespace()), 1)

    def test_default_setup_install_and_child_interpreter(self):
        with tempfile.TemporaryDirectory() as temp:
            args = SimpleNamespace(package='six', version='1.17.0', output=Path(temp) / 'nested' / 'output')
            parser = SimpleNamespace(error=lambda message: self.fail(message))
            with patch('package_discovery.venv.EnvBuilder') as builder, patch('package_discovery.subprocess.run') as run, patch('package_discovery.sys.argv', ['package_discovery.py', 'six', '1.17.0']), patch.dict(os.environ, {'PYTHONPATH': 'leak', 'PYTHONHOME': 'leak'}):
                run.side_effect = [SimpleNamespace(returncode=0), SimpleNamespace(returncode=0)]
                self.assertEqual(install_and_run(args, parser), 0)
                builder.assert_called_once_with(with_pip=True)
                environment = builder.return_value.create.call_args.args[0]
                self.assertEqual(environment.parent, args.output / '.venvs')
                install = run.call_args_list[0]
                self.assertEqual(install.args[0][-1], 'six==1.17.0')
                self.assertIn('--isolated', install.args[0])
                self.assertNotIn('PYTHONPATH', install.kwargs['env'])
                self.assertNotIn('PYTHONHOME', install.kwargs['env'])
                child = run.call_args_list[1].args[0]
                self.assertEqual(child[0], install.args[0][0])
                self.assertEqual(child[-1], '--installed')

    def test_install_failure_stops_documentation(self):
        with tempfile.TemporaryDirectory() as temp:
            args = SimpleNamespace(package='six', version='1.17.0', output=Path(temp), cleanup_venv=True)
            with patch('package_discovery.venv.EnvBuilder'), patch('package_discovery.subprocess.run', return_value=SimpleNamespace(returncode=7)) as run:
                self.assertEqual(install_and_run(args, SimpleNamespace()), 7)
                run.assert_called_once()
                self.assertFalse((Path(temp) / 'six-1.17.0').exists())

    def test_venv_failure_is_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            args = SimpleNamespace(package='six', version='1.17.0', output=Path(temp))
            with patch('package_discovery.venv.EnvBuilder') as builder, patch('package_discovery.subprocess.run') as run:
                builder.return_value.create.side_effect = OSError('creation failed')
                self.assertEqual(install_and_run(args, SimpleNamespace()), 1)
                run.assert_not_called()


if __name__ == '__main__':
    unittest.main()
