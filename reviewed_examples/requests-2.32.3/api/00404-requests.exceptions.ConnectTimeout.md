# requests.exceptions.ConnectTimeout

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

The request timed out while trying to connect to the remote server.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(*args, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| args | var positional | No | Not provided | Collects extra arguments | Not described in the docstring |
| kwargs | var keyword | No | Not provided | Collects extra arguments | Not described in the docstring |

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
m = importlib.import_module('requests.exceptions')
result = m.ConnectTimeout()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [add_note](00405-requests.exceptions.ConnectTimeout.add_note.md) | function | Add a note to the exception |
| [with_traceback](00406-requests.exceptions.ConnectTimeout.with_traceback.md) | function | Set self.__traceback__ to tb and return self. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.exceptions')
obj = m
obj = inspect.getattr_static(obj, 'ConnectTimeout')
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
The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    
```

[Full module inspection](../modules/00034-requests.exceptions.md)
