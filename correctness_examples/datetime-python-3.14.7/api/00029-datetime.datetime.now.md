# datetime.datetime.now

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Returns new datetime object representing current time local to tz.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(type, /, tz=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| tz | positional or keyword | No | Not provided | None | Not described in the docstring |

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
m = importlib.import_module('datetime')
instance = ...  # TODO: construct m.datetime using its constructor page
result = instance.now()
print(result)

```

Construct `datetime.datetime` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('datetime')
obj = m
obj = inspect.getattr_static(obj, 'datetime')
obj = inspect.getattr_static(obj, 'now')
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
Returns new datetime object representing current time local to tz.

  tz
    Timezone object.

If no tz is specified, uses local timezone.
```

[Full module inspection](../modules/runtime-00000.md)
