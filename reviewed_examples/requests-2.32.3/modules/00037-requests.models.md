# requests.models

Source: `requests/models.py`

```text

requests.models
~~~~~~~~~~~~~~~

This module contains the primary objects that power Requests.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.models')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import datetime

```json
{
  "name": "import datetime",
  "kind": "import",
  "line": 8,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "datetime",
      "local": "datetime"
    }
  ]
}
```

```text
No docstring available.
```

## import encodings.idna

```json
{
  "name": "import encodings.idna",
  "kind": "import",
  "line": 13,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "encodings.idna",
      "local": "encodings"
    }
  ]
}
```

```text
No docstring available.
```

## from io import UnsupportedOperation

```json
{
  "name": "from io import UnsupportedOperation",
  "kind": "import",
  "line": 14,
  "from_module": "io",
  "level": 0,
  "bindings": [
    {
      "imported": "UnsupportedOperation",
      "local": "UnsupportedOperation"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.exceptions import DecodeError, LocationParseError, ProtocolError, ReadTimeoutError, SSLError

```json
{
  "name": "from urllib3.exceptions import DecodeError, LocationParseError, ProtocolError, ReadTimeoutError, SSLError",
  "kind": "import",
  "line": 16,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "DecodeError",
      "local": "DecodeError"
    },
    {
      "imported": "LocationParseError",
      "local": "LocationParseError"
    },
    {
      "imported": "ProtocolError",
      "local": "ProtocolError"
    },
    {
      "imported": "ReadTimeoutError",
      "local": "ReadTimeoutError"
    },
    {
      "imported": "SSLError",
      "local": "SSLError"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.fields import RequestField

```json
{
  "name": "from urllib3.fields import RequestField",
  "kind": "import",
  "line": 23,
  "from_module": "urllib3.fields",
  "level": 0,
  "bindings": [
    {
      "imported": "RequestField",
      "local": "RequestField"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.filepost import encode_multipart_formdata

```json
{
  "name": "from urllib3.filepost import encode_multipart_formdata",
  "kind": "import",
  "line": 24,
  "from_module": "urllib3.filepost",
  "level": 0,
  "bindings": [
    {
      "imported": "encode_multipart_formdata",
      "local": "encode_multipart_formdata"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.util import parse_url

```json
{
  "name": "from urllib3.util import parse_url",
  "kind": "import",
  "line": 25,
  "from_module": "urllib3.util",
  "level": 0,
  "bindings": [
    {
      "imported": "parse_url",
      "local": "parse_url"
    }
  ]
}
```

```text
No docstring available.
```

## from ._internal_utils import to_native_string, unicode_is_ascii

```json
{
  "name": "from ._internal_utils import to_native_string, unicode_is_ascii",
  "kind": "import",
  "line": 27,
  "from_module": "_internal_utils",
  "level": 1,
  "bindings": [
    {
      "imported": "to_native_string",
      "local": "to_native_string"
    },
    {
      "imported": "unicode_is_ascii",
      "local": "unicode_is_ascii"
    }
  ]
}
```

```text
No docstring available.
```

## from .auth import HTTPBasicAuth

```json
{
  "name": "from .auth import HTTPBasicAuth",
  "kind": "import",
  "line": 28,
  "from_module": "auth",
  "level": 1,
  "bindings": [
    {
      "imported": "HTTPBasicAuth",
      "local": "HTTPBasicAuth"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import Callable, JSONDecodeError, Mapping, basestring, builtin_str, chardet, cookielib

```json
{
  "name": "from .compat import Callable, JSONDecodeError, Mapping, basestring, builtin_str, chardet, cookielib",
  "kind": "import",
  "line": 29,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "Callable",
      "local": "Callable"
    },
    {
      "imported": "JSONDecodeError",
      "local": "JSONDecodeError"
    },
    {
      "imported": "Mapping",
      "local": "Mapping"
    },
    {
      "imported": "basestring",
      "local": "basestring"
    },
    {
      "imported": "builtin_str",
      "local": "builtin_str"
    },
    {
      "imported": "chardet",
      "local": "chardet"
    },
    {
      "imported": "cookielib",
      "local": "cookielib"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import json as complexjson

```json
{
  "name": "from .compat import json as complexjson",
  "kind": "import",
  "line": 38,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "json",
      "local": "complexjson"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import urlencode, urlsplit, urlunparse

```json
{
  "name": "from .compat import urlencode, urlsplit, urlunparse",
  "kind": "import",
  "line": 39,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "urlencode",
      "local": "urlencode"
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

## from .cookies import _copy_cookie_jar, cookiejar_from_dict, get_cookie_header

```json
{
  "name": "from .cookies import _copy_cookie_jar, cookiejar_from_dict, get_cookie_header",
  "kind": "import",
  "line": 40,
  "from_module": "cookies",
  "level": 1,
  "bindings": [
    {
      "imported": "_copy_cookie_jar",
      "local": "_copy_cookie_jar"
    },
    {
      "imported": "cookiejar_from_dict",
      "local": "cookiejar_from_dict"
    },
    {
      "imported": "get_cookie_header",
      "local": "get_cookie_header"
    }
  ]
}
```

```text
No docstring available.
```

## from .exceptions import ChunkedEncodingError, ConnectionError, ContentDecodingError, HTTPError, InvalidJSONError, InvalidURL

```json
{
  "name": "from .exceptions import ChunkedEncodingError, ConnectionError, ContentDecodingError, HTTPError, InvalidJSONError, InvalidURL",
  "kind": "import",
  "line": 41,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "ChunkedEncodingError",
      "local": "ChunkedEncodingError"
    },
    {
      "imported": "ConnectionError",
      "local": "ConnectionError"
    },
    {
      "imported": "ContentDecodingError",
      "local": "ContentDecodingError"
    },
    {
      "imported": "HTTPError",
      "local": "HTTPError"
    },
    {
      "imported": "InvalidJSONError",
      "local": "InvalidJSONError"
    },
    {
      "imported": "InvalidURL",
      "local": "InvalidURL"
    }
  ]
}
```

```text
No docstring available.
```

## from .exceptions import JSONDecodeError as RequestsJSONDecodeError

```json
{
  "name": "from .exceptions import JSONDecodeError as RequestsJSONDecodeError",
  "kind": "import",
  "line": 49,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "JSONDecodeError",
      "local": "RequestsJSONDecodeError"
    }
  ]
}
```

```text
No docstring available.
```

## from .exceptions import MissingSchema

```json
{
  "name": "from .exceptions import MissingSchema",
  "kind": "import",
  "line": 50,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "MissingSchema",
      "local": "MissingSchema"
    }
  ]
}
```

```text
No docstring available.
```

## from .exceptions import SSLError as RequestsSSLError

```json
{
  "name": "from .exceptions import SSLError as RequestsSSLError",
  "kind": "import",
  "line": 51,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "SSLError",
      "local": "RequestsSSLError"
    }
  ]
}
```

```text
No docstring available.
```

## from .exceptions import StreamConsumedError

```json
{
  "name": "from .exceptions import StreamConsumedError",
  "kind": "import",
  "line": 52,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "StreamConsumedError",
      "local": "StreamConsumedError"
    }
  ]
}
```

```text
No docstring available.
```

## from .hooks import default_hooks

```json
{
  "name": "from .hooks import default_hooks",
  "kind": "import",
  "line": 53,
  "from_module": "hooks",
  "level": 1,
  "bindings": [
    {
      "imported": "default_hooks",
      "local": "default_hooks"
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
  "line": 54,
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

## from .structures import CaseInsensitiveDict

```json
{
  "name": "from .structures import CaseInsensitiveDict",
  "kind": "import",
  "line": 55,
  "from_module": "structures",
  "level": 1,
  "bindings": [
    {
      "imported": "CaseInsensitiveDict",
      "local": "CaseInsensitiveDict"
    }
  ]
}
```

```text
No docstring available.
```

## from .utils import check_header_validity, get_auth_from_url, guess_filename, guess_json_utf, iter_slices, parse_header_links, requote_uri, stream_decode_response_unicode, super_len, to_key_val_list

```json
{
  "name": "from .utils import check_header_validity, get_auth_from_url, guess_filename, guess_json_utf, iter_slices, parse_header_links, requote_uri, stream_decode_response_unicode, super_len, to_key_val_list",
  "kind": "import",
  "line": 56,
  "from_module": "utils",
  "level": 1,
  "bindings": [
    {
      "imported": "check_header_validity",
      "local": "check_header_validity"
    },
    {
      "imported": "get_auth_from_url",
      "local": "get_auth_from_url"
    },
    {
      "imported": "guess_filename",
      "local": "guess_filename"
    },
    {
      "imported": "guess_json_utf",
      "local": "guess_json_utf"
    },
    {
      "imported": "iter_slices",
      "local": "iter_slices"
    },
    {
      "imported": "parse_header_links",
      "local": "parse_header_links"
    },
    {
      "imported": "requote_uri",
      "local": "requote_uri"
    },
    {
      "imported": "stream_decode_response_unicode",
      "local": "stream_decode_response_unicode"
    },
    {
      "imported": "super_len",
      "local": "super_len"
    },
    {
      "imported": "to_key_val_list",
      "local": "to_key_val_list"
    }
  ]
}
```

```text
No docstring available.
```

## REDIRECT_STATI

```json
{
  "name": "REDIRECT_STATI",
  "kind": "assignment",
  "line": 71,
  "source": "REDIRECT_STATI = (codes.moved, codes.found, codes.other, codes.temporary_redirect, codes.permanent_redirect)"
}
```

```text
No docstring available.
```

## DEFAULT_REDIRECT_LIMIT

```json
{
  "name": "DEFAULT_REDIRECT_LIMIT",
  "kind": "assignment",
  "line": 79,
  "source": "DEFAULT_REDIRECT_LIMIT = 30"
}
```

```text
No docstring available.
```

## CONTENT_CHUNK_SIZE

```json
{
  "name": "CONTENT_CHUNK_SIZE",
  "kind": "assignment",
  "line": 80,
  "source": "CONTENT_CHUNK_SIZE = 10 * 1024"
}
```

```text
No docstring available.
```

## ITER_CHUNK_SIZE

```json
{
  "name": "ITER_CHUNK_SIZE",
  "kind": "assignment",
  "line": 81,
  "source": "ITER_CHUNK_SIZE = 512"
}
```

```text
No docstring available.
```

## RequestEncodingMixin

```json
{
  "name": "RequestEncodingMixin",
  "kind": "class",
  "line": 84,
  "bases": [],
  "decorators": []
}
```

```text
No docstring available.
```

### path_url

```json
{
  "name": "path_url",
  "kind": "function",
  "signature": "path_url(self)",
  "line": 86,
  "decorators": [
    "property"
  ],
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
Build the path URL to use.
```

### _encode_params

```json
{
  "name": "_encode_params",
  "kind": "function",
  "signature": "_encode_params(data)",
  "line": 107,
  "decorators": [
    "staticmethod"
  ],
  "parameters": [
    {
      "name": "data",
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
Encode parameters in a piece of data.

        Will successfully encode parameters when passed as a dict or a list of
        2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
        if parameters are supplied as a dict.
        
```

### _encode_files

```json
{
  "name": "_encode_files",
  "kind": "function",
  "signature": "_encode_files(files, data)",
  "line": 137,
  "decorators": [
    "staticmethod"
  ],
  "parameters": [
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "data",
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
Build the body for a multipart/form-data request.

        Will successfully encode files when passed as a dict or a list of
        tuples. Order is retained if data is a list of tuples but arbitrary
        if parameters are supplied as a dict.
        The tuples may be 2-tuples (filename, fileobj), 3-tuples (filename, fileobj, contentype)
        or 4-tuples (filename, fileobj, contentype, custom_headers).
        
```

## RequestHooksMixin

```json
{
  "name": "RequestHooksMixin",
  "kind": "class",
  "line": 206,
  "bases": [],
  "decorators": []
}
```

```text
No docstring available.
```

### register_hook

```json
{
  "name": "register_hook",
  "kind": "function",
  "signature": "register_hook(self, event, hook)",
  "line": 207,
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
      "name": "event",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hook",
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
Properly register a hook.
```

### deregister_hook

```json
{
  "name": "deregister_hook",
  "kind": "function",
  "signature": "deregister_hook(self, event, hook)",
  "line": 218,
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
      "name": "event",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hook",
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
Deregister a previously registered hook.
        Returns True if the hook existed, False if not.
        
```

## Request

```json
{
  "name": "Request",
  "kind": "class",
  "line": 230,
  "bases": [
    "RequestHooksMixin"
  ],
  "decorators": []
}
```

```text
A user-created :class:`Request <Request>` object.

    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

    :param method: HTTP method to use.
    :param url: URL to send.
    :param headers: dictionary of headers to send.
    :param files: dictionary of {filename: fileobject} files to multipart upload.
    :param data: the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param json: json for the body to attach to the request (if files or data is not specified).
    :param params: URL parameters to append to the URL. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param auth: Auth handler or (user, pass) tuple.
    :param cookies: dictionary or CookieJar of cookies to attach to this request.
    :param hooks: dictionary of callback hooks, for internal usage.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> req.prepare()
      <PreparedRequest [GET]>
    
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)",
  "line": 258,
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
      "default": "None",
      "required": false
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "params",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "auth",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cookies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "json",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "signature": "__repr__(self)",
  "line": 292,
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

### prepare

```json
{
  "name": "prepare",
  "kind": "function",
  "signature": "prepare(self)",
  "line": 295,
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
Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.
```

## PreparedRequest

```json
{
  "name": "PreparedRequest",
  "kind": "class",
  "line": 313,
  "bases": [
    "RequestEncodingMixin",
    "RequestHooksMixin"
  ],
  "decorators": []
}
```

```text
The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
    containing the exact bytes that will be sent to the server.

    Instances are generated from a :class:`Request <Request>` object, and
    should not be instantiated manually; doing so may produce undesirable
    effects.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> r = req.prepare()
      >>> r
      <PreparedRequest [GET]>

      >>> s = requests.Session()
      >>> s.send(r)
      <Response [200]>
    
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self)",
  "line": 334,
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

### prepare

```json
{
  "name": "prepare",
  "kind": "function",
  "signature": "prepare(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)",
  "line": 351,
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
      "default": "None",
      "required": false
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "params",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "auth",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cookies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "json",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Prepares the entire request with the given parameters.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "signature": "__repr__(self)",
  "line": 379,
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

### copy

```json
{
  "name": "copy",
  "kind": "function",
  "signature": "copy(self)",
  "line": 382,
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

### prepare_method

```json
{
  "name": "prepare_method",
  "kind": "function",
  "signature": "prepare_method(self, method)",
  "line": 393,
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
    }
  ],
  "returns": null
}
```

```text
Prepares the given HTTP method.
```

### _get_idna_encoded_host

```json
{
  "name": "_get_idna_encoded_host",
  "kind": "function",
  "signature": "_get_idna_encoded_host(host)",
  "line": 400,
  "decorators": [
    "staticmethod"
  ],
  "parameters": [
    {
      "name": "host",
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

### prepare_url

```json
{
  "name": "prepare_url",
  "kind": "function",
  "signature": "prepare_url(self, url, params)",
  "line": 409,
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
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "params",
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
Prepares the given HTTP URL.
```

### prepare_headers

```json
{
  "name": "prepare_headers",
  "kind": "function",
  "signature": "prepare_headers(self, headers)",
  "line": 483,
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
      "name": "headers",
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
Prepares the given HTTP headers.
```

### prepare_body

```json
{
  "name": "prepare_body",
  "kind": "function",
  "signature": "prepare_body(self, data, files, json=None)",
  "line": 494,
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
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "json",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Prepares the given HTTP body data.
```

### prepare_content_length

```json
{
  "name": "prepare_content_length",
  "kind": "function",
  "signature": "prepare_content_length(self, body)",
  "line": 572,
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
      "name": "body",
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
Prepare Content-Length header based on request method and body
```

### prepare_auth

```json
{
  "name": "prepare_auth",
  "kind": "function",
  "signature": "prepare_auth(self, auth, url='')",
  "line": 588,
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
      "name": "auth",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "''",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Prepares the given HTTP auth data.
```

### prepare_cookies

```json
{
  "name": "prepare_cookies",
  "kind": "function",
  "signature": "prepare_cookies(self, cookies)",
  "line": 610,
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
      "name": "cookies",
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
Prepares the given HTTP cookie data.

        This function eventually generates a ``Cookie`` header from the
        given cookies using cookielib. Due to cookielib's design, the header
        will not be regenerated if it already exists, meaning this function
        can only be called once for the life of the
        :class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
        to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
        header is removed beforehand.
        
```

### prepare_hooks

```json
{
  "name": "prepare_hooks",
  "kind": "function",
  "signature": "prepare_hooks(self, hooks)",
  "line": 630,
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
      "name": "hooks",
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
Prepares the given hooks.
```

## Response

```json
{
  "name": "Response",
  "kind": "class",
  "line": 640,
  "bases": [],
  "decorators": []
}
```

```text
The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.
    
```

### __attrs__

```json
{
  "name": "__attrs__",
  "kind": "assignment",
  "line": 645,
  "source": "__attrs__ = ['_content', 'status_code', 'headers', 'url', 'history', 'encoding', 'reason', 'cookies', 'elapsed', 'request']"
}
```

```text
No docstring available.
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self)",
  "line": 658,
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

### __enter__

```json
{
  "name": "__enter__",
  "kind": "function",
  "signature": "__enter__(self)",
  "line": 705,
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

### __exit__

```json
{
  "name": "__exit__",
  "kind": "function",
  "signature": "__exit__(self, *args)",
  "line": 708,
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
      "name": "args",
      "kind": "variadic positional",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "signature": "__getstate__(self)",
  "line": 711,
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

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "signature": "__setstate__(self, state)",
  "line": 719,
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
      "name": "state",
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

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "signature": "__repr__(self)",
  "line": 727,
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

### __bool__

```json
{
  "name": "__bool__",
  "kind": "function",
  "signature": "__bool__(self)",
  "line": 730,
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
Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
```

### __nonzero__

```json
{
  "name": "__nonzero__",
  "kind": "function",
  "signature": "__nonzero__(self)",
  "line": 740,
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
Returns True if :attr:`status_code` is less than 400.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code, is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
```

### __iter__

```json
{
  "name": "__iter__",
  "kind": "function",
  "signature": "__iter__(self)",
  "line": 750,
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
Allows you to use a response as an iterator.
```

### ok

```json
{
  "name": "ok",
  "kind": "function",
  "signature": "ok(self)",
  "line": 755,
  "decorators": [
    "property"
  ],
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
Returns True if :attr:`status_code` is less than 400, False if not.

        This attribute checks if the status code of the response is between
        400 and 600 to see if there was a client error or a server error. If
        the status code is between 200 and 400, this will return True. This
        is **not** a check to see if the response code is ``200 OK``.
        
```

### is_redirect

```json
{
  "name": "is_redirect",
  "kind": "function",
  "signature": "is_redirect(self)",
  "line": 770,
  "decorators": [
    "property"
  ],
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
True if this Response is a well-formed HTTP redirect that could have
        been processed automatically (by :meth:`Session.resolve_redirects`).
        
```

### is_permanent_redirect

```json
{
  "name": "is_permanent_redirect",
  "kind": "function",
  "signature": "is_permanent_redirect(self)",
  "line": 777,
  "decorators": [
    "property"
  ],
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
True if this Response one of the permanent versions of redirect.
```

### next

```json
{
  "name": "next",
  "kind": "function",
  "signature": "next(self)",
  "line": 785,
  "decorators": [
    "property"
  ],
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
Returns a PreparedRequest for the next request in a redirect chain, if there is one.
```

### apparent_encoding

```json
{
  "name": "apparent_encoding",
  "kind": "function",
  "signature": "apparent_encoding(self)",
  "line": 790,
  "decorators": [
    "property"
  ],
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
The apparent encoding, provided by the charset_normalizer or chardet libraries.
```

### iter_content

```json
{
  "name": "iter_content",
  "kind": "function",
  "signature": "iter_content(self, chunk_size=1, decode_unicode=False)",
  "line": 799,
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
      "name": "chunk_size",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "1",
      "required": false
    },
    {
      "name": "decode_unicode",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Iterates over the response data.  When stream=True is set on the
        request, this avoids reading the content at once into memory for
        large responses.  The chunk size is the number of bytes it should
        read into memory.  This is not necessarily the length of each item
        returned as decoding can take place.

        chunk_size must be of type int or None. A value of None will
        function differently depending on the value of `stream`.
        stream=True will read data as it arrives in whatever size the
        chunks are received. If stream=False, data is returned as
        a single chunk.

        If decode_unicode is True, content will be decoded using the best
        available encoding based on the response.
        
```

### iter_lines

```json
{
  "name": "iter_lines",
  "kind": "function",
  "signature": "iter_lines(self, chunk_size=ITER_CHUNK_SIZE, decode_unicode=False, delimiter=None)",
  "line": 857,
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
      "name": "chunk_size",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "ITER_CHUNK_SIZE",
      "required": false
    },
    {
      "name": "decode_unicode",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "delimiter",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Iterates over the response data, one line at a time.  When
        stream=True is set on the request, this avoids reading the
        content at once into memory for large responses.

        .. note:: This method is not reentrant safe.
        
```

### content

```json
{
  "name": "content",
  "kind": "function",
  "signature": "content(self)",
  "line": 891,
  "decorators": [
    "property"
  ],
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
Content of the response, in bytes.
```

### text

```json
{
  "name": "text",
  "kind": "function",
  "signature": "text(self)",
  "line": 910,
  "decorators": [
    "property"
  ],
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
Content of the response, in unicode.

        If Response.encoding is None, encoding will be guessed using
        ``charset_normalizer`` or ``chardet``.

        The encoding of the response content is determined based solely on HTTP
        headers, following RFC 2616 to the letter. If you can take advantage of
        non-HTTP knowledge to make a better guess at the encoding, you should
        set ``r.encoding`` appropriately before accessing this property.
        
```

### json

```json
{
  "name": "json",
  "kind": "function",
  "signature": "json(self, **kwargs)",
  "line": 947,
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
Returns the json-encoded content of a response, if any.

        :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
        :raises requests.exceptions.JSONDecodeError: If the response body does not
            contain valid json.
        
```

### links

```json
{
  "name": "links",
  "kind": "function",
  "signature": "links(self)",
  "line": 981,
  "decorators": [
    "property"
  ],
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
Returns the parsed header links of the response, if any.
```

### raise_for_status

```json
{
  "name": "raise_for_status",
  "kind": "function",
  "signature": "raise_for_status(self)",
  "line": 997,
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
Raises :class:`HTTPError`, if one occurred.
```

### close

```json
{
  "name": "close",
  "kind": "function",
  "signature": "close(self)",
  "line": 1026,
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
Releases the connection back to the pool. Once this method has been
        called the underlying ``raw`` object must not be accessed again.

        *Note: Should not normally need to be called explicitly.*
        
```
