# decimal.Decimal.quantize

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return a value equal to the first operand after rounding and having the

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, /, exp, rounding=None, context=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| exp | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| rounding | positional or keyword | No | Not provided | None | Not described in the docstring |
| context | positional or keyword | No | Not provided | None | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
Decimal('1.41421356').quantize(Decimal('1.000'))
```

Expected output recorded in the docstring:

```text
Decimal('1.414')
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('decimal')
exp = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Decimal using its constructor page
result = instance.quantize(exp=exp)
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
obj = inspect.getattr_static(obj, 'quantize')
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
Return a value equal to the first operand after rounding and having the
exponent of the second operand.

    >>> Decimal('1.41421356').quantize(Decimal('1.000'))
    Decimal('1.414')

Unlike other operations, if the length of the coefficient after the quantize
operation would be greater than precision, then an InvalidOperation is signaled.
This guarantees that, unless there is an error condition, the quantized exponent
is always equal to that of the right-hand operand.

Also unlike other operations, quantize never signals Underflow, even if the
result is subnormal and inexact.

If the exponent of the second operand is larger than that of the first, then
rounding may be necessary. In this case, the rounding mode is determined by the
rounding argument if given, else by the given context argument; if neither
argument is given, the rounding mode of the current thread's context is used.
```

[Full module inspection](../modules/runtime-00000.md)
