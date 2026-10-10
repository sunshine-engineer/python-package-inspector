# requests.Session

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

A Requests session.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.sessions.Session`.

## Signature

```text
()
```

## Inputs

No caller-supplied parameters are declared.

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
import requests
```

```python
s = requests.Session()
```

```python
s.get('https://httpbin.org/get')
```

Expected output recorded in the docstring:

```text
<Response [200]>
```

```python
with requests.Session() as s:
    s.get('https://httpbin.org/get')
```

Expected output recorded in the docstring:

```text
<Response [200]>
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests')
result = m.Session()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [close](00057-requests.Session.close.md) | function | Closes all adapters and as such the session |
| [delete](00058-requests.Session.delete.md) | function | Sends a DELETE request. Returns :class:`Response` object. |
| [get](00059-requests.Session.get.md) | function | Sends a GET request. Returns :class:`Response` object. |
| [get_adapter](00060-requests.Session.get_adapter.md) | function | Returns the appropriate connection adapter for the given URL. |
| [get_redirect_target](00061-requests.Session.get_redirect_target.md) | function | Receives a Response. Returns a redirect URI or ``None`` |
| [head](00062-requests.Session.head.md) | function | Sends a HEAD request. Returns :class:`Response` object. |
| [merge_environment_settings](00063-requests.Session.merge_environment_settings.md) | function | Check the environment and merge it with some settings. |
| [mount](00064-requests.Session.mount.md) | function | Registers a connection adapter to a prefix. |
| [options](00065-requests.Session.options.md) | function | Sends a OPTIONS request. Returns :class:`Response` object. |
| [patch](00066-requests.Session.patch.md) | function | Sends a PATCH request. Returns :class:`Response` object. |
| [post](00067-requests.Session.post.md) | function | Sends a POST request. Returns :class:`Response` object. |
| [prepare_request](00068-requests.Session.prepare_request.md) | function | Constructs a :class:`PreparedRequest <PreparedRequest>` for |
| [put](00069-requests.Session.put.md) | function | Sends a PUT request. Returns :class:`Response` object. |
| [rebuild_auth](00070-requests.Session.rebuild_auth.md) | function | When being redirected we may want to strip authentication from the |
| [rebuild_method](00071-requests.Session.rebuild_method.md) | function | When being redirected we may want to change the method of the request |
| [rebuild_proxies](00072-requests.Session.rebuild_proxies.md) | function | This method re-evaluates the proxy configuration by considering the |
| [request](00073-requests.Session.request.md) | function | Constructs a :class:`Request <Request>`, prepares it and sends it. |
| [resolve_redirects](00074-requests.Session.resolve_redirects.md) | function | Receives a Response. Returns a generator of Responses or Requests. |
| [send](00075-requests.Session.send.md) | function | Send a given PreparedRequest. |
| [should_strip_auth](00076-requests.Session.should_strip_auth.md) | function | Decide whether Authorization header should be removed when redirecting |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests')
obj = m
obj = inspect.getattr_static(obj, 'Session')
if isinstance(obj, (staticmethod, classmethod)):
    obj = obj.__func__
print(inspect.getdoc(obj) or 'No docstring supplied')
try:
    print(inspect.signature(obj))
except (TypeError, ValueError):
    print('Signature unavailable')
help(obj)
```

## Original docstring

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

[Full module inspection](../modules/00007-requests.md)
