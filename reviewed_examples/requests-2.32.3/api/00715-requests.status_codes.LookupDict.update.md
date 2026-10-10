# requests.status_codes.LookupDict.update

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.

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
obj = inspect.getattr_static(obj, 'update')
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
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E is present and has a .keys() method, then does:  for k in E.keys(): D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]
```

[Full module inspection](../modules/runtime-00015.md)
