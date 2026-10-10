# requests.adapters.PreparedRequest.prepare_method

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Prepares the given HTTP method.

Kind: **function**. Evidence: **source**. Discovery: **public member name**.

## Signature

```text
prepare_method(self, method)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| method | positional or keyword | Yes | Not provided | — | Not described in the docstring |

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
m = importlib.import_module('requests.adapters')
method = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.PreparedRequest using its constructor page
result = instance.prepare_method(method=method)
print(result)

```

This is a class member. Construct `requests.adapters.PreparedRequest` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'PreparedRequest')
obj = inspect.getattr_static(obj, 'prepare_method')
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
Prepares the given HTTP method.
```

[Full module inspection](../modules/00028-requests.adapters.md)
