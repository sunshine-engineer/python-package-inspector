# requests.models.PreparedRequest

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

The fully mutable :class:`PreparedRequest <PreparedRequest>` object,

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

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
m = importlib.import_module('requests.models')
result = m.PreparedRequest()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [copy](00515-requests.models.PreparedRequest.copy.md) | function | No description supplied by the package. |
| [deregister_hook](00516-requests.models.PreparedRequest.deregister_hook.md) | function | Deregister a previously registered hook. |
| [path_url](00517-requests.models.PreparedRequest.path_url.md) | property | Build the path URL to use. |
| [prepare](00518-requests.models.PreparedRequest.prepare.md) | function | Prepares the entire request with the given parameters. |
| [prepare_auth](00519-requests.models.PreparedRequest.prepare_auth.md) | function | Prepares the given HTTP auth data. |
| [prepare_body](00520-requests.models.PreparedRequest.prepare_body.md) | function | Prepares the given HTTP body data. |
| [prepare_content_length](00521-requests.models.PreparedRequest.prepare_content_length.md) | function | Prepare Content-Length header based on request method and body |
| [prepare_cookies](00522-requests.models.PreparedRequest.prepare_cookies.md) | function | Prepares the given HTTP cookie data. |
| [prepare_headers](00523-requests.models.PreparedRequest.prepare_headers.md) | function | Prepares the given HTTP headers. |
| [prepare_hooks](00524-requests.models.PreparedRequest.prepare_hooks.md) | function | Prepares the given hooks. |
| [prepare_method](00525-requests.models.PreparedRequest.prepare_method.md) | function | Prepares the given HTTP method. |
| [prepare_url](00526-requests.models.PreparedRequest.prepare_url.md) | function | Prepares the given HTTP URL. |
| [register_hook](00527-requests.models.PreparedRequest.register_hook.md) | function | Properly register a hook. |

## Related APIs mentioned in the docstring

- [requests.models.Request](00528-requests.models.Request.md) — A user-created :class:`Request <Request>` object.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.models')
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

[Full module inspection](../modules/00037-requests.models.md)
