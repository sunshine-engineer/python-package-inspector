# requests.Session.merge_environment_settings

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Check the environment and merge it with some settings.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, url, proxies, stream, verify, cert)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| url | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| proxies | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| stream | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| verify | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| cert | positional or keyword | Yes | Not provided | — | Not described in the docstring |

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
m = importlib.import_module('requests')
url = ...  # TODO: supply a valid value from your application
proxies = ...  # TODO: supply a valid value from your application
stream = ...  # TODO: supply a valid value from your application
verify = ...  # TODO: supply a valid value from your application
cert = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Session using its constructor page
result = instance.merge_environment_settings(url=url, proxies=proxies, stream=stream, verify=verify, cert=cert)
print(result)

```

This is a class member. Construct `requests.Session` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests')
obj = m
obj = inspect.getattr_static(obj, 'Session')
obj = inspect.getattr_static(obj, 'merge_environment_settings')
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

        Check the environment and merge it with some settings.

        :rtype: dict
        
```

[Full module inspection](../modules/00007-requests.md)
