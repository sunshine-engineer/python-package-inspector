# requests.sessions

Source: `requests/sessions.py`

```text

requests.sessions
~~~~~~~~~~~~~~~~~

This module provides a Session object to manage and persist settings across
requests (cookies, auth, proxies).

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.sessions')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import os

```json
{
  "name": "import os",
  "kind": "import",
  "line": 8,
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

## import sys

```json
{
  "name": "import sys",
  "kind": "import",
  "line": 9,
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

## import time

```json
{
  "name": "import time",
  "kind": "import",
  "line": 10,
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

## from collections import OrderedDict

```json
{
  "name": "from collections import OrderedDict",
  "kind": "import",
  "line": 11,
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

## from datetime import timedelta

```json
{
  "name": "from datetime import timedelta",
  "kind": "import",
  "line": 12,
  "from_module": "datetime",
  "level": 0,
  "bindings": [
    {
      "imported": "timedelta",
      "local": "timedelta"
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

## from .adapters import HTTPAdapter

```json
{
  "name": "from .adapters import HTTPAdapter",
  "kind": "import",
  "line": 15,
  "from_module": "adapters",
  "level": 1,
  "bindings": [
    {
      "imported": "HTTPAdapter",
      "local": "HTTPAdapter"
    }
  ]
}
```

```text
No docstring available.
```

## from .auth import _basic_auth_str

```json
{
  "name": "from .auth import _basic_auth_str",
  "kind": "import",
  "line": 16,
  "from_module": "auth",
  "level": 1,
  "bindings": [
    {
      "imported": "_basic_auth_str",
      "local": "_basic_auth_str"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import Mapping, cookielib, urljoin, urlparse

```json
{
  "name": "from .compat import Mapping, cookielib, urljoin, urlparse",
  "kind": "import",
  "line": 17,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "Mapping",
      "local": "Mapping"
    },
    {
      "imported": "cookielib",
      "local": "cookielib"
    },
    {
      "imported": "urljoin",
      "local": "urljoin"
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

## from .cookies import RequestsCookieJar, cookiejar_from_dict, extract_cookies_to_jar, merge_cookies

```json
{
  "name": "from .cookies import RequestsCookieJar, cookiejar_from_dict, extract_cookies_to_jar, merge_cookies",
  "kind": "import",
  "line": 18,
  "from_module": "cookies",
  "level": 1,
  "bindings": [
    {
      "imported": "RequestsCookieJar",
      "local": "RequestsCookieJar"
    },
    {
      "imported": "cookiejar_from_dict",
      "local": "cookiejar_from_dict"
    },
    {
      "imported": "extract_cookies_to_jar",
      "local": "extract_cookies_to_jar"
    },
    {
      "imported": "merge_cookies",
      "local": "merge_cookies"
    }
  ]
}
```

```text
No docstring available.
```

## from .exceptions import ChunkedEncodingError, ContentDecodingError, InvalidSchema, TooManyRedirects

```json
{
  "name": "from .exceptions import ChunkedEncodingError, ContentDecodingError, InvalidSchema, TooManyRedirects",
  "kind": "import",
  "line": 24,
  "from_module": "exceptions",
  "level": 1,
  "bindings": [
    {
      "imported": "ChunkedEncodingError",
      "local": "ChunkedEncodingError"
    },
    {
      "imported": "ContentDecodingError",
      "local": "ContentDecodingError"
    },
    {
      "imported": "InvalidSchema",
      "local": "InvalidSchema"
    },
    {
      "imported": "TooManyRedirects",
      "local": "TooManyRedirects"
    }
  ]
}
```

```text
No docstring available.
```

## from .hooks import default_hooks, dispatch_hook

```json
{
  "name": "from .hooks import default_hooks, dispatch_hook",
  "kind": "import",
  "line": 30,
  "from_module": "hooks",
  "level": 1,
  "bindings": [
    {
      "imported": "default_hooks",
      "local": "default_hooks"
    },
    {
      "imported": "dispatch_hook",
      "local": "dispatch_hook"
    }
  ]
}
```

```text
No docstring available.
```

## from .models import DEFAULT_REDIRECT_LIMIT, REDIRECT_STATI, PreparedRequest, Request

```json
{
  "name": "from .models import DEFAULT_REDIRECT_LIMIT, REDIRECT_STATI, PreparedRequest, Request",
  "kind": "import",
  "line": 33,
  "from_module": "models",
  "level": 1,
  "bindings": [
    {
      "imported": "DEFAULT_REDIRECT_LIMIT",
      "local": "DEFAULT_REDIRECT_LIMIT"
    },
    {
      "imported": "REDIRECT_STATI",
      "local": "REDIRECT_STATI"
    },
    {
      "imported": "PreparedRequest",
      "local": "PreparedRequest"
    },
    {
      "imported": "Request",
      "local": "Request"
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
  "line": 39,
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
  "line": 40,
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

## from .utils import DEFAULT_PORTS, default_headers, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, resolve_proxies, rewind_body, should_bypass_proxies, to_key_val_list

```json
{
  "name": "from .utils import DEFAULT_PORTS, default_headers, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, resolve_proxies, rewind_body, should_bypass_proxies, to_key_val_list",
  "kind": "import",
  "line": 41,
  "from_module": "utils",
  "level": 1,
  "bindings": [
    {
      "imported": "DEFAULT_PORTS",
      "local": "DEFAULT_PORTS"
    },
    {
      "imported": "default_headers",
      "local": "default_headers"
    },
    {
      "imported": "get_auth_from_url",
      "local": "get_auth_from_url"
    },
    {
      "imported": "get_environ_proxies",
      "local": "get_environ_proxies"
    },
    {
      "imported": "get_netrc_auth",
      "local": "get_netrc_auth"
    },
    {
      "imported": "requote_uri",
      "local": "requote_uri"
    },
    {
      "imported": "resolve_proxies",
      "local": "resolve_proxies"
    },
    {
      "imported": "rewind_body",
      "local": "rewind_body"
    },
    {
      "imported": "should_bypass_proxies",
      "local": "should_bypass_proxies"
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

## preferred_clock

```json
{
  "name": "preferred_clock",
  "kind": "assignment",
  "line": 56,
  "source": "preferred_clock = time.perf_counter",
  "conditional": true
}
```

```text
No docstring available.
```

## preferred_clock

```json
{
  "name": "preferred_clock",
  "kind": "assignment",
  "line": 58,
  "source": "preferred_clock = time.time",
  "conditional": true
}
```

```text
No docstring available.
```

## merge_setting

```json
{
  "name": "merge_setting",
  "kind": "function",
  "signature": "merge_setting(request_setting, session_setting, dict_class=OrderedDict)",
  "line": 61,
  "decorators": [],
  "parameters": [
    {
      "name": "request_setting",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "session_setting",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "dict_class",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "OrderedDict",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Determines appropriate setting for a given request, taking into account
    the explicit setting on that request, and the setting in the session. If a
    setting is a dictionary, they will be merged together using `dict_class`
    
```

## merge_hooks

```json
{
  "name": "merge_hooks",
  "kind": "function",
  "signature": "merge_hooks(request_hooks, session_hooks, dict_class=OrderedDict)",
  "line": 91,
  "decorators": [],
  "parameters": [
    {
      "name": "request_hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "session_hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "dict_class",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "OrderedDict",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Properly merges both requests and session hooks.

    This is necessary because when request_hooks == {'response': []}, the
    merge breaks Session hooks entirely.
    
```

## SessionRedirectMixin

```json
{
  "name": "SessionRedirectMixin",
  "kind": "class",
  "line": 106,
  "bases": [],
  "decorators": []
}
```

```text
No docstring available.
```

### get_redirect_target

```json
{
  "name": "get_redirect_target",
  "kind": "function",
  "signature": "get_redirect_target(self, resp)",
  "line": 107,
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
      "name": "resp",
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
Receives a Response. Returns a redirect URI or ``None``
```

### should_strip_auth

```json
{
  "name": "should_strip_auth",
  "kind": "function",
  "signature": "should_strip_auth(self, old_url, new_url)",
  "line": 127,
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
      "name": "old_url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "new_url",
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
Decide whether Authorization header should be removed when redirecting
```

### resolve_redirects

```json
{
  "name": "resolve_redirects",
  "kind": "function",
  "signature": "resolve_redirects(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs)",
  "line": 159,
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
      "name": "resp",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "req",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "stream",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "timeout",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    },
    {
      "name": "cert",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "yield_requests",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "adapter_kwargs",
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
Receives a Response. Returns a generator of Responses or Requests.
```

### rebuild_auth

```json
{
  "name": "rebuild_auth",
  "kind": "function",
  "signature": "rebuild_auth(self, prepared_request, response)",
  "line": 282,
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
      "name": "prepared_request",
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
When being redirected we may want to strip authentication from the
        request to avoid leaking credentials. This method intelligently removes
        and reapplies authentication where possible to avoid credential loss.
        
```

### rebuild_proxies

```json
{
  "name": "rebuild_proxies",
  "kind": "function",
  "signature": "rebuild_proxies(self, prepared_request, proxies)",
  "line": 302,
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
      "name": "prepared_request",
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
This method re-evaluates the proxy configuration by considering the
        environment variables. If we are redirected to a URL covered by
        NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
        proxy keys for this URL (in case they were stripped by a previous
        redirect).

        This method also replaces the Proxy-Authorization header where
        necessary.

        :rtype: dict
        
```

### rebuild_method

```json
{
  "name": "rebuild_method",
  "kind": "function",
  "signature": "rebuild_method(self, prepared_request, response)",
  "line": 333,
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
      "name": "prepared_request",
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
When being redirected we may want to change the method of the request
        based on certain specs or browser behavior.
        
```

## Session

```json
{
  "name": "Session",
  "kind": "class",
  "line": 356,
  "bases": [
    "SessionRedirectMixin"
  ],
  "decorators": []
}
```

```text
A Requests session.

    Provides cookie persistence, connection-pooling, and configuration.

    Basic Usage::

      >>> import requests
      >>> s = requests.Session()
      >>> s.get('https://httpbin.org/get')
      <Response [200]>

    Or as a context manager::

      >>> with requests.Session() as s:
      ...     s.get('https://httpbin.org/get')
      <Response [200]>
    
```

### __attrs__

```json
{
  "name": "__attrs__",
  "kind": "assignment",
  "line": 375,
  "source": "__attrs__ = ['headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify', 'cert', 'adapters', 'stream', 'trust_env', 'max_redirects']"
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
  "line": 390,
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
  "line": 451,
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
  "line": 454,
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

### prepare_request

```json
{
  "name": "prepare_request",
  "kind": "function",
  "signature": "prepare_request(self, request)",
  "line": 457,
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
Constructs a :class:`PreparedRequest <PreparedRequest>` for
        transmission and returns it. The :class:`PreparedRequest` has settings
        merged from the :class:`Request <Request>` instance and those of the
        :class:`Session`.

        :param request: :class:`Request` instance to prepare with this
            session's settings.
        :rtype: requests.PreparedRequest
        
```

### request

```json
{
  "name": "request",
  "kind": "function",
  "signature": "request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)",
  "line": 500,
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
    },
    {
      "name": "params",
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
      "name": "headers",
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
      "name": "files",
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
      "name": "timeout",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "allow_redirects",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    },
    {
      "name": "proxies",
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
      "name": "stream",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cert",
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
Constructs a :class:`Request <Request>`, prepares it and sends it.
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param hooks: (optional) Dictionary mapping hook name to one event or
            list of events, event must be callable.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``. When set to
            ``False``, requests will accept any TLS certificate presented by
            the server, and will ignore hostname mismatches and/or expired
            certificates, which will make your application vulnerable to
            man-in-the-middle (MitM) attacks. Setting verify to ``False``
            may be useful during local development or testing.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        
```

### get

```json
{
  "name": "get",
  "kind": "function",
  "signature": "get(self, url, **kwargs)",
  "line": 593,
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
Sends a GET request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
```

### options

```json
{
  "name": "options",
  "kind": "function",
  "signature": "options(self, url, **kwargs)",
  "line": 604,
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
Sends a OPTIONS request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
```

### head

```json
{
  "name": "head",
  "kind": "function",
  "signature": "head(self, url, **kwargs)",
  "line": 615,
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
Sends a HEAD request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
```

### post

```json
{
  "name": "post",
  "kind": "function",
  "signature": "post(self, url, data=None, json=None, **kwargs)",
  "line": 626,
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
      "name": "data",
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
Sends a POST request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
```

### put

```json
{
  "name": "put",
  "kind": "function",
  "signature": "put(self, url, data=None, **kwargs)",
  "line": 639,
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
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
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
Sends a PUT request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
```

### patch

```json
{
  "name": "patch",
  "kind": "function",
  "signature": "patch(self, url, data=None, **kwargs)",
  "line": 651,
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
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
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
Sends a PATCH request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
```

### delete

```json
{
  "name": "delete",
  "kind": "function",
  "signature": "delete(self, url, **kwargs)",
  "line": 663,
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
Sends a DELETE request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
```

### send

```json
{
  "name": "send",
  "kind": "function",
  "signature": "send(self, request, **kwargs)",
  "line": 673,
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
Send a given PreparedRequest.

        :rtype: requests.Response
        
```

### merge_environment_settings

```json
{
  "name": "merge_environment_settings",
  "kind": "function",
  "signature": "merge_environment_settings(self, url, proxies, stream, verify, cert)",
  "line": 750,
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
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "stream",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cert",
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

        Check the environment and merge it with some settings.

        :rtype: dict
        
```

### get_adapter

```json
{
  "name": "get_adapter",
  "kind": "function",
  "signature": "get_adapter(self, url)",
  "line": 781,
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
    }
  ],
  "returns": null
}
```

```text

        Returns the appropriate connection adapter for the given URL.

        :rtype: requests.adapters.BaseAdapter
        
```

### close

```json
{
  "name": "close",
  "kind": "function",
  "signature": "close(self)",
  "line": 794,
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
Closes all adapters and as such the session
```

### mount

```json
{
  "name": "mount",
  "kind": "function",
  "signature": "mount(self, prefix, adapter)",
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
      "name": "prefix",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "adapter",
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
Registers a connection adapter to a prefix.

        Adapters are sorted in descending order by prefix length.
        
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "signature": "__getstate__(self)",
  "line": 810,
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
  "line": 814,
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

## session

```json
{
  "name": "session",
  "kind": "function",
  "signature": "session()",
  "line": 819,
  "decorators": [],
  "parameters": [],
  "returns": null
}
```

```text

    Returns a :class:`Session` for context-management.

    .. deprecated:: 1.0.0

        This method has been deprecated since version 1.0.0 and is only kept for
        backwards compatibility. New code should use :class:`~requests.sessions.Session`
        to create a session. This may be removed at a future date.

    :rtype: Session
    
```
