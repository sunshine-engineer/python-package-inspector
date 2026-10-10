# datetime.tzinfo

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Abstract base class for time zone info objects.

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
| [dst](00062-datetime.tzinfo.dst.md) | function | datetime -> DST offset as timedelta positive east of UTC. |
| [fromutc](00063-datetime.tzinfo.fromutc.md) | function | datetime in UTC -> datetime in local time. |
| [tzname](00064-datetime.tzinfo.tzname.md) | function | datetime -> string name of time zone. |
| [utcoffset](00065-datetime.tzinfo.utcoffset.md) | function | datetime -> timedelta showing offset from UTC, negative values indicating West of UTC |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'tzinfo')
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
Abstract base class for time zone info objects.
```

[Full module inspection](../modules/runtime-00000.md)
