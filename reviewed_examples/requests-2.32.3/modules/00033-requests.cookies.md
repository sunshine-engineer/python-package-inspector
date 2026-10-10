# requests.cookies

Source: `requests/cookies.py`

```text

requests.cookies
~~~~~~~~~~~~~~~~

Compatibility code to be able to use `http.cookiejar.CookieJar` with requests.

requests.utils imports from here, so be careful with imports.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.cookies')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import calendar

```json
{
  "name": "import calendar",
  "kind": "import",
  "line": 10,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "calendar",
      "local": "calendar"
    }
  ]
}
```

```text
No docstring available.
```

## import copy

```json
{
  "name": "import copy",
  "kind": "import",
  "line": 11,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "copy",
      "local": "copy"
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

## from ._internal_utils import to_native_string

```json
{
  "name": "from ._internal_utils import to_native_string",
  "kind": "import",
  "line": 14,
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

## from .compat import Morsel, MutableMapping, cookielib, urlparse, urlunparse

```json
{
  "name": "from .compat import Morsel, MutableMapping, cookielib, urlparse, urlunparse",
  "kind": "import",
  "line": 15,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "Morsel",
      "local": "Morsel"
    },
    {
      "imported": "MutableMapping",
      "local": "MutableMapping"
    },
    {
      "imported": "cookielib",
      "local": "cookielib"
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

## import threading

```json
{
  "name": "import threading",
  "kind": "import",
  "line": 18,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "threading",
      "local": "threading"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## import dummy_threading as threading

```json
{
  "name": "import dummy_threading as threading",
  "kind": "import",
  "line": 20,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "dummy_threading",
      "local": "threading"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## MockRequest

```json
{
  "name": "MockRequest",
  "kind": "class",
  "line": 23,
  "bases": [],
  "decorators": []
}
```

```text
Wraps a `requests.Request` to mimic a `urllib2.Request`.

    The code in `http.cookiejar.CookieJar` expects this interface in order to correctly
    manage cookie policies, i.e., determine whether a cookie can be set, given the
    domains of the request and the cookie.

    The original request object is read-only. The client is responsible for collecting
    the new headers via `get_new_headers()` and interpreting them appropriately. You
    probably want `get_cookie_header`, defined below.
    
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, request)",
  "line": 35,
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
      "name": "request",
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

### get_type

```json
{
  "name": "get_type",
  "kind": "function",
  "signature": "get_type(self)",
  "line": 40,
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

### get_host

```json
{
  "name": "get_host",
  "kind": "function",
  "signature": "get_host(self)",
  "line": 43,
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

### get_origin_req_host

```json
{
  "name": "get_origin_req_host",
  "kind": "function",
  "signature": "get_origin_req_host(self)",
  "line": 46,
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

### get_full_url

```json
{
  "name": "get_full_url",
  "kind": "function",
  "signature": "get_full_url(self)",
  "line": 49,
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

### is_unverifiable

```json
{
  "name": "is_unverifiable",
  "kind": "function",
  "signature": "is_unverifiable(self)",
  "line": 69,
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

### has_header

```json
{
  "name": "has_header",
  "kind": "function",
  "signature": "has_header(self, name)",
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
      "name": "name",
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

### get_header

```json
{
  "name": "get_header",
  "kind": "function",
  "signature": "get_header(self, name, default=None)",
  "line": 75,
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
      "name": "name",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "default",
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

### add_header

```json
{
  "name": "add_header",
  "kind": "function",
  "signature": "add_header(self, key, val)",
  "line": 78,
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
      "name": "key",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "val",
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
cookiejar has no legitimate use for this method; add it back if you find one.
```

### add_unredirected_header

```json
{
  "name": "add_unredirected_header",
  "kind": "function",
  "signature": "add_unredirected_header(self, name, value)",
  "line": 84,
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
      "name": "name",
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
No docstring available.
```

### get_new_headers

```json
{
  "name": "get_new_headers",
  "kind": "function",
  "signature": "get_new_headers(self)",
  "line": 87,
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

### unverifiable

```json
{
  "name": "unverifiable",
  "kind": "function",
  "signature": "unverifiable(self)",
  "line": 91,
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
No docstring available.
```

### origin_req_host

```json
{
  "name": "origin_req_host",
  "kind": "function",
  "signature": "origin_req_host(self)",
  "line": 95,
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
No docstring available.
```

### host

```json
{
  "name": "host",
  "kind": "function",
  "signature": "host(self)",
  "line": 99,
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
No docstring available.
```

## MockResponse

```json
{
  "name": "MockResponse",
  "kind": "class",
  "line": 103,
  "bases": [],
  "decorators": []
}
```

```text
Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.

    ...what? Basically, expose the parsed HTTP headers from the server response
    the way `http.cookiejar` expects to see them.
    
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, headers)",
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
Make a MockResponse for `cookiejar` to read.

        :param headers: a httplib.HTTPMessage or analogous carrying the headers
        
```

### info

```json
{
  "name": "info",
  "kind": "function",
  "signature": "info(self)",
  "line": 117,
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

### getheaders

```json
{
  "name": "getheaders",
  "kind": "function",
  "signature": "getheaders(self, name)",
  "line": 120,
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
      "name": "name",
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

## extract_cookies_to_jar

```json
{
  "name": "extract_cookies_to_jar",
  "kind": "function",
  "signature": "extract_cookies_to_jar(jar, request, response)",
  "line": 124,
  "decorators": [],
  "parameters": [
    {
      "name": "jar",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "response",
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
Extract the cookies from the response into a CookieJar.

    :param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)
    :param request: our own requests.Request object
    :param response: urllib3.HTTPResponse object
    
```

## get_cookie_header

```json
{
  "name": "get_cookie_header",
  "kind": "function",
  "signature": "get_cookie_header(jar, request)",
  "line": 140,
  "decorators": [],
  "parameters": [
    {
      "name": "jar",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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

    Produce an appropriate Cookie header string to be sent with `request`, or None.

    :rtype: str
    
```

## remove_cookie_by_name

```json
{
  "name": "remove_cookie_by_name",
  "kind": "function",
  "signature": "remove_cookie_by_name(cookiejar, name, domain=None, path=None)",
  "line": 151,
  "decorators": [],
  "parameters": [
    {
      "name": "cookiejar",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Unsets a cookie by name, by default over all domains and paths.

    Wraps CookieJar.clear(), is O(n).
    
```

## CookieConflictError

```json
{
  "name": "CookieConflictError",
  "kind": "class",
  "line": 170,
  "bases": [
    "RuntimeError"
  ],
  "decorators": []
}
```

```text
There are two cookies that meet the criteria specified in the cookie jar.
    Use .get and .set and include domain and path args in order to be more specific.
    
```

## RequestsCookieJar

```json
{
  "name": "RequestsCookieJar",
  "kind": "class",
  "line": 176,
  "bases": [
    "cookielib.CookieJar",
    "MutableMapping"
  ],
  "decorators": []
}
```

```text
Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict
    interface.

    This is the CookieJar we create by default for requests and sessions that
    don't specify one, since some clients may expect response.cookies and
    session.cookies to support dict operations.

    Requests does not use the dict interface internally; it's just for
    compatibility with external client code. All requests code should work
    out of the box with externally provided instances of ``CookieJar``, e.g.
    ``LWPCookieJar`` and ``FileCookieJar``.

    Unlike a regular CookieJar, this class is pickleable.

    .. warning:: dictionary operations that are normally O(1) may be O(n).
    
```

### get

```json
{
  "name": "get",
  "kind": "function",
  "signature": "get(self, name, default=None, domain=None, path=None)",
  "line": 194,
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
      "name": "name",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "default",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Dict-like get() that also supports optional domain and path args in
        order to resolve naming collisions from using one cookie jar over
        multiple domains.

        .. warning:: operation is O(n), not O(1).
        
```

### set

```json
{
  "name": "set",
  "kind": "function",
  "signature": "set(self, name, value, **kwargs)",
  "line": 206,
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
      "name": "name",
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
Dict-like set() that also supports optional domain and path args in
        order to resolve naming collisions from using one cookie jar over
        multiple domains.
        
```

### iterkeys

```json
{
  "name": "iterkeys",
  "kind": "function",
  "signature": "iterkeys(self)",
  "line": 225,
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
Dict-like iterkeys() that returns an iterator of names of cookies
        from the jar.

        .. seealso:: itervalues() and iteritems().
        
```

### keys

```json
{
  "name": "keys",
  "kind": "function",
  "signature": "keys(self)",
  "line": 234,
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
Dict-like keys() that returns a list of names of cookies from the
        jar.

        .. seealso:: values() and items().
        
```

### itervalues

```json
{
  "name": "itervalues",
  "kind": "function",
  "signature": "itervalues(self)",
  "line": 242,
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
Dict-like itervalues() that returns an iterator of values of cookies
        from the jar.

        .. seealso:: iterkeys() and iteritems().
        
```

### values

```json
{
  "name": "values",
  "kind": "function",
  "signature": "values(self)",
  "line": 251,
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
Dict-like values() that returns a list of values of cookies from the
        jar.

        .. seealso:: keys() and items().
        
```

### iteritems

```json
{
  "name": "iteritems",
  "kind": "function",
  "signature": "iteritems(self)",
  "line": 259,
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
Dict-like iteritems() that returns an iterator of name-value tuples
        from the jar.

        .. seealso:: iterkeys() and itervalues().
        
```

### items

```json
{
  "name": "items",
  "kind": "function",
  "signature": "items(self)",
  "line": 268,
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
Dict-like items() that returns a list of name-value tuples from the
        jar. Allows client-code to call ``dict(RequestsCookieJar)`` and get a
        vanilla python dict of key value pairs.

        .. seealso:: keys() and values().
        
```

### list_domains

```json
{
  "name": "list_domains",
  "kind": "function",
  "signature": "list_domains(self)",
  "line": 277,
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
Utility method to list all the domains in the jar.
```

### list_paths

```json
{
  "name": "list_paths",
  "kind": "function",
  "signature": "list_paths(self)",
  "line": 285,
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
Utility method to list all the paths in the jar.
```

### multiple_domains

```json
{
  "name": "multiple_domains",
  "kind": "function",
  "signature": "multiple_domains(self)",
  "line": 293,
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
Returns True if there are multiple domains in the jar.
        Returns False otherwise.

        :rtype: bool
        
```

### get_dict

```json
{
  "name": "get_dict",
  "kind": "function",
  "signature": "get_dict(self, domain=None, path=None)",
  "line": 306,
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
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Takes as an argument an optional domain and path and returns a plain
        old Python dict of name-value pairs of cookies that meet the
        requirements.

        :rtype: dict
        
```

### __contains__

```json
{
  "name": "__contains__",
  "kind": "function",
  "signature": "__contains__(self, name)",
  "line": 321,
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
      "name": "name",
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

### __getitem__

```json
{
  "name": "__getitem__",
  "kind": "function",
  "signature": "__getitem__(self, name)",
  "line": 327,
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
      "name": "name",
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
Dict-like __getitem__() for compatibility with client code. Throws
        exception if there are more than one cookie with name. In that case,
        use the more explicit get() method instead.

        .. warning:: operation is O(n), not O(1).
        
```

### __setitem__

```json
{
  "name": "__setitem__",
  "kind": "function",
  "signature": "__setitem__(self, name, value)",
  "line": 336,
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
      "name": "name",
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
Dict-like __setitem__ for compatibility with client code. Throws
        exception if there is already a cookie of that name in the jar. In that
        case, use the more explicit set() method instead.
        
```

### __delitem__

```json
{
  "name": "__delitem__",
  "kind": "function",
  "signature": "__delitem__(self, name)",
  "line": 343,
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
      "name": "name",
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
Deletes a cookie given a name. Wraps ``http.cookiejar.CookieJar``'s
        ``remove_cookie_by_name()``.
        
```

### set_cookie

```json
{
  "name": "set_cookie",
  "kind": "function",
  "signature": "set_cookie(self, cookie, *args, **kwargs)",
  "line": 349,
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
      "name": "cookie",
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
No docstring available.
```

### update

```json
{
  "name": "update",
  "kind": "function",
  "signature": "update(self, other)",
  "line": 358,
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
Updates this jar with cookies from another CookieJar or dict-like
```

### _find

```json
{
  "name": "_find",
  "kind": "function",
  "signature": "_find(self, name, domain=None, path=None)",
  "line": 366,
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
      "name": "name",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Requests uses this method internally to get cookie values.

        If there are conflicting cookies, _find arbitrarily chooses one.
        See _find_no_duplicates if you want an exception thrown if there are
        conflicting cookies.

        :param name: a string containing name of cookie
        :param domain: (optional) string containing domain of cookie
        :param path: (optional) string containing path of cookie
        :return: cookie.value
        
```

### _find_no_duplicates

```json
{
  "name": "_find_no_duplicates",
  "kind": "function",
  "signature": "_find_no_duplicates(self, name, domain=None, path=None)",
  "line": 386,
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
      "name": "name",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Both ``__get_item__`` and ``get`` call this function: it's never
        used elsewhere in Requests.

        :param name: a string containing name of cookie
        :param domain: (optional) string containing domain of cookie
        :param path: (optional) string containing path of cookie
        :raises KeyError: if cookie is not found
        :raises CookieConflictError: if there are multiple cookies
            that match name and optionally domain and path
        :return: cookie.value
        
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "signature": "__getstate__(self)",
  "line": 415,
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
Unlike a normal CookieJar, this class is pickleable.
```

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "signature": "__setstate__(self, state)",
  "line": 422,
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
Unlike a normal CookieJar, this class is pickleable.
```

### copy

```json
{
  "name": "copy",
  "kind": "function",
  "signature": "copy(self)",
  "line": 428,
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
Return a copy of this RequestsCookieJar.
```

### get_policy

```json
{
  "name": "get_policy",
  "kind": "function",
  "signature": "get_policy(self)",
  "line": 435,
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
Return the CookiePolicy instance used.
```

## _copy_cookie_jar

```json
{
  "name": "_copy_cookie_jar",
  "kind": "function",
  "signature": "_copy_cookie_jar(jar)",
  "line": 440,
  "decorators": [],
  "parameters": [
    {
      "name": "jar",
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

## create_cookie

```json
{
  "name": "create_cookie",
  "kind": "function",
  "signature": "create_cookie(name, value, **kwargs)",
  "line": 455,
  "decorators": [],
  "parameters": [
    {
      "name": "name",
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
Make a cookie from underspecified parameters.

    By default, the pair of `name` and `value` will be set for the domain ''
    and sent on every request (this is sometimes called a "supercookie").
    
```

## morsel_to_cookie

```json
{
  "name": "morsel_to_cookie",
  "kind": "function",
  "signature": "morsel_to_cookie(morsel)",
  "line": 492,
  "decorators": [],
  "parameters": [
    {
      "name": "morsel",
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
Convert a Morsel object into a Cookie containing the one k/v pair.
```

## cookiejar_from_dict

```json
{
  "name": "cookiejar_from_dict",
  "kind": "function",
  "signature": "cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)",
  "line": 521,
  "decorators": [],
  "parameters": [
    {
      "name": "cookie_dict",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookiejar",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "overwrite",
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
Returns a CookieJar from a key/value dictionary.

    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :param cookiejar: (optional) A cookiejar to add the cookies to.
    :param overwrite: (optional) If False, will not replace cookies
        already in the jar with new ones.
    :rtype: CookieJar
    
```

## merge_cookies

```json
{
  "name": "merge_cookies",
  "kind": "function",
  "signature": "merge_cookies(cookiejar, cookies)",
  "line": 542,
  "decorators": [],
  "parameters": [
    {
      "name": "cookiejar",
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
Add cookies to cookiejar and returns a merged CookieJar.

    :param cookiejar: CookieJar object to add the cookies to.
    :param cookies: Dictionary or CookieJar object to be added.
    :rtype: CookieJar
    
```
