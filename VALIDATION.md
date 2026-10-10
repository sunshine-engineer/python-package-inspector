# Validation record

Date: 2026-10-07. Environment: Windows, Python 3.14.7.

## Executed checks

- Python compilation of the script and test module.
- All 81 unit and CLI integration tests passed. Source/runtime and Markdown checks use a temporary local distribution; installation and official-documentation tests use mocks. Standard-library tests cover json, math, decimal, datetime, os.path, explicit-version rejection, and cleanup behavior. Separate real runs verify installation, cleanup, official-source retrieval, and offline cache reuse.
- Static API signatures, positional-only and keyword-only parameters, decorators, class/property docstrings, conditional definitions, and distribution file-to-module mapping.
- Static generation does not import the target package, verified with an import marker.
- Runtime signatures and import marker, missing optional dependency reporting, and timed-out worker reporting.
- Wrong version, absent package, invalid/nonfinite timeout, existing output preservation, and missing distribution file inventory.
- Markdown relative link targets, matching code fences including embedded fences, valid Python syntax in generated inspection blocks, and valid JSON in JSON blocks.

## Real installed-package run

```powershell
python package_discovery.py pip 26.2.1 --installed --output examples
```

Historical results: 478 installed file records, 403 parsed Python modules, 455 Markdown pages, zero recorded inspection errors. Every generated Markdown page passed link, fence, Python-block, and JSON-block checks. This obsolete generated output was removed during project cleanup; the reviewed requests reference remains available.

## Automatic installation run

```powershell
python package_discovery.py six 1.17.0 --runtime
```

Executed successfully: created `package_docs/.venvs/six-1.17.0-7resb359/`, installed `six==1.17.0`, and generated `package_docs/six-1.17.0/README.md` without an output-directory argument. Static and runtime inspection produced 11 Markdown pages and one runtime report, with zero errors. All generated links, fences, Python blocks, and JSON blocks passed checks. The interpreter and environment in the report point to the created venv. The base Python environment was checked and still does not contain six.

Additional regression coverage checks omitted output paths and repeat numbering, nested-directory creation, rejection of requirement URLs/ranges, environment variable isolation, venv creation failure, and pip failure stopping generation.

## Optional cleanup run

```powershell
python package_discovery.py six 1.17.0 --runtime --cleanup-venv
```

The new environment `package_docs/.venvs/six-1.17.0-c1fs8ypp/` was removed after generation, and the previous environment remained intact. Output in `package_docs/six-1.17.0-2/` contains 11 Markdown pages and records zero inspection errors. All generated links, fences, Python blocks, and JSON blocks passed checks after deletion. The report records the cleanup request and its inspection environment path no longer exists.

Regression tests cover successful cleanup, preservation on generation failure, cleanup failure reporting, rejecting outside/non-venv deletion targets, preserving sibling environments and documentation, and rejecting `--installed --cleanup-venv`.

## Developer documentation review

Generated `requests==2.32.3` with runtime inspection into `reviewed_examples/`, using automatic installation and venv cleanup. Generation recorded zero inspection errors. The redesigned overview is about 2 KB; the main index lists 219 module-level candidates, with methods linked from class pages and available through search. The full searchable catalog includes 807 candidates, 770 with docstrings, 766 with signatures, and 21 with extracted docstring examples. These are discovery counts, not a guarantee that each name is supported public API.

All 855 Markdown pages passed relative-link, code-fence, Python-block syntax, and JSON-block validation. Searching `get` returns `requests.get` first. Reviewed the generated GET input table, its keyword-argument documentation, class navigation, and environment cleanup. Docstring example execution and exact API inspection were tested on controlled fixture code; requests network examples were not executed. See [QUALITY_REVIEW.md](QUALITY_REVIEW.md).

## Optional-version run

```powershell
python package_discovery.py six --runtime --cleanup-venv --output latest_examples
```

Executed successfully with the version omitted. pip selected and installed `six==1.17.0`; the documentation was written to `latest_examples/six-1.17.0/`, and the new `six-latest-cae6x8w1` venv was removed. Generation recorded zero inspection errors. Regression tests verify that omitted versions use an unpinned pip requirement with `--upgrade`, and that offline `--installed` uses local metadata without creating a venv. Explicit-version mismatch behavior remains covered.

## Guide rewrite and project cleanup

Rewrote `PACKAGE_DISCOVERY.md` around use cases, option choices, a complete discovery-to-practice workflow, file navigation, and troubleshooting. The guide's links and Python blocks passed structural checks. Its `requests.Request.prepare()` example ran successfully with `requests==2.32.3` while `Session.send` was patched to reject network sending; it produced the documented method and URL. All 31 regression tests passed again.

Removed duplicate generated runs (`examples`, `developer_examples`, `discovery`, `latest_examples`, and `package_docs`), Python caches, and the unused environment folder inside `reviewed_examples`. Their results above remain historical validation evidence, not links to present files. Source modules, tests, the guide, this record, the quality review, and one reviewed requests reference are retained. Cleanup was scoped to this tool's directory; neighboring GCP project files were left intact.

## Official-documentation enrichment

Executed `python package_discovery.py json --official-docs --docs-max-pages 1 --docs-timeout 10 --output official_examples`. One page was fetched from Python's official 3.14 json reference. Four API pages received supplemental information; unresolved fields remained explicitly recorded. Retrieval completed without errors, and generated Markdown passed relative-link, Python/JSON syntax, and fence checks. The HTML cache and retrieval manifest are under `official_examples/json-python-3.14.7/official_docs/`.

Regression tests verify exact-anchor matching, local-field preservation, description/field/example extraction, default no-network behavior, source selection, URL validation, network-failure reporting, same-host boundaries, page limits, and provenance rendering. This supports server-rendered HTML with recognizable API anchors, not every documentation platform. Third-party documentation versions are not automatically verified; examples are not executed.

## Offline cache reuse

Executed `python package_discovery.py json --docs-offline --docs-cache official_examples/json-python-3.14.7/official_docs --output offline_examples`. The previous Python JSON HTML was reused, with four APIs enriched and no documentation downloads. Original source URLs and retrieval timestamps were retained; reuse was labeled. Cache tests block the network-fetch function and verify successful reuse, empty/corrupted-cache handling, cache-miss downloads in online mode, and CLI cache validation before installation. Offline cache contents may be stale and do not establish third-party documentation-version compatibility.

## Correctness regressions

Fixed compiled-export wrappers (`decimal`, `datetime`) by checking source API resolution and wildcard exports before selecting automatic runtime inspection. Resolved dotted standard-library aliases (`os.path`) using isolated Python. The source remains associated with the requested import path.

Runtime inspection and source/runtime merging preserve async classification for functions and instance/class/static methods. Templates and input tables now use explicit method binding to omit only the first positional receiver. Ordinary functions/static methods retain inputs named `self` or `cls`; constructor receivers with other names are also handled.

Four regression tests cover 12 executable source/runtime template scenarios, input-table correctness, constructor receivers, and real standard-library catalogs. The default commands for `decimal`, `datetime`, and `os.path` ran without pip installation and recorded zero inspection errors. All generated Markdown in `correctness_examples/` passed link, fence, and Python/JSON block checks. These checks were executed on Windows with Python 3.14.7.

## GenAI extraction fixes

Six new regression tests cover Python fences, indentation and setup preservation, mixed doctests without duplication, unsupported/unclosed fences, longer fence delimiters, async snippets, and implementation selection for overloaded functions, reexports, and class methods. A controlled local extracted example was executed successfully. Original inspection records remain intact.

The existing GenAI references were regenerated from saved local reports, without package installation or official-documentation fetching:

| Package | APIs with examples before | APIs with examples after | Extracted example blocks/commands |
| --- | ---: | ---: | ---: |
| langchain 1.4.3 | 0 | 120 | 323 |
| langgraph 1.2.14 | 2 | 35 | 95 |
| langsmith 0.14.4 | 20 | 84 | 370 |

All 494 LangChain, 670 LangGraph, and 1,465 LangSmith API pages passed Markdown link, fence, Python syntax, and JSON checks. Counts include aliases. Package examples were not executed against providers; credentials, optional dependencies, and example correctness remain unverified.

## Limits

Standard-library fix: executed `python package_discovery.py json` successfully with Python 3.14.7. It generated `package_docs/json-python-3.14.7/README.md` with zero recorded errors, without invoking pip or creating a venv. Tests verify `json.dumps`/`json.loads` are indexed and generated quick-start pages contain no pip installation command.

The real pip run used static inspection. Runtime inspection was tested on the controlled fixture, not on all pip modules. Syntax checks do not execute bundled examples or prove their correctness. These checks validate Markdown structure and content; no browser-rendered visual inspection was performed. Python 3.11–3.13 were not available for execution in this environment. Zero recorded errors does not establish complete API coverage.

## Official enrichment continuation and layouts

Regression fixtures verify exact heading matching, section boundaries, child-element Python language markers, continuation across two pages, preservation of the first description, unique enriched-API counts, and multi-page provenance. Live HTML checks of LangGraph graphs and LangChain agents URLs exposed no matching API anchors; these checks do not demonstrate live GenAI enrichment success.

## API boundaries, structured fields, and GenAI adapters

Saved official HTML fixtures (2026-10-07) cover LangChain create_agent, LangGraph StateGraph, and LangSmith traceable. Exact route identity, unrelated-host/name rejection, actual description text, parameter tables, and available examples are checked offline. Further regressions cover nested API containers and headings, heading/table returns and raises, and field-level provenance across cached and live sources. The LangSmith fixture contains no example block. These checks demonstrate support for the saved layouts; they do not prove full-package crawl coverage or documentation-version compatibility.

All three saved reference pages were also passed through full developer-document generation with mocked downloads. Resulting API pages display field-level sources and pass relative-link, fence, Python syntax, and JSON validation. Temporary output is automatically removed by the integration tests.

## Developer workflow fixes

Regressions cover Google/Sphinx field boundaries, NumPy fields, executable shared-state doctest sessions and prose boundaries, core-task navigation links, present/missing interpreter guidance, task-first crawl ordering, and cache-order priority. Controlled fixture examples execute locally. Provider examples are not executed.

Final GenAI regeneration verified corrected create_agent exception extraction, task navigation, and missing-interpreter messaging in all three packages. Official supplements increased from 3/0/0 to 32/6/20 for LangChain/LangGraph/LangSmith within 30 pages per package. Final logs record no retrieval errors. Every regenerated Markdown file passed structural and code-block syntax validation.

## Streamed HTML and practice readiness fixes

81 regression tests passed. New tests verify streamed descriptions using saved real HTML, declarative insertion without script execution, a setup-complete controlled example executed in a fresh namespace, isolation of unrelated function-local names, source-derived prerequisites without invented credential names, invocation/streaming navigation, and absence of encoding artifacts. All three GenAI outputs were regenerated with cached official HTML; Markdown links, fences, Python syntax, and JSON passed checks. StateGraph input/output descriptions and LangSmith setup-copy/prerequisite sections were checked in the final output. Official supplementation remains 32/6/20; these counts include aliases. Provider examples remain unexecuted and documentation-version compatibility remains unverified.
