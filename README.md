# Python Package Inspector

Explore Python libraries systematically and turn their installed APIs into searchable local documentation.

Python Package Inspector generates Markdown and JSON references from package source, installation metadata, and optional runtime inspection. It helps developers find functions and classes, understand parameters, examine original docstrings, and prepare small implementation experiments.

Use it to explore an unfamiliar dependency, document a project's installed version, or build local references for libraries used in data engineering and GenAI applications.

## Features

- **Package discovery:** inspect standard-library modules or third-party distributions.
- **Isolated installation:** install third-party packages in a dedicated virtual environment, with an optional exact version.
- **Existing-environment inspection:** use `--installed` to inspect a dependency without installing or upgrading it.
- **Static analysis:** extract source definitions, signatures, annotations, decorators, docstrings, and resolvable re-exports.
- **Optional runtime inspection:** inspect loaded objects, inherited members, and dynamic or compiled APIs.
- **Searchable documentation:** generate API pages, navigation indexes, JSON catalogs, and a standalone search script.
- **Example extraction:** preserve supported Python examples and doctests from documentation without executing them.
- **Documentation enrichment:** optionally supplement missing details from official or package-declared documentation.
- **Offline reuse:** reuse downloaded documentation with source records and validated content hashes.
- **Inspection reports:** record package versions, environments, source evidence, and discovery gaps.

## Requirements

- Python **3.11 or later**, with virtual-environment support.
- The generator itself uses the Python standard library.
- Automatic third-party installation requires access to a package index and any dependencies needed by the target package.
- Online documentation enrichment requires network access.

Recorded validation was performed on Windows with Python 3.14.7. Python 3.11–3.13 compatibility has not been verified by the recorded test runs.

## Quick start

Clone the repository and run commands from its root:

```bash
git clone https://github.com/sunshine-engineer/python-package-inspector.git
cd python-package-inspector
python --version
python package_discovery.py --help
```

Start with a standard-library module, which requires no package installation:

```bash
python package_discovery.py json
```

Explore a third-party library:

```bash
python package_discovery.py requests
```

The second command creates a dedicated virtual environment, installs the latest compatible stable release, and writes documentation under:

```text
package_docs/requests-<resolved-version>/
```

Open the generated `README.md` first. The inspection environment is retained by default so you can practice against the documented version.

## Usage

| Goal | Command |
| --- | --- |
| Inspect a standard-library module | `python package_discovery.py datetime` |
| Document an exact package version | `python package_discovery.py requests 2.32.3` |
| Inspect the current environment | `python package_discovery.py requests --installed` |
| Add runtime inspection | `python package_discovery.py requests --runtime` |
| Specify an additional import name | `python package_discovery.py beautifulsoup4 --runtime --module bs4` |
| Choose an output parent | `python package_discovery.py requests --output learning_docs/http` |
| Remove the newly created environment after success | `python package_discovery.py requests --cleanup-venv` |

The pinned version above is an example, not a recommendation for production use.

For `--installed`, run the script with the interpreter containing the target package. Distribution names and import names may differ.

Repeated runs using the default output directory receive numbered folders. With a custom output directory, an existing package/version folder causes an error.

### Search the generated API catalog

From a generated reference directory:

```bash
python search_api.py get --limit 5
python search_api.py "Session.get" --limit 5
```

Search reads the generated catalog without importing the target package. It remains usable after the inspection environment has been removed.

### Explore GenAI libraries

```bash
python package_discovery.py langchain --output learning_docs/genai
python package_discovery.py langgraph --output learning_docs/genai
```

Use an explicit version to match your application's dependencies. Runtime inspection may require optional dependencies and can execute import-time code.

Generating a reference does not require making an LLM request. Running extracted provider examples may require credentials, additional dependencies, and paid API access.

### Supplement missing documentation

```bash
python package_discovery.py json --official-docs
python package_discovery.py requests --docs-url https://requests.readthedocs.io/en/latest/api/
```

Enrichment preserves local signatures and original documentation while adding supported missing fields with source information.

Third-party documentation is not automatically verified against the installed package version. Prefer a version-specific documentation URL when available.

### Reuse documentation offline

```bash
python package_discovery.py json --docs-offline --docs-cache official_examples/json-python-3.14.7/official_docs --output offline_docs
```

The cache must contain `retrieval.json` and its downloaded HTML files.

For third-party packages, combine cache reuse with `--installed` to avoid automatic package installation:

```bash
python package_discovery.py requests --installed --docs-offline --docs-cache path/to/official_docs --output offline_docs
```

Replace the cache path with a previous run's `official_docs` directory.

## Generated output

```text
package_docs/
├── .venvs/
└── <package>-<version>/
    ├── README.md
    ├── QUICKSTART.md
    ├── API_INDEX.md
    ├── api/
    ├── api_index.json
    ├── search_api.py
    ├── REFERENCE.md
    ├── report.json
    ├── modules/
    └── bundled/
```

Runtime inspection adds runtime reports. Documentation enrichment adds an `official_docs/` directory.

| Output | Purpose |
| --- | --- |
| `README.md` | Package overview, inspection environment, coverage, and navigation |
| `QUICKSTART.md` | Environment setup and discovery-to-practice workflow |
| `API_INDEX.md` and `api/` | API navigation and individual function/class references |
| `api_index.json` and `search_api.py` | Searchable API catalog |
| `REFERENCE.md` and `report.json` | Detailed metadata, collected evidence, and inspection gaps |
| `modules/` and `bundled/` | Module inspection and installed documentation/metadata |

## Implementation

The tool separates collection, presentation, and external documentation retrieval:

- `package_discovery.py` handles CLI arguments, environments, installation metadata, source parsing, and runtime workers.
- `developer_docs.py` builds API catalogs, extracts documentation fields and examples, and writes developer references.
- `official_docs.py` retrieves and parses documentation, manages caches, and records provenance.

Static inspection is the default for third-party packages. Standard-library modules may automatically use runtime inspection when source information cannot resolve their exports.

## Tests and validation

Run the regression suite from the repository root:

```bash
python -m unittest discover -v
```

The [validation record](VALIDATION.md) reports 81 passing tests on Windows with Python 3.14.7, including controlled source/runtime fixtures, CLI behavior, documentation parsing, cache handling, and generated Markdown checks.

These are recorded results, not a CI status. Provider-backed examples were not executed, and Python syntax checks do not establish example correctness.

Further review notes:

- [Developer guide](PACKAGE_DISCOVERY.md)
- [Documentation quality review](QUALITY_REVIEW.md)
- [GenAI extraction review](GENAI_REVIEW.md)
- [Reviewed Requests reference](reviewed_examples/requests-2.32.3/README.md)

## Limitations

- Discovered names are API candidates; their presence does not prove public support or stability.
- Dynamic exports, compiled code, editable installations, and missing optional dependencies can leave gaps.
- Signatures and docstrings cannot establish undocumented behavior, performance, or trade-offs.
- Extracted examples are preserved without automatic execution. Generated call templates require valid inputs.
- A virtual environment isolates dependencies, but is not a security sandbox. Installation and runtime imports can execute package code.
- Runtime timeouts bound worker waits; they do not bound package installation or all descendant processes.
- Documentation retrieval supports selected HTML layouts. It does not provide general JavaScript rendering or PDF parsing.
- Cached documentation may be stale, and third-party documentation-version compatibility remains unverified.

Inspect the generated coverage and error reports before relying on a reference. Zero recorded errors does not guarantee complete API coverage.

## Contributing

Report bugs with the Python version, target package/version, command used, and relevant error output.

For code changes, include a focused regression test and run the test suite. Keep source-derived evidence distinct from supplemental documentation and generated templates.

## License

This repository currently has no project license. A license should be selected before distributing it as a reusable open-source tool. Included third-party documentation and examples retain their original licensing terms.