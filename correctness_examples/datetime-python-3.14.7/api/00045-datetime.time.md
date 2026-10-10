# datetime.time

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object

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
| [dst](00046-datetime.time.dst.md) | function | Return self.tzinfo.dst(self). |
| [fromisoformat](00047-datetime.time.fromisoformat.md) | function | string -> time from a string in ISO 8601 format |
| [isoformat](00048-datetime.time.isoformat.md) | function | Return string in ISO 8601 format, &#91;HH&#91;:MM&#91;:SS&#91;.mmm&#91;uuu&#93;&#93;&#93;&#93;&#93;&#91;+HH:MM&#93;. |
| [replace](00049-datetime.time.replace.md) | function | Return time with new specified fields. |
| [strftime](00050-datetime.time.strftime.md) | function | format -> strftime() style string. |
| [strptime](00051-datetime.time.strptime.md) | function | string, format -> new time parsed from a string (like time.strptime()). |
| [tzname](00052-datetime.time.tzname.md) | function | Return self.tzinfo.tzname(self). |
| [utcoffset](00053-datetime.time.utcoffset.md) | function | Return self.tzinfo.utcoffset(self). |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'time')
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
time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object

All arguments are optional. tzinfo may be None, or an instance of
a tzinfo subclass. The remaining arguments may be ints.
```

[Full module inspection](../modules/runtime-00000.md)
