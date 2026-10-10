# requests.api.get

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Sends a GET request.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(url, params=None, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| url | positional or keyword | Yes | Not provided | — | URL for the new :class:`Request` object. |
| params | positional or keyword | No | Not provided | None | (optional) Dictionary, list of tuples or bytes to send in the query string for the :class:`Request`. |
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
m = importlib.import_module('requests.api')
url = ...  # TODO: supply a valid value from your application
result = m.get(url=url)
print(result)

```

## Related APIs mentioned in the docstring

- [requests.api.request](00194-requests.api.request.md) — Constructs and sends a :class:`Request <Request>`.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.api')
obj = m
obj = inspect.getattr_static(obj, 'get')
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
Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    
```

[Full module inspection](../modules/00029-requests.api.md)
