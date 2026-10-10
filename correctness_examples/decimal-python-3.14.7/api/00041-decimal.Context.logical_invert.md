# decimal.Context.logical_invert

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Invert all the digits in the operand.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, x, /)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| x | positional only | Yes | Not provided | — | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
ExtendedContext.logical_invert(Decimal('0'))
```

Expected output recorded in the docstring:

```text
Decimal('111111111')
```

```python
ExtendedContext.logical_invert(Decimal('1'))
```

Expected output recorded in the docstring:

```text
Decimal('111111110')
```

```python
ExtendedContext.logical_invert(Decimal('111111111'))
```

Expected output recorded in the docstring:

```text
Decimal('0')
```

```python
ExtendedContext.logical_invert(Decimal('101010101'))
```

Expected output recorded in the docstring:

```text
Decimal('10101010')
```

```python
ExtendedContext.logical_invert(1101)
```

Expected output recorded in the docstring:

```text
Decimal('111110010')
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('decimal')
x = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Context using its constructor page
result = instance.logical_invert(x)
print(result)

```

Construct `decimal.Context` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('decimal')
obj = m
obj = inspect.getattr_static(obj, 'Context')
obj = inspect.getattr_static(obj, 'logical_invert')
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
Invert all the digits in the operand.

The operand must be a logical number.

    >>> ExtendedContext.logical_invert(Decimal('0'))
    Decimal('111111111')
    >>> ExtendedContext.logical_invert(Decimal('1'))
    Decimal('111111110')
    >>> ExtendedContext.logical_invert(Decimal('111111111'))
    Decimal('0')
    >>> ExtendedContext.logical_invert(Decimal('101010101'))
    Decimal('10101010')
    >>> ExtendedContext.logical_invert(1101)
    Decimal('111110010')
```

[Full module inspection](../modules/runtime-00000.md)
