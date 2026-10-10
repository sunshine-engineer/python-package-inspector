# requests.sessions.PreparedRequest.path_url

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Build the path URL to use.

Kind: **property**. Evidence: **runtime**. Discovery: **public member name**.

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

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.sessions')
instance = ...  # TODO: construct m.PreparedRequest using its constructor page
result = instance.path_url

```

This is a class member. Construct `requests.sessions.PreparedRequest` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'PreparedRequest')
obj = inspect.getattr_static(obj, 'path_url')
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
Build the path URL to use.
```

[Full module inspection](../modules/runtime-00014.md)
