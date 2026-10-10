# requests.cookies.MockRequest

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Wraps a `requests.Request` to mimic a `urllib2.Request`.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(request)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| request | positional or keyword | Yes | Not provided | — | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.cookies')
request = ...  # TODO: supply a valid value from your application
result = m.MockRequest(request=request)
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [add_header](00349-requests.cookies.MockRequest.add_header.md) | function | cookiejar has no legitimate use for this method; add it back if you find one. |
| [add_unredirected_header](00350-requests.cookies.MockRequest.add_unredirected_header.md) | function | No description supplied by the package. |
| [get_full_url](00351-requests.cookies.MockRequest.get_full_url.md) | function | No description supplied by the package. |
| [get_header](00352-requests.cookies.MockRequest.get_header.md) | function | No description supplied by the package. |
| [get_host](00353-requests.cookies.MockRequest.get_host.md) | function | No description supplied by the package. |
| [get_new_headers](00354-requests.cookies.MockRequest.get_new_headers.md) | function | No description supplied by the package. |
| [get_origin_req_host](00355-requests.cookies.MockRequest.get_origin_req_host.md) | function | No description supplied by the package. |
| [get_type](00356-requests.cookies.MockRequest.get_type.md) | function | No description supplied by the package. |
| [has_header](00357-requests.cookies.MockRequest.has_header.md) | function | No description supplied by the package. |
| [host](00358-requests.cookies.MockRequest.host.md) | property | No description supplied by the package. |
| [is_unverifiable](00359-requests.cookies.MockRequest.is_unverifiable.md) | function | No description supplied by the package. |
| [origin_req_host](00360-requests.cookies.MockRequest.origin_req_host.md) | property | No description supplied by the package. |
| [unverifiable](00361-requests.cookies.MockRequest.unverifiable.md) | property | No description supplied by the package. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
obj = m
obj = inspect.getattr_static(obj, 'MockRequest')
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
Wraps a `requests.Request` to mimic a `urllib2.Request`.

    The code in `http.cookiejar.CookieJar` expects this interface in order to correctly
    manage cookie policies, i.e., determine whether a cookie can be set, given the
    domains of the request and the cookie.

    The original request object is read-only. The client is responsible for collecting
    the new headers via `get_new_headers()` and interpreting them appropriately. You
    probably want `get_cookie_header`, defined below.
    
```

[Full module inspection](../modules/00033-requests.cookies.md)
