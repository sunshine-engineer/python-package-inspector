# decimal.Context.logical_and

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Applies the logical operation 'and' between each operand's digits.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, x, y, /)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| x | positional only | Yes | Not provided | — | Not described in the docstring |
| y | positional only | Yes | Not provided | — | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
ExtendedContext.logical_and(Decimal('0'), Decimal('0'))
```

Expected output recorded in the docstring:

```text
Decimal('0')
```

```python
ExtendedContext.logical_and(Decimal('0'), Decimal('1'))
```

Expected output recorded in the docstring:

```text
Decimal('0')
```

```python
ExtendedContext.logical_and(Decimal('1'), Decimal('0'))
```

Expected output recorded in the docstring:

```text
Decimal('0')
```

```python
ExtendedContext.logical_and(Decimal('1'), Decimal('1'))
```

Expected output recorded in the docstring:

```text
Decimal('1')
```

```python
ExtendedContext.logical_and(Decimal('1100'), Decimal('1010'))
```

Expected output recorded in the docstring:

```text
Decimal('1000')
```

```python
ExtendedContext.logical_and(Decimal('1111'), Decimal('10'))
```

Expected output recorded in the docstring:

```text
Decimal('10')
```

```python
ExtendedContext.logical_and(110, 1101)
```

Expected output recorded in the docstring:

```text
Decimal('100')
```

```python
ExtendedContext.logical_and(Decimal(110), 1101)
```

Expected output recorded in the docstring:

```text
Decimal('100')
```

```python
ExtendedContext.logical_and(110, Decimal(1101))
```

Expected output recorded in the docstring:

```text
Decimal('100')
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('decimal')
x = ...  # TODO: supply a valid value from your application
y = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Context using its constructor page
result = instance.logical_and(x, y)
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
obj = inspect.getattr_static(obj, 'logical_and')
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
Applies the logical operation 'and' between each operand's digits.

The operands must be both logical numbers.

    >>> ExtendedContext.logical_and(Decimal('0'), Decimal('0'))
    Decimal('0')
    >>> ExtendedContext.logical_and(Decimal('0'), Decimal('1'))
    Decimal('0')
    >>> ExtendedContext.logical_and(Decimal('1'), Decimal('0'))
    Decimal('0')
    >>> ExtendedContext.logical_and(Decimal('1'), Decimal('1'))
    Decimal('1')
    >>> ExtendedContext.logical_and(Decimal('1100'), Decimal('1010'))
    Decimal('1000')
    >>> ExtendedContext.logical_and(Decimal('1111'), Decimal('10'))
    Decimal('10')
    >>> ExtendedContext.logical_and(110, 1101)
    Decimal('100')
    >>> ExtendedContext.logical_and(Decimal(110), 1101)
    Decimal('100')
    >>> ExtendedContext.logical_and(110, Decimal(1101))
    Decimal('100')
```

[Full module inspection](../modules/runtime-00000.md)
