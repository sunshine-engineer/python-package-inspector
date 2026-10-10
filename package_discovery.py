#!/usr/bin/env python3
"""Build Markdown for PyPI packages or Python standard-library modules (Python 3.11+).

Use --installed to inspect the current environment without installation.
Standard-library modules automatically skip pip and venv creation.
Static inspection never imports the target package during documentation generation.
Optional runtime inspection imports it in subprocesses; this is not a sandbox.
"""
from __future__ import annotations

import argparse
import ast
import importlib
import importlib.metadata as metadata
import importlib.machinery
from email.message import Message
import inspect
import json
import math
import os
import re
import shutil
import subprocess
import sys
import sysconfig
import tempfile
import tokenize
import venv
from pathlib import Path


class StandardLibraryModule:
    """Source inventory adapter; metadata here describes Python, not a PyPI distribution."""
    def __init__(self, name):
        self.version = '.'.join(map(str, sys.version_info[:3]))
        self.requires = []
        self.entry_points = []
        self.metadata = Message()
        self.metadata['Name'] = name
        self.metadata['Python-Version'] = self.version
        self.metadata['Summary'] = 'Python standard-library module; included with this interpreter, not installed from PyPI.'
        self.root = Path(sysconfig.get_path('stdlib')).resolve()
        self.module_aliases = {}
        candidate = self.root.joinpath(*name.split('.'))
        if (candidate / '__init__.py').is_file():
            paths = sorted(candidate.rglob('*.py'))
        elif candidate.with_suffix('.py').is_file():
            paths = [candidate.with_suffix('.py')]
        else:
            search = [str(self.root), sysconfig.get_config_var('DESTSHARED') or str(self.root), str(Path(sys.base_prefix) / 'DLLs')]
            spec = importlib.machinery.BuiltinImporter.find_spec(name) or importlib.machinery.FrozenImporter.find_spec(name) or importlib.machinery.PathFinder.find_spec(name, search)
            if spec is None and '.' in name:
                # Dotted imports can be aliases (os.path -> ntpath/posixpath).
                # Resolve using isolated Python so project paths cannot shadow stdlib.
                probe = subprocess.run([sys.executable, '-I', '-c',
                    "import importlib.util,json,sys; s=importlib.util.find_spec(sys.argv[1]); print(json.dumps(None if s is None else {'name':s.name,'origin':s.origin}))", name],
                    capture_output=True, text=True, timeout=10)
                if probe.returncode == 0:
                    info = json.loads(probe.stdout)
                    if info:
                        spec = importlib.machinery.ModuleSpec(info['name'], loader=None, origin=info['origin'])
            if spec is None:
                raise ImportError(f'{name} is unavailable in this Python installation')
            self.module_aliases[spec.name] = name
            origin = Path(spec.origin) if spec.origin and spec.origin not in ('built-in', 'frozen') else self.root / (spec.name.replace('.', '/') + '.py')
            paths = [origin] if origin.suffix == '.py' and origin.is_file() and origin.resolve().is_relative_to(self.root) else []
        self.files = []
        for path in paths:
            item = metadata.PackagePath(path.relative_to(self.root).as_posix())
            item.size = path.stat().st_size
            item.hash = None
            self.files.append(item)

    def locate_file(self, file):
        return self.root / str(file)

    def read_text(self, name):
        return None


def fence(value: str, language: str = "text") -> str:
    runs = re.findall(r"`+", value)
    delimiter = "`" * max(3, max((len(x) + 1 for x in runs), default=3))
    return f"{delimiter}{language}\n{value}\n{delimiter}\n"


def expression(node):
    return ast.unparse(node) if node is not None else None


def source_parameters(arguments):
    parameters = []
    positional = [*arguments.posonlyargs, *arguments.args]
    defaults = [None] * (len(positional) - len(arguments.defaults)) + list(arguments.defaults)
    for number, (arg, default) in enumerate(zip(positional, defaults)):
        parameters.append({'name': arg.arg, 'kind': 'positional-only' if number < len(arguments.posonlyargs) else 'positional or keyword',
                           'annotation': expression(arg.annotation), 'default': expression(default), 'required': default is None})
    if arguments.vararg:
        parameters.append({'name': arguments.vararg.arg, 'kind': 'variadic positional', 'annotation': expression(arguments.vararg.annotation), 'default': None, 'required': False})
    for arg, default in zip(arguments.kwonlyargs, arguments.kw_defaults):
        parameters.append({'name': arg.arg, 'kind': 'keyword-only', 'annotation': expression(arg.annotation), 'default': expression(default), 'required': default is None})
    if arguments.kwarg:
        parameters.append({'name': arguments.kwarg.arg, 'kind': 'variadic keyword', 'annotation': expression(arguments.kwarg.annotation), 'default': None, 'required': False})
    return parameters


def static_api(tree):
    """Preserve source signatures, including positional-only and keyword-only args."""
    result = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            signature = f"{node.name}({ast.unparse(node.args)})"
            if node.returns:
                signature += f" -> {expression(node.returns)}"
            result.append({"name": node.name, "kind": "async function" if isinstance(node, ast.AsyncFunctionDef) else "function",
                           "signature": signature, "line": node.lineno,
                           "decorators": [expression(d) for d in node.decorator_list],
                           "parameters": source_parameters(node.args), "returns": expression(node.returns),
                           "docstring": ast.get_docstring(node, clean=False)})
        elif isinstance(node, ast.ClassDef):
            result.append({"name": node.name, "kind": "class", "line": node.lineno,
                           "bases": [expression(b) for b in node.bases],
                           "decorators": [expression(d) for d in node.decorator_list],
                           "docstring": ast.get_docstring(node, clean=False), "members": static_api(node)})
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            result.append({"name": ", ".join(expression(t) for t in targets), "kind": "assignment",
                           "line": node.lineno, "source": ast.unparse(node)})
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            result.append({"name": ast.unparse(node), "kind": "import", "line": node.lineno,
                           "from_module": node.module if isinstance(node, ast.ImportFrom) else None,
                           "level": node.level if isinstance(node, ast.ImportFrom) else 0,
                           "bindings": [{"imported": alias.name, "local": alias.asname or alias.name.split('.')[0]} for alias in node.names]})
        elif isinstance(node, (ast.If, ast.Try, ast.With)):
            # Include conditional definitions, but label their source context.
            for branch in [node.body, getattr(node, "orelse", []), getattr(node, "finalbody", [])] + [h.body for h in getattr(node, "handlers", [])]:
                for item in static_api(ast.Module(body=branch, type_ignores=[])):
                    item["conditional"] = True
                    result.append(item)
    return result


def runtime_object(name, obj):
    item = {"name": name, "kind": 'class' if inspect.isclass(obj) else ('async function' if inspect.iscoroutinefunction(obj) else ('function' if callable(obj) else type(obj).__name__)),
            "origin": getattr(obj, '__module__', None)}
    try:
        item["docstring"] = inspect.getdoc(obj)
    except Exception as exc:
        item["docstring_error"] = str(exc)
    if callable(obj):
        try:
            item.update(runtime_object_signature(obj))
        except (ValueError, TypeError) as exc:
            item["signature_error"] = str(exc)
    if inspect.isclass(obj):
        item["members"] = []
        for key, value in inspect.getmembers_static(obj):
            decorator = 'staticmethod' if isinstance(value, staticmethod) else ('classmethod' if isinstance(value, classmethod) else None)
            if isinstance(value, (staticmethod, classmethod)):
                value = value.__func__
            member = {"name": key, "kind": 'property' if isinstance(value, property) else ('async function' if inspect.iscoroutinefunction(value) else ('function' if callable(value) else type(value).__name__)),
                      "binding": 'static' if decorator == 'staticmethod' else ('class' if decorator == 'classmethod' else ('instance' if callable(value) or isinstance(value, property) else None)),
                      "decorators": [decorator] if decorator else [], "inherited": key not in vars(obj)}
            try:
                member["docstring"] = inspect.getdoc(value)
                if callable(value):
                    details = runtime_object_signature(value)
                    member.update(details)
            except Exception as exc:
                member["inspection_error"] = str(exc)
            item["members"].append(member)
    return item


def runtime_object_signature(obj):
    signature = inspect.signature(obj)
    return {'signature': str(signature), 'parameters': [
        {'name': p.name, 'kind': p.kind.name.lower().replace('_', ' '),
         'annotation': None if p.annotation is inspect.Parameter.empty else inspect.formatannotation(p.annotation),
         'default': None if p.default is inspect.Parameter.empty else repr(p.default),
         'required': p.default is inspect.Parameter.empty and p.kind not in (p.VAR_POSITIONAL, p.VAR_KEYWORD)}
        for p in signature.parameters.values()],
        'returns': None if signature.return_annotation is inspect.Signature.empty else inspect.formatannotation(signature.return_annotation)}


def worker(module, output):
    try:
        obj = importlib.import_module(module)
        result = {"module": module, "docstring": inspect.getdoc(obj),
                  "exports": vars(obj).get('__all__') if isinstance(vars(obj).get('__all__'), (list, tuple)) and all(isinstance(x, str) for x in vars(obj).get('__all__', [])) else None,
                  "members": [runtime_object(k, v) for k, v in inspect.getmembers_static(obj)]}
    except BaseException as exc:
        result = {"error": f"{type(exc).__name__}: {exc}"}
    Path(output).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


def module_name(file):
    parts = list(Path(str(file)).parts)
    if any(p.endswith((".dist-info", ".egg-info")) or p in ("..", "__pycache__") for p in parts):
        return None
    if not parts:
        return None
    leaf = parts[-1]
    if leaf.endswith((".py", ".pyi")):
        parts[-1] = leaf.rsplit(".", 1)[0]
    elif leaf.endswith((".so", ".pyd")):
        parts[-1] = leaf.split(".", 1)[0]
    else:
        return None
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts) if parts and all(p.isidentifier() for p in parts) else None


def render_members(items, depth=2):
    output = []
    for item in items:
        output.append(f"{'#' * min(depth, 6)} {item['name']}\n")
        output.append(fence(json.dumps({k: v for k, v in item.items() if k not in ('docstring', 'members')}, ensure_ascii=False, indent=2), "json"))
        output.append(fence(item.get("docstring") or "No docstring available."))
        output.extend(render_members(item.get("members", []), depth + 1))
    return output


def create_output(base, slug, automatic):
    """Create missing parents and preserve previous runs with numbered defaults."""
    base.mkdir(parents=True, exist_ok=True)
    number = 1
    while True:
        candidate = base / (slug if number == 1 else f"{slug}-{number}")
        try:
            candidate.mkdir()
            return candidate
        except FileExistsError:
            if not automatic:
                raise
            number += 1


def install_and_run(args, parser):
    base = (args.output or Path('package_docs')).resolve()
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", f"{args.package}-{args.version or 'latest'}")
    if args.version is not None and args.output is not None and (base / slug).exists():
        parser.error(f"Output already exists: {base / slug}. Choose a fresh --output directory.")
    environments = base / '.venvs'
    environments.mkdir(parents=True, exist_ok=True)
    environment = Path(tempfile.mkdtemp(prefix=f'{slug}-', dir=environments))
    python = environment / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    # Prevent the caller's package paths from leaking into the isolated environment.
    clean_env = {k: v for k, v in os.environ.items() if k.upper() not in ('PYTHONPATH', 'PYTHONHOME')}
    clean_env['PYTHONIOENCODING'] = 'utf-8'
    cleanup_requested = getattr(args, 'cleanup_venv', False)
    clean_env['PACKAGE_DISCOVERY_CLEANUP_REQUESTED'] = '1' if cleanup_requested else '0'
    clean_env['PACKAGE_DISCOVERY_VERSION_SELECTION'] = 'pinned' if args.version is not None else 'latest-compatible'
    print(f'Creating environment: {environment}', flush=True)
    try:
        venv.EnvBuilder(with_pip=True).create(environment)
        requirement = f'{args.package}=={args.version}' if args.version is not None else args.package
        command = [str(python), '-m', 'pip', '--isolated', 'install', '--disable-pip-version-check']
        if args.version is None:
            command.append('--upgrade')
        command.append(requirement)
        print(f'Installing {requirement}' + (' (latest compatible stable release)' if args.version is None else ''), flush=True)
        result = subprocess.run(command, env=clean_env)
        if result.returncode:
            print(f'Installation failed; environment retained at {environment}. Documentation was not generated.', file=sys.stderr)
            return result.returncode
        child_args = [value for value in sys.argv[1:] if value != '--cleanup-venv']
        command = [str(python), str(Path(__file__).resolve()), *child_args, '--installed']
        result = subprocess.run(command, env=clean_env)
        if result.returncode:
            print(f'Generation failed; environment retained at {environment}.', file=sys.stderr)
            return result.returncode
        if cleanup_requested:
            try:
                remove_created_environment(environment, environments)
            except (OSError, ValueError) as exc:
                print(f'Documentation was generated, but venv cleanup failed: {exc}. Check {environment}.', file=sys.stderr)
                return 1
            print(f'Removed environment: {environment}', flush=True)
        return 0
    except (OSError, subprocess.SubprocessError) as exc:
        print(f'Environment setup failed: {exc}. Environment retained at {environment}.', file=sys.stderr)
        return 1


def remove_created_environment(environment, environments):
    """Remove only the fresh venv directly inside this run's environment parent."""
    environment = Path(environment)
    parent = Path(environments).resolve(strict=True)
    target = environment.resolve(strict=True)
    if environment.is_symlink() or target.parent != parent or not (target / 'pyvenv.cfg').is_file():
        raise ValueError('Refusing cleanup: target is not a venv directly inside the expected directory')
    shutil.rmtree(target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", help="Distribution name (beautifulsoup4) or standard-library module (json)")
    parser.add_argument("version", nargs='?', help="Exact version; omit to install the latest compatible stable release (with --installed: use current installed version)")
    parser.add_argument("--output", type=Path, help="Output parent (default: ./package_docs; repeated default runs get numbered folders)")
    parser.add_argument("--installed", action="store_true", help="Inspect the current environment without creating a venv or installing")
    parser.add_argument("--cleanup-venv", action="store_true", help="Remove the newly created venv after successful generation; retain it on failure")
    parser.add_argument("--runtime", action="store_true", help="Import discovered modules in subprocesses (executes package code)")
    parser.add_argument("--module", action="append", default=[], help="Additional import name for runtime inspection; repeatable")
    parser.add_argument("--timeout", type=float, default=20, help="Runtime timeout per module in seconds")
    parser.add_argument('--official-docs', action='store_true', help='Fetch official/package-declared documentation to supplement missing local API details')
    parser.add_argument('--docs-url', help='Official HTTPS documentation URL; implies --official-docs')
    parser.add_argument('--docs-max-pages', type=int, default=10, help='Maximum documentation pages to fetch (default 10)')
    parser.add_argument('--docs-timeout', type=float, default=15, help='HTTP timeout per documentation request in seconds')
    parser.add_argument('--docs-cache', type=Path, help='Reuse HTML from a previous official_docs folder')
    parser.add_argument('--docs-offline', action='store_true', help='Enrich only from --docs-cache; never fetch documentation over the network')
    args = parser.parse_args()
    if args.docs_offline and args.docs_cache is None:
        parser.error('--docs-offline requires --docs-cache pointing to a previous official_docs folder')
    if args.docs_cache is not None and not (args.docs_cache.is_dir() and (args.docs_cache / 'retrieval.json').is_file()):
        parser.error('--docs-cache must contain retrieval.json and downloaded HTML files')
    if args.docs_max_pages < 1 or not math.isfinite(args.docs_timeout) or args.docs_timeout <= 0:
        parser.error('Documentation page limit and timeout must be positive and finite')
    if args.docs_url:
        from official_docs import validate_url
        try:
            validate_url(args.docs_url)
        except ValueError as exc:
            parser.error(str(exc))
    standard_library = args.package.split('.')[0] in sys.stdlib_module_names
    if args.cleanup_venv and args.installed and not standard_library:
        parser.error('--cleanup-venv cannot be combined with --installed; no new venv is created')
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        parser.error("--timeout must be a finite positive number")
    if not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?', args.package):
        parser.error('package must be a distribution name, not a URL, path, or pip option')
    if args.version is not None and not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9.!+_-]*', args.version):
        parser.error('version must be an exact version, without ranges or wildcards')
    if standard_library:
        if args.version is not None:
            parser.error('Standard-library modules have no independent package version. Omit the version and use the required Python interpreter.')
        try:
            dist = StandardLibraryModule(args.package)
        except ImportError as exc:
            parser.error(str(exc))
        print(f'{args.package} is part of Python {dist.version}; skipping pip and venv creation.', flush=True)
        if args.cleanup_venv:
            print('--cleanup-venv has no effect: no environment was created.', flush=True)
        if not dist.files:
            args.runtime = True
            print('No Python source available; inspecting the loaded standard-library module.', flush=True)
    elif not args.installed:
        return install_and_run(args, parser)
    else:
        try:
            dist = metadata.distribution(args.package)
        except metadata.PackageNotFoundError:
            parser.error(f"{args.package!r} is not installed in {sys.executable}")
    if args.version is not None and dist.version != args.version:
        parser.error(f"Requested {args.version}; installed {dist.version}. Use the matching Python environment.")
    if args.version is None and not standard_library:
        print(f'Resolved package: {args.package}=={dist.version}', flush=True)
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", f"{args.package}-{'python-' if standard_library else ''}{dist.version}")
    try:
        out = create_output((args.output or Path('package_docs')).resolve(), slug, args.output is None)
    except FileExistsError:
        parser.error(f"Output already exists: {args.output.resolve() / slug}. Choose a fresh --output directory.")
    pages = out / "modules"
    pages.mkdir()
    bundled = out / "bundled"
    bundled.mkdir()
    fields = {key: dist.metadata.get_all(key) for key in dict.fromkeys(dist.metadata.keys())}
    files = list(dist.files or [])
    report = {"package": args.package, "version": dist.version, "python": sys.version,
              "requested_version": args.version,
              "version_selection": 'python-interpreter' if standard_library else os.environ.get('PACKAGE_DISCOVERY_VERSION_SELECTION', 'installed'),
              "package_type": 'standard-library' if standard_library else 'distribution',
              "official_docs_options": {'enabled': args.official_docs or bool(args.docs_url) or args.docs_cache is not None, 'url': args.docs_url,
                                       'max_pages': args.docs_max_pages, 'timeout': args.docs_timeout,
                                       'cache': str(args.docs_cache.resolve()) if args.docs_cache is not None else None,
                                       'offline': args.docs_offline},
              "executable": sys.executable, "environment": sys.prefix,
              "cleanup_requested": not standard_library and os.environ.get('PACKAGE_DISCOVERY_CLEANUP_REQUESTED') == '1',
              "metadata": fields, "requirements": dist.requires or [],
              "entry_points": [{"name": ep.name, "group": ep.group, "value": ep.value} for ep in dist.entry_points],
              "files": [], "modules": [], "errors": []}
    if dist.files is None:
        report["errors"].append("Distribution file inventory is unavailable; source discovery is incomplete.")
    for metadata_name in ("METADATA", "PKG-INFO", "WHEEL", "RECORD", "entry_points.txt", "top_level.txt", "direct_url.json", "INSTALLER", "REQUESTED"):
        raw = dist.read_text(metadata_name)
        if raw is not None:
            (bundled / f"metadata-{metadata_name}.md").write_text(
                f"# {metadata_name}\n\n" + fence(raw), encoding="utf-8")
    index = [f"# {args.package} {dist.version}\n", "## Scope and limitations\n",
             "This documents the installed distribution in this Python environment. Source inspection does not execute package code. Runtime mode executes imports and is not a security sandbox. Signatures and docstrings are evidence, not generated usage examples. Return behavior is only known when annotations or documentation describe it. Dynamic APIs, unavailable source, editable installs, and missing optional dependencies can leave gaps. Private names are included.\n",
             "## Installation metadata\n", fence(json.dumps(fields, ensure_ascii=False, indent=2), "json"),
             "## Dependencies\n", fence("\n".join(dist.requires or []) or "None declared."),
             "## Entry points\n", fence(json.dumps(report["entry_points"], indent=2), "json"), "## Module pages\n"]
    environment_note = ('Cleanup was requested for the temporary environment after generation. The paths above record the inspection environment; recreate the package environment before running manual queries if cleanup succeeds.\n'
                        if report['cleanup_requested'] else 'Run manual queries using this Python interpreter so they inspect the documented version.\n')
    index[1:1] = ['## Inspection environment\n', fence(f'Python: {sys.executable}\nEnvironment: {sys.prefix}'), environment_note]
    index.extend(f"- [Raw {p.stem}](bundled/{p.name})\n" for p in sorted(bundled.glob('metadata-*.md')))
    discovered = set(args.module) | ({args.package} if standard_library else set())
    for number, file in enumerate(files):
        path = Path(dist.locate_file(file))
        report["files"].append({"path": str(file), "size": file.size, "hash": str(file.hash) if file.hash else None})
        module = module_name(file)
        if standard_library:
            module = dist.module_aliases.get(module, module)
        if module:
            discovered.add(module)
        if module and path.suffix in (".py", ".pyi"):
            try:
                with tokenize.open(path) as stream:
                    tree = ast.parse(stream.read(), filename=str(path))
                data = {"module": module, "source": str(file), "docstring": ast.get_docstring(tree, clean=False), "members": static_api(tree)}
                data['exports'] = None
                for node in tree.body:
                    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == '__all__' for t in node.targets):
                        try:
                            value = ast.literal_eval(node.value)
                            if isinstance(value, (list, tuple)) and all(isinstance(x, str) for x in value):
                                data['exports'] = value
                        except (ValueError, TypeError):
                            pass
                report["modules"].append(data)
                page = f"{number:05d}-{module}.md"
                data['page'] = f'modules/{page}'
                text = [f"# {module}\n", f"Source: `{file}`\n", fence(data["docstring"] or "No module docstring."), "## Manual inspection\n",
                        fence(f"import importlib, inspect\nm = importlib.import_module({module!r})\ndir(m)\nhelp(m)\ninspect.getmembers_static(m)\n# For a discovered callable:\n# inspect.signature(m.function_name)\n# inspect.getdoc(m.function_name)\n# inspect.getsource(m.function_name)", "python")]
                text.extend(render_members(data["members"]))
                (pages / page).write_text("\n".join(text), encoding="utf-8")
                index.append(f"- [{module} ({path.suffix})](modules/{page})\n")
            except Exception as exc:
                report["errors"].append(f"{file}: {type(exc).__name__}: {exc}")
        if path.suffix.lower() in (".md", ".rst", ".txt") or path.name.lower().startswith(("license", "copying", "notice")):
            try:
                content = path.read_text(encoding="utf-8")
                page = f"{number:05d}.md"
                (bundled / page).write_text(f"# {file}\n\n" + fence(content), encoding="utf-8")
                index.append(f"- [Bundled text: {file}](bundled/{page})\n")
            except Exception as exc:
                report["errors"].append(f"Bundled text {file}: {exc}")
    runtime_targets = set(discovered) if args.runtime else set()
    if standard_library and not args.runtime:
        from developer_docs import collect_apis
        static_rows = collect_apis(report)
        root_rows = [r for r in static_rows if r['module'] == args.package]
        unresolved_stars = any(item['kind'] == 'import' and any(b['imported'] == '*' for b in item.get('bindings', [])) for data in report['modules'] if data['module'] == args.package for item in data['members'])
        if not root_rows or unresolved_stars:
            runtime_targets.add(args.package)
            report['automatic_runtime_reason'] = 'No resolved public callables or unresolved wildcard exports in standard-library source'
            print('Source exports are incomplete; inspecting the standard-library module at runtime.', flush=True)
    if runtime_targets:
        for number, module in enumerate(sorted(runtime_targets)):
            result_path = out / f"runtime-{number:05d}.json"
            try:
                proc = subprocess.run([sys.executable, *(['-I'] if standard_library else []), str(Path(__file__).resolve()), "--worker", module, str(result_path)],
                                      timeout=args.timeout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                data = json.loads(result_path.read_text(encoding="utf-8")) if result_path.exists() else {"error": f"Worker exited {proc.returncode} without a report"}
                data['module'] = module
                page = f"runtime-{number:05d}.md"
                data['page'] = f'modules/{page}'
                report.setdefault('runtime_modules', []).append(data)
                content = [f"# Runtime: {module}\n", fence(data.get("docstring") or data.get("error") or "No module docstring.")]
                content.extend(render_members(data.get("members", [])))
                (pages / page).write_text("\n".join(content), encoding="utf-8")
                index.append(f"- [Runtime: {module}](modules/{page})\n")
                if "error" in data:
                    report["errors"].append(f"{module}: {data['error']}")
            except Exception as exc:
                report["errors"].append(f"Runtime {module}: {type(exc).__name__}: {exc}")
    query = (f"import sys, sysconfig, importlib.util\nprint(sys.version)\nprint(sysconfig.get_path('stdlib'))\nprint(importlib.util.find_spec({args.package!r}))" if standard_library else f"from importlib import metadata\nd = metadata.distribution({args.package!r})\nd.version\nlist(d.metadata.items())\nd.requires\nlist(d.entry_points)\nlist(d.files or [])\nd.read_text('METADATA')\nd.read_text('entry_points.txt')")
    index.extend(["## Installed files\n", fence(json.dumps(report["files"], indent=2), "json"),
                  "## Manual metadata queries\n", fence(query, "python"),
                  "## Inspection gaps and errors\n", fence("\n".join(report["errors"]) or "No inspection errors recorded. This does not prove complete API coverage."),
                  "## Python reference\n", "- https://docs.python.org/3/library/importlib.metadata.html\n- https://docs.python.org/3/library/inspect.html\n- https://docs.python.org/3/library/ast.html\n- https://docs.python.org/3/library/functions.html#help\n"])
    (out / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "README.md").write_text("\n".join(index), encoding="utf-8")
    from developer_docs import write_developer_docs
    write_developer_docs(out, report, fence)
    print(out / "README.md")
    print(f"Inspection gaps/errors: {len(report['errors'])}")


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--worker":
        worker(sys.argv[2], sys.argv[3])
    else:
        sys.exit(main())
