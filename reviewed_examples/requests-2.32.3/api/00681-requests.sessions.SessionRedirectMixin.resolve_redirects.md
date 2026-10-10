# requests.sessions.SessionRedirectMixin.resolve_redirects

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Receives a Response. Returns a generator of Responses or Requests.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| resp | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| req | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| stream | positional or keyword | No | Not provided | False | Not described in the docstring |
| timeout | positional or keyword | No | Not provided | None | Not described in the docstring |
| verify | positional or keyword | No | Not provided | True | Not described in the docstring |
| cert | positional or keyword | No | Not provided | None | Not described in the docstring |
| proxies | positional or keyword | No | Not provided | None | Not described in the docstring |
| yield_requests | positional or keyword | No | Not provided | False | Not described in the docstring |
| adapter_kwargs | var keyword | No | Not provided | Collects extra arguments | Not described in the docstring |

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
resp = ...  # TODO: supply a valid value from your application
req = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.SessionRedirectMixin using its constructor page
result = instance.resolve_redirects(resp=resp, req=req)
print(result)

```

This is a class member. Construct `requests.sessions.SessionRedirectMixin` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'SessionRedirectMixin')
obj = inspect.getattr_static(obj, 'resolve_redirects')
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
Receives a Response. Returns a generator of Responses or Requests.
```

[Full module inspection](../modules/00039-requests.sessions.md)
