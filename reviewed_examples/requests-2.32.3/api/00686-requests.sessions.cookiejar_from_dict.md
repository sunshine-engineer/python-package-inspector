# requests.sessions.cookiejar_from_dict

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Returns a CookieJar from a key/value dictionary.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.cookies.cookiejar_from_dict`.

## Signature

```text
(cookie_dict, cookiejar=None, overwrite=True)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| cookie_dict | positional or keyword | Yes | Not provided | — | Dict of key/values to insert into CookieJar. |
| cookiejar | positional or keyword | No | Not provided | None | (optional) A cookiejar to add the cookies to. |
| overwrite | positional or keyword | No | Not provided | True | (optional) If False, will not replace cookies already in the jar with new ones. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- CookieJar

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.sessions')
cookie_dict = ...  # TODO: supply a valid value from your application
result = m.cookiejar_from_dict(cookie_dict=cookie_dict)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'cookiejar_from_dict')
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
Returns a CookieJar from a key/value dictionary.

    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :param cookiejar: (optional) A cookiejar to add the cookies to.
    :param overwrite: (optional) If False, will not replace cookies
        already in the jar with new ones.
    :rtype: CookieJar
    
```

[Full module inspection](../modules/00039-requests.sessions.md)
