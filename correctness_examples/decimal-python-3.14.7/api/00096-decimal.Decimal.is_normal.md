# decimal.Decimal.is_normal

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return True if the argument is a normal finite non-zero number with an

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, /, context=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| context | positional or keyword | No | Not provided | None | Not described in the docstring |

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
result = instance.is_normal()
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
obj = inspect.getattr_static(obj, 'is_normal')
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
Return True if the argument is a normal finite non-zero number with an
adjusted exponent greater than or equal to Emin. Return False if the
argument is zero, subnormal, infinite or a NaN.
```

[Full module inspection](../modules/runtime-00000.md)
