# requests.utils.select_proxy

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Select a proxy for the url, if applicable.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(url, proxies)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| url | positional or keyword | Yes | Not provided | — | The url being for the request |
| proxies | positional or keyword | Yes | Not provided | — | A dictionary of schemes or schemes and hosts to proxy URLs |

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
m = importlib.import_module('requests.utils')
url = ...  # TODO: supply a valid value from your application
proxies = ...  # TODO: supply a valid value from your application
result = m.select_proxy(url=url, proxies=proxies)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.utils')
obj = m
obj = inspect.getattr_static(obj, 'select_proxy')
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
Select a proxy for the url, if applicable.

    :param url: The url being for the request
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    
```

[Full module inspection](../modules/00042-requests.utils.md)
