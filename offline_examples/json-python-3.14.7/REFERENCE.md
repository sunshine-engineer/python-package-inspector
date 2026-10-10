# json 3.14.7

## Inspection environment

```text
Python: C:\Users\sunny\AppData\Local\Python\pythoncore-3.14-64\python.exe
Environment: C:\Users\sunny\AppData\Local\Python\pythoncore-3.14-64
```

Run manual queries using this Python interpreter so they inspect the documented version.

## Scope and limitations

This documents the installed distribution in this Python environment. Source inspection does not execute package code. Runtime mode executes imports and is not a security sandbox. Signatures and docstrings are evidence, not generated usage examples. Return behavior is only known when annotations or documentation describe it. Dynamic APIs, unavailable source, editable installs, and missing optional dependencies can leave gaps. Private names are included.

## Installation metadata

```json
{
  "Name": [
    "json"
  ],
  "Python-Version": [
    "3.14.7"
  ],
  "Summary": [
    "Python standard-library module; included with this interpreter, not installed from PyPI."
  ]
}
```

## Dependencies

```text
None declared.
```

## Entry points

```json
[]
```

## Module pages

- [json (.py)](modules/00000-json.md)

- [json.__main__ (.py)](modules/00001-json.__main__.md)

- [json.decoder (.py)](modules/00002-json.decoder.md)

- [json.encoder (.py)](modules/00003-json.encoder.md)

- [json.scanner (.py)](modules/00004-json.scanner.md)

- [json.tool (.py)](modules/00005-json.tool.md)

## Installed files

```json
[
  {
    "path": "json/__init__.py",
    "size": 14497,
    "hash": null
  },
  {
    "path": "json/__main__.py",
    "size": 441,
    "hash": null
  },
  {
    "path": "json/decoder.py",
    "size": 13241,
    "hash": null
  },
  {
    "path": "json/encoder.py",
    "size": 17451,
    "hash": null
  },
  {
    "path": "json/scanner.py",
    "size": 2507,
    "hash": null
  },
  {
    "path": "json/tool.py",
    "size": 4740,
    "hash": null
  }
]
```

## Manual metadata queries

```python
import sys, sysconfig, importlib.util
print(sys.version)
print(sysconfig.get_path('stdlib'))
print(importlib.util.find_spec('json'))
```

## Inspection gaps and errors

```text
No inspection errors recorded. This does not prove complete API coverage.
```

## Python reference

- https://docs.python.org/3/library/importlib.metadata.html
- https://docs.python.org/3/library/inspect.html
- https://docs.python.org/3/library/ast.html
- https://docs.python.org/3/library/functions.html#help
