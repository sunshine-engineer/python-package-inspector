# requests.cookies.RequestsCookieJar.pop

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

D.pop(k[,d]) -> v, remove specified key and return the corresponding

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Inherited class member.

## Signature

```text
(self, key, default=<object object at 0x000001A94AC401D0>)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| key | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| default | positional or keyword | No | Not provided | <object object at 0x000001A94AC401D0> | Not described in the docstring |

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
key = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.RequestsCookieJar using its constructor page
result = instance.pop(key=key)
print(result)

```

This is a class member. Construct `requests.cookies.RequestsCookieJar` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
obj = m
obj = inspect.getattr_static(obj, 'RequestsCookieJar')
obj = inspect.getattr_static(obj, 'pop')
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
D.pop(k[,d]) -> v, remove specified key and return the corresponding
value.  If key is not found, d is returned if given, otherwise
KeyError is raised.
```

[Full module inspection](../modules/runtime-00008.md)
