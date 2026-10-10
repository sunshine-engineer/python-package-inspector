"""Evidence-based developer navigation built from the full inspection report."""
from __future__ import annotations

import ast
import builtins
import doctest
import json
from pathlib import Path
import re
import textwrap


def cell(value):
    return str(value if value is not None else 'Not provided').replace('|', '\\|').replace('\n', ' ').replace('\r', '').replace('[', '&#91;').replace(']', '&#93;')


def summary(doc):
    return next((line.strip() for line in (doc or '').splitlines() if line.strip()), 'No description supplied by the package.')


def doc_details(doc):
    """Extract common Sphinx, Google and NumPy fields without inferring behavior."""
    result = {'parameters': {}, 'returns': [], 'raises': []}
    section = None
    current = None
    section_indent = None
    lines = (doc or '').splitlines()
    for line in lines:
        text = line.strip()
        indent = len(line) - len(line.lstrip())
        sphinx = re.match(r':param\s+(?:(\S+)\s+)?([\\*\w]+)\s*:\s*(.*)', text)
        if sphinx:
            typ, name, description = sphinx.groups()
            name = name.replace('\\', '').lstrip('*')
            result['parameters'][name] = {'description': description, 'type': typ}
            current = name
            section = 'parameters'
            section_indent = indent
            continue
        typed = re.match(r':type\s+(\w+)\s*:\s*(.*)', text)
        if typed:
            result['parameters'].setdefault(typed[1], {})['type'] = typed[2]
            continue
        if text.startswith(':') and not re.match(r':(?:return|returns|rtype|raises?)', text):
            section = None
            current = None
            continue
        returned = re.match(r':(?:return|returns|rtype):\s*(.*)', text)
        raised = re.match(r':raises?\s+([^:]+):\s*(.*)', text)
        if returned:
            result['returns'].append(returned[1])
            section = 'returns'
            section_indent = indent
            current = None
            continue
        if raised:
            result['raises'].append(f'{raised[1]}: {raised[2]}')
            section = 'raises'
            section_indent = indent
            current = None
            continue
        heading = text.rstrip(':').lower()
        if heading in ('args', 'arguments', 'parameters', 'keyword args', 'keyword arguments', 'returns', 'yields', 'raises'):
            section = 'parameters' if heading in ('args', 'arguments', 'parameters', 'keyword args', 'keyword arguments') else ('returns' if heading == 'yields' else heading)
            current = None
            section_indent = indent if text.endswith(':') else None
            continue
        if heading in ('examples', 'example', 'notes', 'note', 'see also', 'warnings', 'attributes', 'references'):
            section = None
            current = None
            continue
        if not text or set(text) == {'-'}:
            continue
        if section_indent is not None and indent <= section_indent:
            section = None
            current = None
        if section == 'parameters':
            google = re.match(r'(\*{0,2}\w+)\s*(?:\(([^)]+)\))?\s*:\s*(.*)', text)
            if google:
                name, typ, description = google.groups()
                # NumPy's "name : type" puts the type after the colon.
                numpy = bool(re.match(r'^\w+\s+:', text))
                current = name.lstrip('*')
                result['parameters'][current] = {'type': description if numpy else typ,
                                                  'description': '' if numpy else description}
            elif current:
                entry = result['parameters'][current]
                entry['description'] = (entry.get('description', '') + ' ' + text).strip()
        elif section in ('returns', 'raises'):
            result[section].append(text)
    return result


def doctest_sessions(doc):
    """Keep sequential commands together; prose separates independent sessions."""
    sessions, commands, outputs, lineno = [], [], [], None
    def flush():
        if commands:
            sessions.append((lineno, {'code': '\n'.join(commands), 'expected': '\n'.join(outputs),
                                     'format': 'doctest session', 'command_count': len(commands)}))
            commands.clear()
            outputs.clear()
    for part in doctest.DocTestParser().parse(doc):
        if isinstance(part, str):
            if part.strip():
                flush()
        else:
            if not commands:
                lineno = part.lineno
            commands.append(part.source.rstrip())
            if part.want.strip():
                outputs.append(part.want.rstrip())
    flush()
    return sessions


def examples_from_doc(doc):
    """Preserve Python fences and standalone doctests without double extraction."""
    lines = (doc or '').splitlines(keepends=True)
    masked = list(lines)
    found = []
    index = 0
    while index < len(lines):
        opening = re.match(r'^([ \t]*)(`{3,}|~{3,})\s*([^\s]*)', lines[index])
        if not opening:
            index += 1
            continue
        indent, delimiter, language = opening.groups()
        end = index + 1
        while end < len(lines) and not re.fullmatch(r'\s*' + re.escape(delimiter[0]) + '{' + str(len(delimiter)) + r',}\s*', lines[end]):
            end += 1
        for offset in range(index, min(end + 1, len(lines))):
            masked[offset] = 'Example boundary\n' if offset == index else '\n'
        if end < len(lines) and language.lower() in ('python', 'python3', 'py', 'pycon'):
            code = textwrap.dedent(''.join(line[len(indent):] if line.startswith(indent) else line for line in lines[index + 1:end])).strip('\n')
            if code.strip():
                if re.search(r'^\s*>>>', code, re.M):
                    try:
                        found.extend((index, item) for _, item in doctest_sessions(code))
                    except ValueError:
                        found.append((index, {'code': code, 'expected': '', 'format': 'unparsed interactive block'}))
                else:
                    found.append((index, {'code': code, 'expected': '', 'format': 'Python code fence'}))
        index = end + 1
    try:
        found.extend(doctest_sessions(''.join(masked)))
    except ValueError:
        pass
    return [item for _, item in sorted(found, key=lambda pair: pair[0])]


def statement_names(node):
    """Conservative static names for optional setup copies, never evaluation."""
    stores = {n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
    local = stores | {n.arg for n in ast.walk(node) if isinstance(n, ast.arg)}
    local.update(n.name for n in ast.walk(node) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)))
    imports = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Import):
            imports.update(a.asname or a.name.split('.')[0] for a in n.names)
        elif isinstance(n, ast.ImportFrom):
            imports.update(a.asname or a.name for a in n.names)
    local.update(imports)
    loaded = {n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
    bound = {node.name} if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) else stores | imports
    excluded = local if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) else imports
    return bound, loaded - excluded - set(dir(builtins))


def setup_complete_examples(examples):
    previous, output = [], []
    for example in examples:
        if example.get('format') != 'doctest session':
            previous = []
            output.append(dict(example))
            continue
        try:
            body = ast.parse(example['code']).body
        except SyntaxError:
            output.append(dict(example))
            previous = []
            continue
        needed, available = set(), set()
        for node in body:
            bound, loaded = statement_names(node)
            needed.update(loaded - available)
            available.update(bound)
        selected = []
        for node in reversed(previous):
            bound, loaded = statement_names(node)
            if bound & needed:
                selected.append(node)
                needed = (needed - bound) | loaded
        selected.reverse()
        copy = dict(example, unresolved_names=sorted(needed))
        if selected:
            copy['with_setup'] = '\n'.join(ast.unparse(n) for n in selected) + '\n' + example['code']
        output.append(copy)
        previous.extend(body)
    return output


def practice_prerequisites(item, examples):
    code = '\n'.join(e.get('with_setup', e['code']) for e in examples)
    modules = set()
    for example in examples:
        try:
            tree = ast.parse(example.get('with_setup', example['code']))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                modules.update(a.name.split('.')[0] for a in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])
    notes = []
    if modules:
        notes.append('Imported modules in these examples: ' + ', '.join('`' + m + '`' for m in sorted(modules)) + '.')
    requirements = []
    for requirement in item.get('practice_requirements', []):
        name = re.split(r'[<>=!~;\[ ]', requirement)[0].replace('-', '_').casefold()
        if name in {m.casefold() for m in modules}:
            requirements.append(requirement)
    if requirements:
        notes.append('Matching declared package dependencies: ' + '; '.join('`' + r + '`' for r in requirements) + '.')
    env = sorted(set(re.findall(r'\b(?:LANGSMITH|OPENAI|ANTHROPIC|AZURE_OPENAI|GOOGLE|GROQ)_[A-Z0-9_]+\b', (item.get('docstring') or '') + code)))
    if env:
        notes.append('Environment variable names mentioned by the source: ' + ', '.join('`' + v + '`' for v in env) + '. Consult the original documentation for their values and whether they are required.')
    providers = sorted(set(re.findall(r'["\'](openai|anthropic|google|groq|azure_openai):', code)))
    service = bool(providers or re.search(r'\b(?:Client|AsyncClient|clone_public_dataset|create_dataset|create_examples)\s*\(', code) or env)
    if providers:
        notes.append('Provider identifiers in the example: ' + ', '.join(providers) + '. Configure the matching integration and provider access before calling it; model availability is not checked.')
    notes.append('Service-related setup is present. Check authentication, connectivity, and service access before running. No service calls were validated.' if service else 'No explicit external-service setup was detected. Imports, files, application inputs, and runtime behavior still require checking.')
    return notes


def select_implementations(members):
    """Keep overload signatures while choosing the callable implementation's docs."""
    def overloaded(item):
        return any(d.rsplit('.', 1)[-1] == 'overload' for d in item.get('decorators', []))
    groups = {}
    for item in members:
        if item['kind'] in ('function', 'async function'):
            groups.setdefault(item['name'], []).append(item)
    choices = {}
    for name, group in groups.items():
        declarations = [item for item in group if overloaded(item)]
        if declarations:
            implementations = [item for item in group if not overloaded(item)]
            chosen = implementations[-1] if implementations else declarations[0]
            choices[name] = dict(chosen, overload_signatures=[item['signature'] for item in declarations if item.get('signature')],
                                 overload_only=not bool(implementations))
    output, emitted = [], set()
    for item in members:
        if item['kind'] in ('function', 'async function') and item['name'] in choices:
            if item['name'] in emitted:
                continue
            emitted.add(item['name'])
            item = choices[item['name']]
        if item['kind'] == 'class':
            item = dict(item, members=select_implementations(item.get('members', [])))
        output.append(item)
    return output


def is_public_module(name):
    return all(not part.startswith('_') and part not in ('tests', 'test', 'vendor', 'vendored') for part in name.split('.'))


def parameter_signature(parameters):
    parts = []
    positionals = [p for p in parameters if p['kind'] in ('positional-only', 'positional only')]
    has_varargs = any(p['kind'] in ('variadic positional', 'var positional') for p in parameters)
    inserted_star = False
    for p in parameters:
        kind = p['kind']
        if kind in ('keyword-only', 'keyword only') and not has_varargs and not inserted_star:
            parts.append('*')
            inserted_star = True
        name = p['name']
        if kind in ('variadic positional', 'var positional'):
            name = '*' + name
        elif kind in ('variadic keyword', 'var keyword'):
            name = '**' + name
        if p.get('annotation'):
            name += ': ' + p['annotation']
        if p.get('default') is not None:
            name += '=' + p['default']
        parts.append(name)
        if positionals and p is positionals[-1]:
            parts.append('/')
    return '(' + ', '.join(parts) + ')'


def collect_apis(report):
    modules = {m['module']: dict(m, members=select_implementations(m['members'])) for m in report['modules']}
    rows = {}

    def add(module, item, path=None, evidence='source', export_basis='name heuristic'):
        path = path or item['name']
        qualified = f'{module["module"]}.{path}'
        data = dict(item, qualified=qualified, module=module['module'], path=path,
                    evidence=evidence, export_basis=export_basis, raw_page=module.get('page'))
        if 'property' in data.get('decorators', []):
            data['kind'] = 'property'
        if qualified in rows and evidence == 'runtime':
            # Runtime confirms re-exports and signatures; source retains decorators/docs.
            old = rows[qualified]
            for key in ('signature', 'parameters', 'returns', 'origin'):
                if data.get(key) is not None:
                    old[key] = data[key]
            for key in ('kind', 'binding'):
                if data.get(key) is not None:
                    old[key] = data[key]
            if not old.get('docstring'):
                old['docstring'] = data.get('docstring')
            old['evidence'] = 'source + runtime'
        rows.setdefault(qualified, data)
        if item.get('kind') == 'class':
            initializer = next((m for m in item.get('members', []) if m['name'] == '__init__'), None)
            if initializer and evidence == 'source':
                init_params = initializer.get('parameters', [])
                params = init_params if 'staticmethod' in initializer.get('decorators', []) else init_params[1:]
                rows[qualified]['parameters'] = params
                sig = initializer.get('signature', '')
                if sig:
                    rows[qualified]['signature'] = item['name'] + parameter_signature(params)
                rows[qualified]['constructor_docstring'] = initializer.get('docstring')
            for member in item.get('members', []):
                if not member['name'].startswith('_') and member.get('kind') in ('function', 'async function', 'property'):
                    decorators = member.get('decorators', [])
                    binding = member.get('binding') or ('static' if 'staticmethod' in decorators else ('class' if 'classmethod' in decorators else 'instance'))
                    member_data = dict(member, binding=binding)
                    if item.get('alias_of'):
                        member_data['alias_of'] = item['alias_of'] + '.' + member['name']
                    add(module, member_data, f'{path}.{member["name"]}', evidence, 'public member name')

    def source_symbol(module_name, name, seen=None):
        seen = set() if seen is None else seen
        if (module_name, name) in seen or module_name not in modules:
            return None
        seen.add((module_name, name))
        module = modules[module_name]
        own = next((m for m in module['members'] if m['name'] == name and m['kind'] in ('function', 'async function', 'class')), None)
        if own:
            return own
        for imp in (m for m in module['members'] if m['kind'] == 'import' and m.get('from_module') is not None):
            for binding in imp.get('bindings', []):
                if binding['local'] == name:
                    target = resolve_import(module, imp)
                    found = source_symbol(target, binding['imported'], seen)
                    if found:
                        return dict(found, name=name, alias_of=found.get('alias_of') or f'{target}.{binding["imported"]}')
        return None

    def resolve_import(module, imp):
        if not imp.get('level'):
            return imp.get('from_module') or ''
        parts = module['module'].split('.')
        is_package = Path(module.get('source', '')).name in ('__init__.py', '__init__.pyi')
        package = parts if is_package else parts[:-1]
        up = imp['level'] - 1
        if up:
            package = package[:-up]
        return '.'.join([*package, *([imp['from_module']] if imp.get('from_module') else [])])

    for module in modules.values():
        if not is_public_module(module['module']):
            continue
        exports = module.get('exports')
        basis = '__all__' if exports is not None else 'name heuristic'
        for item in module['members']:
            name = item['name']
            public = name in exports if exports is not None else not name.startswith('_')
            if public and item['kind'] in ('function', 'async function', 'class'):
                add(module, item, export_basis=basis)
            elif item['kind'] == 'import' and item.get('from_module') is not None:
                for binding in item.get('bindings', []):
                    name = binding['local']
                    if binding['imported'] == '*' or (name not in exports if exports is not None else name.startswith('_')):
                        continue
                    target = resolve_import(module, item)
                    own = source_symbol(target, binding['imported'])
                    if own:
                        add(module, dict(own, name=name, alias_of=own.get('alias_of') or f'{target}.{binding["imported"]}'), export_basis=basis)

    for module in report.get('runtime_modules', []):
        if not is_public_module(module['module']) or 'error' in module:
            continue
        exports = module.get('exports')
        source = modules.get(module['module'], {})
        assignments = {m['name'] for m in source.get('members', []) if m['kind'] == 'assignment' and m['name'].isidentifier()}
        root = module['module'].split('.')[0]
        for item in module.get('members', []):
            origin = item.get('origin') or ''
            # Imported helpers from dependencies are usually not part of this package.
            # Retain explicit exports, source-resolved aliases, and assigned public aliases.
            if exports is None and not (origin == root or origin.startswith(root + '.') or item['name'] in assignments or f'{module["module"]}.{item["name"]}' in rows):
                continue
            if (item['name'] in exports if exports is not None else not item['name'].startswith('_')) and item.get('kind') in ('function', 'async function', 'class'):
                add(module, item, evidence='runtime', export_basis='runtime __all__' if exports is not None else 'runtime name heuristic')
    return sorted(rows.values(), key=lambda r: (r['module'].count('.'), r['module'], r['path']))


def inspection_code(item):
    code = f"import importlib\nimport inspect\n\nm = importlib.import_module({item['module']!r})\nobj = m\n"
    for part in item['path'].split('.'):
        code += f"obj = inspect.getattr_static(obj, {part!r})\n"
    code += "if isinstance(obj, (staticmethod, classmethod)):\n    obj = obj.__func__\n"
    code += "print(inspect.getdoc(obj) or 'No docstring supplied')\ntry:\n    print(inspect.signature(obj))\nexcept (TypeError, ValueError):\n    print('Signature unavailable')\nhelp(obj)"
    return code


def call_template(item):
    """Show correct argument passing without claiming valid input values."""
    if 'parameters' not in item and item.get('kind') != 'property':
        return None
    parameters = [p for p in caller_parameters(item) if p['required']]
    code = f"import importlib\nm = importlib.import_module({item['module']!r})\n"
    for parameter in parameters:
        code += f"{parameter['name']} = ...  # TODO: supply a valid value from your application\n"
    arguments = ', '.join(p['name'] if p['kind'] in ('positional-only', 'positional only') else f"{p['name']}={p['name']}" for p in parameters)
    path = item['path']
    decorators = item.get('decorators', [])
    if item.get('binding') == 'instance':
        code += f"instance = ...  # TODO: construct m.{path.rsplit('.', 1)[0]} using its constructor page\n"
        target = 'instance.' + path.rsplit('.', 1)[1]
    else:
        target = 'm.' + path
    if item.get('kind') == 'property' or 'property' in decorators:
        code += f'result = {target}\n'
    elif item['kind'] == 'async function':
        code += f'async def practice():\n    result = await {target}({arguments})\n    return result\n# Run practice() in your application event loop after replacing placeholders.\n'
    else:
        code += f'result = {target}({arguments})\nprint(result)\n'
    return code


def caller_parameters(item):
    """Receiver identity follows method binding, never a parameter's spelling."""
    parameters = item.get('parameters', [])
    if item.get('binding') in ('instance', 'class') and parameters and parameters[0]['kind'] in ('positional-only', 'positional only', 'positional or keyword'):
        return parameters[1:]
    return parameters


def write_api_page(item, fence):
    doc = item.get('docstring') or ''
    details = doc_details(doc + '\n' + (item.get('constructor_docstring') or ''))
    kind = 'property' if 'property' in item.get('decorators', []) else item['kind']
    lines = [f"# {item['qualified']}\n", '[API index](../API_INDEX.md)  |  [Quick start](../QUICKSTART.md)\n',
             summary(doc) + '\n', f"Kind: **{kind}**. Evidence: **{item['evidence']}**. Discovery: **{item['export_basis']}**.\n"]
    official = item.get('official_documentation')
    if official:
        lines.extend(['## Supplement from official documentation\n',
                      f"Source: [{item['qualified']}]({official['url']}). Retrieved {official['retrieved_at']}. Documentation version: **{official['version_status']}**.\n",
                      f"Source selection: {official['source_basis']}.\n",
                      ('Reused downloaded HTML; the retrieval date above is the original download date. The cache may be stale.\n' if official.get('from_cache') else ''),
                      'Fetched material supplements missing local fields. Local signatures and original docstrings remain unchanged. Online examples are not executed.\n'])
        for source in official.get('sources', [])[1:]:
            lines.append(f"Additional source: [API section]({source['url']}). Retrieved {source['retrieved_at']}.\n")
        for field, source in official.get('field_sources', {}).items():
            state = 'cached download' if source['from_cache'] else 'live download'
            lines.append(f"{field.capitalize()} source: [API section]({source['url']}); {state}; retrieved {source['retrieved_at']}.\n")
        if official.get('description'):
            lines.extend(['### Description missing locally\n', fence(official['description'])])
        for field in ('parameters', 'returns', 'raises'):
            if official.get(field):
                lines.extend([f'### Additional {field} information\n', fence(official[field])])
        if official.get('examples'):
            lines.append('### Examples missing locally\n')
            for example in official['examples']:
                lines.append(fence(example['code'], 'python' if example['python_syntax_valid'] else 'text'))
                if example.get('expected'):
                    lines.extend(['Expected output copied from the documentation:\n', fence(example['expected'])])
    if item.get('alias_of'):
        lines.append(f"Re-export of `{item['alias_of']}`.\n")
    if item.get('conditional'):
        lines.append('Defined conditionally in source; availability and the selected implementation depend on the environment.\n')
    if item.get('inherited'):
        lines.append('Inherited class member.\n')
    if item.get('signature'):
        lines.extend(['## Signature\n', fence(item['signature'], 'text')])
    else:
        lines.append('Signature unavailable. Inspect the docstring before calling this API.\n')
    if item.get('overload_signatures'):
        lines.extend(['### Type overloads\n',
                      'Alternative signatures declared for type checking; the implementation signature and docstring above are used when available.\n',
                      fence('\n'.join(item['overload_signatures']))])
        if item.get('overload_only'):
            lines.append('Only overload declarations were found in source; the runtime implementation remains unresolved.\n')
    parameters = caller_parameters(item)
    lines.extend(['## Inputs\n'])
    if parameters:
        lines.append('| Parameter | Passing style | Required | Type | Default | Description |\n| --- | --- | --- | --- | --- | --- |')
        for p in parameters:
            detail = details['parameters'].get(p['name'], {})
            default = p.get('default') if p.get('default') is not None else ('-' if p['required'] else 'Collects extra arguments')
            lines.append('| ' + ' | '.join(cell(x) for x in (p['name'], p['kind'], 'Yes' if p['required'] else 'No', p.get('annotation') or detail.get('type'), default, detail.get('description') or 'Not described in the docstring')) + ' |')
        lines.append('')
    elif 'parameters' in item:
        lines.append('No caller-supplied parameters are declared.\n')
    else:
        lines.append('Parameter details unavailable.\n')
    documented_options = {name: value for name, value in details['parameters'].items() if name not in {p['name'] for p in item.get('parameters', [])} and name not in ('self', 'cls')}
    if documented_options:
        lines.extend(['### Additional inputs documented by the package\n',
                      'These names appear in the docstring but not as explicit signature parameters. They may be forwarded through `**kwargs`; verify the documented call path before passing them. Required status and defaults are not inferred.\n',
                      '| Name | Documented type | Description |\n| --- | --- | --- |'])
        for name, detail in documented_options.items():
            lines.append('| ' + ' | '.join(cell(x) for x in (name, detail.get('type'), detail.get('description') or 'Not described')) + ' |')
        lines.append('')
    lines.extend(['## Returns and exceptions\n', f"Return annotation: `{cell(item.get('returns'))}`.\n"])
    if details['returns']:
        lines.append('Documented return/yield information:\n\n' + '\n'.join('- ' + cell(x) for x in details['returns']) + '\n')
    else:
        lines.append('Return behavior is not separately documented; consult the original docstring below.\n')
    if details['raises']:
        lines.append('Documented exceptions:\n\n' + '\n'.join('- ' + cell(x) for x in details['raises']) + '\n')
    else:
        lines.append('No exception section was extracted. This does not mean the call cannot raise.\n')
    examples = setup_complete_examples(examples_from_doc(doc))
    lines.append('## Practice\n')
    if examples:
        lines.append('### Before running\n')
        lines.extend('- ' + note for note in practice_prerequisites(item, examples))
        lines.append('\n')
        lines.append('Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.\n')
        if any(e.get('format') == 'doctest session' for e in examples):
            lines.append('Doctest sessions preserve command order and shared state within each block. Read the original docstring for context between blocks; later sessions may require earlier setup. Run related sessions in order in the same interpreter. Expected output is copied separately, not validated.\n')
        for number, example in enumerate(examples, 1):
            lines.append(f'### Package example {number}\n')
            lines.append(f"Source format: {example.get('format', 'doctest')}.\n")
            try:
                ast.parse(example['code'])
                language = 'python'
            except SyntaxError:
                language = 'text'
            lines.append(fence(example['code'], language))
            if example.get('with_setup'):
                lines.extend(['#### Copy with earlier setup\n', 'This optional copy includes statically selected earlier setup statements. Setup may call external services; review it before execution. The original example above remains unchanged.\n', fence(example['with_setup'], 'python')])
            if example.get('unresolved_names'):
                lines.append('Names still supplied by application/context: ' + ', '.join('`' + name + '`' for name in example['unresolved_names']) + '.\n')
            if example['expected']:
                lines.extend(['Expected output recorded in the docstring:\n', fence(example['expected'])])
    else:
        lines.append('No supported Python code-fence or doctest usage example was found. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.\n')
    template = call_template(item)
    if template:
        lines.extend(['### Call template - edit before running\n',
                      'Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.\n',
                      fence(template, 'python')])
    if item.get('binding'):
        owner = item['path'].rsplit('.', 1)[0]
        if item['binding'] == 'instance':
            lines.append(f'Construct `{item["module"]}.{owner}` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.\n')
        elif item['binding'] == 'class':
            lines.append(f'Call this member through `{item["module"]}.{owner}`. Python supplies its first positional class receiver automatically.\n')
        else:
            lines.append(f'Call this static member through `{item["module"]}.{owner}`. All declared parameters are caller-supplied, including parameters named `self` or `cls`.\n')
    if item.get('decorators'):
        lines.append('Decorators: ' + ', '.join('`' + x + '`' for x in item['decorators']) + '.\n')
    if item.get('related_members'):
        lines.extend(['## Public members\n', '| Member | Kind | Purpose |\n| --- | --- | --- |'])
        for member in item['related_members']:
            lines.append(f"| [{member['path'].rsplit('.', 1)[-1]}]({Path(member['page']).name}) | {cell(member['kind'])} | {cell(member['summary'])} |")
        lines.append('')
    if item.get('related_references'):
        lines.extend(['## Related APIs mentioned in the docstring\n'])
        for related in item['related_references']:
            lines.append(f"- [{related['qualified']}]({Path(related['page']).name}) - {cell(related['summary'])}")
        lines.append('')
    lines.extend(['### Inspect this exact API\n', fence(inspection_code(item), 'python'),
                  '## Original docstring\n', fence(doc or 'No docstring supplied.')])
    if item.get('constructor_docstring'):
        lines.extend(['### Constructor docstring\n', fence(item['constructor_docstring'])])
    if item.get('raw_page'):
        lines.append(f"[Full module inspection](../{item['raw_page']})\n")
    return '\n'.join(lines)


SEARCH_SCRIPT = '''"""Search generated API names, signatures and descriptions; imports no target package."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('query', nargs='?', default='')
parser.add_argument('--limit', type=int, default=20)
args = parser.parse_args()
if args.limit < 1:
    parser.error('--limit must be positive')
root = Path(__file__).resolve().parent
rows = json.loads((root / 'api_index.json').read_text(encoding='utf-8'))
terms = args.query.casefold().split()
matches = [r for r in rows if all(t in (' '.join(str(r.get(k) or '') for k in ('qualified', 'signature', 'summary'))).casefold() for t in terms)]
matches.sort(key=lambda r: (r['qualified'].rsplit('.', 1)[-1].casefold() != args.query.casefold(), r['qualified'].count('.'), r['qualified']))
for item in matches[:args.limit]:
    print(item['qualified'])
    print('  ' + (item.get('signature') or 'Signature unavailable'))
    print('  ' + item['summary'])
    print('  ' + str(root / item['page']))
print(f'{len(matches)} matches; showing {min(len(matches), args.limit)}')
'''


GENAI_TASKS = {
    'langchain': [('Build an agent with tools', 'langchain.agents.create_agent'),
                  ('Define a tool', 'langchain.tools.tool'),
                  ('Initialize a chat model', 'langchain.chat_models.init_chat_model')],
    'langgraph': [('Define graph state', 'langgraph.graph.StateGraph'),
                  ('Add a graph node', 'langgraph.graph.StateGraph.add_node'),
                  ('Connect nodes', 'langgraph.graph.StateGraph.add_edge'),
                  ('Compile the graph', 'langgraph.graph.StateGraph.compile'),
                  ('Run the compiled graph', 'langgraph.pregel.Pregel.invoke'),
                  ('Stream graph results', 'langgraph.pregel.Pregel.stream')],
    'langsmith': [('Trace a function', 'langsmith.traceable'),
                  ('Connect to LangSmith', 'langsmith.Client'),
                  ('Evaluate a dataset', 'langsmith.evaluate'),
                  ('Create a dataset', 'langsmith.Client.create_dataset'),
                  ('Add dataset examples', 'langsmith.Client.create_examples')],
}


def task_rows(package, rows):
    lookup = {row['qualified']: row for row in rows}
    return [(label, lookup[name]) for label, name in GENAI_TASKS.get(package, []) if name in lookup]


def write_developer_docs(out, report, fence):
    rows = collect_apis(report)
    options = report.get('official_docs_options', {})
    if options.get('enabled'):
        from official_docs import enrich_apis
        report['official_documentation'] = enrich_apis(rows, report, out, options, doc_details, examples_from_doc)
    api = out / 'api'
    api.mkdir(exist_ok=True)
    for number, item in enumerate(rows):
        item['page'] = f'api/{number:05d}-{item["qualified"]}.md'
        item['summary'] = summary(item.get('docstring') or item.get('official_documentation', {}).get('description'))
    for item in rows:
        item['practice_requirements'] = report.get('requirements', [])
        if item['kind'] == 'class':
            item['related_members'] = [m for m in rows if m['qualified'].startswith(item['qualified'] + '.') and m['qualified'].count('.') == item['qualified'].count('.') + 1]
        references = set(re.findall(r'``([\w.]+)``|:(?:class|func|meth):`([\w.]+)(?:[^`]*)`', item.get('docstring') or ''))
        names = {a or b for a, b in references}
        owner = item['path'].rsplit('.', 1)[0] if '.' in item['path'] else ''
        item['related_references'] = [r for r in rows if r['module'] == item['module'] and r['qualified'] != item['qualified'] and (r['path'] in names or (owner and r['path'].startswith(owner + '.') and r['path'].rsplit('.', 1)[-1] in names))]
        (out / item['page']).write_text(write_api_page(item, fence), encoding='utf-8')
    compact = [{k: item.get(k) for k in ('qualified', 'module', 'kind', 'signature', 'summary', 'page', 'evidence')} for item in rows]
    (out / 'api_index.json').write_text(json.dumps(compact, ensure_ascii=False, indent=2), encoding='utf-8')
    (out / 'search_api.py').write_text(SEARCH_SCRIPT, encoding='utf-8')
    table = ['# API index\n', '[Quick start](QUICKSTART.md)  |  [Package overview](README.md)\n',
             'Search this page in your editor or run `python search_api.py "keyword"`. Public names are candidates, not a guarantee of API stability. Private definitions and raw imports remain in [full inspection](REFERENCE.md).\n']
    for module in dict.fromkeys(r['module'] for r in rows):
        table.extend([f'## {module}\n', '| API | Kind | Purpose from docstring |\n| --- | --- | --- |'])
        for item in (r for r in rows if r['module'] == module and '.' not in r['path']):
            table.append(f"| [{item['path']}]({item['page']}) | {cell(item['kind'])} | {cell(item['summary'])} |")
        table.append('')
    table.insert(3, 'The index lists module-level functions and classes. Open a class page for its member table, or use search to find methods directly.\n')
    if not rows:
        table.append('No public callables could be resolved. See full inspection; try `--runtime` for dynamic APIs.\n')
    (out / 'API_INDEX.md').write_text('\n'.join(table), encoding='utf-8')
    import_modules = sorted({r['module'] for r in rows}, key=lambda name: (name.count('.'), name))
    quick = ['# Quick start\n', '[API index](API_INDEX.md)  |  [Package overview](README.md)\n',
             '1. Search for the operation you need in the API index.\n2. Open its API page and check required inputs, passing style, return information, and documented exceptions.\n3. Run the exact inspection snippet in the package environment.\n4. Try a package-authored example if available, then adapt it to a small local input.\n',
             '## Install or recreate the environment\n', fence(f'python -m venv .practice-venv\n# Windows PowerShell:\n& .\\.practice-venv\\Scripts\\python.exe -m pip install "{report["package"]}=={report["version"]}"\n& .\\.practice-venv\\Scripts\\python.exe', 'powershell'),
             'On Linux/macOS, use `.practice-venv/bin/python` in place of the Windows interpreter. If the inspection environment was retained, you can use its interpreter directly.\n',
             '## Available public modules\n', fence('\n'.join(import_modules) or 'No public modules resolved.')]
    tasks = task_rows(report['package'], rows)
    if tasks:
        navigation = ['## Choose a task\n', 'Open an API page for its inputs, package-authored examples, and original docstring. These links are navigation, not tested recipes.\n']
        for label, row in tasks:
            navigation.append(f"- {label}: [{row['qualified']}]({row['page']})")
        navigation.append('\n')
        quick[2:2] = navigation
    if rows:
        quick.extend(['## First inspection\n', 'This inspects an API without calling it. It imports the package.\n', fence(inspection_code(tasks[0][1] if tasks else rows[0]), 'python')])
    if report.get('package_type') == 'standard-library':
        start = quick.index('## Install or recreate the environment\n')
        stop = quick.index('## Available public modules\n')
        quick[start:stop] = ['## Use the documented Python interpreter\n',
                            f'This module ships with Python {report["version"]}. There is no pip package to install. Use this interpreter or another installation of the same Python version:\n',
                            fence(f'& "{report["executable"]}"', 'powershell')]
    quick.extend(['## Search locally\n', fence('python search_api.py "keyword"\npython search_api.py --limit 10', 'powershell'),
                  'Search runs using any Python 3.11+ interpreter and does not require the package or its venv.\n',
                  '## Example reliability\n', 'Python code fences and doctest-style examples already present in installed docstrings are extracted. They may require setup, files, credentials, or dependencies. Output comments in fenced examples are preserved, not interpreted as verified results. No API calls or docstring examples are executed during generation. Missing examples and descriptions are shown explicitly.\n'])
    (out / 'QUICKSTART.md').write_text('\n'.join(quick), encoding='utf-8')
    # Keep the existing full report as an appendix; do not lose source evidence.
    if not (out / 'REFERENCE.md').exists():
        (out / 'README.md').rename(out / 'REFERENCE.md')
    coverage = {'public_api_candidates': len(rows), 'with_docstrings': sum(bool(r.get('docstring')) for r in rows),
                'with_signatures': sum(bool(r.get('signature')) for r in rows),
                'with_docstring_examples': sum(bool(examples_from_doc(r.get('docstring'))) for r in rows)}
    report['developer_documentation'] = coverage
    (out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    meta = report['metadata']
    def field(name):
        return ', '.join(meta.get(name) or []) or 'Not declared'
    readme = [f'# {report["package"]} {report["version"]}\n', field('Summary') + '\n',
              '## Start here\n', '- [Quick start and practice workflow](QUICKSTART.md)\n- [Public API index](API_INDEX.md)\n- [Full metadata, module inspection, and bundled files](REFERENCE.md)\n',
              '## Find an operation\n', fence('python search_api.py "keyword"', 'powershell'),
              'Search names, signatures, and docstring summaries without importing the package. Open the returned API page for inputs, returns, exceptions, and practice material.\n',
              '## Package facts\n', '| Fact | Value |\n| --- | --- |', f'| Python requirement | {cell(field("Requires-Python"))} |',
              f'| License metadata | {cell(field("License-Expression") if meta.get("License-Expression") else field("License"))} |',
              f'| Discovered public API candidates | {coverage["public_api_candidates"]} |', f'| APIs with signatures | {coverage["with_signatures"]} |',
              f'| APIs with docstrings | {coverage["with_docstrings"]} |', f'| APIs with docstring examples | {coverage["with_docstring_examples"]} |',
              f'| Recorded inspection gaps/errors | {len(report["errors"])} |\n',
              '## Inspection environment\n', fence(f'Python: {report["executable"]}\nEnvironment: {report["environment"]}'),
              ('The inspection interpreter is no longer available. The paths above record inspection provenance. Recreate the environment using Quick start before practice.\n' if not Path(report['executable']).is_file() else 'The inspection interpreter is available. Use it for practice, or recreate the environment using Quick start.\n'),
              '## Dependencies\n', fence('\n'.join(report['requirements']) or 'None declared.'),
              '## Coverage and limits\n', 'Public APIs are selected using a statically resolved `__all__` where available, otherwise public names. Resolvable local re-exports are included. Runtime mode adds loaded callables and classes, including compiled APIs. Internal/test/vendor modules and private members remain in full inspection. Parameter documentation is parsed from common Google, NumPy, and Sphinx styles; consult original docstrings when extraction is incomplete. Missing return behavior or examples is not invented. Static aliases, dynamic exports, and optional imports can remain unresolved.\n']
    if report['errors']:
        readme.extend(['## Inspection gaps\n', fence('\n'.join(report['errors']))])
    if report.get('official_documentation'):
        info = report['official_documentation']
        readme.extend(['## Official documentation fallback\n',
                       f"Supplemented APIs: {info['enriched_apis']}. Fetched pages: {info['fetched_pages']}. Cached pages reused: {info.get('cached_pages', 0)}. APIs with unresolved fields: {len(info['unresolved_apis'])}. Retrieval errors: {len(info['errors'])}. See [retrieval details](official_docs/retrieval.json).\n",
                       'External documentation is supplemental. Package metadata identifies package-declared sources; third-party documentation versions are not automatically verified. Missing API anchors or unsupported page layouts remain unresolved.\n'])
    (out / 'README.md').write_text('\n'.join(readme), encoding='utf-8')
