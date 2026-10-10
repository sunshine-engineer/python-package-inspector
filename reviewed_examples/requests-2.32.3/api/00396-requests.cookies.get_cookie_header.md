# requests.cookies.get_cookie_header

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Produce an appropriate Cookie header string to be sent with `request`, or None.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(jar, request)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| jar | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| request | positional or keyword | Yes | Not provided | — | Not described in the docstring |

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
m = importlib.import_module('requests.cookies')
jar = ...  # TODO: supply a valid value from your application
request = ...  # TODO: supply a valid value from your application
result = m.get_cookie_header(jar=jar, request=request)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
obj = m
obj = inspect.getattr_static(obj, 'get_cookie_header')
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

    Produce an appropriate Cookie header string to be sent with `request`, or None.

    :rtype: str
    
```

[Full module inspection](../modules/00033-requests.cookies.md)
