# datetime.datetime

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

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
| [astimezone](00017-datetime.datetime.astimezone.md) | function | tz -> convert to local time in new timezone tz |
| [combine](00018-datetime.datetime.combine.md) | function | date, time -> datetime with same date and time fields |
| [ctime](00019-datetime.datetime.ctime.md) | function | Return ctime() style string. |
| [date](00020-datetime.datetime.date.md) | function | Return date object with same year, month and day. |
| [dst](00021-datetime.datetime.dst.md) | function | Return self.tzinfo.dst(self). |
| [fromisocalendar](00022-datetime.datetime.fromisocalendar.md) | function | int, int, int -> Construct a date from the ISO year, week number and weekday. |
| [fromisoformat](00023-datetime.datetime.fromisoformat.md) | function | string -> datetime from a string in most ISO 8601 formats |
| [fromordinal](00024-datetime.datetime.fromordinal.md) | function | int -> date corresponding to a proleptic Gregorian ordinal. |
| [fromtimestamp](00025-datetime.datetime.fromtimestamp.md) | function | timestamp&#91;, tz&#93; -> tz's local time from POSIX timestamp. |
| [isocalendar](00026-datetime.datetime.isocalendar.md) | function | Return a named tuple containing ISO year, week number, and weekday. |
| [isoformat](00027-datetime.datetime.isoformat.md) | function | &#91;sep&#93; -> string in ISO 8601 format, YYYY-MM-DDT&#91;HH&#91;:MM&#91;:SS&#91;.mmm&#91;uuu&#93;&#93;&#93;&#93;&#93;&#91;+HH:MM&#93;. |
| [isoweekday](00028-datetime.datetime.isoweekday.md) | function | Return the day of the week represented by the date. |
| [now](00029-datetime.datetime.now.md) | function | Returns new datetime object representing current time local to tz. |
| [replace](00030-datetime.datetime.replace.md) | function | Return datetime with new specified fields. |
| [strftime](00031-datetime.datetime.strftime.md) | function | format -> strftime() style string. |
| [strptime](00032-datetime.datetime.strptime.md) | function | string, format -> new datetime parsed from a string (like time.strptime()). |
| [time](00033-datetime.datetime.time.md) | function | Return time object with same time but with tzinfo=None. |
| [timestamp](00034-datetime.datetime.timestamp.md) | function | Return POSIX timestamp as float. |
| [timetuple](00035-datetime.datetime.timetuple.md) | function | Return time tuple, compatible with time.localtime(). |
| [timetz](00036-datetime.datetime.timetz.md) | function | Return time object with same time and tzinfo. |
| [today](00037-datetime.datetime.today.md) | function | Current date or datetime:  same as self.__class__.fromtimestamp(time.time()). |
| [toordinal](00038-datetime.datetime.toordinal.md) | function | Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1. |
| [tzname](00039-datetime.datetime.tzname.md) | function | Return self.tzinfo.tzname(self). |
| [utcfromtimestamp](00040-datetime.datetime.utcfromtimestamp.md) | function | Construct a naive UTC datetime from a POSIX timestamp. |
| [utcnow](00041-datetime.datetime.utcnow.md) | function | Return a new datetime representing UTC day and time. |
| [utcoffset](00042-datetime.datetime.utcoffset.md) | function | Return self.tzinfo.utcoffset(self). |
| [utctimetuple](00043-datetime.datetime.utctimetuple.md) | function | Return UTC time tuple, compatible with time.localtime(). |
| [weekday](00044-datetime.datetime.weekday.md) | function | Return the day of the week represented by the date. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'datetime')
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
datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.
```

[Full module inspection](../modules/runtime-00000.md)
