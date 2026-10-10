# decimal.Decimal.fma

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Fused multiply-add.  Return self*other+third with no rounding of the

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, /, other, third, context=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| other | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| third | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| context | positional or keyword | No | Not provided | None | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
Decimal(2).fma(3, 5)
```

Expected output recorded in the docstring:

```text
Decimal('11')
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('decimal')
other = ...  # TODO: supply a valid value from your application
third = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Decimal using its constructor page
result = instance.fma(other=other, third=third)
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
obj = inspect.getattr_static(obj, 'fma')
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
Fused multiply-add.  Return self*other+third with no rounding of the
intermediate product self*other.

    >>> Decimal(2).fma(3, 5)
    Decimal('11')
```

[Full module inspection](../modules/runtime-00000.md)
