# requests 2.32.3

Python HTTP for Humans.

## Start here

- [Quick start and practice workflow](QUICKSTART.md)
- [Public API index](API_INDEX.md)
- [Full metadata, module inspection, and bundled files](REFERENCE.md)

## Find an operation

```powershell
python search_api.py "keyword"
```

Search names, signatures, and docstring summaries without importing the package. Open the returned API page for inputs, returns, exceptions, and practice material.

## Package facts

| Fact | Value |
| --- | --- |
| Python requirement | >=3.8 |
| License metadata | Apache-2.0 |
| Discovered public API candidates | 807 |
| APIs with signatures | 766 |
| APIs with docstrings | 770 |
| APIs with docstring examples | 21 |
| Recorded inspection gaps/errors | 0 |

## Inspection environment

```text
Python: D:\projects\GCP_Deployments\package_discovery\reviewed_examples\.venvs\requests-2.32.3-81ut82qk\Scripts\python.exe
Environment: D:\projects\GCP_Deployments\package_discovery\reviewed_examples\.venvs\requests-2.32.3-81ut82qk
```

Cleanup was requested after generation. Recreate the package environment before practice if the interpreter has been removed.

## Dependencies

```text
charset-normalizer <4,>=2
idna <4,>=2.5
urllib3 <3,>=1.21.1
certifi >=2017.4.17
PySocks !=1.5.7,>=1.5.6 ; extra == 'socks'
chardet <6,>=3.0.2 ; extra == 'use_chardet_on_py3'
```

## Coverage and limits

Public APIs are selected using a statically resolved `__all__` where available, otherwise public names. Resolvable local re-exports are included. Runtime mode adds loaded callables and classes, including compiled APIs. Internal/test/vendor modules and private members remain in full inspection. Parameter documentation is parsed from common Google, NumPy, and Sphinx styles; consult original docstrings when extraction is incomplete. Missing return behavior or examples is not invented. Static aliases, dynamic exports, and optional imports can remain unresolved.
