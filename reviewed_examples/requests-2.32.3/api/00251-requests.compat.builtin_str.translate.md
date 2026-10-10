# requests.compat.builtin_str.translate

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Replace each character in the string using the given translation table.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, table, /)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| table | positional only | Yes | Not provided | — | Not described in the docstring |

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
table = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.builtin_str using its constructor page
result = instance.translate(table)
print(result)

```

This is a class member. Construct `requests.compat.builtin_str` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.compat')
obj = m
obj = inspect.getattr_static(obj, 'builtin_str')
obj = inspect.getattr_static(obj, 'translate')
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
Replace each character in the string using the given translation table.

  table
    Translation table, which must be a mapping of Unicode ordinals
    to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for
instance a dictionary or list.  If this operation raises
LookupError, the character is left untouched.  Characters mapped to
None are deleted.
```

[Full module inspection](../modules/runtime-00007.md)
