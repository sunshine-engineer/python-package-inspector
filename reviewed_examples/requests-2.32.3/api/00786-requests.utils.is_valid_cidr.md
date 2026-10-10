# requests.utils.is_valid_cidr

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Very simple check of the cidr format in no_proxy variable.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(string_network)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| string_network | positional or keyword | Yes | Not provided | — | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- bool

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.utils')
string_network = ...  # TODO: supply a valid value from your application
result = m.is_valid_cidr(string_network=string_network)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.utils')
obj = m
obj = inspect.getattr_static(obj, 'is_valid_cidr')
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

    Very simple check of the cidr format in no_proxy variable.

    :rtype: bool
    
```

[Full module inspection](../modules/00042-requests.utils.md)
