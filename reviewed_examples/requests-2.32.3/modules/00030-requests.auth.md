# requests.auth

Source: `requests/auth.py`

```text

requests.auth
~~~~~~~~~~~~~

This module contains the authentication handlers for Requests.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.auth')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import hashlib

```json
{
  "name": "import hashlib",
  "kind": "import",
  "line": 8,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "hashlib",
      "local": "hashlib"
    }
  ]
}
```

```text
No docstring available.
```

## import os

```json
{
  "name": "import os",
  "kind": "import",
  "line": 9,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "os",
      "local": "os"
    }
  ]
}
```

```text
No docstring available.
```

## import re

```json
{
  "name": "import re",
  "kind": "import",
  "line": 10,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "re",
      "local": "re"
    }
  ]
}
```

```text
No docstring available.
```

## import threading

```json
{
  "name": "import threading",
  "kind": "import",
  "line": 11,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "threading",
      "local": "threading"
    }
  ]
}
```

```text
No docstring available.
```

## import time

```json
{
  "name": "import time",
  "kind": "import",
  "line": 12,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "time",
      "local": "time"
    }
  ]
}
```

```text
No docstring available.
```

## import warnings

```json
{
  "name": "import warnings",
  "kind": "import",
  "line": 13,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "warnings",
      "local": "warnings"
    }
  ]
}
```

```text
No docstring available.
```

## from base64 import b64encode

```json
{
  "name": "from base64 import b64encode",
  "kind": "import",
  "line": 14,
  "from_module": "base64",
  "level": 0,
  "bindings": [
    {
      "imported": "b64encode",
      "local": "b64encode"
    }
  ]
}
```

```text
No docstring available.
```

## from ._internal_utils import to_native_string

```json
{
  "name": "from ._internal_utils import to_native_string",
  "kind": "import",
  "line": 16,
  "from_module": "_internal_utils",
  "level": 1,
  "bindings": [
    {
      "imported": "to_native_string",
      "local": "to_native_string"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import basestring, str, urlparse

```json
{
  "name": "from .compat import basestring, str, urlparse",
  "kind": "import",
  "line": 17,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "basestring",
      "local": "basestring"
    },
    {
      "imported": "str",
      "local": "str"
    },
    {
      "imported": "urlparse",
      "local": "urlparse"
    }
  ]
}
```

```text
No docstring available.
```

## from .cookies import extract_cookies_to_jar

```json
{
  "name": "from .cookies import extract_cookies_to_jar",
  "kind": "import",
  "line": 18,
  "from_module": "cookies",
  "level": 1,
  "bindings": [
    {
      "imported": "extract_cookies_to_jar",
      "local": "extract_cookies_to_jar"
    }
  ]
}
```

```text
No docstring available.
```

## from .utils import parse_dict_header

```json
{
  "name": "from .utils import parse_dict_header",
  "kind": "import",
  "line": 19,
  "from_module": "utils",
  "level": 1,
  "bindings": [
    {
      "imported": "parse_dict_header",
      "local": "parse_dict_header"
    }
  ]
}
```

```text
No docstring available.
```

## CONTENT_TYPE_FORM_URLENCODED

```json
{
  "name": "CONTENT_TYPE_FORM_URLENCODED",
  "kind": "assignment",
  "line": 21,
  "source": "CONTENT_TYPE_FORM_URLENCODED = 'application/x-www-form-urlencoded'"
}
```

```text
No docstring available.
```

## CONTENT_TYPE_MULTI_PART

```json
{
  "name": "CONTENT_TYPE_MULTI_PART",
  "kind": "assignment",
  "line": 22,
  "source": "CONTENT_TYPE_MULTI_PART = 'multipart/form-data'"
}
```

```text
No docstring available.
```

## _basic_auth_str

```json
{
  "name": "_basic_auth_str",
  "kind": "function",
  "signature": "_basic_auth_str(username, password)",
  "line": 25,
  "decorators": [],
  "parameters": [
    {
      "name": "username",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "password",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Returns a Basic Auth string.
```

## AuthBase

```json
{
  "name": "AuthBase",
  "kind": "class",
  "line": 69,
  "bases": [],
  "decorators": []
}
```

```text
Base class that all auth implementations derive from
```

### __call__

```json
{
  "name": "__call__",
  "kind": "function",
  "signature": "__call__(self, r)",
  "line": 72,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "r",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

## HTTPBasicAuth

```json
{
  "name": "HTTPBasicAuth",
  "kind": "class",
  "line": 76,
  "bases": [
    "AuthBase"
  ],
  "decorators": []
}
```

```text
Attaches HTTP Basic Authentication to the given Request object.
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, username, password)",
  "line": 79,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "username",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "password",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "signature": "__eq__(self, other)",
  "line": 83,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "other",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "signature": "__ne__(self, other)",
  "line": 91,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "other",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __call__

```json
{
  "name": "__call__",
  "kind": "function",
  "signature": "__call__(self, r)",
  "line": 94,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "r",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

## HTTPProxyAuth

```json
{
  "name": "HTTPProxyAuth",
  "kind": "class",
  "line": 99,
  "bases": [
    "HTTPBasicAuth"
  ],
  "decorators": []
}
```

```text
Attaches HTTP Proxy Authentication to a given Request object.
```

### __call__

```json
{
  "name": "__call__",
  "kind": "function",
  "signature": "__call__(self, r)",
  "line": 102,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "r",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

## HTTPDigestAuth

```json
{
  "name": "HTTPDigestAuth",
  "kind": "class",
  "line": 107,
  "bases": [
    "AuthBase"
  ],
  "decorators": []
}
```

```text
Attaches HTTP Digest Authentication to the given Request object.
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, username, password)",
  "line": 110,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "username",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "password",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### init_per_thread_state

```json
{
  "name": "init_per_thread_state",
  "kind": "function",
  "signature": "init_per_thread_state(self)",
  "line": 116,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### build_digest_header

```json
{
  "name": "build_digest_header",
  "kind": "function",
  "signature": "build_digest_header(self, method, url)",
  "line": 126,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "method",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text

        :rtype: str
        
```

### handle_redirect

```json
{
  "name": "handle_redirect",
  "kind": "function",
  "signature": "handle_redirect(self, r, **kwargs)",
  "line": 236,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "r",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "variadic keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Reset num_401_calls counter on redirects.
```

### handle_401

```json
{
  "name": "handle_401",
  "kind": "function",
  "signature": "handle_401(self, r, **kwargs)",
  "line": 241,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "r",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "variadic keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text

        Takes the given response and tries digest-auth, if needed.

        :rtype: requests.Response
        
```

### __call__

```json
{
  "name": "__call__",
  "kind": "function",
  "signature": "__call__(self, r)",
  "line": 285,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "r",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "signature": "__eq__(self, other)",
  "line": 305,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "other",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "signature": "__ne__(self, other)",
  "line": 313,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "other",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```
