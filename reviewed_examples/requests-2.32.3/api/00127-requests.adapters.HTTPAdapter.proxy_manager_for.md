# requests.adapters.HTTPAdapter.proxy_manager_for

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Return urllib3 ProxyManager for the given proxy.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, proxy, **proxy_kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| proxy | positional or keyword | Yes | Not provided | — | The proxy to return a urllib3 ProxyManager for. |
| proxy_kwargs | var keyword | No | Not provided | Collects extra arguments | Extra keyword arguments used to configure the Proxy Manager. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- ProxyManager
- urllib3.ProxyManager

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.adapters')
proxy = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.HTTPAdapter using its constructor page
result = instance.proxy_manager_for(proxy=proxy)
print(result)

```

This is a class member. Construct `requests.adapters.HTTPAdapter` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.adapters.HTTPAdapter](00117-requests.adapters.HTTPAdapter.md) — The built-in HTTP Adapter for urllib3.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'HTTPAdapter')
obj = inspect.getattr_static(obj, 'proxy_manager_for')
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
Return urllib3 ProxyManager for the given proxy.

        This method should not be called from user code, and is only
        exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param proxy: The proxy to return a urllib3 ProxyManager for.
        :param proxy_kwargs: Extra keyword arguments used to configure the Proxy Manager.
        :returns: ProxyManager
        :rtype: urllib3.ProxyManager
        
```

[Full module inspection](../modules/00028-requests.adapters.md)
