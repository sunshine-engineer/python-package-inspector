# requests.Session.get_adapter

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Returns the appropriate connection adapter for the given URL.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, url)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| url | positional or keyword | Yes | Not provided | — | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- requests.adapters.BaseAdapter

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests')
url = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Session using its constructor page
result = instance.get_adapter(url=url)
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
obj = inspect.getattr_static(obj, 'get_adapter')
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

        Returns the appropriate connection adapter for the given URL.

        :rtype: requests.adapters.BaseAdapter
        
```

[Full module inspection](../modules/00007-requests.md)
