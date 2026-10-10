# requests.sessions.merge_hooks

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Properly merges both requests and session hooks.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(request_hooks, session_hooks, dict_class=<class 'collections.OrderedDict'>)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| request_hooks | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| session_hooks | positional or keyword | Yes | Not provided | — | Not described in the docstring |
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
request_hooks = ...  # TODO: supply a valid value from your application
session_hooks = ...  # TODO: supply a valid value from your application
result = m.merge_hooks(request_hooks=request_hooks, session_hooks=session_hooks)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'merge_hooks')
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
Properly merges both requests and session hooks.

    This is necessary because when request_hooks == {'response': []}, the
    merge breaks Session hooks entirely.
    
```

[Full module inspection](../modules/00039-requests.sessions.md)
