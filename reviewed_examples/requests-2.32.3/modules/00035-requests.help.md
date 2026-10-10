# requests.help

Source: `requests/help.py`

```text
Module containing bug report helper(s).
```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.help')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import json

```json
{
  "name": "import json",
  "kind": "import",
  "line": 3,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "json",
      "local": "json"
    }
  ]
}
```

```text
No docstring available.
```

## import platform

```json
{
  "name": "import platform",
  "kind": "import",
  "line": 4,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "platform",
      "local": "platform"
    }
  ]
}
```

```text
No docstring available.
```

## import ssl

```json
{
  "name": "import ssl",
  "kind": "import",
  "line": 5,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "ssl",
      "local": "ssl"
    }
  ]
}
```

```text
No docstring available.
```

## import sys

```json
{
  "name": "import sys",
  "kind": "import",
  "line": 6,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "sys",
      "local": "sys"
    }
  ]
}
```

```text
No docstring available.
```

## import idna

```json
{
  "name": "import idna",
  "kind": "import",
  "line": 8,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "idna",
      "local": "idna"
    }
  ]
}
```

```text
No docstring available.
```

## import urllib3

```json
{
  "name": "import urllib3",
  "kind": "import",
  "line": 9,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "urllib3",
      "local": "urllib3"
    }
  ]
}
```

```text
No docstring available.
```

## from . import __version__ as requests_version

```json
{
  "name": "from . import __version__ as requests_version",
  "kind": "import",
  "line": 11,
  "from_module": null,
  "level": 1,
  "bindings": [
    {
      "imported": "__version__",
      "local": "requests_version"
    }
  ]
}
```

```text
No docstring available.
```

## import charset_normalizer

```json
{
  "name": "import charset_normalizer",
  "kind": "import",
  "line": 14,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "charset_normalizer",
      "local": "charset_normalizer"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## charset_normalizer

```json
{
  "name": "charset_normalizer",
  "kind": "assignment",
  "line": 16,
  "source": "charset_normalizer = None",
  "conditional": true
}
```

```text
No docstring available.
```

## import chardet

```json
{
  "name": "import chardet",
  "kind": "import",
  "line": 19,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "chardet",
      "local": "chardet"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## chardet

```json
{
  "name": "chardet",
  "kind": "assignment",
  "line": 21,
  "source": "chardet = None",
  "conditional": true
}
```

```text
No docstring available.
```

## from urllib3.contrib import pyopenssl

```json
{
  "name": "from urllib3.contrib import pyopenssl",
  "kind": "import",
  "line": 24,
  "from_module": "urllib3.contrib",
  "level": 0,
  "bindings": [
    {
      "imported": "pyopenssl",
      "local": "pyopenssl"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## import cryptography

```json
{
  "name": "import cryptography",
  "kind": "import",
  "line": 30,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "cryptography",
      "local": "cryptography"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## import OpenSSL

```json
{
  "name": "import OpenSSL",
  "kind": "import",
  "line": 31,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "OpenSSL",
      "local": "OpenSSL"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## pyopenssl

```json
{
  "name": "pyopenssl",
  "kind": "assignment",
  "line": 26,
  "source": "pyopenssl = None",
  "conditional": true
}
```

```text
No docstring available.
```

## OpenSSL

```json
{
  "name": "OpenSSL",
  "kind": "assignment",
  "line": 27,
  "source": "OpenSSL = None",
  "conditional": true
}
```

```text
No docstring available.
```

## cryptography

```json
{
  "name": "cryptography",
  "kind": "assignment",
  "line": 28,
  "source": "cryptography = None",
  "conditional": true
}
```

```text
No docstring available.
```

## _implementation

```json
{
  "name": "_implementation",
  "kind": "function",
  "signature": "_implementation()",
  "line": 34,
  "decorators": [],
  "parameters": [],
  "returns": null
}
```

```text
Return a dict with the Python implementation and version.

    Provide both the name and the version of the Python implementation
    currently running. For example, on CPython 3.10.3 it will return
    {'name': 'CPython', 'version': '3.10.3'}.

    This function works best on CPython and PyPy: in particular, it probably
    doesn't work for Jython or IronPython. Future investigation should be done
    to work out the correct shape of the code for those platforms.
    
```

## info

```json
{
  "name": "info",
  "kind": "function",
  "signature": "info()",
  "line": 69,
  "decorators": [],
  "parameters": [],
  "returns": null
}
```

```text
Generate information for a bug report.
```

## main

```json
{
  "name": "main",
  "kind": "function",
  "signature": "main()",
  "line": 128,
  "decorators": [],
  "parameters": [],
  "returns": null
}
```

```text
Pretty-print the bug information as JSON.
```
