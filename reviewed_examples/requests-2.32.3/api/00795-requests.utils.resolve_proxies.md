# requests.utils.resolve_proxies

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

This method takes proxy information from a request and configuration

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(request, proxies, trust_env=True)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| request | positional or keyword | Yes | Not provided | — | Request or PreparedRequest |
| proxies | positional or keyword | Yes | Not provided | — | A dictionary of schemes or schemes and hosts to proxy URLs |
| trust_env | positional or keyword | No | Not provided | True | Boolean declaring whether to trust environment configs |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- dict

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.utils')
request = ...  # TODO: supply a valid value from your application
proxies = ...  # TODO: supply a valid value from your application
result = m.resolve_proxies(request=request, proxies=proxies)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.utils')
obj = m
obj = inspect.getattr_static(obj, 'resolve_proxies')
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
This method takes proxy information from a request and configuration
    input to resolve a mapping of target proxies. This will consider settings
    such as NO_PROXY to strip proxy configurations.

    :param request: Request or PreparedRequest
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    :param trust_env: Boolean declaring whether to trust environment configs

    :rtype: dict
    
```

[Full module inspection](../modules/00042-requests.utils.md)
