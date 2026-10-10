# Python package discovery: a developer's guide

Turn a Python package installation into locally searchable Markdown. Use it to find an API, understand its inputs, inspect the original docstring, and prepare a small implementation experiment.

The only required input is the **distribution name**. The script creates a venv, installs the package, collects local source and metadata, and writes documentation. Your existing Python environment remains unchanged.

## Guide outline

1. Choose a command for your use case.
2. Generate documentation and understand the output.
3. Find an API and read its inputs and return information.
4. Inspect and practice with the documented version.
5. Understand evidence, cleanup, and troubleshooting.

## Quick start

Requires Python **3.11 or later**. The generator uses the standard library; the target package and dependencies are installed in a separate venv. Automatic installation usually requires network access to PyPI.

From this repository's root, enter the tool folder:

```powershell
Set-Location package_discovery
python --version
python package_discovery.py requests
```

This command:

1. Creates a fresh venv under `package_docs/.venvs/`.
2. Asks pip to install the latest compatible stable release of `requests` and its dependencies.
3. Prints the resolved version and generates docs under `package_docs/requests-<resolved-version>/`.
4. Prints the generated `README.md` path. Open that file first.

The venv is retained for practice. No activation step is required: the generator invokes its Python directly. To keep the docs but remove the new venv after successful generation:

```powershell
python package_discovery.py requests --cleanup-venv
```

For a ready-to-read example, open the [reviewed requests overview](reviewed_examples/requests-2.32.3/README.md), [API index](reviewed_examples/requests-2.32.3/API_INDEX.md), or [requests.get page](reviewed_examples/requests-2.32.3/api/00088-requests.get.md). This reference documents a historical version; it is not a recommendation to install that version in production.

## Choose the right command

### Standard-library modules need no installation

Modules such as `json`, `math`, and `datetime` ship with Python. They have no independent PyPI version. The tool detects them before installation and reads the current interpreter's source or runtime metadata:

```powershell
python package_discovery.py json
python package_discovery.py json.decoder
python package_discovery.py math
```

Output uses names such as `package_docs/json-python-3.14.7/`, identifying the Python version rather than a pip package version. No new venv is created and pip is not called. Modules without Python source, with no resolved public callables, or with unresolved wildcard exports automatically use runtime inspection. This covers compiled exports behind source wrappers such as `decimal` and `datetime`. `--runtime` adds runtime inspection to source-based modules too. Dotted aliases such as `os.path` are resolved using isolated Python and documented under their requested import path. An unavailable standard-library module reports an error instead of falling back to PyPI.

Omit the version for standard-library modules. To document another Python release, run the script using that release's interpreter. `--cleanup-venv` has no effect here because no environment was created. The generated quick start uses the matching Python interpreter and does not suggest `pip install json`.

### Third-party packages

Run generator commands from the tool folder. Versions shown are explicit examples, not claims about today's latest releases.

| Your use case | Command | Why it helps |
| --- | --- | --- |
| Explore a new library | `python package_discovery.py requests` | Latest compatible stable release; no manual setup |
| Match a project's pinned dependency | `python package_discovery.py requests 2.32.3` | Documents and verifies that exact version |
| Inspect your current project environment | `python package_discovery.py requests --installed` | Reads the local installation without installing or contacting PyPI |
| Verify the local version | `python package_discovery.py requests 2.32.3 --installed` | Stops if the installed version differs |
| Explore compiled or dynamic APIs | `python package_discovery.py requests --runtime` | Adds loaded-object signatures and docstrings |
| Save a reference without retaining the venv | `python package_discovery.py requests --cleanup-venv` | Keeps Markdown and JSON; removes only the new venv on success |
| Organize references by project | `python package_discovery.py requests --output learning_docs/http` | Creates missing parents and a package/version subfolder |
| Distribution and import names differ | `python package_discovery.py beautifulsoup4 --runtime --module bs4` | Installs the distribution and explicitly inspects the import name |

For `--installed`, use the Python interpreter containing the package. From the tool folder:

```powershell
& "D:\my-project\.venv\Scripts\python.exe" .\package_discovery.py requests --installed
```

Replace that interpreter path with your project's actual path. Distribution and import names can differ: pip installs `beautifulsoup4`, while Python imports `bs4`. The generator normally discovers import names from installed files. `--module` adds a runtime inspection target when needed.

## Worked example: find and practice an HTTP API

### 1. Generate a reference for a known version

```powershell
python package_discovery.py requests 2.32.3 --runtime --output practice_docs
Set-Location .\practice_docs\requests-2.32.3
python search_api.py get --limit 5
```

Search uses names, signatures, and docstring summaries. Exact API names rank first, so `get` finds `requests.get` before more distant matches. Results include the API name, signature, purpose, and Markdown path. Search works after venv cleanup: it reads `api_index.json` and never imports the target package.

### 2. Read the API page before calling it

For `requests.get`, check:

- `url` is required; `params` has a default.
- `**kwargs` forwards options. Follow `requests.request` to find documented inputs such as `timeout` and `headers`.
- Return information comes from installed docstrings or annotations.
- Original package examples and generated templates are clearly distinguished.

For a class, open its page and follow its public-member table. For example, `requests.Session` links to individual methods. You can also search directly:

```powershell
python search_api.py "Session.get" --limit 5
```

### 3. Launch the correct interpreter

Copy the full interpreter path from **Inspection environment** in the generated overview. Launch it in PowerShell:

```powershell
& "<interpreter path copied from the generated README>"
```

This is an editable path template. If the venv was removed, recreate the documented version:

```powershell
python -m venv .practice-venv
& .\.practice-venv\Scripts\python.exe -m pip install "requests==2.32.3"
& .\.practice-venv\Scripts\python.exe
```

On Linux/macOS, use `.practice-venv/bin/python` instead of the Windows interpreter path.

### 4. Inspect without calling the API

Run this in the package interpreter:

```python
import inspect
import requests

print(inspect.signature(requests.get))
print(inspect.getdoc(requests.get))
help(requests.get)
print([name for name in dir(requests.Session) if not name.startswith("_")])
```

Each API page also supplies an inspection block for its exact import path. `inspect.signature()` and `inspect.getsource()` can fail when information is unavailable; generated inspection blocks handle unavailable signatures.

### 5. Practice without making a network request

This guide-authored example constructs and prepares a request locally. It exercises a constructor and a method while letting you inspect the result:

```python
import requests

request = requests.Request(
    method="GET",
    url="https://example.com/search",
    params={"q": "python", "limit": 2},
)
prepared = request.prepare()

print(prepared.method)
print(prepared.url)
assert prepared.method == "GET"
assert prepared.url == "https://example.com/search?q=python&limit=2"
```

Expected output, verified with `requests==2.32.3`:

```text
GET
https://example.com/search?q=python&limit=2
```

Change the query values and inspect the resulting URL. This example does not call `requests.get()` or send a request. For another API, begin with a small valid input, inspect its result, and check documented exceptions before integrating it into your application.

## Understand the generated files

```text
package_docs/
  .venvs/<package>-<version-or-latest>-<unique-id>/
  <package>-<resolved-version>/
    README.md
    QUICKSTART.md
    API_INDEX.md
    api/*.md
    api_index.json
    search_api.py
    REFERENCE.md
    report.json
    modules/*.md
    bundled/*.md
    runtime-*.json
```

| File or folder | Open it when you need to... |
| --- | --- |
| `README.md` | Understand package facts, coverage, environment, and navigation |
| `QUICKSTART.md` | Recreate the environment and follow the practice workflow |
| `API_INDEX.md` | Scan module-level functions and classes |
| `api/*.md` | Read one API's signature, inputs, returns, exceptions, examples, and original docstring |
| `search_api.py` | Find an operation quickly from the command line |
| `api_index.json` | Build your own search or tooling over the API catalog |
| `REFERENCE.md` | Read full metadata, dependencies, entry points, installed files, and module links |
| `report.json` | Inspect collected evidence and recorded gaps programmatically |
| `modules/*.md` | Examine complete module inspection, including internals |
| `bundled/*.md` | Read installed documentation, licenses, and raw metadata |
| `runtime-*.json` | Inspect raw loaded-object results; present with runtime inspection |

## Version and directory selection

**Omitted version:** pip selects the latest stable release compatible with your Python and dependency constraints. It can be older than the newest release for another Python version. Pre-releases are not explicitly enabled. See [pip's selection rules](https://pip.pypa.io/en/stable/cli/pip_install/#satisfying-requirements).

**Explicit version:** pip installs `package==version`, and the generator checks installation metadata against the requested version. For existing installations, use the version returned by `importlib.metadata.version()`.

**`--installed` without a version:** uses current local metadata without a latest-version lookup or upgrade. `report.json` records `version`, `requested_version`, and `version_selection`.

**Default output:** `package_docs/` is relative to where you run the command. Repeated default runs preserve earlier docs with suffixes such as `-2` and `-3`.

**Custom output:** missing parents are created, followed by a package/version child. An existing child stops generation. Pinned-version collisions are checked before installation; omitted-version collisions are checked after installation resolves the version. Choose another output parent to retain both runs.

The temporary venv name uses `latest` when the version is omitted; documentation folders always use the resolved version. The tool does not install a different Python interpreter. URLs, paths, extras, and version ranges are not accepted as package/version inputs.

## Static inspection, runtime inspection, and reliability

| Evidence | What it provides | Practical limit |
| --- | --- | --- |
| Static parsing, enabled by default | Source definitions, signatures, annotations, decorators, original docstrings, and resolvable local re-exports | Does not execute the target package during inspection; compiled/dynamic APIs can be absent |
| `--runtime` | Loaded functions/classes, signatures, and inherited members | Imports discovered modules; imports can execute code or fail on optional dependencies |
| Docstring parsing | Common Google, NumPy, and Sphinx input/return/exception fields | Unusual layouts may be incomplete; original text remains accessible |
| Package-authored Python fences and doctests | Original code, setup, comments, and doctest expected output | Copied without execution; setup or dependencies may be needed |
| Generated call templates | Argument placement based on the signature | Replace every `...` placeholder; valid inputs and expected results are not invented |

Public candidates use statically resolved `__all__` where possible, otherwise naming heuristics. A public-looking name does not prove API stability. Dynamic exports, indirect aliases, editable installs, and missing file inventories can leave gaps. Zero recorded errors does not prove complete coverage.

Installation can execute build code; runtime imports can have side effects. A venv isolates dependencies, not execution. `--timeout` bounds each runtime-worker wait, not installation or descendant processes. The generator does not execute package examples. Online API supplements are fetched only when explicitly enabled.

## Fill local documentation gaps from official sources

Opt in to online enrichment when installed docstrings lack descriptions, examples, input details, returns, or exception information:

```powershell
python package_discovery.py json --official-docs
python package_discovery.py requests --official-docs --cleanup-venv
python package_discovery.py requests --docs-url https://requests.readthedocs.io/en/latest/api/
```

`--docs-url` implies enrichment and lets you supply an official source explicitly. Standard-library modules use `docs.python.org` for the matching Python minor version. Third-party packages use a Documentation/Docs entry from installed `Project-URL` metadata. That entry is package-declared; ownership is not independently verified. If no documentation URL is declared, the tool records the unresolved fields and requires `--docs-url` to fetch a source. It does not substitute a homepage or search result.

Each API supplement requires an exact API anchor, such as `json.load`, or a resolved source alias. HTML API sections supply missing descriptions, parameter/return/exception text, and Python or doctest examples. Existing local signatures, original docstrings, and examples remain unchanged. Supplements carry a source link, retrieval timestamp, and documentation-version status. Third-party documentation is labeled **not verified against the installed version**; supply a version-specific URL when available.

```powershell
python package_discovery.py json --official-docs --docs-max-pages 1 --docs-timeout 10
```

The default limit is ten page attempts with a 15-second timeout per HTTP request. Fetching uses HTTPS, bounded page sizes, and same-host redirects/crawling. Python standard-library enrichment reads only the module's official page. Each URL is fetched at most once within a run; HTML is stored under `official_docs/` with content hashes. No JavaScript rendering, PDF parsing, or cross-host crawling is provided.

The overview reports supplemented APIs, unresolved fields, and retrieval errors. `official_docs/retrieval.json` records sources, timestamps, hashes, and gaps. A network failure or unsupported page layout leaves local documentation available. Some packages use different anchors or layouts; not every missing field can be filled automatically. Fetched examples are not executed or tested by the generator.

Without `--official-docs` or `--docs-url`, documentation generation remains local. Offline `--installed` behavior is preserved unless you explicitly request enrichment.

## Reuse downloaded documentation offline

Point `--docs-cache` at a previous run's **official_docs folder**, which must contain `retrieval.json` and its downloaded HTML files. Adding `--docs-offline` makes enrichment use only that cache, with no HTTP requests or online fallback:

```powershell
python package_discovery.py json --docs-offline --docs-cache .\official_examples\json-python-3.14.7\official_docs --output offline_docs
```

This works with the retained JSON download in this project. Standard-library inspection needs no installation. For a third-party package, first install the target package in the interpreter you intend to use, then use `--installed` to avoid pip/network installation as well:

```powershell
python package_discovery.py requests --installed --docs-offline --docs-cache .\downloaded_docs\requests-<version>\official_docs --output offline_docs
```

The second command is a path template: replace `<version>` and the cache path with your own previous output. Offline enrichment does not install missing packages. `--docs-offline` requires `--docs-cache`; a missing cache folder or manifest is rejected before installation.

Cached HTML hashes are validated, and cached source URLs must match the selected documentation source. Missing, unreadable, or corrupted pages are recorded as retrieval gaps; local documentation is still generated. The original retrieval timestamp is preserved, reuse is labeled, and the source cache is left unchanged. Cached pages are copied into the new output, which can itself serve as a cache for later runs. Package-version metadata from newer cache manifests is recorded, but third-party documentation-version compatibility remains unverified; cached documentation may be stale.

To reuse cached pages while allowing downloads on cache misses, omit `--docs-offline`:

```powershell
python package_discovery.py json --docs-cache .\official_examples\json-python-3.14.7\official_docs
```

Either cache option enables enrichment automatically. The overview and `retrieval.json` distinguish downloaded pages from reused pages. The page-attempt limit also applies to offline runs.

## Cleanup behavior

```powershell
python package_discovery.py requests --runtime --cleanup-venv
```

Cleanup removes only the environment created by that run after successful generation. Markdown and JSON remain; earlier environments stay intact. Successfully completed docs may still contain recorded inspection gaps.

Installation or generation failure retains the venv. Cleanup failure reports an error and returns a nonzero status; docs remain, and the venv may be partly removed. `--cleanup-venv --installed` is rejected because no new environment exists. Cleanup does not remove pip's cache or the containing `.venvs/` folder.

## Command reference

```powershell
python package_discovery.py --help
```

| Input or option | Meaning |
| --- | --- |
| `package` | Required distribution name |
| `version` | Optional exact version; omission selects the latest compatible stable release |
| `--output PATH` | Parent folder for docs and newly created environments |
| `--installed` | Inspect the current environment without installing |
| `--runtime` | Add subprocess-based runtime inspection |
| `--module NAME` | Add an import name; repeatable, takes effect with `--runtime` |
| `--timeout SECONDS` | Finite positive timeout per runtime module; default 20 seconds |
| `--cleanup-venv` | Remove the new venv after successful generation |
| `--official-docs` | Supplement missing local API details from official/package-declared documentation |
| `--docs-url HTTPS_URL` | Explicit documentation source; enables enrichment |
| `--docs-max-pages N` | Maximum documentation-page attempts; default 10 |
| `--docs-timeout SECONDS` | HTTP timeout per documentation request; default 15 seconds |
| `--docs-cache PATH` | Reuse a previous `official_docs` folder; cache misses may download |
| `--docs-offline` | Use only cached documentation; requires `--docs-cache` |

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Package missing with `--installed` | Use the correct project's Python or automatic installation |
| Installed version differs | Supply the local version or omit it with `--installed` |
| pip cannot find a compatible release | Check the distribution name, version, Python support, and network access |
| Output already exists | Choose another `--output` parent or omit it for numbered default runs |
| Optional dependency import fails | Read the recorded gap; static docs remain useful, runtime coverage is incomplete |
| Signature or examples missing | Read the original docstring and full reference; try runtime mode where appropriate |
| Interpreter path no longer exists | Recreate the documented version using `QUICKSTART.md` |
| Search finds no results | Try a shorter name; search covers names, signatures, and summaries, not full parameter descriptions |

## Test and maintain the tool

Async APIs keep their coroutine classification in both source and runtime inspection; their call templates use `await` inside an async practice function. Receiver parameters are removed only for identified instance/class methods, by position rather than spelling. Ordinary functions and static methods retain caller inputs named `self` or `cls`. Class constructors also handle a receiver named something other than `self`.

Keep `package_discovery.py`, `developer_docs.py`, and `official_docs.py` together. The helpers build developer-facing pages and optional online supplements. Tests use controlled temporary distributions and mocked HTML responses without downloading target packages or documentation.

```powershell
python -m unittest discover -s . -v
```

The [validation record](VALIDATION.md) describes executed checks. The [quality review](QUALITY_REVIEW.md) explains the design and remaining gaps. One reviewed requests reference is retained; obsolete generated test runs and caches have been removed from the project folder.

## References

- [Python virtual environments](https://docs.python.org/3/library/venv.html)
- [pip installation and version selection](https://pip.pypa.io/en/stable/cli/pip_install/)
- [Installed distribution metadata](https://docs.python.org/3/library/importlib.metadata.html)
- [Runtime inspection](https://docs.python.org/3/library/inspect.html)
- [Python abstract syntax trees](https://docs.python.org/3/library/ast.html)

### Local example and overload extraction

Python docstring fences (`python`, `python3`, `py`, and `pycon`) and standalone doctests populate practice examples. Imports and nested indentation are preserved. Non-Python and unclosed fences are excluded. Examples are package-authored excerpts, not verified end-to-end recipes; inspect their setup and required credentials before running them.

For functions and methods declared with `@overload`, the documented implementation supplies the description and call signature. Alternative type overloads appear on the API page. If only overload declarations are available, the page labels that limitation.

### Enrichment coverage

Exact API IDs on HTML headings are supported alongside Sphinx definition lists and section containers. Heading extraction stops at the next peer or higher-level heading. Python language markers on child code elements are recognized. When a matching page supplies only some missing fields, bounded crawling continues for remaining fields; additional source URLs and retrieval dates are retained. Local content takes precedence. Pages without exact API identities, JavaScript-only documentation, and Markdown responses remain unsupported.

### GenAI official reference adapters

For `langchain`, `langgraph`, and `langsmith`, automatic source selection uses `https://reference.langchain.com/python/<package>/`. An explicit `--docs-url` still takes precedence. The adapter matches exact dotted API identities to Python reference routes, including source aliases; it reads rendered description containers and parameter tables, and prioritizes matching detail links within the page limit. It excludes member cards and nested API sections. Saved official HTML pages provide offline regression coverage.

Generic HTML enrichment also reads Parameters, Returns, and Raises headings and tables. Each supplemented field records its own URL, original retrieval timestamp, content hash, and cache status in `field_sources`; API Markdown displays those sources. Existing local content remains authoritative. Third-party documentation versions remain unverified, and bounded crawling can leave APIs unresolved. Markdown-only responses and JavaScript-only pages remain unsupported.

### Developer workflow improvements

GenAI quick starts provide task links backed by APIs actually present in the inspection report. The first inspection targets a core task API when available. Official crawling shares these priorities, then prefers public exports and other public routes over internal routes; source aliases remain eligible. Cached pages follow the same priority, so an old cache cannot force alphabetical internal-first crawling. The fetch limit still applies.

Adjacent doctest commands form a shared-state session with one copyable code block and separately retained expected output. Explanatory prose or a fenced-block boundary separates sessions. Google and Sphinx field parsing stops at unindented narrative. Package overview pages check whether the inspection interpreter still exists and direct users to recreate missing environments; the original path remains provenance.

### Streamed descriptions and practice readiness

The HTML parser restores recognized React `$RS` and `$RC` segment references using their static IDs. It never evaluates JavaScript. Unknown stream formats remain unsupported. LangGraph task links include the existing Pregel invocation and streaming methods used by compiled graphs.

Practice pages summarize imports, matching declared dependencies, environment-variable names explicitly present in source, and detected provider/service setup. They do not invent credentials or claim a model/service was validated. Doctest sessions can include an optional copy with statically selected earlier setup statements; the original snippets remain visible. Names that cannot be resolved are listed. This static recovery cannot guarantee external resources, side effects, files, or standalone execution. Normalized ASCII navigation avoids encoding artifacts.
