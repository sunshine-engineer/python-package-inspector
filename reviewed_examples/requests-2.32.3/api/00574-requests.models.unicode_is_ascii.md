# requests.models.unicode_is_ascii

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Determine if unicode string only contains ASCII characters.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests._internal_utils.unicode_is_ascii`.

## Signature

```text
(u_string)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| u_string | positional or keyword | Yes | str | — | unicode string to check. Must be unicode and not Python 2 `str`. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- bool

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.models')
u_string = ...  # TODO: supply a valid value from your application
result = m.unicode_is_ascii(u_string=u_string)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.models')
obj = m
obj = inspect.getattr_static(obj, 'unicode_is_ascii')
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
Determine if unicode string only contains ASCII characters.

    :param str u_string: unicode string to check. Must be unicode
        and not Python 2 `str`.
    :rtype: bool
    
```

[Full module inspection](../modules/00037-requests.models.md)
