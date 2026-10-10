# requests.adapters.get_encoding_from_headers

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Returns encodings from given HTTP Header Dict.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.utils.get_encoding_from_headers`.

## Signature

```text
(headers)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| headers | positional or keyword | Yes | Not provided | — | dictionary to extract encoding from. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- str

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.adapters')
headers = ...  # TODO: supply a valid value from your application
result = m.get_encoding_from_headers(headers=headers)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'get_encoding_from_headers')
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
Returns encodings from given HTTP Header Dict.

    :param headers: dictionary to extract encoding from.
    :rtype: str
    
```

[Full module inspection](../modules/00028-requests.adapters.md)
