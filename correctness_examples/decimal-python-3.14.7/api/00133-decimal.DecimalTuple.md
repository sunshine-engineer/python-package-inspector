# decimal.DecimalTuple

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

DecimalTuple(sign, digits, exponent)

Kind: **class**. Evidence: **runtime**. Discovery: **runtime name heuristic**.

## Signature

```text
(sign, digits, exponent)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| sign | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| digits | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| exponent | positional or keyword | Yes | Not provided | — | Not described in the docstring |

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
m = importlib.import_module('decimal')
sign = ...  # TODO: supply a valid value from your application
digits = ...  # TODO: supply a valid value from your application
exponent = ...  # TODO: supply a valid value from your application
result = m.DecimalTuple(sign=sign, digits=digits, exponent=exponent)
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [count](00134-decimal.DecimalTuple.count.md) | function | Return number of occurrences of value. |
| [index](00135-decimal.DecimalTuple.index.md) | function | Return first index of value. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('decimal')
obj = m
obj = inspect.getattr_static(obj, 'DecimalTuple')
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
DecimalTuple(sign, digits, exponent)
```

[Full module inspection](../modules/runtime-00000.md)
