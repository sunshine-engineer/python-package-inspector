# decimal.Decimal.from_float

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Class method that converts a float to a decimal number, exactly.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(type, f, /)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| f | positional only | Yes | Not provided | — | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
Decimal.from_float(0.1)
```

Expected output recorded in the docstring:

```text
Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

```python
Decimal.from_float(float('nan'))
```

Expected output recorded in the docstring:

```text
Decimal('NaN')
```

```python
Decimal.from_float(float('inf'))
```

Expected output recorded in the docstring:

```text
Decimal('Infinity')
```

```python
Decimal.from_float(float('-inf'))
```

Expected output recorded in the docstring:

```text
Decimal('-Infinity')
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('decimal')
f = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Decimal using its constructor page
result = instance.from_float(f)
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
obj = inspect.getattr_static(obj, 'from_float')
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
Class method that converts a float to a decimal number, exactly.
Since 0.1 is not exactly representable in binary floating point,
Decimal.from_float(0.1) is not the same as Decimal('0.1').

    >>> Decimal.from_float(0.1)
    Decimal('0.1000000000000000055511151231257827021181583404541015625')
    >>> Decimal.from_float(float('nan'))
    Decimal('NaN')
    >>> Decimal.from_float(float('inf'))
    Decimal('Infinity')
    >>> Decimal.from_float(float('-inf'))
    Decimal('-Infinity')
```

[Full module inspection](../modules/runtime-00000.md)
