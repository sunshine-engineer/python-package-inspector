import json
from pathlib import Path
import tempfile
import sys
import unittest
from unittest.mock import patch

from developer_docs import doc_details, examples_from_doc, write_developer_docs
from official_docs import Page, api_section, documentation_source, enrich_apis, section_content, validate_url
from package_discovery import fence, main
import test_package_discovery as helpers


HTML = '''<html><body><dl class="py function"><dt id="demo.fetch">fetch(value)</dt><dd>
<p>Fetch a documented value.</p><dl class="field-list"><dt>Parameters:</dt><dd>value (int) â€“ A valid number.</dd>
<dt>Returns:</dt><dd>A converted number.</dd><dt>Raises:</dt><dd>ValueError on invalid input.</dd></dl>
<div class="highlight-python"><pre>&gt;&gt;&gt; fetch(2)
4</pre></div></dd></dl><a href="https://evil.example/api/">outside</a></body></html>'''


def report():
    return {'package': 'demo', 'version': '1.0', 'package_type': 'distribution',
            'metadata': {'Project-URL': ['Documentation, https://docs.example/api/']},
            'modules': [{'module': 'demo', 'members': [{'name': 'fetch', 'kind': 'function', 'signature': 'fetch(value)',
                                                       'parameters': [{'name': 'value', 'required': True, 'kind': 'positional or keyword'}]}]}],
            'errors': [], 'requirements': [], 'executable': 'python', 'environment': 'env', 'cleanup_requested': False,
            'official_docs_options': {'enabled': True, 'max_pages': 2, 'timeout': 1}}


class OfficialDocsTests(unittest.TestCase):
    def test_offline_requires_cache_before_installation(self):
        with patch('sys.argv', ['package_discovery.py', 'demo', '--docs-offline']), patch('package_discovery.install_and_run') as install:
            with self.assertRaises(SystemExit) as exc:
                main()
            self.assertEqual(exc.exception.code, 2)
            install.assert_not_called()

    def test_invalid_cache_path_rejected_before_installation(self):
        with tempfile.TemporaryDirectory() as temp, patch('sys.argv', ['package_discovery.py', 'demo', '--docs-cache', temp]), patch('package_discovery.install_and_run') as install:
            with self.assertRaises(SystemExit) as exc:
                main()
            self.assertEqual(exc.exception.code, 2)
            install.assert_not_called()

    def test_offline_cache_reuse_keeps_original_provenance(self):
        with tempfile.TemporaryDirectory() as temp:
            cache_run = Path(temp) / 'download'
            cache_run.mkdir()
            with patch('official_docs.fetch_html', return_value=HTML):
                first = enrich_apis([{'qualified': 'demo.fetch'}], report(), cache_run, {'max_pages': 1}, doc_details, examples_from_doc)
            second_run = Path(temp) / 'offline'
            second_run.mkdir()
            item = {'qualified': 'demo.fetch'}
            with patch('official_docs.fetch_html', side_effect=AssertionError('Network forbidden')) as fetch:
                result = enrich_apis([item], report(), second_run, {'cache': str(cache_run / 'official_docs'), 'offline': True}, doc_details, examples_from_doc)
                fetch.assert_not_called()
            self.assertEqual(result['cached_pages'], 1)
            self.assertEqual(result['fetched_pages'], 0)
            self.assertEqual(result['enriched_apis'], 1)
            self.assertEqual(result['pages'][0]['retrieved_at'], first['pages'][0]['retrieved_at'])
            self.assertTrue(item['official_documentation']['from_cache'])
            self.assertEqual(result['errors'], [])

    def test_offline_empty_cache_does_not_fetch(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / 'cache'
            cache.mkdir()
            (cache / 'retrieval.json').write_text(json.dumps({'source_url': 'https://docs.example/api/', 'pages': []}))
            output = Path(temp) / 'out'
            output.mkdir()
            with patch('official_docs.fetch_html') as fetch:
                result = enrich_apis([{'qualified': 'demo.fetch'}], report(), output, {'cache': str(cache), 'offline': True}, doc_details, examples_from_doc)
                fetch.assert_not_called()
            self.assertEqual(result['enriched_apis'], 0)
            self.assertIn('offline mode forbids', result['errors'][0]['error'])
            self.assertTrue(result['unresolved_apis'])

    def test_corrupted_cache_not_used_offline(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            with patch('official_docs.fetch_html', return_value=HTML):
                enrich_apis([{'qualified': 'demo.fetch'}], report(), base, {}, doc_details, examples_from_doc)
            next((base / 'official_docs').glob('*.html')).write_text('corrupted')
            out = base / 'new'
            out.mkdir()
            with patch('official_docs.fetch_html') as fetch:
                log = enrich_apis([{'qualified': 'demo.fetch'}], report(), out, {'cache': str(base / 'official_docs'), 'offline': True}, doc_details, examples_from_doc)
                fetch.assert_not_called()
            self.assertIn('checksum mismatch', log['errors'][0]['error'])
            self.assertEqual(log['enriched_apis'], 0)

    def test_online_cache_miss_fetches_page(self):
        with tempfile.TemporaryDirectory() as temp:
            cache = Path(temp) / 'cache'
            cache.mkdir()
            (cache / 'retrieval.json').write_text(json.dumps({'source_url': 'https://docs.example/api/', 'pages': []}))
            out = Path(temp) / 'out'
            out.mkdir()
            with patch('official_docs.fetch_html', return_value=HTML) as fetch:
                log = enrich_apis([{'qualified': 'demo.fetch'}], report(), out, {'cache': str(cache)}, doc_details, examples_from_doc)
                fetch.assert_called_once()
            self.assertEqual(log['fetched_pages'], 1)

    def test_default_generation_does_not_fetch(self):
        with tempfile.TemporaryDirectory() as temp, patch('official_docs.fetch_html') as fetch:
            out = Path(temp)
            (out / 'README.md').write_text('# Raw reference')
            data = report()
            data['official_docs_options']['enabled'] = False
            write_developer_docs(out, data, fence)
            fetch.assert_not_called()
            self.assertFalse((out / 'official_docs').exists())

    def test_exact_anchor_extracts_only_api_section(self):
        anchor, region = api_section(Page(HTML), ['demo.fetch'])
        self.assertEqual(anchor, 'demo.fetch')
        content = section_content(region, examples_from_doc)
        self.assertEqual(content['description'], 'Fetch a documented value.')
        self.assertIn('valid number', content['parameters'])
        self.assertEqual(content['examples'][0]['expected'], '4')
        self.assertNotIn('outside', content['description'])
        self.assertIsNone(api_section(Page(HTML), ['demo.unrelated'])[1])

    def test_enrichment_and_rendered_provenance(self):
        with tempfile.TemporaryDirectory() as temp, patch('official_docs.fetch_html', return_value=HTML) as fetch:
            out = Path(temp)
            (out / 'README.md').write_text('# Raw reference')
            data = report()
            write_developer_docs(out, data, fence)
            self.assertEqual(data['official_documentation']['enriched_apis'], 1)
            self.assertEqual(data['official_documentation']['fetched_pages'], 1)
            fetch.assert_called_once()
            self.assertIn('not verified against installed version', next((out / 'api').glob('*.md')).read_text(encoding='utf-8'))
            self.assertIn('Fetch a documented value.', (out / 'API_INDEX.md').read_text(encoding='utf-8'))
            self.assertTrue((out / 'official_docs' / 'retrieval.json').is_file())
            helpers.IntegrationTests().check_markdown(out)

    def test_preserves_local_fields(self):
        with tempfile.TemporaryDirectory() as temp, patch('official_docs.fetch_html', return_value=HTML):
            item = {'qualified': 'demo.fetch', 'docstring': 'Local description.\n>>> fetch(1)\n2', 'parameters': []}
            enrich_apis([item], report(), Path(temp), {'max_pages': 1}, doc_details, examples_from_doc)
            self.assertNotIn('description', item['official_documentation'])
            self.assertNotIn('examples', item['official_documentation'])
            self.assertTrue(item['docstring'].startswith('Local description.'))

    def test_network_failure_preserves_generation(self):
        with tempfile.TemporaryDirectory() as temp, patch('official_docs.fetch_html', side_effect=TimeoutError('offline')):
            item = {'qualified': 'demo.fetch', 'docstring': None}
            log = enrich_apis([item], report(), Path(temp), {'max_pages': 1}, doc_details, examples_from_doc)
            self.assertEqual(log['enriched_apis'], 0)
            self.assertIn('offline', log['errors'][0]['error'])
            self.assertEqual(log['unresolved_apis'][0]['api'], 'demo.fetch')

    def test_page_limit_and_host_boundary(self):
        root = '<a href="next.html">next</a><a href="https://other.example/page">other</a>'
        with tempfile.TemporaryDirectory() as temp, patch('official_docs.fetch_html', return_value=root) as fetch:
            log = enrich_apis([{'qualified': 'demo.absent'}], report(), Path(temp), {'max_pages': 1}, doc_details, examples_from_doc)
            fetch.assert_called_once()
            self.assertEqual(log['fetched_pages'], 1)
            self.assertTrue(log['unresolved_apis'])
        with tempfile.TemporaryDirectory() as temp, patch('official_docs.fetch_html', return_value=root) as fetch:
            log = enrich_apis([{'qualified': 'demo.absent'}], report(), Path(temp), {'max_pages': 3}, doc_details, examples_from_doc)
            self.assertEqual(fetch.call_count, 2)
            self.assertTrue(all(call.args[0].startswith('https://docs.example/') for call in fetch.call_args_list))

    def test_heading_section_and_child_code_language(self):
        html = '<h2 id="demo.fetch">fetch</h2><p>Fetch value.</p><pre><code class="language-python">fetch(2)</code></pre><h2 id="demo.other">Other</h2><p>Do not include.</p>'
        _, region = api_section(Page(html), ['demo.fetch'])
        content = section_content(region, examples_from_doc)
        self.assertEqual(content['description'], 'Fetch value.')
        self.assertEqual(content['examples'][0]['code'], 'fetch(2)')
        self.assertNotIn('Do not include', region.text())
        self.assertIsNone(api_section(Page(html), ['other.fetch'])[1])

    def test_missing_fields_continue_to_second_page(self):
        first = '<section id="demo.fetch"><p>First description.</p></section><a href="examples.html">Examples</a>'
        second = '<section id="demo.fetch"><p>Second description.</p><pre><code class="language-python">fetch(3)</code></pre></section>'
        with tempfile.TemporaryDirectory() as temp, patch('official_docs.fetch_html', side_effect=[first, second]):
            item = {'qualified': 'demo.fetch'}
            log = enrich_apis([item], report(), Path(temp), {'max_pages': 2}, doc_details, examples_from_doc)
            self.assertEqual(log['enriched_apis'], 1)
            self.assertEqual(log['fetched_pages'], 2)
            self.assertEqual(item['official_documentation']['description'], 'First description.')
            self.assertEqual(item['official_documentation']['examples'][0]['code'], 'fetch(3)')
            self.assertEqual(len(item['official_documentation']['sources']), 2)
            self.assertNotIn('examples', log['unresolved_apis'][0]['missing'])

    def test_nested_api_boundaries(self):
        html = '<section id="demo.Parent"><p>Parent.</p><section id="demo.Parent.child"><pre class="language-python">child_only()</pre></section><div id="member-other-1"><p>Other method.</p></div><pre class="language-python">parent_only()</pre></section>'
        _, region = api_section(Page(html), ['demo.Parent'])
        content = section_content(region, examples_from_doc)
        self.assertEqual([x['code'] for x in content['examples']], ['parent_only()'])
        self.assertEqual(content['description'], 'Parent.')

    def test_nested_method_heading_ends_parent_region(self):
        html = '<section id="demo.Parent"><p>Parent.</p><h3 id="demo.Parent.child">Child</h3><pre class="language-python">child_only()</pre></section>'
        _, region = api_section(Page(html), ['demo.Parent'])
        self.assertEqual(section_content(region, examples_from_doc)['examples'], [])

    def test_heading_table_fields(self):
        html = '<section id="demo.fetch"><p>Fetch.</p><h3>Parameters</h3><table><tr><th>Name</th><th>Description</th></tr><tr><td>value</td><td>An integer.</td></tr></table><h3>Returns</h3><p>A number.</p><h3>Raises</h3><ul><li>ValueError on bad input.</li></ul><h3>Notes</h3><p>Not return information.</p></section>'
        _, region = api_section(Page(html), ['demo.fetch'])
        content = section_content(region, examples_from_doc)
        self.assertIn('value | An integer.', content['parameters'])
        self.assertEqual(content['returns'], 'A number.')
        self.assertIn('ValueError', content['raises'])
        self.assertNotIn('Not return', content['returns'])

    def test_saved_genai_reference_pages(self):
        base = Path(__file__).parent / 'tests/fixtures/official_reference'
        sources = json.loads((base / 'sources.json').read_text(encoding='utf-8'))
        expected = {'langchain': 'Creates an agent graph', 'langgraph': 'A graph whose nodes', 'langsmith': 'Trace a function'}
        for package, url in sources.items():
            with self.subTest(package=package):
                page = Page((base / (package + '.html')).read_text(encoding='utf-8'))
                identity = url.split('/python/')[1].replace('/', '.')
                _, region = api_section(page, [identity], url)
                self.assertIsNotNone(region)
                content = section_content(region, examples_from_doc)
                self.assertTrue(content['description'].startswith(expected[package]), content['description'])
                if package != 'langsmith':
                    self.assertTrue(content['examples'])
                else:
                    self.assertEqual(content['examples'], [])
                self.assertIn('parameters', content)
                self.assertIsNone(api_section(page, ['unrelated.' + identity.split('.')[-1]], url)[1])
                self.assertIsNone(api_section(page, [identity], url.replace('reference.langchain.com', 'other.example'))[1])

    def test_saved_reference_enrichment_renders_valid_markdown(self):
        base = Path(__file__).parent / 'tests/fixtures/official_reference'
        sources = json.loads((base / 'sources.json').read_text(encoding='utf-8'))
        for package, url in sources.items():
            with self.subTest(package=package), tempfile.TemporaryDirectory() as temp:
                data = report()
                data['package'] = package
                identity = url.split('/python/')[1].replace('/', '.')
                module, name = identity.rsplit('.', 1)
                data['modules'] = [{'module': module, 'members': [{'name': name, 'kind': 'function',
                                    'signature': name + '(value)', 'parameters': [{'name': 'value', 'required': True, 'kind': 'positional or keyword'}]}]}]
                data['official_docs_options'].update(url=url, max_pages=1)
                out = Path(temp)
                (out / 'README.md').write_text('# Raw reference')
                with patch('official_docs.fetch_html', return_value=(base / (package + '.html')).read_text(encoding='utf-8')):
                    write_developer_docs(out, data, fence)
                self.assertEqual(data['official_documentation']['enriched_apis'], 1)
                page = next((out / 'api').glob('*.md')).read_text(encoding='utf-8')
                self.assertIn('Description source:', page)
                self.assertIn('Parameters source:', page)
                self.assertIn('live download', page)
                helpers.IntegrationTests().check_markdown(out)

    def test_field_provenance_mixed_cache_and_live(self):
        first = '<section id="demo.fetch"><p>First description.</p></section><a href="examples.html">Examples</a>'
        second = '<section id="demo.fetch"><pre class="language-python">fetch(3)</pre></section>'
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            cache = base / 'cache'
            cache.mkdir()
            with patch('official_docs.fetch_html', return_value=first):
                original = enrich_apis([{'qualified': 'demo.fetch'}], report(), cache, {'max_pages': 1}, doc_details, examples_from_doc)
            out = base / 'out'
            out.mkdir()
            item = {'qualified': 'demo.fetch'}
            with patch('official_docs.fetch_html', return_value=second) as fetch:
                log = enrich_apis([item], report(), out, {'cache': str(cache / 'official_docs'), 'max_pages': 2}, doc_details, examples_from_doc)
                fetch.assert_called_once()
            fields = item['official_documentation']['field_sources']
            self.assertTrue(fields['description']['from_cache'])
            self.assertFalse(fields['examples']['from_cache'])
            self.assertTrue(fields['examples']['url'].endswith('examples.html#demo.fetch'))
            self.assertEqual(fields['description']['retrieved_at'], original['pages'][0]['retrieved_at'])
            self.assertEqual(log['enriched_apis'], 1)

    def test_static_stream_segments_restore_descriptions_without_execution(self):
        html = '<table><tr><td><template id="P:1"></template></td></tr></table><div hidden id="S:1"><p>Recovered description.</p></div><script>$RS("S:1","P:1");throw new Error("must not execute")</script>'
        page = Page(html)
        table = next(n for n in page.root.nodes() if n.tag == 'table')
        self.assertIn('Recovered description.', table.text())
        self.assertNotIn('S:1', page.ids)

    def test_saved_streamed_parameter_descriptions(self):
        base = Path(__file__).parent / 'tests/fixtures/official_reference'
        page = Page((base / 'langgraph.html').read_text(encoding='utf-8'))
        _, region = api_section(page, ['langgraph.graph.state.StateGraph'], 'https://reference.langchain.com/python/langgraph/graph/state/StateGraph')
        content = section_content(region, examples_from_doc)
        self.assertIn('defines the input to the graph', content['parameters'])
        self.assertIn('defines the output from the graph', content['parameters'])

    def test_source_selection_and_invalid_urls(self):
        self.assertEqual(documentation_source({'package_type': 'standard-library', 'package': 'json', 'version': '3.14.7'}, None)[0], 'https://docs.python.org/3.14/library/json.html')
        self.assertIsNone(documentation_source({'metadata': {}}, None)[0])
        for url in ('http://docs.example/', 'file:///tmp/docs', 'https://localhost/', 'https://127.0.0.1/', 'https://u:p@docs.example/'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                validate_url(url)


if __name__ == '__main__':
    unittest.main()
