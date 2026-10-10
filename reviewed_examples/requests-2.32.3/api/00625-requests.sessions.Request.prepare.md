# requests.sessions.Request.prepare

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self)
```

## Inputs

No caller-supplied parameters are declared.

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
instance = ...  # TODO: construct m.Request using its constructor page
result = instance.prepare()
print(result)

```

This is a class member. Construct `requests.sessions.Request` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.sessions.PreparedRequest](00609-requests.sessions.PreparedRequest.md) — The fully mutable :class:`PreparedRequest <PreparedRequest>` object,

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'Request')
obj = inspect.getattr_static(obj, 'prepare')
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
Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.
```

[Full module inspection](../modules/00039-requests.sessions.md)
