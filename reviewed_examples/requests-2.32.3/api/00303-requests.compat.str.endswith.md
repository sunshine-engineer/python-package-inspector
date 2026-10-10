# requests.compat.str.endswith

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return True if the string ends with the specified suffix, False otherwise.

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

This is a class member. Construct `requests.compat.str` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.compat')
obj = m
obj = inspect.getattr_static(obj, 'str')
obj = inspect.getattr_static(obj, 'endswith')
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
Return True if the string ends with the specified suffix, False otherwise.

suffix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.
```

[Full module inspection](../modules/runtime-00007.md)
