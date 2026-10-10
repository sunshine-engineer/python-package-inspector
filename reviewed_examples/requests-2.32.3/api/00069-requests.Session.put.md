# requests.Session.put

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Sends a PUT request. Returns :class:`Response` object.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, url, data=None, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| url | positional or keyword | Yes | Not provided | — | URL for the new :class:`Request` object. |
| data | positional or keyword | No | Not provided | None | (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the :class:`Request`. |
| kwargs | var keyword | No | Not provided | Collects extra arguments | Optional arguments that ``request`` takes. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- requests.Response

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests')
url = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Session using its constructor page
result = instance.put(url=url)
print(result)

```

This is a class member. Construct `requests.Session` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.Request](00032-requests.Request.md) — A user-created :class:`Request <Request>` object.
- [requests.Response](00042-requests.Response.md) — The :class:`Response <Response>` object, which contains a
- [requests.Session.request](00073-requests.Session.request.md) — Constructs a :class:`Request <Request>`, prepares it and sends it.
- [requests.request](00094-requests.request.md) — Constructs and sends a :class:`Request <Request>`.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests')
obj = m
obj = inspect.getattr_static(obj, 'Session')
obj = inspect.getattr_static(obj, 'put')
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
Sends a PUT request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \*\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        
```

[Full module inspection](../modules/00007-requests.md)
