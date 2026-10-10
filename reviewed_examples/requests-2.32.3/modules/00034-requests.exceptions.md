# requests.exceptions

Source: `requests/exceptions.py`

```text

requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.exceptions')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## from urllib3.exceptions import HTTPError as BaseHTTPError

```json
{
  "name": "from urllib3.exceptions import HTTPError as BaseHTTPError",
  "kind": "import",
  "line": 7,
  "from_module": "urllib3.exceptions",
  "level": 0,
  "bindings": [
    {
      "imported": "HTTPError",
      "local": "BaseHTTPError"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import JSONDecodeError as CompatJSONDecodeError

```json
{
  "name": "from .compat import JSONDecodeError as CompatJSONDecodeError",
  "kind": "import",
  "line": 9,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "JSONDecodeError",
      "local": "CompatJSONDecodeError"
    }
  ]
}
```

```text
No docstring available.
```

## RequestException

```json
{
  "name": "RequestException",
  "kind": "class",
  "line": 12,
  "bases": [
    "IOError"
  ],
  "decorators": []
}
```

```text
There was an ambiguous exception that occurred while handling your
    request.
    
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, *args, **kwargs)",
  "line": 17,
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
Initialize RequestException with `request` and `response` objects.
```

## InvalidJSONError

```json
{
  "name": "InvalidJSONError",
  "kind": "class",
  "line": 27,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
A JSON error occurred.
```

## JSONDecodeError

```json
{
  "name": "JSONDecodeError",
  "kind": "class",
  "line": 31,
  "bases": [
    "InvalidJSONError",
    "CompatJSONDecodeError"
  ],
  "decorators": []
}
```

```text
Couldn't decode the text into json
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, *args, **kwargs)",
  "line": 34,
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

        Construct the JSONDecodeError instance first with all
        args. Then use it's args to construct the IOError so that
        the json specific args aren't used as IOError specific args
        and the error message from JSONDecodeError is preserved.
        
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "signature": "__reduce__(self)",
  "line": 44,
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

        The __reduce__ method called when pickling the object must
        be the one from the JSONDecodeError (be it json/simplejson)
        as it expects all the arguments for instantiation, not just
        one like the IOError, and the MRO would by default call the
        __reduce__ method from the IOError due to the inheritance order.
        
```

## HTTPError

```json
{
  "name": "HTTPError",
  "kind": "class",
  "line": 55,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
An HTTP error occurred.
```

## ConnectionError

```json
{
  "name": "ConnectionError",
  "kind": "class",
  "line": 59,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
A Connection error occurred.
```

## ProxyError

```json
{
  "name": "ProxyError",
  "kind": "class",
  "line": 63,
  "bases": [
    "ConnectionError"
  ],
  "decorators": []
}
```

```text
A proxy error occurred.
```

## SSLError

```json
{
  "name": "SSLError",
  "kind": "class",
  "line": 67,
  "bases": [
    "ConnectionError"
  ],
  "decorators": []
}
```

```text
An SSL error occurred.
```

## Timeout

```json
{
  "name": "Timeout",
  "kind": "class",
  "line": 71,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
The request timed out.

    Catching this error will catch both
    :exc:`~requests.exceptions.ConnectTimeout` and
    :exc:`~requests.exceptions.ReadTimeout` errors.
    
```

## ConnectTimeout

```json
{
  "name": "ConnectTimeout",
  "kind": "class",
  "line": 80,
  "bases": [
    "ConnectionError",
    "Timeout"
  ],
  "decorators": []
}
```

```text
The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    
```

## ReadTimeout

```json
{
  "name": "ReadTimeout",
  "kind": "class",
  "line": 87,
  "bases": [
    "Timeout"
  ],
  "decorators": []
}
```

```text
The server did not send any data in the allotted amount of time.
```

## URLRequired

```json
{
  "name": "URLRequired",
  "kind": "class",
  "line": 91,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
A valid URL is required to make a request.
```

## TooManyRedirects

```json
{
  "name": "TooManyRedirects",
  "kind": "class",
  "line": 95,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
Too many redirects.
```

## MissingSchema

```json
{
  "name": "MissingSchema",
  "kind": "class",
  "line": 99,
  "bases": [
    "RequestException",
    "ValueError"
  ],
  "decorators": []
}
```

```text
The URL scheme (e.g. http or https) is missing.
```

## InvalidSchema

```json
{
  "name": "InvalidSchema",
  "kind": "class",
  "line": 103,
  "bases": [
    "RequestException",
    "ValueError"
  ],
  "decorators": []
}
```

```text
The URL scheme provided is either invalid or unsupported.
```

## InvalidURL

```json
{
  "name": "InvalidURL",
  "kind": "class",
  "line": 107,
  "bases": [
    "RequestException",
    "ValueError"
  ],
  "decorators": []
}
```

```text
The URL provided was somehow invalid.
```

## InvalidHeader

```json
{
  "name": "InvalidHeader",
  "kind": "class",
  "line": 111,
  "bases": [
    "RequestException",
    "ValueError"
  ],
  "decorators": []
}
```

```text
The header value provided was somehow invalid.
```

## InvalidProxyURL

```json
{
  "name": "InvalidProxyURL",
  "kind": "class",
  "line": 115,
  "bases": [
    "InvalidURL"
  ],
  "decorators": []
}
```

```text
The proxy URL provided is invalid.
```

## ChunkedEncodingError

```json
{
  "name": "ChunkedEncodingError",
  "kind": "class",
  "line": 119,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
The server declared chunked encoding but sent an invalid chunk.
```

## ContentDecodingError

```json
{
  "name": "ContentDecodingError",
  "kind": "class",
  "line": 123,
  "bases": [
    "RequestException",
    "BaseHTTPError"
  ],
  "decorators": []
}
```

```text
Failed to decode response content.
```

## StreamConsumedError

```json
{
  "name": "StreamConsumedError",
  "kind": "class",
  "line": 127,
  "bases": [
    "RequestException",
    "TypeError"
  ],
  "decorators": []
}
```

```text
The content for this response was already consumed.
```

## RetryError

```json
{
  "name": "RetryError",
  "kind": "class",
  "line": 131,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
Custom retries logic failed
```

## UnrewindableBodyError

```json
{
  "name": "UnrewindableBodyError",
  "kind": "class",
  "line": 135,
  "bases": [
    "RequestException"
  ],
  "decorators": []
}
```

```text
Requests encountered an error when trying to rewind a body.
```

## RequestsWarning

```json
{
  "name": "RequestsWarning",
  "kind": "class",
  "line": 142,
  "bases": [
    "Warning"
  ],
  "decorators": []
}
```

```text
Base warning for Requests.
```

## FileModeWarning

```json
{
  "name": "FileModeWarning",
  "kind": "class",
  "line": 146,
  "bases": [
    "RequestsWarning",
    "DeprecationWarning"
  ],
  "decorators": []
}
```

```text
A file was opened in text mode, but Requests determined its binary length.
```

## RequestsDependencyWarning

```json
{
  "name": "RequestsDependencyWarning",
  "kind": "class",
  "line": 150,
  "bases": [
    "RequestsWarning"
  ],
  "decorators": []
}
```

```text
An imported dependency doesn't match the expected version range.
```
