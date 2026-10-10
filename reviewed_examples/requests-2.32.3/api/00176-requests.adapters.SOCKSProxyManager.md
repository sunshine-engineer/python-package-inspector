# requests.adapters.SOCKSProxyManager

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

No description supplied by the package.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Defined conditionally in source; availability and the selected implementation depend on the environment.

## Signature

```text
(*args, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| args | var positional | No | Not provided | Collects extra arguments | Not described in the docstring |
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
m = importlib.import_module('requests.adapters')
result = m.SOCKSProxyManager()
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'SOCKSProxyManager')
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
No docstring supplied.
```

[Full module inspection](../modules/00028-requests.adapters.md)
