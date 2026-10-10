# requests.compat.bytes.rjust

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return a right-justified string of length width.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, width, fillchar=b' ', /)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| width | positional only | Yes | Not provided | — | Not described in the docstring |
| fillchar | positional only | No | Not provided | b' ' | Not described in the docstring |

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
m = importlib.import_module('requests.compat')
width = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.bytes using its constructor page
result = instance.rjust(width)
print(result)

```

This is a class member. Construct `requests.compat.bytes` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.compat')
obj = m
obj = inspect.getattr_static(obj, 'bytes')
obj = inspect.getattr_static(obj, 'rjust')
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
Return a right-justified string of length width.

Padding is done using the specified fill character.
```

[Full module inspection](../modules/runtime-00007.md)
