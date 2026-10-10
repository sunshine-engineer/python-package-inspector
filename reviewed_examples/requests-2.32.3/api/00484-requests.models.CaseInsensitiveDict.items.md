# requests.models.CaseInsensitiveDict.items

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

D.items() -> a set-like object providing a view on D's items

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Inherited class member.

## Signature

```text
(self)
```

## Inputs

No caller-supplied parameters are declared.

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
m = importlib.import_module('requests.models')
instance = ...  # TODO: construct m.CaseInsensitiveDict using its constructor page
result = instance.items()
print(result)

```

This is a class member. Construct `requests.models.CaseInsensitiveDict` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.models')
obj = m
obj = inspect.getattr_static(obj, 'CaseInsensitiveDict')
obj = inspect.getattr_static(obj, 'items')
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
D.items() -> a set-like object providing a view on D's items
```

[Full module inspection](../modules/runtime-00012.md)
