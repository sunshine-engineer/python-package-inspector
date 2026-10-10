# requests.Session.rebuild_proxies

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

This method re-evaluates the proxy configuration by considering the

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Inherited class member.

## Signature

```text
(self, prepared_request, proxies)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| prepared_request | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| proxies | positional or keyword | Yes | Not provided | — | Not described in the docstring |

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
prepared_request = ...  # TODO: supply a valid value from your application
proxies = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Session using its constructor page
result = instance.rebuild_proxies(prepared_request=prepared_request, proxies=proxies)
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
obj = inspect.getattr_static(obj, 'rebuild_proxies')
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
This method re-evaluates the proxy configuration by considering the
environment variables. If we are redirected to a URL covered by
NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
proxy keys for this URL (in case they were stripped by a previous
redirect).

This method also replaces the Proxy-Authorization header where
necessary.

:rtype: dict
```

[Full module inspection](../modules/runtime-00000.md)
