# datetime.datetime.fromisocalendar

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

int, int, int -> Construct a date from the ISO year, week number and weekday.

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

Construct `datetime.datetime` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'datetime')
obj = inspect.getattr_static(obj, 'fromisocalendar')
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
int, int, int -> Construct a date from the ISO year, week number and weekday.

This is the inverse of the date.isocalendar() function
```

[Full module inspection](../modules/runtime-00000.md)
