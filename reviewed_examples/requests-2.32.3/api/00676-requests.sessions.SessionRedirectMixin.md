# requests.sessions.SessionRedirectMixin

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

No description supplied by the package.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
()
```

## Inputs

No caller-supplied parameters are declared.

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
result = m.SessionRedirectMixin()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [get_redirect_target](00677-requests.sessions.SessionRedirectMixin.get_redirect_target.md) | function | Receives a Response. Returns a redirect URI or ``None`` |
| [rebuild_auth](00678-requests.sessions.SessionRedirectMixin.rebuild_auth.md) | function | When being redirected we may want to strip authentication from the |
| [rebuild_method](00679-requests.sessions.SessionRedirectMixin.rebuild_method.md) | function | When being redirected we may want to change the method of the request |
| [rebuild_proxies](00680-requests.sessions.SessionRedirectMixin.rebuild_proxies.md) | function | This method re-evaluates the proxy configuration by considering the |
| [resolve_redirects](00681-requests.sessions.SessionRedirectMixin.resolve_redirects.md) | function | Receives a Response. Returns a generator of Responses or Requests. |
| [should_strip_auth](00682-requests.sessions.SessionRedirectMixin.should_strip_auth.md) | function | Decide whether Authorization header should be removed when redirecting |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'SessionRedirectMixin')
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
No docstring supplied.
```

[Full module inspection](../modules/00039-requests.sessions.md)
