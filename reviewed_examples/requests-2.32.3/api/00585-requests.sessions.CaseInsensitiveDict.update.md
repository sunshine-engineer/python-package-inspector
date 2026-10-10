# requests.sessions.CaseInsensitiveDict.update

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Inherited class member.

## Signature

```text
(self, other=(), /, **kwds)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| other | positional only | No | Not provided | () | Not described in the docstring |
| kwds | var keyword | No | Not provided | Collects extra arguments | Not described in the docstring |

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
instance = ...  # TODO: construct m.CaseInsensitiveDict using its constructor page
result = instance.update()
print(result)

```

This is a class member. Construct `requests.sessions.CaseInsensitiveDict` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'CaseInsensitiveDict')
obj = inspect.getattr_static(obj, 'update')
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
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:
    for k in E.keys(): D[k] = E[k]
If E present and lacks .keys() method, does:
    for (k, v) in E: D[k] = v
In either case, this is followed by:
    for k, v in F.items(): D[k] = v
```

[Full module inspection](../modules/runtime-00014.md)
