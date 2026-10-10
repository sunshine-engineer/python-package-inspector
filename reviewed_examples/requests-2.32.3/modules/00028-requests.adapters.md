# requests.adapters

Source: `requests/adapters.py`

```text

requests.adapters
~~~~~~~~~~~~~~~~~

This module contains the transport adapters that Requests uses to define
and maintain connections.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.adapters')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import os.path

```json
{
  "name": "import os.path",
  "kind": "import",
  "line": 9,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "os.path",
      "local": "os"
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
  "line": 10,
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

## import typing

```json
{
  "name": "import typing",
  "kind": "import",
  "line": 11,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "typing",
      "local": "typing"
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
  "line": 12,
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

## from urllib3.exceptions import ClosedPoolError, ConnectTimeoutError

```json
{
  "name": "from urllib3.exceptions import ClosedPoolError, ConnectTimeoutError",
  "kind": "import",
  "line": 14,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "ClosedPoolError",
      "local": "ClosedPoolError"
    },
    {
      "imported": "ConnectTimeoutError",
      "local": "ConnectTimeoutError"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.exceptions import HTTPError as _HTTPError

```json
{
  "name": "from urllib3.exceptions import HTTPError as _HTTPError",
  "kind": "import",
  "line": 15,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "HTTPError",
      "local": "_HTTPError"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.exceptions import InvalidHeader as _InvalidHeader

```json
{
  "name": "from urllib3.exceptions import InvalidHeader as _InvalidHeader",
  "kind": "import",
  "line": 16,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "InvalidHeader",
      "local": "_InvalidHeader"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.exceptions import LocationValueError, MaxRetryError, NewConnectionError, ProtocolError

```json
{
  "name": "from urllib3.exceptions import LocationValueError, MaxRetryError, NewConnectionError, ProtocolError",
  "kind": "import",
  "line": 17,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "LocationValueError",
      "local": "LocationValueError"
    },
    {
      "imported": "MaxRetryError",
      "local": "MaxRetryError"
    },
    {
      "imported": "NewConnectionError",
      "local": "NewConnectionError"
    },
    {
      "imported": "ProtocolError",
      "local": "ProtocolError"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.exceptions import ProxyError as _ProxyError

```json
{
  "name": "from urllib3.exceptions import ProxyError as _ProxyError",
  "kind": "import",
  "line": 23,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "ProxyError",
      "local": "_ProxyError"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.exceptions import ReadTimeoutError, ResponseError

```json
{
  "name": "from urllib3.exceptions import ReadTimeoutError, ResponseError",
  "kind": "import",
  "line": 24,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "ReadTimeoutError",
      "local": "ReadTimeoutError"
    },
    {
      "imported": "ResponseError",
      "local": "ResponseError"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.exceptions import SSLError as _SSLError

```json
{
  "name": "from urllib3.exceptions import SSLError as _SSLError",
  "kind": "import",
  "line": 25,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "SSLError",
      "local": "_SSLError"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.poolmanager import PoolManager, proxy_from_url

```json
{
  "name": "from urllib3.poolmanager import PoolManager, proxy_from_url",
  "kind": "import",
  "line": 26,
  "from_module": "urllib3.poolmanager",
  "level": 0,
  "bindings": [
    {
      "imported": "PoolManager",
      "local": "PoolManager"
    },
    {
      "imported": "proxy_from_url",
      "local": "proxy_from_url"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.util import Timeout as TimeoutSauce

```json
{
  "name": "from urllib3.util import Timeout as TimeoutSauce",
  "kind": "import",
  "line": 27,
  "from_module": "urllib3.util",
  "level": 0,
  "bindings": [
    {
      "imported": "Timeout",
      "local": "TimeoutSauce"
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
  "line": 28,
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

## from urllib3.util.retry import Retry

```json
{
  "name": "from urllib3.util.retry import Retry",
  "kind": "import",
  "line": 29,
  "from_module": "urllib3.util.retry",
  "level": 0,
  "bindings": [
    {
      "imported": "Retry",
      "local": "Retry"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.util.ssl_ import create_urllib3_context

```json
{
  "name": "from urllib3.util.ssl_ import create_urllib3_context",
  "kind": "import",
  "line": 30,
  "from_module": "urllib3.util.ssl_",
  "level": 0,
  "bindings": [
    {
      "imported": "create_urllib3_context",
      "local": "create_urllib3_context"
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
  "line": 32,
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

## from .compat import basestring, urlparse

```json
{
  "name": "from .compat import basestring, urlparse",
  "kind": "import",
  "line": 33,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "basestring",
      "local": "basestring"
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
  "line": 34,
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

## from .exceptions import ConnectionError, ConnectTimeout, InvalidHeader, InvalidProxyURL, InvalidSchema, InvalidURL, ProxyError, ReadTimeout, RetryError, SSLError

```json
{
  "name": "from .exceptions import ConnectionError, ConnectTimeout, InvalidHeader, InvalidProxyURL, InvalidSchema, InvalidURL, ProxyError, ReadTimeout, RetryError, SSLError",
  "kind": "import",
  "line": 35,
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
      "imported": "InvalidHeader",
      "local": "InvalidHeader"
    },
    {
      "imported": "InvalidProxyURL",
      "local": "InvalidProxyURL"
    },
    {
      "imported": "InvalidSchema",
      "local": "InvalidSchema"
    },
    {
      "imported": "InvalidURL",
      "local": "InvalidURL"
    },
    {
      "imported": "ProxyError",
      "local": "ProxyError"
    },
    {
      "imported": "ReadTimeout",
      "local": "ReadTimeout"
    },
    {
      "imported": "RetryError",
      "local": "RetryError"
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

## from .models import Response

```json
{
  "name": "from .models import Response",
  "kind": "import",
  "line": 47,
  "from_module": "models",
  "level": 1,
  "bindings": [
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

## from .structures import CaseInsensitiveDict

```json
{
  "name": "from .structures import CaseInsensitiveDict",
  "kind": "import",
  "line": 48,
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

## from .utils import DEFAULT_CA_BUNDLE_PATH, extract_zipped_paths, get_auth_from_url, get_encoding_from_headers, prepend_scheme_if_needed, select_proxy, urldefragauth

```json
{
  "name": "from .utils import DEFAULT_CA_BUNDLE_PATH, extract_zipped_paths, get_auth_from_url, get_encoding_from_headers, prepend_scheme_if_needed, select_proxy, urldefragauth",
  "kind": "import",
  "line": 49,
  "from_module": "utils",
  "level": 1,
  "bindings": [
    {
      "imported": "DEFAULT_CA_BUNDLE_PATH",
      "local": "DEFAULT_CA_BUNDLE_PATH"
    },
    {
      "imported": "extract_zipped_paths",
      "local": "extract_zipped_paths"
    },
    {
      "imported": "get_auth_from_url",
      "local": "get_auth_from_url"
    },
    {
      "imported": "get_encoding_from_headers",
      "local": "get_encoding_from_headers"
    },
    {
      "imported": "prepend_scheme_if_needed",
      "local": "prepend_scheme_if_needed"
    },
    {
      "imported": "select_proxy",
      "local": "select_proxy"
    },
    {
      "imported": "urldefragauth",
      "local": "urldefragauth"
    }
  ]
}
```

```text
No docstring available.
```

## from urllib3.contrib.socks import SOCKSProxyManager

```json
{
  "name": "from urllib3.contrib.socks import SOCKSProxyManager",
  "kind": "import",
  "line": 60,
  "from_module": "urllib3.contrib.socks",
  "level": 0,
  "bindings": [
    {
      "imported": "SOCKSProxyManager",
      "local": "SOCKSProxyManager"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## SOCKSProxyManager

```json
{
  "name": "SOCKSProxyManager",
  "kind": "function",
  "signature": "SOCKSProxyManager(*args, **kwargs)",
  "line": 63,
  "decorators": [],
  "parameters": [
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
  "returns": null,
  "conditional": true
}
```

```text
No docstring available.
```

## from .models import PreparedRequest

```json
{
  "name": "from .models import PreparedRequest",
  "kind": "import",
  "line": 68,
  "from_module": "models",
  "level": 1,
  "bindings": [
    {
      "imported": "PreparedRequest",
      "local": "PreparedRequest"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## DEFAULT_POOLBLOCK

```json
{
  "name": "DEFAULT_POOLBLOCK",
  "kind": "assignment",
  "line": 71,
  "source": "DEFAULT_POOLBLOCK = False"
}
```

```text
No docstring available.
```

## DEFAULT_POOLSIZE

```json
{
  "name": "DEFAULT_POOLSIZE",
  "kind": "assignment",
  "line": 72,
  "source": "DEFAULT_POOLSIZE = 10"
}
```

```text
No docstring available.
```

## DEFAULT_RETRIES

```json
{
  "name": "DEFAULT_RETRIES",
  "kind": "assignment",
  "line": 73,
  "source": "DEFAULT_RETRIES = 0"
}
```

```text
No docstring available.
```

## DEFAULT_POOL_TIMEOUT

```json
{
  "name": "DEFAULT_POOL_TIMEOUT",
  "kind": "assignment",
  "line": 74,
  "source": "DEFAULT_POOL_TIMEOUT = None"
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
  "line": 78,
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

## _preloaded_ssl_context

```json
{
  "name": "_preloaded_ssl_context",
  "kind": "assignment",
  "line": 80,
  "source": "_preloaded_ssl_context = create_urllib3_context()",
  "conditional": true
}
```

```text
No docstring available.
```

## _preloaded_ssl_context

```json
{
  "name": "_preloaded_ssl_context",
  "kind": "assignment",
  "line": 87,
  "source": "_preloaded_ssl_context = None",
  "conditional": true
}
```

```text
No docstring available.
```

## _urllib3_request_context

```json
{
  "name": "_urllib3_request_context",
  "kind": "function",
  "signature": "_urllib3_request_context(request: 'PreparedRequest', verify: 'bool | str | None', client_cert: 'typing.Tuple[str, str] | str | None', poolmanager: 'PoolManager') -> '(typing.Dict[str, typing.Any], typing.Dict[str, typing.Any])'",
  "line": 90,
  "decorators": [],
  "parameters": [
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": "'PreparedRequest'",
      "default": null,
      "required": true
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": "'bool | str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "client_cert",
      "kind": "positional or keyword",
      "annotation": "'typing.Tuple[str, str] | str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "poolmanager",
      "kind": "positional or keyword",
      "annotation": "'PoolManager'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'(typing.Dict[str, typing.Any], typing.Dict[str, typing.Any])'"
}
```

```text
No docstring available.
```

## BaseAdapter

```json
{
  "name": "BaseAdapter",
  "kind": "class",
  "line": 137,
  "bases": [],
  "decorators": []
}
```

```text
The Base Transport Adapter
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self)",
  "line": 140,
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

### send

```json
{
  "name": "send",
  "kind": "function",
  "signature": "send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None)",
  "line": 143,
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
    }
  ],
  "returns": null
}
```

```text
Sends PreparedRequest object. Returns Response object.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param stream: (optional) Whether to stream the request content.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use
        :param cert: (optional) Any user-provided SSL certificate to be trusted.
        :param proxies: (optional) The proxies dictionary to apply to the request.
        
```

### close

```json
{
  "name": "close",
  "kind": "function",
  "signature": "close(self)",
  "line": 162,
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
Cleans up adapter specific items.
```

## HTTPAdapter

```json
{
  "name": "HTTPAdapter",
  "kind": "class",
  "line": 167,
  "bases": [
    "BaseAdapter"
  ],
  "decorators": []
}
```

```text
The built-in HTTP Adapter for urllib3.

    Provides a general-case interface for Requests sessions to contact HTTP and
    HTTPS urls by implementing the Transport Adapter interface. This class will
    usually be created by the :class:`Session <Session>` class under the
    covers.

    :param pool_connections: The number of urllib3 connection pools to cache.
    :param pool_maxsize: The maximum number of connections to save in the pool.
    :param max_retries: The maximum number of retries each connection
        should attempt. Note, this applies only to failed DNS lookups, socket
        connections and connection timeouts, never to requests where data has
        made it to the server. By default, Requests does not retry failed
        connections. If you need granular control over the conditions under
        which we retry a request, import urllib3's ``Retry`` class and pass
        that instead.
    :param pool_block: Whether the connection pool should block for connections.

    Usage::

      >>> import requests
      >>> s = requests.Session()
      >>> a = requests.adapters.HTTPAdapter(max_retries=3)
      >>> s.mount('http://', a)
    
```

### __attrs__

```json
{
  "name": "__attrs__",
  "kind": "assignment",
  "line": 194,
  "source": "__attrs__ = ['max_retries', 'config', '_pool_connections', '_pool_maxsize', '_pool_block']"
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
  "signature": "__init__(self, pool_connections=DEFAULT_POOLSIZE, pool_maxsize=DEFAULT_POOLSIZE, max_retries=DEFAULT_RETRIES, pool_block=DEFAULT_POOLBLOCK)",
  "line": 202,
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
      "name": "pool_connections",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "DEFAULT_POOLSIZE",
      "required": false
    },
    {
      "name": "pool_maxsize",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "DEFAULT_POOLSIZE",
      "required": false
    },
    {
      "name": "max_retries",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "DEFAULT_RETRIES",
      "required": false
    },
    {
      "name": "pool_block",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "DEFAULT_POOLBLOCK",
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
  "line": 224,
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
  "line": 227,
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

### init_poolmanager

```json
{
  "name": "init_poolmanager",
  "kind": "function",
  "signature": "init_poolmanager(self, connections, maxsize, block=DEFAULT_POOLBLOCK, **pool_kwargs)",
  "line": 240,
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
      "name": "connections",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "maxsize",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "block",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "DEFAULT_POOLBLOCK",
      "required": false
    },
    {
      "name": "pool_kwargs",
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
Initializes a urllib3 PoolManager.

        This method should not be called from user code, and is only
        exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param connections: The number of urllib3 connection pools to cache.
        :param maxsize: The maximum number of connections to save in the pool.
        :param block: Block when no free connections are available.
        :param pool_kwargs: Extra keyword arguments used to initialize the Pool Manager.
        
```

### proxy_manager_for

```json
{
  "name": "proxy_manager_for",
  "kind": "function",
  "signature": "proxy_manager_for(self, proxy, **proxy_kwargs)",
  "line": 266,
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
      "name": "proxy",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxy_kwargs",
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
Return urllib3 ProxyManager for the given proxy.

        This method should not be called from user code, and is only
        exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param proxy: The proxy to return a urllib3 ProxyManager for.
        :param proxy_kwargs: Extra keyword arguments used to configure the Proxy Manager.
        :returns: ProxyManager
        :rtype: urllib3.ProxyManager
        
```

### cert_verify

```json
{
  "name": "cert_verify",
  "kind": "function",
  "signature": "cert_verify(self, conn, url, verify, cert)",
  "line": 304,
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
      "name": "conn",
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
Verify a SSL certificate. This method should not be called from user
        code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param conn: The urllib3 connection object associated with the cert.
        :param url: The requested URL.
        :param verify: Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use
        :param cert: The SSL certificate to verify.
        
```

### build_response

```json
{
  "name": "build_response",
  "kind": "function",
  "signature": "build_response(self, req, resp)",
  "line": 359,
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
      "name": "req",
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
Builds a :class:`Response <requests.Response>` object from a urllib3
        response. This should not be called from user code, and is only exposed
        for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`

        :param req: The :class:`PreparedRequest <PreparedRequest>` used to generate the response.
        :param resp: The urllib3 response object.
        :rtype: requests.Response
        
```

### build_connection_pool_key_attributes

```json
{
  "name": "build_connection_pool_key_attributes",
  "kind": "function",
  "signature": "build_connection_pool_key_attributes(self, request, verify, cert=None)",
  "line": 396,
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
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Build the PoolKey attributes used by urllib3 to return a connection.

        This looks at the PreparedRequest, the user-specified verify value,
        and the value of the cert parameter to determine what PoolKey values
        to use to select a connection from a given urllib3 Connection Pool.

        The SSL related pool key arguments are not consistently set. As of
        this writing, use the following to determine what keys may be in that
        dictionary:

        * If ``verify`` is ``True``, ``"ssl_context"`` will be set and will be the
          default Requests SSL Context
        * If ``verify`` is ``False``, ``"ssl_context"`` will not be set but
          ``"cert_reqs"`` will be set
        * If ``verify`` is a string, (i.e., it is a user-specified trust bundle)
          ``"ca_certs"`` will be set if the string is not a directory recognized
          by :py:func:`os.path.isdir`, otherwise ``"ca_certs_dir"`` will be
          set.
        * If ``"cert"`` is specified, ``"cert_file"`` will always be set. If
          ``"cert"`` is a tuple with a second item, ``"key_file"`` will also
          be present

        To override these settings, one may subclass this class, call this
        method and use the above logic to change parameters as desired. For
        example, if one wishes to use a custom :py:class:`ssl.SSLContext` one
        must both set ``"ssl_context"`` and based on what else they require,
        alter the other keys to ensure the desired behaviour.

        :param request:
            The PreparedReqest being sent over the connection.
        :type request:
            :class:`~requests.models.PreparedRequest`
        :param verify:
            Either a boolean, in which case it controls whether
            we verify the server's TLS certificate, or a string, in which case it
            must be a path to a CA bundle to use.
        :param cert:
            (optional) Any user-provided SSL certificate for client
            authentication (a.k.a., mTLS). This may be a string (i.e., just
            the path to a file which holds both certificate and key) or a
            tuple of length 2 with the certificate file path and key file
            path.
        :returns:
            A tuple of two dictionaries. The first is the "host parameters"
            portion of the Pool Key including scheme, hostname, and port. The
            second is a dictionary of SSLContext related parameters.
        
```

### get_connection_with_tls_context

```json
{
  "name": "get_connection_with_tls_context",
  "kind": "function",
  "signature": "get_connection_with_tls_context(self, request, verify, proxies=None, cert=None)",
  "line": 446,
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
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
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
    }
  ],
  "returns": null
}
```

```text
Returns a urllib3 connection for the given request and TLS settings.
        This should not be called from user code, and is only exposed for use
        when subclassing the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request:
            The :class:`PreparedRequest <PreparedRequest>` object to be sent
            over the connection.
        :param verify:
            Either a boolean, in which case it controls whether we verify the
            server's TLS certificate, or a string, in which case it must be a
            path to a CA bundle to use.
        :param proxies:
            (optional) The proxies dictionary to apply to the request.
        :param cert:
            (optional) Any user-provided SSL certificate to be used for client
            authentication (a.k.a., mTLS).
        :rtype:
            urllib3.ConnectionPool
        
```

### get_connection

```json
{
  "name": "get_connection",
  "kind": "function",
  "signature": "get_connection(self, url, proxies=None)",
  "line": 495,
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
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
DEPRECATED: Users should move to `get_connection_with_tls_context`
        for all subclasses of HTTPAdapter using Requests>=2.32.2.

        Returns a urllib3 connection for the given URL. This should not be
        called from user code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param url: The URL to connect to.
        :param proxies: (optional) A Requests-style dictionary of proxies used on this request.
        :rtype: urllib3.ConnectionPool
        
```

### close

```json
{
  "name": "close",
  "kind": "function",
  "signature": "close(self)",
  "line": 536,
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
Disposes of any internal state.

        Currently, this closes the PoolManager and any active ProxyManager,
        which closes any pooled connections.
        
```

### request_url

```json
{
  "name": "request_url",
  "kind": "function",
  "signature": "request_url(self, request, proxies)",
  "line": 546,
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
Obtain the url to use when making the final request.

        If the message is being sent through a HTTP proxy, the full URL has to
        be used. Otherwise, we should only use the path portion of the URL.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs.
        :rtype: str
        
```

### add_headers

```json
{
  "name": "add_headers",
  "kind": "function",
  "signature": "add_headers(self, request, **kwargs)",
  "line": 578,
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
Add any headers needed by the connection. As of v2.0 this does
        nothing by default, but is left for overriding by users that subclass
        the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request: The :class:`PreparedRequest <PreparedRequest>` to add headers to.
        :param kwargs: The keyword arguments from the call to send().
        
```

### proxy_headers

```json
{
  "name": "proxy_headers",
  "kind": "function",
  "signature": "proxy_headers(self, proxy)",
  "line": 592,
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
      "name": "proxy",
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
Returns a dictionary of the headers to add to any request sent
        through a proxy. This works with urllib3 magic to ensure that they are
        correctly sent to the proxy, rather than in a tunnelled request if
        CONNECT is being used.

        This should not be called from user code, and is only exposed for use
        when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param proxy: The url of the proxy being used for this request.
        :rtype: dict
        
```

### send

```json
{
  "name": "send",
  "kind": "function",
  "signature": "send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None)",
  "line": 613,
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
    }
  ],
  "returns": null
}
```

```text
Sends PreparedRequest object. Returns Response object.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param stream: (optional) Whether to stream the request content.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple or urllib3 Timeout object
        :param verify: (optional) Either a boolean, in which case it controls whether
            we verify the server's TLS certificate, or a string, in which case it
            must be a path to a CA bundle to use
        :param cert: (optional) Any user-provided SSL certificate to be trusted.
        :param proxies: (optional) The proxies dictionary to apply to the request.
        :rtype: requests.Response
        
```
