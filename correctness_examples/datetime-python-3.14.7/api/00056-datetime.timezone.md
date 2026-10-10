# datetime.timezone

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Fixed offset from UTC implementation of tzinfo.

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
| [dst](00057-datetime.timezone.dst.md) | function | Return None. |
| [fromutc](00058-datetime.timezone.fromutc.md) | function | datetime in UTC -> datetime in local time. |
| [tzname](00059-datetime.timezone.tzname.md) | function | If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+\|-)HH:MM'. |
| [utcoffset](00060-datetime.timezone.utcoffset.md) | function | Return fixed offset. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'timezone')
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
Fixed offset from UTC implementation of tzinfo.
```

[Full module inspection](../modules/runtime-00000.md)
