# requests.sessions.merge_setting

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Determines appropriate setting for a given request, taking into account

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(request_setting, session_setting, dict_class=<class 'collections.OrderedDict'>)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| request_setting | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| session_setting | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| dict_class | positional or keyword | No | Not provided | <class 'collections.OrderedDict'> | Not described in the docstring |

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
request_setting = ...  # TODO: supply a valid value from your application
session_setting = ...  # TODO: supply a valid value from your application
result = m.merge_setting(request_setting=request_setting, session_setting=session_setting)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'merge_setting')
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
Determines appropriate setting for a given request, taking into account
    the explicit setting on that request, and the setting in the session. If a
    setting is a dictionary, they will be merged together using `dict_class`
    
```

[Full module inspection](../modules/00039-requests.sessions.md)
