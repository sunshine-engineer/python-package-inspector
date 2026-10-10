# requests.PreparedRequest.prepare

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Prepares the entire request with the given parameters.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| method | positional or keyword | No | Not provided | None | Not described in the docstring |
| url | positional or keyword | No | Not provided | None | Not described in the docstring |
| headers | positional or keyword | No | Not provided | None | Not described in the docstring |
| files | positional or keyword | No | Not provided | None | Not described in the docstring |
| data | positional or keyword | No | Not provided | None | Not described in the docstring |
| params | positional or keyword | No | Not provided | None | Not described in the docstring |
| auth | positional or keyword | No | Not provided | None | Not described in the docstring |
| cookies | positional or keyword | No | Not provided | None | Not described in the docstring |
| hooks | positional or keyword | No | Not provided | None | Not described in the docstring |
| json | positional or keyword | No | Not provided | None | Not described in the docstring |

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
m = importlib.import_module('requests')
instance = ...  # TODO: construct m.PreparedRequest using its constructor page
result = instance.prepare()
print(result)

```

This is a class member. Construct `requests.PreparedRequest` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests')
obj = m
obj = inspect.getattr_static(obj, 'PreparedRequest')
obj = inspect.getattr_static(obj, 'prepare')
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
Prepares the entire request with the given parameters.
```

[Full module inspection](../modules/00007-requests.md)
