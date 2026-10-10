# requests.sessions.merge_cookies

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Add cookies to cookiejar and returns a merged CookieJar.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.cookies.merge_cookies`.

## Signature

```text
(cookiejar, cookies)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| cookiejar | positional or keyword | Yes | Not provided | — | CookieJar object to add the cookies to. |
| cookies | positional or keyword | Yes | Not provided | — | Dictionary or CookieJar object to be added. |

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
cookiejar = ...  # TODO: supply a valid value from your application
cookies = ...  # TODO: supply a valid value from your application
result = m.merge_cookies(cookiejar=cookiejar, cookies=cookies)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'merge_cookies')
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
Add cookies to cookiejar and returns a merged CookieJar.

    :param cookiejar: CookieJar object to add the cookies to.
    :param cookies: Dictionary or CookieJar object to be added.
    :rtype: CookieJar
    
```

[Full module inspection](../modules/00039-requests.sessions.md)
