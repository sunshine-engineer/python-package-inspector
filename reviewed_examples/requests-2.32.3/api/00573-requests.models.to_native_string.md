# requests.models.to_native_string

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Given a string object, regardless of type, returns a representation of

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests._internal_utils.to_native_string`.

## Signature

```text
(string, encoding='ascii')
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| string | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| encoding | positional or keyword | No | Not provided | 'ascii' | Not described in the docstring |

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
string = ...  # TODO: supply a valid value from your application
result = m.to_native_string(string=string)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.models')
obj = m
obj = inspect.getattr_static(obj, 'to_native_string')
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
Given a string object, regardless of type, returns a representation of
    that string in the native string type, encoding and decoding where
    necessary. This assumes ASCII unless told otherwise.
    
```

[Full module inspection](../modules/00037-requests.models.md)
