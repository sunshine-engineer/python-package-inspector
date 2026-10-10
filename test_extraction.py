import ast
import unittest

from developer_docs import collect_apis, examples_from_doc, write_api_page, doc_details, write_developer_docs
from package_discovery import static_api, fence


class ExampleExtractionTests(unittest.TestCase):
    def test_indented_fence_preserves_setup_nested_code_and_output_comments(self):
        examples = examples_from_doc('''Example:
    ```python
    from typing import TypedDict

    def increment(value):
        return value + 1

    result = increment(2)
    # Expected: 3
    ```
''')
        self.assertEqual(len(examples), 1)
        code = examples[0]['code']
        ast.parse(code)
        namespace = {}
        exec(code, namespace)
        self.assertEqual(namespace['result'], 3)
        self.assertIn('    return value + 1', code)
        self.assertIn('# Expected: 3', code)
        self.assertEqual(examples[0]['expected'], '')

    def test_mixed_formats_are_ordered_and_doctest_fence_not_duplicated(self):
        doc = '''>>> first = 1

```pycon
>>> first + 1
2
```

~~~py
last = 3
~~~
'''
        examples = examples_from_doc(doc)
        self.assertEqual(len(examples), 3)
        self.assertEqual(examples[0]['code'], 'first = 1')
        self.assertEqual(examples[1]['expected'], '2')
        self.assertEqual(examples[2]['code'], 'last = 3')

    def test_nonpython_and_unclosed_fences_are_not_examples(self):
        self.assertEqual(examples_from_doc('```bash\n>>> not_python\n```'), [])
        self.assertEqual(examples_from_doc('```python\nnot_closed = True'), [])

    def test_longer_fence_and_invalid_python_are_preserved(self):
        doc = '````python title="snippet"\ntext = "```"\n````\n\n```python\nawait action()\n```'
        examples = examples_from_doc(doc)
        self.assertEqual(len(examples), 2)
        self.assertIn('text = "```"', examples[0]['code'])
        self.assertEqual(examples[1]['code'], 'await action()')


class OverloadExtractionTests(unittest.TestCase):
    def test_implementation_docs_and_signature_are_used_for_reexports(self):
        tree = ast.parse('''
@overload
def fetch(value: int) -> int: ...
@typing.overload
def fetch(value: str) -> str: ...
def fetch(value, *, option=True):
    """Documented implementation."""
    return value
''')
        members = static_api(tree)
        report = {'modules': [
            {'module': 'demo.core', 'source': 'demo/core.py', 'members': members},
            {'module': 'demo', 'source': 'demo/__init__.py', 'members': [
                {'name': 'from .core import fetch', 'kind': 'import', 'from_module': 'core', 'level': 1,
                 'bindings': [{'local': 'fetch', 'imported': 'fetch'}]}]}]}
        rows = collect_apis(report)
        for item in rows:
            self.assertEqual(item['docstring'], 'Documented implementation.')
            self.assertIn('option=True', item['signature'])
            self.assertEqual(len(item['overload_signatures']), 2)
            self.assertFalse(item['overload_only'])
            self.assertIn('Type overloads', write_api_page(item, fence))
        self.assertEqual(len(members), 3)

    def test_class_overloads_and_overload_only_stubs(self):
        tree = ast.parse('''
class Client:
    @overload
    def run(receiver, value: int): ...
    def run(receiver, value):
        """Run with a value."""
        return value
@overload
def unavailable(value: int): ...
''')
        rows = collect_apis({'modules': [{'module': 'demo', 'members': static_api(tree)}]})
        method = next(r for r in rows if r['path'] == 'Client.run')
        self.assertEqual(method['docstring'], 'Run with a value.')
        self.assertEqual(method['binding'], 'instance')
        stub = next(r for r in rows if r['path'] == 'unavailable')
        self.assertTrue(stub['overload_only'])
        self.assertIn('runtime implementation remains unresolved', write_api_page(stub, fence))


if __name__ == '__main__':
    unittest.main()


class DeveloperWorkflowTests(unittest.TestCase):
    def test_google_sections_stop_at_unindented_narrative(self):
        doc = "Raises:\n    AssertionError: Duplicate middleware.\n        Continuation.\n\nThe agent calls the model.\n"
        self.assertEqual(doc_details(doc)['raises'], ['AssertionError: Duplicate middleware.', 'Continuation.'])
        self.assertEqual(doc_details('Returns:\n    A result.\n\nNarrative.')['returns'], ['A result.'])

    def test_sphinx_continuation_and_numpy_remain_supported(self):
        self.assertEqual(doc_details(':raises ValueError: Bad input.\n    Details.\nNarrative.')['raises'], ['ValueError: Bad input.', 'Details.'])
        self.assertEqual(doc_details('Returns\n-------\nint\n    A count.\nNotes\n-----\nOther.')['returns'], ['int', 'A count.'])

    def test_doctest_sessions_keep_shared_state_and_separate_prose(self):
        doc = '>>> value = 2\n>>> result = value + 1\n>>> result\n3\n\nA separate example:\n>>> other = 5\n>>> other\n5\n'
        examples = examples_from_doc(doc)
        self.assertEqual(len(examples), 2)
        self.assertEqual(examples[0]['command_count'], 3)
        namespace = {}
        exec(examples[0]['code'], namespace)
        self.assertEqual(namespace['result'], 3)
        self.assertEqual(examples[0]['expected'], '3')
        self.assertNotIn('other', examples[0]['code'])

    def test_tasks_and_missing_environment_rendered(self):
        import tempfile
        from pathlib import Path
        from test_official_docs import report
        from test_package_discovery import IntegrationTests
        data = report()
        data['package'] = 'langgraph'
        data['executable'] = '/nonexistent/inspection/python.exe'
        data['official_docs_options']['enabled'] = False
        data['modules'] = [{'module': 'langgraph.graph', 'members': [{'name': 'StateGraph', 'kind': 'class', 'members': [], 'docstring': 'Build a graph.'}]}]
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            (out / 'README.md').write_text('# Raw')
            write_developer_docs(out, data, fence)
            quick = (out / 'QUICKSTART.md').read_text(encoding='utf-8')
            self.assertIn('Define graph state', quick)
            self.assertIn("'StateGraph'", quick)
            self.assertIn('no longer available', (out / 'README.md').read_text(encoding='utf-8'))
            IntegrationTests().check_markdown(out)

    def test_crawl_tasks_precede_private_routes(self):
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from test_official_docs import report
        from official_docs import enrich_apis
        data = report()
        data['package'] = 'langchain'
        rows = [{'qualified': 'langchain.agents.create_agent', 'alias_of': 'langchain.agents.factory.create_agent'}]
        root = '<a href="/python/langchain/_internal/noise">noise</a><a href="/python/langchain/agents/factory/create_agent">agent</a><a href="/python/langchain/other/Other">other</a>'
        with tempfile.TemporaryDirectory() as temp, patch('official_docs.fetch_html', return_value=root) as fetch:
            log = enrich_apis(rows, data, Path(temp), {'max_pages': 2}, doc_details, examples_from_doc)
            self.assertTrue(fetch.call_args_list[1].args[0].endswith('/agents/factory/create_agent'))
            self.assertEqual(len(log['pages']), 2)

    def test_crawl_cached_pages_do_not_displace_core_tasks(self):
        from official_docs import reference_priority
        rows = [{'qualified': 'langgraph.graph.StateGraph', 'alias_of': 'langgraph.graph.state.StateGraph'},
                {'qualified': 'langgraph.channels.BaseChannel', 'alias_of': 'langgraph.channels.base.BaseChannel'}]
        links = ['https://reference.langchain.com/python/langgraph/_internal/_config/ensure_config',
                 'https://reference.langchain.com/python/langgraph/channels/base/BaseChannel',
                 'https://reference.langchain.com/python/langgraph/graph/state/StateGraph']
        ordered = sorted(links, key=lambda url: reference_priority(url, rows, 'langgraph'))
        self.assertTrue(ordered[0].endswith('/graph/state/StateGraph'))
        self.assertIn('_internal', ordered[-1])

    def test_existing_interpreter_is_reported_available(self):
        import tempfile
        import sys
        from pathlib import Path
        from test_official_docs import report
        data = report()
        data['official_docs_options']['enabled'] = False
        data['executable'] = sys.executable
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            (out / 'README.md').write_text('# Raw')
            write_developer_docs(out, data, fence)
            self.assertIn('inspection interpreter is available', (out / 'README.md').read_text(encoding='utf-8'))

    def test_class_alias_methods_and_chained_aliases_resolve_to_source(self):
        tree = ast.parse('class Graph:\n    def run(self):\n        """Run a graph."""\n        pass\n')
        imports = lambda source, symbol: [{'name': 'import', 'kind': 'import', 'from_module': source, 'level': 0, 'bindings': [{'local': symbol, 'imported': symbol}]}]
        rows = collect_apis({'modules': [{'module': 'demo.impl', 'members': static_api(tree)},
                              {'module': 'demo.middle', 'members': imports('demo.impl', 'Graph')},
                              {'module': 'demo', 'members': imports('demo.middle', 'Graph')}]})
        method = next(r for r in rows if r['qualified'] == 'demo.Graph.run')
        self.assertEqual(method['alias_of'], 'demo.impl.Graph.run')


class PracticeReadinessTests(unittest.TestCase):
    def test_setup_copy_executes_without_earlier_session(self):
        from developer_docs import setup_complete_examples
        examples = examples_from_doc('>>> import math\n>>> scale = 2\n\nNow calculate:\n>>> result = math.sqrt(9) * scale\n>>> result\n6.0\n')
        copies = setup_complete_examples(examples)
        namespace = {}
        exec(copies[1]['with_setup'], namespace)
        self.assertEqual(namespace['result'], 6.0)
        self.assertEqual(copies[1]['unresolved_names'], [])
        self.assertNotIn('import math', copies[1]['code'])

    def test_setup_does_not_use_unrelated_function_locals(self):
        from developer_docs import setup_complete_examples
        copies = setup_complete_examples(examples_from_doc('>>> def unrelated():\n...     value = 5\n...     return value\n\nOther example:\n>>> value + 1\n'))
        self.assertNotIn('with_setup', copies[1])
        self.assertIn('value', copies[1]['unresolved_names'])

    def test_prerequisites_use_source_evidence(self):
        from developer_docs import practice_prerequisites
        notes = '\n'.join(practice_prerequisites({'docstring': 'Set LANGSMITH_TRACING_V2.', 'practice_requirements': ['langchain-core>=1.0']}, [{'code': 'from langchain_core.messages import HumanMessage\nmodel = "anthropic:demo"'}]))
        self.assertIn('LANGSMITH_TRACING_V2', notes)
        self.assertIn('langchain-core>=1.0', notes)
        self.assertIn('anthropic', notes)
        self.assertNotIn('ANTHROPIC_API_KEY', notes)

    def test_graph_navigation_and_generated_encoding(self):
        from developer_docs import task_rows
        rows = [{'qualified': 'langgraph.pregel.Pregel.invoke'}, {'qualified': 'langgraph.pregel.Pregel.stream'}]
        labels = [label for label, _ in task_rows('langgraph', rows)]
        self.assertIn('Run the compiled graph', labels)
        self.assertIn('Stream graph results', labels)
        source = __import__('pathlib').Path(__import__('developer_docs').__file__).read_text(encoding='utf-8')
        self.assertNotIn(chr(194) + chr(183), source)
        self.assertNotIn(chr(226) + chr(8364) + chr(8221), source)

    def test_setup_recovers_read_before_reassignment(self):
        from developer_docs import setup_complete_examples
        copies = setup_complete_examples(examples_from_doc('>>> value = 2\n\nNext step:\n>>> value = value + 1\n'))
        namespace = {}
        exec(copies[1]['with_setup'], namespace)
        self.assertEqual(namespace['value'], 3)
