# decimal.DecimalTuple.index

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return first index of value.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Inherited class member.

## Signature

```text
(self, value, start=0, stop=9223372036854775807, /)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| value | positional only | Yes | Not provided | — | Not described in the docstring |
| start | positional only | No | Not provided | 0 | Not described in the docstring |
| stop | positional only | No | Not provided | 9223372036854775807 | Not described in the docstring |

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
value = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.DecimalTuple using its constructor page
result = instance.index(value)
print(result)

```

Construct `decimal.DecimalTuple` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('decimal')
obj = m
obj = inspect.getattr_static(obj, 'DecimalTuple')
obj = inspect.getattr_static(obj, 'index')
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
Return first index of value.

Raises ValueError if the value is not present.
```

[Full module inspection](../modules/runtime-00000.md)
