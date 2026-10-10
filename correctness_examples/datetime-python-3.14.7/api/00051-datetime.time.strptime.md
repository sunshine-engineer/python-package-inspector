# datetime.time.strptime

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

string, format -> new time parsed from a string (like time.strptime()).

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

Construct `datetime.time` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'time')
obj = inspect.getattr_static(obj, 'strptime')
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
string, format -> new time parsed from a string (like time.strptime()).
```

[Full module inspection](../modules/runtime-00000.md)
