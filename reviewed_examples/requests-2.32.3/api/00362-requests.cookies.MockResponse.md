# requests.cookies.MockResponse

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(headers)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| headers | positional or keyword | Yes | Not provided | — | a httplib.HTTPMessage or analogous carrying the headers |

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
headers = ...  # TODO: supply a valid value from your application
result = m.MockResponse(headers=headers)
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [getheaders](00363-requests.cookies.MockResponse.getheaders.md) | function | No description supplied by the package. |
| [info](00364-requests.cookies.MockResponse.info.md) | function | No description supplied by the package. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
obj = m
obj = inspect.getattr_static(obj, 'MockResponse')
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
Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.

    ...what? Basically, expose the parsed HTTP headers from the server response
    the way `http.cookiejar` expects to see them.
    
```

### Constructor docstring

```text
Make a MockResponse for `cookiejar` to read.

        :param headers: a httplib.HTTPMessage or analogous carrying the headers
        
```

[Full module inspection](../modules/00033-requests.cookies.md)
