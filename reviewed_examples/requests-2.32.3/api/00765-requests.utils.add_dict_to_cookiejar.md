# requests.utils.add_dict_to_cookiejar

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Returns a CookieJar from a key/value dictionary.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(cj, cookie_dict)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| cj | positional or keyword | Yes | Not provided | — | CookieJar to insert cookies into. |
| cookie_dict | positional or keyword | Yes | Not provided | — | Dict of key/values to insert into CookieJar. |

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
m = importlib.import_module('requests.utils')
cj = ...  # TODO: supply a valid value from your application
cookie_dict = ...  # TODO: supply a valid value from your application
result = m.add_dict_to_cookiejar(cj=cj, cookie_dict=cookie_dict)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.utils')
obj = m
obj = inspect.getattr_static(obj, 'add_dict_to_cookiejar')
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

    :param cj: CookieJar to insert cookies into.
    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :rtype: CookieJar
    
```

[Full module inspection](../modules/00042-requests.utils.md)
