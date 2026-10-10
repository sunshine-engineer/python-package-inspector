# requests

Source: `requests/__init__.py`

```text

Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import warnings

```json
{
  "name": "import warnings",
  "kind": "import",
  "line": 41,
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

## import urllib3

```json
{
  "name": "import urllib3",
  "kind": "import",
  "line": 43,
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

## from .exceptions import RequestsDependencyWarning

```json
{
  "name": "from .exceptions import RequestsDependencyWarning",
  "kind": "import",
  "line": 45,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "RequestsDependencyWarning",
      "local": "RequestsDependencyWarning"
    }
  ]
}
```

```text
No docstring available.
```

## from charset_normalizer import __version__ as charset_normalizer_version

```json
{
  "name": "from charset_normalizer import __version__ as charset_normalizer_version",
  "kind": "import",
  "line": 48,
  "from_module": "charset_normalizer",
  "level": 0,
  "bindings": [
    {
      "imported": "__version__",
      "local": "charset_normalizer_version"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## charset_normalizer_version

```json
{
  "name": "charset_normalizer_version",
  "kind": "assignment",
  "line": 50,
  "source": "charset_normalizer_version = None",
  "conditional": true
}
```

```text
No docstring available.
```

## from chardet import __version__ as chardet_version

```json
{
  "name": "from chardet import __version__ as chardet_version",
  "kind": "import",
  "line": 53,
  "from_module": "chardet",
  "level": 0,
  "bindings": [
    {
      "imported": "__version__",
      "local": "chardet_version"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## chardet_version

```json
{
  "name": "chardet_version",
  "kind": "assignment",
  "line": 55,
  "source": "chardet_version = None",
  "conditional": true
}
```

```text
No docstring available.
```

## check_compatibility

```json
{
  "name": "check_compatibility",
  "kind": "function",
  "signature": "check_compatibility(urllib3_version, chardet_version, charset_normalizer_version)",
  "line": 58,
  "decorators": [],
  "parameters": [
    {
      "name": "urllib3_version",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chardet_version",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "charset_normalizer_version",
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

## _check_cryptography

```json
{
  "name": "_check_cryptography",
  "kind": "function",
  "signature": "_check_cryptography(cryptography_version)",
  "line": 93,
  "decorators": [],
  "parameters": [
    {
      "name": "cryptography_version",
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

## import ssl

```json
{
  "name": "import ssl",
  "kind": "import",
  "line": 126,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "ssl",
      "local": "ssl"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## ssl

```json
{
  "name": "ssl",
  "kind": "assignment",
  "line": 128,
  "source": "ssl = None",
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
  "line": 131,
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

## from cryptography import __version__ as cryptography_version

```json
{
  "name": "from cryptography import __version__ as cryptography_version",
  "kind": "import",
  "line": 136,
  "from_module": "cryptography",
  "level": 0,
  "bindings": [
    {
      "imported": "__version__",
      "local": "cryptography_version"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## from urllib3.exceptions import DependencyWarning

```json
{
  "name": "from urllib3.exceptions import DependencyWarning",
  "kind": "import",
  "line": 143,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "DependencyWarning",
      "local": "DependencyWarning"
    }
  ]
}
```

```text
No docstring available.
```

## import logging

```json
{
  "name": "import logging",
  "kind": "import",
  "line": 148,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "logging",
      "local": "logging"
    }
  ]
}
```

```text
No docstring available.
```

## from logging import NullHandler

```json
{
  "name": "from logging import NullHandler",
  "kind": "import",
  "line": 149,
  "from_module": "logging",
  "level": 0,
  "bindings": [
    {
      "imported": "NullHandler",
      "local": "NullHandler"
    }
  ]
}
```

```text
No docstring available.
```

## from . import packages, utils

```json
{
  "name": "from . import packages, utils",
  "kind": "import",
  "line": 151,
  "from_module": null,
  "level": 1,
  "bindings": [
    {
      "imported": "packages",
      "local": "packages"
    },
    {
      "imported": "utils",
      "local": "utils"
    }
  ]
}
```

```text
No docstring available.
```

## from .__version__ import __author__, __author_email__, __build__, __cake__, __copyright__, __description__, __license__, __title__, __url__, __version__

```json
{
  "name": "from .__version__ import __author__, __author_email__, __build__, __cake__, __copyright__, __description__, __license__, __title__, __url__, __version__",
  "kind": "import",
  "line": 152,
  "from_module": "__version__",
  "level": 1,
  "bindings": [
    {
      "imported": "__author__",
      "local": "__author__"
    },
    {
      "imported": "__author_email__",
      "local": "__author_email__"
    },
    {
      "imported": "__build__",
      "local": "__build__"
    },
    {
      "imported": "__cake__",
      "local": "__cake__"
    },
    {
      "imported": "__copyright__",
      "local": "__copyright__"
    },
    {
      "imported": "__description__",
      "local": "__description__"
    },
    {
      "imported": "__license__",
      "local": "__license__"
    },
    {
      "imported": "__title__",
      "local": "__title__"
    },
    {
      "imported": "__url__",
      "local": "__url__"
    },
    {
      "imported": "__version__",
      "local": "__version__"
    }
  ]
}
```

```text
No docstring available.
```

## from .api import delete, get, head, options, patch, post, put, request

```json
{
  "name": "from .api import delete, get, head, options, patch, post, put, request",
  "kind": "import",
  "line": 164,
  "from_module": "api",
  "level": 1,
  "bindings": [
    {
      "imported": "delete",
      "local": "delete"
    },
    {
      "imported": "get",
      "local": "get"
    },
    {
      "imported": "head",
      "local": "head"
    },
    {
      "imported": "options",
      "local": "options"
    },
    {
      "imported": "patch",
      "local": "patch"
    },
    {
      "imported": "post",
      "local": "post"
    },
    {
      "imported": "put",
      "local": "put"
    },
    {
      "imported": "request",
      "local": "request"
    }
  ]
}
```

```text
No docstring available.
```

## from .exceptions import ConnectionError, ConnectTimeout, FileModeWarning, HTTPError, JSONDecodeError, ReadTimeout, RequestException, Timeout, TooManyRedirects, URLRequired

```json
{
  "name": "from .exceptions import ConnectionError, ConnectTimeout, FileModeWarning, HTTPError, JSONDecodeError, ReadTimeout, RequestException, Timeout, TooManyRedirects, URLRequired",
  "kind": "import",
  "line": 165,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "ConnectionError",
      "local": "ConnectionError"
    },
    {
      "imported": "ConnectTimeout",
      "local": "ConnectTimeout"
    },
    {
      "imported": "FileModeWarning",
      "local": "FileModeWarning"
    },
    {
      "imported": "HTTPError",
      "local": "HTTPError"
    },
    {
      "imported": "JSONDecodeError",
      "local": "JSONDecodeError"
    },
    {
      "imported": "ReadTimeout",
      "local": "ReadTimeout"
    },
    {
      "imported": "RequestException",
      "local": "RequestException"
    },
    {
      "imported": "Timeout",
      "local": "Timeout"
    },
    {
      "imported": "TooManyRedirects",
      "local": "TooManyRedirects"
    },
    {
      "imported": "URLRequired",
      "local": "URLRequired"
    }
  ]
}
```

```text
No docstring available.
```

## from .models import PreparedRequest, Request, Response

```json
{
  "name": "from .models import PreparedRequest, Request, Response",
  "kind": "import",
  "line": 177,
  "from_module": "models",
  "level": 1,
  "bindings": [
    {
      "imported": "PreparedRequest",
      "local": "PreparedRequest"
    },
    {
      "imported": "Request",
      "local": "Request"
    },
    {
      "imported": "Response",
      "local": "Response"
    }
  ]
}
```

```text
No docstring available.
```

## from .sessions import Session, session

```json
{
  "name": "from .sessions import Session, session",
  "kind": "import",
  "line": 178,
  "from_module": "sessions",
  "level": 1,
  "bindings": [
    {
      "imported": "Session",
      "local": "Session"
    },
    {
      "imported": "session",
      "local": "session"
    }
  ]
}
```

```text
No docstring available.
```

## from .status_codes import codes

```json
{
  "name": "from .status_codes import codes",
  "kind": "import",
  "line": 179,
  "from_module": "status_codes",
  "level": 1,
  "bindings": [
    {
      "imported": "codes",
      "local": "codes"
    }
  ]
}
```

```text
No docstring available.
```
