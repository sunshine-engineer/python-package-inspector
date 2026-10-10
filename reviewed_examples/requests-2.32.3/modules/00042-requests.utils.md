# requests.utils

Source: `requests/utils.py`

```text

requests.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within Requests
that are also useful for external consumption.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.utils')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import codecs

```json
{
  "name": "import codecs",
  "kind": "import",
  "line": 9,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "codecs",
      "local": "codecs"
    }
  ]
}
```

```text
No docstring available.
```

## import contextlib

```json
{
  "name": "import contextlib",
  "kind": "import",
  "line": 10,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "contextlib",
      "local": "contextlib"
    }
  ]
}
```

```text
No docstring available.
```

## import io

```json
{
  "name": "import io",
  "kind": "import",
  "line": 11,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "io",
      "local": "io"
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
  "line": 12,
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
  "line": 13,
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

## import socket

```json
{
  "name": "import socket",
  "kind": "import",
  "line": 14,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "socket",
      "local": "socket"
    }
  ]
}
```

```text
No docstring available.
```

## import struct

```json
{
  "name": "import struct",
  "kind": "import",
  "line": 15,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "struct",
      "local": "struct"
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
  "line": 16,
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

## import tempfile

```json
{
  "name": "import tempfile",
  "kind": "import",
  "line": 17,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "tempfile",
      "local": "tempfile"
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
  "line": 18,
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

## import zipfile

```json
{
  "name": "import zipfile",
  "kind": "import",
  "line": 19,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "zipfile",
      "local": "zipfile"
    }
  ]
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
  "line": 20,
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

## from urllib3.util import make_headers, parse_url

```json
{
  "name": "from urllib3.util import make_headers, parse_url",
  "kind": "import",
  "line": 22,
  "from_module": "urllib3.util",
  "level": 0,
  "bindings": [
    {
      "imported": "make_headers",
      "local": "make_headers"
    },
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

## from . import certs

```json
{
  "name": "from . import certs",
  "kind": "import",
  "line": 24,
  "from_module": null,
  "level": 1,
  "bindings": [
    {
      "imported": "certs",
      "local": "certs"
    }
  ]
}
```

```text
No docstring available.
```

## from .__version__ import __version__

```json
{
  "name": "from .__version__ import __version__",
  "kind": "import",
  "line": 25,
  "from_module": "__version__",
  "level": 1,
  "bindings": [
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

## from ._internal_utils import _HEADER_VALIDATORS_BYTE, _HEADER_VALIDATORS_STR, HEADER_VALIDATORS, to_native_string

```json
{
  "name": "from ._internal_utils import _HEADER_VALIDATORS_BYTE, _HEADER_VALIDATORS_STR, HEADER_VALIDATORS, to_native_string",
  "kind": "import",
  "line": 28,
  "from_module": "_internal_utils",
  "level": 1,
  "bindings": [
    {
      "imported": "_HEADER_VALIDATORS_BYTE",
      "local": "_HEADER_VALIDATORS_BYTE"
    },
    {
      "imported": "_HEADER_VALIDATORS_STR",
      "local": "_HEADER_VALIDATORS_STR"
    },
    {
      "imported": "HEADER_VALIDATORS",
      "local": "HEADER_VALIDATORS"
    },
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

## from .compat import Mapping, basestring, bytes, getproxies, getproxies_environment, integer_types

```json
{
  "name": "from .compat import Mapping, basestring, bytes, getproxies, getproxies_environment, integer_types",
  "kind": "import",
  "line": 34,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "Mapping",
      "local": "Mapping"
    },
    {
      "imported": "basestring",
      "local": "basestring"
    },
    {
      "imported": "bytes",
      "local": "bytes"
    },
    {
      "imported": "getproxies",
      "local": "getproxies"
    },
    {
      "imported": "getproxies_environment",
      "local": "getproxies_environment"
    },
    {
      "imported": "integer_types",
      "local": "integer_types"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import parse_http_list as _parse_list_header

```json
{
  "name": "from .compat import parse_http_list as _parse_list_header",
  "kind": "import",
  "line": 42,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "parse_http_list",
      "local": "_parse_list_header"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import proxy_bypass, proxy_bypass_environment, quote, str, unquote, urlparse, urlunparse

```json
{
  "name": "from .compat import proxy_bypass, proxy_bypass_environment, quote, str, unquote, urlparse, urlunparse",
  "kind": "import",
  "line": 43,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "proxy_bypass",
      "local": "proxy_bypass"
    },
    {
      "imported": "proxy_bypass_environment",
      "local": "proxy_bypass_environment"
    },
    {
      "imported": "quote",
      "local": "quote"
    },
    {
      "imported": "str",
      "local": "str"
    },
    {
      "imported": "unquote",
      "local": "unquote"
    },
    {
      "imported": "urlparse",
      "local": "urlparse"
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

## from .cookies import cookiejar_from_dict

```json
{
  "name": "from .cookies import cookiejar_from_dict",
  "kind": "import",
  "line": 52,
  "from_module": "cookies",
  "level": 1,
  "bindings": [
    {
      "imported": "cookiejar_from_dict",
      "local": "cookiejar_from_dict"
    }
  ]
}
```

```text
No docstring available.
```

## from .exceptions import FileModeWarning, InvalidHeader, InvalidURL, UnrewindableBodyError

```json
{
  "name": "from .exceptions import FileModeWarning, InvalidHeader, InvalidURL, UnrewindableBodyError",
  "kind": "import",
  "line": 53,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "FileModeWarning",
      "local": "FileModeWarning"
    },
    {
      "imported": "InvalidHeader",
      "local": "InvalidHeader"
    },
    {
      "imported": "InvalidURL",
      "local": "InvalidURL"
    },
    {
      "imported": "UnrewindableBodyError",
      "local": "UnrewindableBodyError"
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
  "line": 59,
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

## NETRC_FILES

```json
{
  "name": "NETRC_FILES",
  "kind": "assignment",
  "line": 61,
  "source": "NETRC_FILES = ('.netrc', '_netrc')"
}
```

```text
No docstring available.
```

## DEFAULT_CA_BUNDLE_PATH

```json
{
  "name": "DEFAULT_CA_BUNDLE_PATH",
  "kind": "assignment",
  "line": 63,
  "source": "DEFAULT_CA_BUNDLE_PATH = certs.where()"
}
```

```text
No docstring available.
```

## DEFAULT_PORTS

```json
{
  "name": "DEFAULT_PORTS",
  "kind": "assignment",
  "line": 65,
  "source": "DEFAULT_PORTS = {'http': 80, 'https': 443}"
}
```

```text
No docstring available.
```

## DEFAULT_ACCEPT_ENCODING

```json
{
  "name": "DEFAULT_ACCEPT_ENCODING",
  "kind": "assignment",
  "line": 68,
  "source": "DEFAULT_ACCEPT_ENCODING = ', '.join(re.split(',\\\\s*', make_headers(accept_encoding=True)['accept-encoding']))"
}
```

```text
No docstring available.
```

## proxy_bypass_registry

```json
{
  "name": "proxy_bypass_registry",
  "kind": "function",
  "signature": "proxy_bypass_registry(host)",
  "line": 76,
  "decorators": [],
  "parameters": [
    {
      "name": "host",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null,
  "conditional": true
}
```

```text
No docstring available.
```

## proxy_bypass

```json
{
  "name": "proxy_bypass",
  "kind": "function",
  "signature": "proxy_bypass(host)",
  "line": 114,
  "decorators": [],
  "parameters": [
    {
      "name": "host",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null,
  "conditional": true
}
```

```text
Return True, if the host should be bypassed.

        Checks proxy settings gathered from the environment, if specified,
        or the registry.
        
```

## dict_to_sequence

```json
{
  "name": "dict_to_sequence",
  "kind": "function",
  "signature": "dict_to_sequence(d)",
  "line": 126,
  "decorators": [],
  "parameters": [
    {
      "name": "d",
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
Returns an internal sequence dictionary update.
```

## super_len

```json
{
  "name": "super_len",
  "kind": "function",
  "signature": "super_len(o)",
  "line": 135,
  "decorators": [],
  "parameters": [
    {
      "name": "o",
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

## get_netrc_auth

```json
{
  "name": "get_netrc_auth",
  "kind": "function",
  "signature": "get_netrc_auth(url, raise_errors=False)",
  "line": 204,
  "decorators": [],
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "raise_errors",
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
Returns the Requests tuple auth for a given url from netrc.
```

## guess_filename

```json
{
  "name": "guess_filename",
  "kind": "function",
  "signature": "guess_filename(obj)",
  "line": 261,
  "decorators": [],
  "parameters": [
    {
      "name": "obj",
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
Tries to guess the filename of the given object.
```

## extract_zipped_paths

```json
{
  "name": "extract_zipped_paths",
  "kind": "function",
  "signature": "extract_zipped_paths(path)",
  "line": 268,
  "decorators": [],
  "parameters": [
    {
      "name": "path",
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
Replace nonexistent paths that look like they refer to a member of a zip
    archive with the location of an extracted copy of the target, or else
    just return the provided path unchanged.
    
```

## atomic_open

```json
{
  "name": "atomic_open",
  "kind": "function",
  "signature": "atomic_open(filename)",
  "line": 306,
  "decorators": [
    "contextlib.contextmanager"
  ],
  "parameters": [
    {
      "name": "filename",
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
Write a file to the disk in an atomic fashion
```

## from_key_val_list

```json
{
  "name": "from_key_val_list",
  "kind": "function",
  "signature": "from_key_val_list(value)",
  "line": 318,
  "decorators": [],
  "parameters": [
    {
      "name": "value",
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
Take an object and test to see if it can be represented as a
    dictionary. Unless it can not be represented as such, return an
    OrderedDict, e.g.,

    ::

        >>> from_key_val_list([('key', 'val')])
        OrderedDict([('key', 'val')])
        >>> from_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples
        >>> from_key_val_list({'key': 'val'})
        OrderedDict([('key', 'val')])

    :rtype: OrderedDict
    
```

## to_key_val_list

```json
{
  "name": "to_key_val_list",
  "kind": "function",
  "signature": "to_key_val_list(value)",
  "line": 345,
  "decorators": [],
  "parameters": [
    {
      "name": "value",
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
Take an object and test to see if it can be represented as a
    dictionary. If it can be, return a list of tuples, e.g.,

    ::

        >>> to_key_val_list([('key', 'val')])
        [('key', 'val')]
        >>> to_key_val_list({'key': 'val'})
        [('key', 'val')]
        >>> to_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples

    :rtype: list
    
```

## parse_list_header

```json
{
  "name": "parse_list_header",
  "kind": "function",
  "signature": "parse_list_header(value)",
  "line": 375,
  "decorators": [],
  "parameters": [
    {
      "name": "value",
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
Parse lists as described by RFC 2068 Section 2.

    In particular, parse comma-separated lists where the elements of
    the list may include quoted-strings.  A quoted-string could
    contain a comma.  A non-quoted string could have quotes in the
    middle.  Quotes are removed automatically after parsing.

    It basically works like :func:`parse_set_header` just that items
    may appear multiple times and case sensitivity is preserved.

    The return value is a standard :class:`list`:

    >>> parse_list_header('token, "quoted value"')
    ['token', 'quoted value']

    To create a header from the :class:`list` again, use the
    :func:`dump_header` function.

    :param value: a string with a list header.
    :return: :class:`list`
    :rtype: list
    
```

## parse_dict_header

```json
{
  "name": "parse_dict_header",
  "kind": "function",
  "signature": "parse_dict_header(value)",
  "line": 407,
  "decorators": [],
  "parameters": [
    {
      "name": "value",
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
Parse lists of key, value pairs as described by RFC 2068 Section 2 and
    convert them into a python dict:

    >>> d = parse_dict_header('foo="is a fish", bar="as well"')
    >>> type(d) is dict
    True
    >>> sorted(d.items())
    [('bar', 'as well'), ('foo', 'is a fish')]

    If there is no value for a key it will be `None`:

    >>> parse_dict_header('key_without_value')
    {'key_without_value': None}

    To create a header from the :class:`dict` again, use the
    :func:`dump_header` function.

    :param value: a string with a dict header.
    :return: :class:`dict`
    :rtype: dict
    
```

## unquote_header_value

```json
{
  "name": "unquote_header_value",
  "kind": "function",
  "signature": "unquote_header_value(value, is_filename=False)",
  "line": 442,
  "decorators": [],
  "parameters": [
    {
      "name": "value",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "is_filename",
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
Unquotes a header value.  (Reversal of :func:`quote_header_value`).
    This does not use the real unquoting but what browsers are actually
    using for quoting.

    :param value: the header value to unquote.
    :rtype: str
    
```

## dict_from_cookiejar

```json
{
  "name": "dict_from_cookiejar",
  "kind": "function",
  "signature": "dict_from_cookiejar(cj)",
  "line": 467,
  "decorators": [],
  "parameters": [
    {
      "name": "cj",
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
Returns a key/value dictionary from a CookieJar.

    :param cj: CookieJar object to extract cookies from.
    :rtype: dict
    
```

## add_dict_to_cookiejar

```json
{
  "name": "add_dict_to_cookiejar",
  "kind": "function",
  "signature": "add_dict_to_cookiejar(cj, cookie_dict)",
  "line": 478,
  "decorators": [],
  "parameters": [
    {
      "name": "cj",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookie_dict",
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
Returns a CookieJar from a key/value dictionary.

    :param cj: CookieJar to insert cookies into.
    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :rtype: CookieJar
    
```

## get_encodings_from_content

```json
{
  "name": "get_encodings_from_content",
  "kind": "function",
  "signature": "get_encodings_from_content(content)",
  "line": 489,
  "decorators": [],
  "parameters": [
    {
      "name": "content",
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
Returns encodings from given content string.

    :param content: bytestring to extract encodings from.
    
```

## _parse_content_type_header

```json
{
  "name": "_parse_content_type_header",
  "kind": "function",
  "signature": "_parse_content_type_header(header)",
  "line": 514,
  "decorators": [],
  "parameters": [
    {
      "name": "header",
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
Returns content type and parameters from given header

    :param header: string
    :return: tuple containing content type and dictionary of
         parameters
    
```

## get_encoding_from_headers

```json
{
  "name": "get_encoding_from_headers",
  "kind": "function",
  "signature": "get_encoding_from_headers(headers)",
  "line": 539,
  "decorators": [],
  "parameters": [
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
Returns encodings from given HTTP Header Dict.

    :param headers: dictionary to extract encoding from.
    :rtype: str
    
```

## stream_decode_response_unicode

```json
{
  "name": "stream_decode_response_unicode",
  "kind": "function",
  "signature": "stream_decode_response_unicode(iterator, r)",
  "line": 564,
  "decorators": [],
  "parameters": [
    {
      "name": "iterator",
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
Stream decodes an iterator.
```

## iter_slices

```json
{
  "name": "iter_slices",
  "kind": "function",
  "signature": "iter_slices(string, slice_length)",
  "line": 581,
  "decorators": [],
  "parameters": [
    {
      "name": "string",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "slice_length",
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
Iterate over slices of a string.
```

## get_unicode_from_response

```json
{
  "name": "get_unicode_from_response",
  "kind": "function",
  "signature": "get_unicode_from_response(r)",
  "line": 591,
  "decorators": [],
  "parameters": [
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
Returns the requested content back in unicode.

    :param r: Response object to get unicode content from.

    Tried:

    1. charset from content-type
    2. fall back and replace all unicode characters

    :rtype: str
    
```

## UNRESERVED_SET

```json
{
  "name": "UNRESERVED_SET",
  "kind": "assignment",
  "line": 631,
  "source": "UNRESERVED_SET = frozenset('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + '0123456789-._~')"
}
```

```text
No docstring available.
```

## unquote_unreserved

```json
{
  "name": "unquote_unreserved",
  "kind": "function",
  "signature": "unquote_unreserved(uri)",
  "line": 636,
  "decorators": [],
  "parameters": [
    {
      "name": "uri",
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
Un-escape any percent-escape sequences in a URI that are unreserved
    characters. This leaves all reserved, illegal and non-ASCII bytes encoded.

    :rtype: str
    
```

## requote_uri

```json
{
  "name": "requote_uri",
  "kind": "function",
  "signature": "requote_uri(uri)",
  "line": 660,
  "decorators": [],
  "parameters": [
    {
      "name": "uri",
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
Re-quote the given URI.

    This function passes the given URI through an unquote/quote cycle to
    ensure that it is fully and consistently quoted.

    :rtype: str
    
```

## address_in_network

```json
{
  "name": "address_in_network",
  "kind": "function",
  "signature": "address_in_network(ip, net)",
  "line": 682,
  "decorators": [],
  "parameters": [
    {
      "name": "ip",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "net",
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
This function allows you to check if an IP belongs to a network subnet

    Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
             returns False if ip = 192.168.1.1 and net = 192.168.100.0/24

    :rtype: bool
    
```

## dotted_netmask

```json
{
  "name": "dotted_netmask",
  "kind": "function",
  "signature": "dotted_netmask(mask)",
  "line": 697,
  "decorators": [],
  "parameters": [
    {
      "name": "mask",
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
Converts mask from /xx format to xxx.xxx.xxx.xxx

    Example: if mask is 24 function returns 255.255.255.0

    :rtype: str
    
```

## is_ipv4_address

```json
{
  "name": "is_ipv4_address",
  "kind": "function",
  "signature": "is_ipv4_address(string_ip)",
  "line": 708,
  "decorators": [],
  "parameters": [
    {
      "name": "string_ip",
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

    :rtype: bool
    
```

## is_valid_cidr

```json
{
  "name": "is_valid_cidr",
  "kind": "function",
  "signature": "is_valid_cidr(string_network)",
  "line": 719,
  "decorators": [],
  "parameters": [
    {
      "name": "string_network",
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

    Very simple check of the cidr format in no_proxy variable.

    :rtype: bool
    
```

## set_environ

```json
{
  "name": "set_environ",
  "kind": "function",
  "signature": "set_environ(env_name, value)",
  "line": 744,
  "decorators": [
    "contextlib.contextmanager"
  ],
  "parameters": [
    {
      "name": "env_name",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
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
Set the environment variable 'env_name' to 'value'

    Save previous value, yield, and then restore the previous value stored in
    the environment variable 'env_name'.

    If 'value' is None, do nothing
```

## should_bypass_proxies

```json
{
  "name": "should_bypass_proxies",
  "kind": "function",
  "signature": "should_bypass_proxies(url, no_proxy)",
  "line": 765,
  "decorators": [],
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "no_proxy",
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

    Returns whether we should bypass proxies or not.

    :rtype: bool
    
```

## get_environ_proxies

```json
{
  "name": "get_environ_proxies",
  "kind": "function",
  "signature": "get_environ_proxies(url, no_proxy=None)",
  "line": 826,
  "decorators": [],
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "no_proxy",
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

    Return a dict of environment proxies.

    :rtype: dict
    
```

## select_proxy

```json
{
  "name": "select_proxy",
  "kind": "function",
  "signature": "select_proxy(url, proxies)",
  "line": 838,
  "decorators": [],
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
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
Select a proxy for the url, if applicable.

    :param url: The url being for the request
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    
```

## resolve_proxies

```json
{
  "name": "resolve_proxies",
  "kind": "function",
  "signature": "resolve_proxies(request, proxies, trust_env=True)",
  "line": 864,
  "decorators": [],
  "parameters": [
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "trust_env",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    }
  ],
  "returns": null
}
```

```text
This method takes proxy information from a request and configuration
    input to resolve a mapping of target proxies. This will consider settings
    such as NO_PROXY to strip proxy configurations.

    :param request: Request or PreparedRequest
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    :param trust_env: Boolean declaring whether to trust environment configs

    :rtype: dict
    
```

## default_user_agent

```json
{
  "name": "default_user_agent",
  "kind": "function",
  "signature": "default_user_agent(name='python-requests')",
  "line": 891,
  "decorators": [],
  "parameters": [
    {
      "name": "name",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'python-requests'",
      "required": false
    }
  ],
  "returns": null
}
```

```text

    Return a string representing the default user agent.

    :rtype: str
    
```

## default_headers

```json
{
  "name": "default_headers",
  "kind": "function",
  "signature": "default_headers()",
  "line": 900,
  "decorators": [],
  "parameters": [],
  "returns": null
}
```

```text

    :rtype: requests.structures.CaseInsensitiveDict
    
```

## parse_header_links

```json
{
  "name": "parse_header_links",
  "kind": "function",
  "signature": "parse_header_links(value)",
  "line": 914,
  "decorators": [],
  "parameters": [
    {
      "name": "value",
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
Return a list of parsed link headers proxies.

    i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"

    :rtype: list
    
```

## _null

```json
{
  "name": "_null",
  "kind": "assignment",
  "line": 952,
  "source": "_null = '\\x00'.encode('ascii')"
}
```

```text
No docstring available.
```

## _null2

```json
{
  "name": "_null2",
  "kind": "assignment",
  "line": 953,
  "source": "_null2 = _null * 2"
}
```

```text
No docstring available.
```

## _null3

```json
{
  "name": "_null3",
  "kind": "assignment",
  "line": 954,
  "source": "_null3 = _null * 3"
}
```

```text
No docstring available.
```

## guess_json_utf

```json
{
  "name": "guess_json_utf",
  "kind": "function",
  "signature": "guess_json_utf(data)",
  "line": 957,
  "decorators": [],
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

    :rtype: str
    
```

## prepend_scheme_if_needed

```json
{
  "name": "prepend_scheme_if_needed",
  "kind": "function",
  "signature": "prepend_scheme_if_needed(url, new_scheme)",
  "line": 989,
  "decorators": [],
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "new_scheme",
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
Given a URL that may or may not have a scheme, prepend the given scheme.
    Does not replace a present scheme with the one provided as an argument.

    :rtype: str
    
```

## get_auth_from_url

```json
{
  "name": "get_auth_from_url",
  "kind": "function",
  "signature": "get_auth_from_url(url)",
  "line": 1018,
  "decorators": [],
  "parameters": [
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
Given a url with authentication components, extract them into a tuple of
    username,password.

    :rtype: (str,str)
    
```

## check_header_validity

```json
{
  "name": "check_header_validity",
  "kind": "function",
  "signature": "check_header_validity(header)",
  "line": 1034,
  "decorators": [],
  "parameters": [
    {
      "name": "header",
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
Verifies that header parts don't contain leading whitespace
    reserved characters, or return characters.

    :param header: tuple, in the format (name, value).
    
```

## _validate_header_part

```json
{
  "name": "_validate_header_part",
  "kind": "function",
  "signature": "_validate_header_part(header, header_part, header_validator_index)",
  "line": 1045,
  "decorators": [],
  "parameters": [
    {
      "name": "header",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "header_part",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "header_validator_index",
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

## urldefragauth

```json
{
  "name": "urldefragauth",
  "kind": "function",
  "signature": "urldefragauth(url)",
  "line": 1064,
  "decorators": [],
  "parameters": [
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

    Given a url remove the fragment and the authentication part.

    :rtype: str
    
```

## rewind_body

```json
{
  "name": "rewind_body",
  "kind": "function",
  "signature": "rewind_body(prepared_request)",
  "line": 1081,
  "decorators": [],
  "parameters": [
    {
      "name": "prepared_request",
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
Move file pointer back to its recorded starting position
    so it can be read again on redirect.
    
```
