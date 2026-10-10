"""Bounded, source-attributed HTML documentation enrichment; no example execution."""
from __future__ import annotations

import ast
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import ipaddress
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit, urldefrag, quote
from urllib.request import Request, build_opener, HTTPRedirectHandler

MAX_BYTES = 4 * 1024 * 1024


def validate_url(url):
    parts = urlsplit(url)
    if parts.scheme != 'https' or not parts.hostname or parts.username or parts.password:
        raise ValueError('Documentation URL must be an HTTPS URL without embedded credentials')
    if parts.hostname.lower() == 'localhost' or parts.hostname.lower().endswith(('.localhost', '.local')):
        raise ValueError('Documentation URL must use a public documentation host')
    try:
        address = ipaddress.ip_address(parts.hostname)
    except ValueError:
        return url
    if not address.is_global:
        raise ValueError('Documentation URL must not use a private or loopback IP address')
    return url


class SameHostRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_url(newurl)
        if urlsplit(newurl).netloc != urlsplit(req.full_url).netloc:
            raise ValueError('Cross-host documentation redirect refused; provide the final official URL explicitly')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_html(url, timeout):
    validate_url(url)
    request = Request(url, headers={'User-Agent': 'PythonPackageDiscovery/1.0', 'Accept': 'text/html'})
    with build_opener(SameHostRedirect()).open(request, timeout=timeout) as response:
        if response.headers.get_content_type() != 'text/html':
            raise ValueError('Only HTML documentation pages are supported')
        data = response.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError('Documentation page exceeds the 4 MiB limit')
        return data.decode(response.headers.get_content_charset() or 'utf-8', errors='replace')


class Node:
    def __init__(self, tag='', attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.parent = parent
        self.children = []

    def nodes(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.nodes()

    def text(self):
        return ''.join(child.text() if isinstance(child, Node) else child for child in self.children)


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.current = self.root
        self.feed(html)
        self.ids = {n.attrs['id']: n for n in self.root.nodes() if n.attrs.get('id')}
        self.restore_streamed_segments()

    def restore_streamed_segments(self):
        # Read declarative React segment IDs only. Never execute JavaScript.
        scripts = [node.text() for node in self.root.nodes() if node.tag == 'script']
        for script in scripts:
            for kind, first, second in re.findall(r'\$(RS|RC)\("([SPB]:[0-9a-f]+)","([SPB]:[0-9a-f]+)"\)', script):
                source_id, target_id = (first, second) if kind == 'RS' else (second, first)
                source, target = self.ids.get(source_id), self.ids.get(target_id)
                if source is None or target is None or source is target or target.tag != 'template':
                    continue
                ancestor = target.parent
                while ancestor and ancestor is not source:
                    ancestor = ancestor.parent
                if ancestor is source or not source.parent or not target.parent:
                    continue
                parent = target.parent
                offset = parent.children.index(target)
                children = list(source.children)
                for child in children:
                    if isinstance(child, Node):
                        child.parent = parent
                parent.children[offset:offset + 1] = children
                source.parent.children.remove(source)
                source.children = []
        self.ids = {n.attrs['id']: n for n in self.root.nodes() if n.attrs.get('id')}


    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in ('area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'):
            self.current = node

    def handle_endtag(self, tag):
        node = self.current
        while node.parent is not None:
            if node.tag == tag:
                self.current = node.parent
                return
            node = node.parent

    def handle_data(self, text):
        self.current.children.append(text)


def clean(text):
    return re.sub(r'\s+', ' ', text).strip()


def reference_region(page, names, url):
    """Adapter for the server-rendered LangChain family reference, exact routes only."""
    parts = urlsplit(url)
    if parts.hostname != 'reference.langchain.com':
        return None, None
    identity = parts.path.removeprefix('/python/').strip('/').replace('/', '.')
    if identity not in names:
        return None, None
    canonical = next((n.attrs.get('href') for n in page.root.nodes()
                      if n.tag == 'link' and n.attrs.get('rel') == 'canonical'), None)
    if canonical and urlsplit(canonical).path.rstrip('/') != parts.path.rstrip('/'):
        return None, None
    region = Node('section', [('id', identity)])
    for node in page.root.nodes():
        classes = node.attrs.get('class', '').split()
        if 'markdown-content' in classes and ('text-lg' in classes or 'markdown-compact' not in classes):
            # Nested markdown containers are included by their outer container.
            ancestor = node.parent
            nested = False
            while ancestor:
                if 'markdown-content' in ancestor.attrs.get('class', '').split():
                    nested = True
                ancestor = ancestor.parent
            if not nested:
                region.children.append(node)
    # Parameters are tables in current reference pages; cards are never content.
    for node in page.root.nodes():
        if node.tag == 'table' and all(word in node.text()[:100] for word in ('Name', 'Type', 'Description')):
            heading = Node('h2', parent=region)
            heading.children = ['Parameters']
            region.children.extend([heading, node])
    for container in region.children:
        for node in container.nodes():
            if node.tag == 'pre' and 'shiki' in node.attrs.get('class', '').split():
                try:
                    ast.parse(node.text())
                except SyntaxError:
                    continue
                node.attrs['data-language'] = 'python'
    region.children.sort(key=lambda n: 0 if 'text-lg' in n.attrs.get('class', '').split() else 1)
    return (identity, region) if region.children else (None, None)


def api_section(page, names, url=''):
    adapted = reference_region(page, names, url)
    if adapted[1] is not None:
        return adapted
    for name in names:
        anchor = page.ids.get(name)
        if anchor is None:
            continue
        if anchor.tag == 'dt' and anchor.parent.tag == 'dl':
            siblings = anchor.parent.children
            start = siblings.index(anchor)
            region = next((n for n in siblings[start + 1:] if isinstance(n, Node) and n.tag == 'dd'), None)
            if region is not None:
                return name, region
        if anchor.tag in ('section', 'div'):
            return name, anchor
        if anchor.tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            # Heading-based API references end at the next peer/ancestor heading.
            region = Node('section')
            siblings = anchor.parent.children
            level = int(anchor.tag[1])
            for node in siblings[siblings.index(anchor) + 1:]:
                if isinstance(node, Node) and re.fullmatch(r'h[1-6]', node.tag) and int(node.tag[1]) <= level:
                    break
                region.children.append(node)
            return name, region
    return None, None


def section_content(region, examples_from_doc):
    # Exclude nested API identities, including non-Sphinx method containers.
    def boundary(node):
        anchor = node.attrs.get('id', '')
        return ('py' in node.attrs.get('class', '').split() and node.tag == 'dl') or bool(
            anchor and (anchor.startswith('member-') or
                        ('.' in anchor and re.fullmatch(r'[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+', anchor))))

    def walk(node):
        yield node
        for child in node.children:
            if isinstance(child, Node) and boundary(child) and re.fullmatch(r'h[1-6]', child.tag):
                break
            if isinstance(child, Node) and not boundary(child):
                yield from walk(child)
    nodes = list(walk(region))
    paragraphs = [clean(n.text()) for n in nodes if n.tag == 'p' and n.parent.tag != 'li']
    fields = {}
    for node in nodes:
        if node.tag == 'dt' and node.parent.tag == 'dl':
            heading = clean(node.text()).rstrip(':').casefold()
            field = {'parameters': 'parameters', 'parameters and keyword arguments': 'parameters', 'returns': 'returns', 'return type': 'returns', 'raises': 'raises'}.get(heading)
            if field:
                siblings = node.parent.children
                following = next((x for x in siblings[siblings.index(node) + 1:] if isinstance(x, Node) and x.tag == 'dd'), None)
                if following:
                    fields[field] = (fields.get(field, '') + '\n' + clean(following.text())).strip()
    labels = {'parameters': 'parameters', 'arguments': 'parameters', 'returns': 'returns',
              'return value': 'returns', 'return type': 'returns', 'raises': 'raises', 'exceptions': 'raises'}
    def block_text(node):
        parts = []
        for child in node.children:
            if isinstance(child, Node):
                value = block_text(child)
                parts.append(' ' + value + ' ' if child.tag in ('p', 'div', 'ul', 'ol', 'br') else value)
            else:
                parts.append(child)
        return ''.join(parts)
    def structured(node):
        if node.tag == 'table':
            return '\n'.join(' | '.join(clean(block_text(cell)) for cell in row.children
                                      if isinstance(cell, Node) and cell.tag in ('th', 'td'))
                             for row in node.nodes() if row.tag == 'tr')
        return clean(node.text())
    for index, node in enumerate(nodes):
        if not re.fullmatch(r'h[1-6]', node.tag):
            continue
        label = clean(node.text()).rstrip(':¶# ').casefold()
        field = labels.get(label)
        if not field:
            continue
        level = int(node.tag[1])
        selected = []
        for following in nodes[index + 1:]:
            if re.fullmatch(r'h[1-6]', following.tag) and int(following.tag[1]) <= level:
                break
            if following.tag in ('p', 'table', 'ul', 'ol', 'pre'):
                if not any(following in list(parent.nodes())[1:] for parent in selected):
                    selected.append(following)
        value = '\n'.join(structured(n) for n in selected).strip()
        if value:
            fields[field] = (fields.get(field, '') + '\n' + value).strip()
    examples = []
    for node in nodes:
        if node.tag != 'pre':
            continue
        raw = node.text().strip()
        if '>>>' in raw:
            candidates = examples_from_doc(raw)
        elif any(re.search(r'(?:python|pycon|language-py(?:\s|$))', ancestor.attrs.get('class', '').lower())
                 or ancestor.attrs.get('data-language', '').lower() in ('python', 'py', 'python3')
                 for ancestor in [node, node.parent, node.parent.parent or node.parent,
                                  *[child for child in node.children if isinstance(child, Node)]]):
            candidates = [{'code': raw, 'expected': ''}]
        else:
            candidates = []
        for item in candidates:
            try:
                ast.parse(item['code'])
                valid = True
            except SyntaxError:
                valid = False
            examples.append(dict(item, python_syntax_valid=valid))
    return dict(fields, description=paragraphs[0] if paragraphs else '', examples=examples)


def documentation_source(report, explicit):
    if explicit:
        return explicit, 'user-supplied official URL'
    if report.get('package_type') == 'standard-library':
        minor = '.'.join(report['version'].split('.')[:2])
        root = report['package'].split('.')[0]
        return f'https://docs.python.org/{minor}/library/{root}.html', 'Python official documentation'
    if report.get('package') in ('langchain', 'langgraph', 'langsmith'):
        return f"https://reference.langchain.com/python/{report['package']}/", 'LangChain family official API reference adapter'
    for value in report['metadata'].get('Project-URL', []):
        label, separator, url = value.partition(',')
        if separator and label.strip().casefold() in ('documentation', 'docs', 'api documentation'):
            return url.strip(), 'package-declared documentation URL (ownership not independently verified)'
    return None, 'No documentation URL declared. Provide --docs-url with the official documentation URL.'


def read_cached_page(directory, entry):
    digest = entry.get('sha256', '')
    if not isinstance(digest, str) or not re.fullmatch(r'[a-f0-9]{64}', digest):
        raise ValueError('Invalid cached HTML hash')
    directory = Path(directory).resolve(strict=True)
    path = (directory / (digest + '.html')).resolve(strict=True)
    if path.parent != directory or path.stat().st_size > MAX_BYTES:
        raise ValueError('Cached HTML is outside the cache or exceeds the size limit')
    with path.open('rb') as stream:
        data = stream.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError('Cached HTML exceeds the size limit')
    html = data.decode('utf-8')
    if hashlib.sha256(html.encode('utf-8')).hexdigest() != digest:
        # Earlier Windows caches were saved through text-mode newline translation.
        normalized = html.replace('\r\n', '\n')
        if hashlib.sha256(normalized.encode('utf-8')).hexdigest() != digest:
            raise ValueError('Cached HTML checksum mismatch')
        html = normalized
    if not entry.get('retrieved_at'):
        raise ValueError('Cached HTML retrieval timestamp is missing')
    return html


def reference_priority(url, rows, package):
    """Rank task APIs, public exports, then other exact APIs; private routes last."""
    from developer_docs import task_rows
    identity = urlsplit(url).path.removeprefix('/python/').strip('/').replace('/', '.')
    tasks = task_rows(package, rows)
    for index, (_, row) in enumerate(tasks):
        if identity in (row['qualified'], row.get('alias_of')):
            return (0, index, url)
    matching = [row for row in rows if identity in (row['qualified'], row.get('alias_of'))]
    private = any(part.startswith('_') for part in identity.split('.'))
    if matching and not private:
        return (1, min(row['qualified'].count('.') for row in matching), url)
    if not private:
        return (2, identity.count('.'), url)
    return (3, identity.count('.'), url)


def enrich_apis(rows, report, out, options, doc_details, examples_from_doc):
    from developer_docs import caller_parameters
    target = out / 'official_docs'
    target.mkdir(exist_ok=True)
    log = {'source_url': None, 'source_basis': None, 'enriched_apis': 0, 'fetched_pages': 0, 'cached_pages': 0,
           'package': report['package'], 'package_version': report['version'], 'offline': bool(options.get('offline')),
           'pages': [], 'unresolved_apis': [], 'errors': []}
    root, basis = documentation_source(report, options.get('url'))
    cache_entries = {}
    if options.get('cache'):
        try:
            manifest = json.loads((Path(options['cache']) / 'retrieval.json').read_text(encoding='utf-8'))
            if not isinstance(manifest, dict) or not isinstance(manifest.get('pages'), list):
                raise ValueError('Invalid cache manifest structure')
            if manifest.get('package') not in (None, report['package']):
                raise ValueError('Cache belongs to a different package')
            if root is None and manifest.get('package') == report['package']:
                root, basis = manifest.get('source_url'), 'previous cache source; ownership and documentation version not independently verified'
            if not root or urldefrag(manifest.get('source_url') or '')[0] != urldefrag(root)[0]:
                raise ValueError('Cache source URL does not match this documentation source')
            cache_entries = {urldefrag(entry['url'])[0]: entry for entry in manifest['pages'] if isinstance(entry, dict) and isinstance(entry.get('url'), str)}
            log['cache_package_version'] = manifest.get('package_version')
        except (OSError, ValueError, TypeError) as exc:
            log['errors'].append({'cache': str(options['cache']), 'error': str(exc)})
    log['source_url'], log['source_basis'] = root, basis
    needed = []
    for item in rows:
        doc = item.get('docstring') or ''
        details = doc_details(doc)
        missing = {'description': not doc.strip(), 'examples': not examples_from_doc(doc),
                   'returns': not details['returns'], 'raises': not details['raises'],
                   'parameters': any(not details['parameters'].get(p['name'], {}).get('description') for p in caller_parameters(item))}
        if any(missing.values()):
            needed.append((item, missing))
    if root and needed:
        try:
            validate_url(root)
            root = urldefrag(root)[0]
            origin = urlsplit(root)
            prefix = origin.path.rsplit('/', 1)[0] + '/'
            if origin.hostname == 'reference.langchain.com' and report['package'] in ('langchain', 'langgraph', 'langsmith'):
                prefix = '/python/' + report['package'] + '/'

            eligible = [url for url in cache_entries if urlsplit(url).netloc == origin.netloc and urlsplit(url).scheme == 'https' and urlsplit(url).path.startswith(prefix)]
            pending, visited = [root, *sorted(url for url in eligible if url != root)], set()
            if report.get('package_type') == 'standard-library':
                pending = [root]
            while pending and len(visited) < options.get('max_pages', 10) and needed:
                if origin.hostname == 'reference.langchain.com' and visited:
                    pending.sort(key=lambda link: reference_priority(link, rows, report['package']))
                url = pending.pop(0)
                if url in visited:
                    continue
                visited.add(url)
                print(f'Inspecting documentation: {url}', flush=True)
                try:
                    cached = False
                    if url in cache_entries:
                        try:
                            html = read_cached_page(options['cache'], cache_entries[url])
                            cached = True
                        except (OSError, ValueError) as exc:
                            log['errors'].append({'url': url, 'error': f'Cache read failed: {exc}'})
                            if options.get('offline'):
                                continue
                    if not cached:
                        if options.get('offline'):
                            raise FileNotFoundError('Documentation page is absent from cache; offline mode forbids network fetching')
                        html = fetch_html(url, options.get('timeout', 15))
                    digest = hashlib.sha256(html.encode('utf-8')).hexdigest()
                    (target / (digest + '.html')).write_bytes(html.encode('utf-8'))
                    page = Page(html)
                    used_at = datetime.now(timezone.utc).isoformat()
                    stamp = cache_entries[url]['retrieved_at'] if cached else used_at
                    log['cached_pages' if cached else 'fetched_pages'] += 1
                    log['pages'].append({'url': url, 'retrieved_at': stamp, 'sha256': digest, 'used_at': used_at, 'from_cache': cached})
                    remaining = []
                    for item, missing in needed:
                        names = [item['qualified']]
                        if item.get('alias_of'):
                            names.append(item['alias_of'])
                        anchor, region = api_section(page, names, url)
                        if region is None:
                            remaining.append((item, missing))
                            continue
                        content = section_content(region, examples_from_doc)
                        supplement = {key: value for key, value in content.items() if missing.get(key) and value}
                        if supplement:
                            supplement.update(url=url if urlsplit(url).hostname == 'reference.langchain.com' else url + '#' + quote(anchor, safe='.'), retrieved_at=stamp,
                                              version_status='Python minor-version documentation' if report.get('package_type') == 'standard-library' else 'not verified against installed version',
                                              source_basis=basis, sha256=digest, from_cache=cached)
                            field_sources = {key: {'url': supplement['url'], 'retrieved_at': stamp,
                                                   'sha256': digest, 'from_cache': cached}
                                             for key in content if key in supplement}
                            supplement['field_sources'] = field_sources
                            previous = item.get('official_documentation')
                            if previous:
                                previous.setdefault('field_sources', {}).update(field_sources)
                                sources = previous.setdefault('sources', [{'url': previous['url'], 'retrieved_at': previous['retrieved_at'], 'sha256': previous['sha256'], 'from_cache': previous['from_cache']}])
                                sources.append({'url': supplement['url'], 'retrieved_at': stamp, 'sha256': digest, 'from_cache': cached})
                                for key in content:
                                    if key in supplement:
                                        previous[key] = supplement[key]
                            else:
                                item['official_documentation'] = supplement
                                log['enriched_apis'] += 1
                        unresolved = [key for key, value in missing.items() if value and not content.get(key)]
                        if unresolved:
                            remaining.append((item, {key: key in unresolved for key in missing}))
                    needed = remaining
                    links = []
                    for node in page.root.nodes():
                        if node.tag != 'a' or not node.attrs.get('href'):
                            continue
                        link = urldefrag(urljoin(url, node.attrs['href']))[0]
                        parts = urlsplit(link)
                        if parts.scheme == 'https' and parts.netloc == origin.netloc and parts.path.startswith(prefix) and not parts.query and link not in visited and not parts.path.endswith(('.pdf', '.zip', '.inv')):
                            if origin.hostname == 'reference.langchain.com':
                                identity = parts.path.removeprefix('/python/').strip('/').replace('/', '.')
                                if any(part.startswith('_') for part in identity.split('.')) and not any(
                                    identity in (row['qualified'], row.get('alias_of')) for row in rows):
                                    continue
                            links.append(link)
                    links = sorted(set(links), key=lambda link: (not any(word in link.casefold() for word in ('api', 'reference', 'generated')), link))
                    if report.get('package_type') == 'standard-library':
                        links = []  # Other library pages describe other modules, not this API.
                    if origin.hostname == 'reference.langchain.com':
                        identities = {name for item, _ in needed for name in (item['qualified'], item.get('alias_of', ''))}
                        links.sort(key=lambda link: urlsplit(link).path.removeprefix('/python/').strip('/').replace('/', '.') not in identities)
                    additions = [link for link in links if link not in pending]
                    if origin.hostname == 'reference.langchain.com':
                        exact = [link for link in additions if urlsplit(link).path.removeprefix('/python/').strip('/').replace('/', '.') in identities]
                        pending = exact + pending + [link for link in additions if link not in exact]
                    else:
                        pending.extend(additions)
                except Exception as exc:
                    log['errors'].append({'url': url, 'error': f'{type(exc).__name__}: {exc}'})
        except ValueError as exc:
            log['errors'].append({'url': root, 'error': str(exc)})
    for item, missing in needed:
        log['unresolved_apis'].append({'api': item['qualified'], 'missing': [k for k, v in missing.items() if v],
                                     'reason': basis if not root else 'API anchor not found within fetch limit or pages failed'})
    (target / 'retrieval.json').write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding='utf-8')
    return log
