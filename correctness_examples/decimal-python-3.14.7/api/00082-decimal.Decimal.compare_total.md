# decimal.Decimal.compare_total

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Compare two operands using their abstract representation rather than

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, /, other, context=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| other | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| context | positional or keyword | No | Not provided | None | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
Decimal('12.0').compare_total(Decimal('12'))
```

Expected output recorded in the docstring:

```text
Decimal('-1')
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('decimal')
other = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Decimal using its constructor page
result = instance.compare_total(other=other)
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
obj = inspect.getattr_static(obj, 'compare_total')
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
Compare two operands using their abstract representation rather than
their numerical value.  Similar to the compare() method, but the result
gives a total ordering on Decimal instances.  Two Decimal instances with
the same numeric value but different representations compare unequal
in this ordering:

    >>> Decimal('12.0').compare_total(Decimal('12'))
    Decimal('-1')

Quiet and signaling NaNs are also included in the total ordering. The result
of this function is Decimal('0') if both operands have the same representation,
Decimal('-1') if the first operand is lower in the total order than the second,
and Decimal('1') if the first operand is higher in the total order than the
second operand. See the specification for details of the total order.

This operation is unaffected by context and is quiet: no flags are changed
and no rounding is performed. As an exception, the C version may raise
InvalidOperation if the second operand cannot be converted exactly.
```

[Full module inspection](../modules/runtime-00000.md)
