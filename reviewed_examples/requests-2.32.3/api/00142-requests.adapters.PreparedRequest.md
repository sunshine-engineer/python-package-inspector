# requests.adapters.PreparedRequest

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

The fully mutable :class:`PreparedRequest <PreparedRequest>` object,

Kind: **class**. Evidence: **source**. Discovery: **name heuristic**.

Re-export of `requests.models.PreparedRequest`.

## Signature

```text
PreparedRequest()
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
req = requests.Request('GET', 'https://httpbin.org/get')
```

```python
r = req.prepare()
```

```python
r
```

Expected output recorded in the docstring:

```text
<PreparedRequest [GET]>
```

```python
s = requests.Session()
```

```python
s.send(r)
```

Expected output recorded in the docstring:

```text
<Response [200]>
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.adapters')
result = m.PreparedRequest()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [copy](00143-requests.adapters.PreparedRequest.copy.md) | function | No description supplied by the package. |
| [prepare](00144-requests.adapters.PreparedRequest.prepare.md) | function | Prepares the entire request with the given parameters. |
| [prepare_auth](00145-requests.adapters.PreparedRequest.prepare_auth.md) | function | Prepares the given HTTP auth data. |
| [prepare_body](00146-requests.adapters.PreparedRequest.prepare_body.md) | function | Prepares the given HTTP body data. |
| [prepare_content_length](00147-requests.adapters.PreparedRequest.prepare_content_length.md) | function | Prepare Content-Length header based on request method and body |
| [prepare_cookies](00148-requests.adapters.PreparedRequest.prepare_cookies.md) | function | Prepares the given HTTP cookie data. |
| [prepare_headers](00149-requests.adapters.PreparedRequest.prepare_headers.md) | function | Prepares the given HTTP headers. |
| [prepare_hooks](00150-requests.adapters.PreparedRequest.prepare_hooks.md) | function | Prepares the given hooks. |
| [prepare_method](00151-requests.adapters.PreparedRequest.prepare_method.md) | function | Prepares the given HTTP method. |
| [prepare_url](00152-requests.adapters.PreparedRequest.prepare_url.md) | function | Prepares the given HTTP URL. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'PreparedRequest')
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

[Full module inspection](../modules/00028-requests.adapters.md)
