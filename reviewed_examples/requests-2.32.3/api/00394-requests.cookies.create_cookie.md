# requests.cookies.create_cookie

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Make a cookie from underspecified parameters.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(name, value, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| name | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| value | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| kwargs | var keyword | No | Not provided | Collects extra arguments | Not described in the docstring |

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
name = ...  # TODO: supply a valid value from your application
value = ...  # TODO: supply a valid value from your application
result = m.create_cookie(name=name, value=value)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
obj = m
obj = inspect.getattr_static(obj, 'create_cookie')
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
Make a cookie from underspecified parameters.

    By default, the pair of `name` and `value` will be set for the domain ''
    and sent on every request (this is sometimes called a "supercookie").
    
```

[Full module inspection](../modules/00033-requests.cookies.md)
