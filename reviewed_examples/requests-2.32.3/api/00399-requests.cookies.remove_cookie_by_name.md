# requests.cookies.remove_cookie_by_name

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Unsets a cookie by name, by default over all domains and paths.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(cookiejar, name, domain=None, path=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| cookiejar | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| name | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| domain | positional or keyword | No | Not provided | None | Not described in the docstring |
| path | positional or keyword | No | Not provided | None | Not described in the docstring |

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
m = importlib.import_module('requests.cookies')
cookiejar = ...  # TODO: supply a valid value from your application
name = ...  # TODO: supply a valid value from your application
result = m.remove_cookie_by_name(cookiejar=cookiejar, name=name)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
obj = m
obj = inspect.getattr_static(obj, 'remove_cookie_by_name')
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
Unsets a cookie by name, by default over all domains and paths.

    Wraps CookieJar.clear(), is O(n).
    
```

[Full module inspection](../modules/00033-requests.cookies.md)
