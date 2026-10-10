# requests.compat.str.maketrans

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return a translation table usable for str.translate().

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

Decorators: `staticmethod`.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.compat')
obj = m
obj = inspect.getattr_static(obj, 'str')
obj = inspect.getattr_static(obj, 'maketrans')
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
Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping
Unicode ordinals (integers) or characters to Unicode ordinals,
strings or None.  Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length,
and in the resulting dictionary, each character in x will be mapped
to the character at the same position in y.  If there is a third
argument, it must be a string, whose characters will be mapped to
None in the result.
```

[Full module inspection](../modules/runtime-00007.md)
