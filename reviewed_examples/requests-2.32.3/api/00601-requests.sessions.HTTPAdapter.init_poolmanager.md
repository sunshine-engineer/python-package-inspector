# requests.sessions.HTTPAdapter.init_poolmanager

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Initializes a urllib3 PoolManager.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, connections, maxsize, block=False, **pool_kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| connections | positional or keyword | Yes | Not provided | — | The number of urllib3 connection pools to cache. |
| maxsize | positional or keyword | Yes | Not provided | — | The maximum number of connections to save in the pool. |
| block | positional or keyword | No | Not provided | False | Block when no free connections are available. |
| pool_kwargs | var keyword | No | Not provided | Collects extra arguments | Extra keyword arguments used to initialize the Pool Manager. |

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
m = importlib.import_module('requests.sessions')
connections = ...  # TODO: supply a valid value from your application
maxsize = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.HTTPAdapter using its constructor page
result = instance.init_poolmanager(connections=connections, maxsize=maxsize)
print(result)

```

This is a class member. Construct `requests.sessions.HTTPAdapter` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.sessions.HTTPAdapter](00593-requests.sessions.HTTPAdapter.md) — The built-in HTTP Adapter for urllib3.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'HTTPAdapter')
obj = inspect.getattr_static(obj, 'init_poolmanager')
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
Initializes a urllib3 PoolManager.

        This method should not be called from user code, and is only
        exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param connections: The number of urllib3 connection pools to cache.
        :param maxsize: The maximum number of connections to save in the pool.
        :param block: Block when no free connections are available.
        :param pool_kwargs: Extra keyword arguments used to initialize the Pool Manager.
        
```

[Full module inspection](../modules/00039-requests.sessions.md)
