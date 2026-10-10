# requests.compat.bytes.index

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end].

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Signature unavailable. Inspect the docstring before calling this API.

## Inputs

Parameter details unavailable.

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

This is a class member. Construct `requests.compat.bytes` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.compat')
obj = m
obj = inspect.getattr_static(obj, 'bytes')
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
Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end].

  start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Raise ValueError if the subsection is not found.
```

[Full module inspection](../modules/runtime-00007.md)
