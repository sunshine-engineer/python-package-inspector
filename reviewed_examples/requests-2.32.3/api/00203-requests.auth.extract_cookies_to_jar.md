# requests.auth.extract_cookies_to_jar

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Extract the cookies from the response into a CookieJar.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.cookies.extract_cookies_to_jar`.

## Signature

```text
(jar, request, response)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| jar | positional or keyword | Yes | Not provided | — | http.cookiejar.CookieJar (not necessarily a RequestsCookieJar) |
| request | positional or keyword | Yes | Not provided | — | our own requests.Request object |
| response | positional or keyword | Yes | Not provided | — | urllib3.HTTPResponse object |

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
m = importlib.import_module('requests.auth')
jar = ...  # TODO: supply a valid value from your application
request = ...  # TODO: supply a valid value from your application
response = ...  # TODO: supply a valid value from your application
result = m.extract_cookies_to_jar(jar=jar, request=request, response=response)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.auth')
obj = m
obj = inspect.getattr_static(obj, 'extract_cookies_to_jar')
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
Extract the cookies from the response into a CookieJar.

    :param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)
    :param request: our own requests.Request object
    :param response: urllib3.HTTPResponse object
    
```

[Full module inspection](../modules/00030-requests.auth.md)
