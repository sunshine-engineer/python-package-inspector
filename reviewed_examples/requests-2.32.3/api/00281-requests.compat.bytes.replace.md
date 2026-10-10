# requests.compat.bytes.replace

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return a copy with all occurrences of substring old replaced by new.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, old, new, count=-1, /)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| old | positional only | Yes | Not provided | — | Not described in the docstring |
| new | positional only | Yes | Not provided | — | Not described in the docstring |
| count | positional only | No | Not provided | -1 | Not described in the docstring |

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
old = ...  # TODO: supply a valid value from your application
new = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.bytes using its constructor page
result = instance.replace(old, new)
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
obj = inspect.getattr_static(obj, 'replace')
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
Return a copy with all occurrences of substring old replaced by new.

  count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.
```

[Full module inspection](../modules/runtime-00007.md)
