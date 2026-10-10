# datetime.timezone.utcoffset

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return fixed offset.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, object, /)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| object | positional only | Yes | Not provided | — | Not described in the docstring |

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
m = importlib.import_module('datetime')
object = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.timezone using its constructor page
result = instance.utcoffset(object)
print(result)

```

Construct `datetime.timezone` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'timezone')
obj = inspect.getattr_static(obj, 'utcoffset')
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
Return fixed offset.
```

[Full module inspection](../modules/runtime-00000.md)
