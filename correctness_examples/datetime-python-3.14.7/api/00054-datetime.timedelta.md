# datetime.timedelta

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Difference between two datetime values.

Kind: **class**. Evidence: **runtime**. Discovery: **runtime __all__**.

Signature unavailable. Inspect the docstring before calling this API.

## Inputs

Parameter details unavailable.

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [total_seconds](00055-datetime.timedelta.total_seconds.md) | function | Total seconds in the duration. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'timedelta')
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
Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.
```

[Full module inspection](../modules/runtime-00000.md)
