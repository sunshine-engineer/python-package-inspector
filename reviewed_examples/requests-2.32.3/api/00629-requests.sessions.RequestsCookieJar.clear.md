# requests.sessions.RequestsCookieJar.clear

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Clear some cookies.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Inherited class member.

## Signature

```text
(self, domain=None, path=None, name=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| domain | positional or keyword | No | Not provided | None | Not described in the docstring |
| path | positional or keyword | No | Not provided | None | Not described in the docstring |
| name | positional or keyword | No | Not provided | None | Not described in the docstring |

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
instance = ...  # TODO: construct m.RequestsCookieJar using its constructor page
result = instance.clear()
print(result)

```

This is a class member. Construct `requests.sessions.RequestsCookieJar` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'RequestsCookieJar')
obj = inspect.getattr_static(obj, 'clear')
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
Clear some cookies.

Invoking this method without arguments will clear all cookies.  If
given a single argument, only cookies belonging to that domain will be
removed.  If given two arguments, cookies belonging to the specified
path within that domain are removed.  If given three arguments, then
the cookie with the specified name, path and domain is removed.

Raises KeyError if no matching cookie exists.
```

[Full module inspection](../modules/runtime-00014.md)
