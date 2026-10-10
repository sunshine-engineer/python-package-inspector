# decimal.Decimal.as_integer_ratio

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Decimal.as_integer_ratio() -> (int, int)

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, /)
```

## Inputs

No caller-supplied parameters are declared.

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
instance = ...  # TODO: construct m.Decimal using its constructor page
result = instance.as_integer_ratio()
print(result)

```

Construct `decimal.Decimal` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('decimal')
obj = m
obj = inspect.getattr_static(obj, 'Decimal')
obj = inspect.getattr_static(obj, 'as_integer_ratio')
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
Decimal.as_integer_ratio() -> (int, int)

Return a pair of integers, whose ratio is exactly equal to the original
Decimal and with a positive denominator. The ratio is in lowest terms.
Raise OverflowError on infinities and a ValueError on NaNs.
```

[Full module inspection](../modules/runtime-00000.md)
