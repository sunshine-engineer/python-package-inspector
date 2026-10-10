# requests.models.Response.apparent_encoding

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

The apparent encoding, provided by the charset_normalizer or chardet libraries.

Kind: **property**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
apparent_encoding(self)
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
instance = ...  # TODO: construct m.Response using its constructor page
result = instance.apparent_encoding

```

This is a class member. Construct `requests.models.Response` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

Decorators: `property`.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.models')
obj = m
obj = inspect.getattr_static(obj, 'Response')
obj = inspect.getattr_static(obj, 'apparent_encoding')
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
The apparent encoding, provided by the charset_normalizer or chardet libraries.
```

[Full module inspection](../modules/00037-requests.models.md)
