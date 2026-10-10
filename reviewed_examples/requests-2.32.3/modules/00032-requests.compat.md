# requests.compat

Source: `requests/compat.py`

```text

requests.compat
~~~~~~~~~~~~~~~

This module previously handled import compatibility issues
between Python 2 and Python 3. It remains for backwards
compatibility until the next major version.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.compat')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import importlib

```json
{
  "name": "import importlib",
  "kind": "import",
  "line": 10,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "importlib",
      "local": "importlib"
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
  "line": 11,
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

## _resolve_char_detection

```json
{
  "name": "_resolve_char_detection",
  "kind": "function",
  "signature": "_resolve_char_detection()",
  "line": 18,
  "decorators": [],
  "parameters": [],
  "returns": null
}
```

```text
Find supported character detection libraries.
```

## chardet

```json
{
  "name": "chardet",
  "kind": "assignment",
  "line": 30,
  "source": "chardet = _resolve_char_detection()"
}
```

```text
No docstring available.
```

## _ver

```json
{
  "name": "_ver",
  "kind": "assignment",
  "line": 37,
  "source": "_ver = sys.version_info"
}
```

```text
No docstring available.
```

## is_py2

```json
{
  "name": "is_py2",
  "kind": "assignment",
  "line": 40,
  "source": "is_py2 = _ver[0] == 2"
}
```

```text
No docstring available.
```

## is_py3

```json
{
  "name": "is_py3",
  "kind": "assignment",
  "line": 43,
  "source": "is_py3 = _ver[0] == 3"
}
```

```text
No docstring available.
```

## has_simplejson

```json
{
  "name": "has_simplejson",
  "kind": "assignment",
  "line": 46,
  "source": "has_simplejson = False"
}
```

```text
No docstring available.
```

## import simplejson as json

```json
{
  "name": "import simplejson as json",
  "kind": "import",
  "line": 48,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "simplejson",
      "local": "json"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## has_simplejson

```json
{
  "name": "has_simplejson",
  "kind": "assignment",
  "line": 50,
  "source": "has_simplejson = True",
  "conditional": true
}
```

```text
No docstring available.
```

## import json

```json
{
  "name": "import json",
  "kind": "import",
  "line": 52,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "json",
      "local": "json"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## from simplejson import JSONDecodeError

```json
{
  "name": "from simplejson import JSONDecodeError",
  "kind": "import",
  "line": 55,
  "from_module": "simplejson",
  "level": 0,
  "bindings": [
    {
      "imported": "JSONDecodeError",
      "local": "JSONDecodeError"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## from json import JSONDecodeError

```json
{
  "name": "from json import JSONDecodeError",
  "kind": "import",
  "line": 57,
  "from_module": "json",
  "level": 0,
  "bindings": [
    {
      "imported": "JSONDecodeError",
      "local": "JSONDecodeError"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## from collections import OrderedDict

```json
{
  "name": "from collections import OrderedDict",
  "kind": "import",
  "line": 60,
  "from_module": "collections",
  "level": 0,
  "bindings": [
    {
      "imported": "OrderedDict",
      "local": "OrderedDict"
    }
  ]
}
```

```text
No docstring available.
```

## from collections.abc import Callable, Mapping, MutableMapping

```json
{
  "name": "from collections.abc import Callable, Mapping, MutableMapping",
  "kind": "import",
  "line": 61,
  "from_module": "collections.abc",
  "level": 0,
  "bindings": [
    {
      "imported": "Callable",
      "local": "Callable"
    },
    {
      "imported": "Mapping",
      "local": "Mapping"
    },
    {
      "imported": "MutableMapping",
      "local": "MutableMapping"
    }
  ]
}
```

```text
No docstring available.
```

## from http import cookiejar as cookielib

```json
{
  "name": "from http import cookiejar as cookielib",
  "kind": "import",
  "line": 62,
  "from_module": "http",
  "level": 0,
  "bindings": [
    {
      "imported": "cookiejar",
      "local": "cookielib"
    }
  ]
}
```

```text
No docstring available.
```

## from http.cookies import Morsel

```json
{
  "name": "from http.cookies import Morsel",
  "kind": "import",
  "line": 63,
  "from_module": "http.cookies",
  "level": 0,
  "bindings": [
    {
      "imported": "Morsel",
      "local": "Morsel"
    }
  ]
}
```

```text
No docstring available.
```

## from io import StringIO

```json
{
  "name": "from io import StringIO",
  "kind": "import",
  "line": 64,
  "from_module": "io",
  "level": 0,
  "bindings": [
    {
      "imported": "StringIO",
      "local": "StringIO"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib.parse import quote, quote_plus, unquote, unquote_plus, urldefrag, urlencode, urljoin, urlparse, urlsplit, urlunparse

```json
{
  "name": "from urllib.parse import quote, quote_plus, unquote, unquote_plus, urldefrag, urlencode, urljoin, urlparse, urlsplit, urlunparse",
  "kind": "import",
  "line": 69,
  "from_module": "urllib.parse",
  "level": 0,
  "bindings": [
    {
      "imported": "quote",
      "local": "quote"
    },
    {
      "imported": "quote_plus",
      "local": "quote_plus"
    },
    {
      "imported": "unquote",
      "local": "unquote"
    },
    {
      "imported": "unquote_plus",
      "local": "unquote_plus"
    },
    {
      "imported": "urldefrag",
      "local": "urldefrag"
    },
    {
      "imported": "urlencode",
      "local": "urlencode"
    },
    {
      "imported": "urljoin",
      "local": "urljoin"
    },
    {
      "imported": "urlparse",
      "local": "urlparse"
    },
    {
      "imported": "urlsplit",
      "local": "urlsplit"
    },
    {
      "imported": "urlunparse",
      "local": "urlunparse"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib.request import getproxies, getproxies_environment, parse_http_list, proxy_bypass, proxy_bypass_environment

```json
{
  "name": "from urllib.request import getproxies, getproxies_environment, parse_http_list, proxy_bypass, proxy_bypass_environment",
  "kind": "import",
  "line": 81,
  "from_module": "urllib.request",
  "level": 0,
  "bindings": [
    {
      "imported": "getproxies",
      "local": "getproxies"
    },
    {
      "imported": "getproxies_environment",
      "local": "getproxies_environment"
    },
    {
      "imported": "parse_http_list",
      "local": "parse_http_list"
    },
    {
      "imported": "proxy_bypass",
      "local": "proxy_bypass"
    },
    {
      "imported": "proxy_bypass_environment",
      "local": "proxy_bypass_environment"
    }
  ]
}
```

```text
No docstring available.
```

## builtin_str

```json
{
  "name": "builtin_str",
  "kind": "assignment",
  "line": 89,
  "source": "builtin_str = str"
}
```

```text
No docstring available.
```

## str

```json
{
  "name": "str",
  "kind": "assignment",
  "line": 90,
  "source": "str = str"
}
```

```text
No docstring available.
```

## bytes

```json
{
  "name": "bytes",
  "kind": "assignment",
  "line": 91,
  "source": "bytes = bytes"
}
```

```text
No docstring available.
```

## basestring

```json
{
  "name": "basestring",
  "kind": "assignment",
  "line": 92,
  "source": "basestring = (str, bytes)"
}
```

```text
No docstring available.
```

## numeric_types

```json
{
  "name": "numeric_types",
  "kind": "assignment",
  "line": 93,
  "source": "numeric_types = (int, float)"
}
```

```text
No docstring available.
```

## integer_types

```json
{
  "name": "integer_types",
  "kind": "assignment",
  "line": 94,
  "source": "integer_types = (int,)"
}
```

```text
No docstring available.
```
