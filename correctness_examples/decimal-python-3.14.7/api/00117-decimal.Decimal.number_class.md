# decimal.Decimal.number_class

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return a string describing the class of the operand.  The returned value

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
result = instance.number_class()
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
obj = inspect.getattr_static(obj, 'number_class')
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
Return a string describing the class of the operand.  The returned value
is one of the following ten strings:

    * '-Infinity', indicating that the operand is negative infinity.
    * '-Normal', indicating that the operand is a negative normal number.
    * '-Subnormal', indicating that the operand is negative and subnormal.
    * '-Zero', indicating that the operand is a negative zero.
    * '+Zero', indicating that the operand is a positive zero.
    * '+Subnormal', indicating that the operand is positive and subnormal.
    * '+Normal', indicating that the operand is a positive normal number.
    * '+Infinity', indicating that the operand is positive infinity.
    * 'NaN', indicating that the operand is a quiet NaN (Not a Number).
    * 'sNaN', indicating that the operand is a signaling NaN.
```

[Full module inspection](../modules/runtime-00000.md)
