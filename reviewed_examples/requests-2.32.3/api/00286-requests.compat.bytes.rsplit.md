# requests.compat.bytes.rsplit

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return a list of the sections in the bytes, using sep as the delimiter.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, /, sep=None, maxsplit=-1)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| sep | positional or keyword | No | Not provided | None | Not described in the docstring |
| maxsplit | positional or keyword | No | Not provided | -1 | Not described in the docstring |

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
instance = ...  # TODO: construct m.bytes using its constructor page
result = instance.rsplit()
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
obj = inspect.getattr_static(obj, 'rsplit')
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
Return a list of the sections in the bytes, using sep as the delimiter.

  sep
    The delimiter according which to split the bytes.
    None (the default value) means split on ASCII whitespace
    characters (space, tab, return, newline, formfeed, vertical tab).
  maxsplit
    Maximum number of splits to do.
    -1 (the default value) means no limit.

Splitting is done starting at the end of the bytes and working to
the front.
```

[Full module inspection](../modules/runtime-00007.md)
