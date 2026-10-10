# decimal.Decimal.to_integral_exact

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Round to the nearest integer, signaling Inexact or Rounded as appropriate if

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, /, rounding=None, context=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| rounding | positional or keyword | No | Not provided | None | Not described in the docstring |
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
result = instance.to_integral_exact()
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
obj = inspect.getattr_static(obj, 'to_integral_exact')
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
Round to the nearest integer, signaling Inexact or Rounded as appropriate if
rounding occurs.  The rounding mode is determined by the rounding parameter
if given, else by the given context. If neither parameter is given, then the
rounding mode of the current default context is used.
```

[Full module inspection](../modules/runtime-00000.md)
