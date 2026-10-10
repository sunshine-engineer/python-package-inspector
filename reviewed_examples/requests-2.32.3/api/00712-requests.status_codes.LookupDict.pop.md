# requests.status_codes.LookupDict.pop

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Inherited class member.

Signature unavailable. Inspect the docstring before calling this API.

## Inputs

Parameter details unavailable.

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

This is a class member. Construct `requests.status_codes.LookupDict` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.status_codes')
obj = m
obj = inspect.getattr_static(obj, 'LookupDict')
obj = inspect.getattr_static(obj, 'pop')
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
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise,
raise a KeyError.
```

[Full module inspection](../modules/runtime-00015.md)
