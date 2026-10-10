# requests.cookies.CookieConflictError

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

There are two cookies that meet the criteria specified in the cookie jar.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

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
| [add_note](00346-requests.cookies.CookieConflictError.add_note.md) | function | Add a note to the exception |
| [with_traceback](00347-requests.cookies.CookieConflictError.with_traceback.md) | function | Set self.__traceback__ to tb and return self. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
obj = m
obj = inspect.getattr_static(obj, 'CookieConflictError')
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
There are two cookies that meet the criteria specified in the cookie jar.
    Use .get and .set and include domain and path args in order to be more specific.
    
```

[Full module inspection](../modules/00033-requests.cookies.md)
