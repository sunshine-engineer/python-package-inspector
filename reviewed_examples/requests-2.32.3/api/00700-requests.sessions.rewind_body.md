# requests.sessions.rewind_body

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Move file pointer back to its recorded starting position

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.utils.rewind_body`.

## Signature

```text
(prepared_request)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| prepared_request | positional or keyword | Yes | Not provided | — | Not described in the docstring |

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
m = importlib.import_module('requests.sessions')
prepared_request = ...  # TODO: supply a valid value from your application
result = m.rewind_body(prepared_request=prepared_request)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'rewind_body')
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
Move file pointer back to its recorded starting position
    so it can be read again on redirect.
    
```

[Full module inspection](../modules/00039-requests.sessions.md)
