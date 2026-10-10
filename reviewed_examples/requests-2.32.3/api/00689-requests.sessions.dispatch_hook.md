# requests.sessions.dispatch_hook

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Dispatches a hook dictionary on a given piece of data.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.hooks.dispatch_hook`.

## Signature

```text
(key, hooks, hook_data, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| key | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| hooks | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| hook_data | positional or keyword | Yes | Not provided | — | Not described in the docstring |
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
m = importlib.import_module('requests.sessions')
key = ...  # TODO: supply a valid value from your application
hooks = ...  # TODO: supply a valid value from your application
hook_data = ...  # TODO: supply a valid value from your application
result = m.dispatch_hook(key=key, hooks=hooks, hook_data=hook_data)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'dispatch_hook')
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
Dispatches a hook dictionary on a given piece of data.
```

[Full module inspection](../modules/00039-requests.sessions.md)
