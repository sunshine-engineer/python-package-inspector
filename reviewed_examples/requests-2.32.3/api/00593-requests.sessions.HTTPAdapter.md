# requests.sessions.HTTPAdapter

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

The built-in HTTP Adapter for urllib3.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.adapters.HTTPAdapter`.

## Signature

```text
(pool_connections=10, pool_maxsize=10, max_retries=0, pool_block=False)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| pool_connections | positional or keyword | No | Not provided | 10 | The number of urllib3 connection pools to cache. |
| pool_maxsize | positional or keyword | No | Not provided | 10 | The maximum number of connections to save in the pool. |
| max_retries | positional or keyword | No | Not provided | 0 | The maximum number of retries each connection should attempt. Note, this applies only to failed DNS lookups, socket connections and connection timeouts, never to requests where data has made it to the server. By default, Requests does not retry failed connections. If you need granular control over the conditions under which we retry a request, import urllib3's ``Retry`` class and pass that instead. |
| pool_block | positional or keyword | No | Not provided | False | Whether the connection pool should block for connections. |

### Additional inputs documented by the package

These names appear in the docstring but not as explicit signature parameters. They may be forwarded through `**kwargs`; verify the documented call path before passing them. Required status and defaults are not inferred.

| Name | Documented type | Description |
| --- | --- | --- |
| Usage | Not provided | : >>> import requests >>> s = requests.Session() >>> a = requests.adapters.HTTPAdapter(max_retries=3) >>> s.mount('http://', a) |

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
a = requests.adapters.HTTPAdapter(max_retries=3)
```

```python
s.mount('http://', a)
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.sessions')
result = m.HTTPAdapter()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [add_headers](00594-requests.sessions.HTTPAdapter.add_headers.md) | function | Add any headers needed by the connection. As of v2.0 this does |
| [build_connection_pool_key_attributes](00595-requests.sessions.HTTPAdapter.build_connection_pool_key_attributes.md) | function | Build the PoolKey attributes used by urllib3 to return a connection. |
| [build_response](00596-requests.sessions.HTTPAdapter.build_response.md) | function | Builds a :class:`Response <requests.Response>` object from a urllib3 |
| [cert_verify](00597-requests.sessions.HTTPAdapter.cert_verify.md) | function | Verify a SSL certificate. This method should not be called from user |
| [close](00598-requests.sessions.HTTPAdapter.close.md) | function | Disposes of any internal state. |
| [get_connection](00599-requests.sessions.HTTPAdapter.get_connection.md) | function | DEPRECATED: Users should move to `get_connection_with_tls_context` |
| [get_connection_with_tls_context](00600-requests.sessions.HTTPAdapter.get_connection_with_tls_context.md) | function | Returns a urllib3 connection for the given request and TLS settings. |
| [init_poolmanager](00601-requests.sessions.HTTPAdapter.init_poolmanager.md) | function | Initializes a urllib3 PoolManager. |
| [proxy_headers](00602-requests.sessions.HTTPAdapter.proxy_headers.md) | function | Returns a dictionary of the headers to add to any request sent |
| [proxy_manager_for](00603-requests.sessions.HTTPAdapter.proxy_manager_for.md) | function | Return urllib3 ProxyManager for the given proxy. |
| [request_url](00604-requests.sessions.HTTPAdapter.request_url.md) | function | Obtain the url to use when making the final request. |
| [send](00605-requests.sessions.HTTPAdapter.send.md) | function | Sends PreparedRequest object. Returns Response object. |

## Related APIs mentioned in the docstring

- [requests.sessions.Session](00655-requests.sessions.Session.md) — A Requests session.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'HTTPAdapter')
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

[Full module inspection](../modules/00039-requests.sessions.md)
