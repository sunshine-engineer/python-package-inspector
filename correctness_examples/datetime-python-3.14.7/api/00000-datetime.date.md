# datetime.date

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

date(year, month, day) --> date object

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
| [ctime](00001-datetime.date.ctime.md) | function | Return ctime() style string. |
| [fromisocalendar](00002-datetime.date.fromisocalendar.md) | function | int, int, int -> Construct a date from the ISO year, week number and weekday. |
| [fromisoformat](00003-datetime.date.fromisoformat.md) | function | str -> Construct a date from a string in ISO 8601 format. |
| [fromordinal](00004-datetime.date.fromordinal.md) | function | int -> date corresponding to a proleptic Gregorian ordinal. |
| [fromtimestamp](00005-datetime.date.fromtimestamp.md) | function | Create a date from a POSIX timestamp. |
| [isocalendar](00006-datetime.date.isocalendar.md) | function | Return a named tuple containing ISO year, week number, and weekday. |
| [isoformat](00007-datetime.date.isoformat.md) | function | Return string in ISO 8601 format, YYYY-MM-DD. |
| [isoweekday](00008-datetime.date.isoweekday.md) | function | Return the day of the week represented by the date. |
| [replace](00009-datetime.date.replace.md) | function | Return date with new specified fields. |
| [strftime](00010-datetime.date.strftime.md) | function | format -> strftime() style string. |
| [strptime](00011-datetime.date.strptime.md) | function | string, format -> new date parsed from a string (like time.strptime()). |
| [timetuple](00012-datetime.date.timetuple.md) | function | Return time tuple, compatible with time.localtime(). |
| [today](00013-datetime.date.today.md) | function | Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). |
| [toordinal](00014-datetime.date.toordinal.md) | function | Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. |
| [weekday](00015-datetime.date.weekday.md) | function | Return the day of the week represented by the date. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'date')
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
date(year, month, day) --> date object
```

[Full module inspection](../modules/runtime-00000.md)
