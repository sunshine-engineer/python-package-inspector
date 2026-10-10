# Quick start

[API index](API_INDEX.md) · [Package overview](README.md)

1. Search for the operation you need in the API index.
2. Open its API page and check required inputs, passing style, return information, and documented exceptions.
3. Run the exact inspection snippet in the package environment.
4. Try a package-authored example if available, then adapt it to a small local input.

## Install or recreate the environment

```powershell
python -m venv .practice-venv
# Windows PowerShell:
& .\.practice-venv\Scripts\python.exe -m pip install "requests==2.32.3"
& .\.practice-venv\Scripts\python.exe
```

On Linux/macOS, use `.practice-venv/bin/python` in place of the Windows interpreter. If the inspection environment was retained, you can use its interpreter directly.

## Available public modules

```text
requests
requests.adapters
requests.api
requests.auth
requests.compat
requests.cookies
requests.exceptions
requests.help
requests.hooks
requests.models
requests.sessions
requests.status_codes
requests.structures
requests.utils
```

## First inspection

This inspects an API without calling it. It imports the package.

```python
import importlib
import inspect

m = importlib.import_module('requests')
obj = m
obj = inspect.getattr_static(obj, 'ConnectTimeout')
if isinstance(obj, (staticmethod, classmethod)):
    obj = obj.__func__
print(inspect.getdoc(obj) or 'No docstring supplied')
try:
    print(inspect.signature(obj))
except (TypeError, ValueError):
    print('Signature unavailable')
help(obj)
```

## Search locally

```powershell
python search_api.py "keyword"
python search_api.py --limit 10
```

Search runs using any Python 3.11+ interpreter and does not require the package or its venv.

## Example reliability

Only doctest-style examples already present in installed docstrings are extracted. They may require setup, files, credentials, or dependencies. No API calls or docstring examples are executed during generation. Missing examples and descriptions are shown explicitly.
