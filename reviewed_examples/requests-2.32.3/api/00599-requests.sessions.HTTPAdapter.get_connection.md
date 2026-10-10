# requests.sessions.HTTPAdapter.get_connection

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

DEPRECATED: Users should move to `get_connection_with_tls_context`

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, url, proxies=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| url | positional or keyword | Yes | Not provided | — | The URL to connect to. |
| proxies | positional or keyword | No | Not provided | None | (optional) A Requests-style dictionary of proxies used on this request. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- urllib3.ConnectionPool

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.sessions')
url = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.HTTPAdapter using its constructor page
result = instance.get_connection(url=url)
print(result)

```

This is a class member. Construct `requests.sessions.HTTPAdapter` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.sessions.HTTPAdapter](00593-requests.sessions.HTTPAdapter.md) — The built-in HTTP Adapter for urllib3.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'HTTPAdapter')
obj = inspect.getattr_static(obj, 'get_connection')
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
DEPRECATED: Users should move to `get_connection_with_tls_context`
        for all subclasses of HTTPAdapter using Requests>=2.32.2.

        Returns a urllib3 connection for the given URL. This should not be
        called from user code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param url: The URL to connect to.
        :param proxies: (optional) A Requests-style dictionary of proxies used on this request.
        :rtype: urllib3.ConnectionPool
        
```

[Full module inspection](../modules/00039-requests.sessions.md)
