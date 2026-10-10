# requests.post

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Sends a POST request.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.api.post`.

## Signature

```text
(url, data=None, json=None, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| url | positional or keyword | Yes | Not provided | — | URL for the new :class:`Request` object. |
| data | positional or keyword | No | Not provided | None | (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the :class:`Request`. |
| json | positional or keyword | No | Not provided | None | (optional) A JSON serializable Python object to send in the body of the :class:`Request`. |
| kwargs | var keyword | No | Not provided | Collects extra arguments | Optional arguments that ``request`` takes. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- :class:`Response <Response>` object
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
result = m.post(url=url)
print(result)

```

## Related APIs mentioned in the docstring

- [requests.Request](00032-requests.Request.md) — A user-created :class:`Request <Request>` object.
- [requests.Response](00042-requests.Response.md) — The :class:`Response <Response>` object, which contains a
- [requests.request](00094-requests.request.md) — Constructs and sends a :class:`Request <Request>`.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests')
obj = m
obj = inspect.getattr_static(obj, 'post')
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
Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
```

[Full module inspection](../modules/00007-requests.md)
