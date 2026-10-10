# requests.sessions.to_key_val_list

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Take an object and test to see if it can be represented as a

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.utils.to_key_val_list`.

## Signature

```text
(value)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| value | positional or keyword | Yes | Not provided | — | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- list

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
to_key_val_list([('key', 'val')])
```

Expected output recorded in the docstring:

```text
[('key', 'val')]
```

```python
to_key_val_list({'key': 'val'})
```

Expected output recorded in the docstring:

```text
[('key', 'val')]
```

```python
to_key_val_list('string')
```

Expected output recorded in the docstring:

```text
Traceback (most recent call last):
...
ValueError: cannot encode objects that are not 2-tuples
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.sessions')
value = ...  # TODO: supply a valid value from your application
result = m.to_key_val_list(value=value)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'to_key_val_list')
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
Take an object and test to see if it can be represented as a
    dictionary. If it can be, return a list of tuples, e.g.,

    ::

        >>> to_key_val_list([('key', 'val')])
        [('key', 'val')]
        >>> to_key_val_list({'key': 'val'})
        [('key', 'val')]
        >>> to_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples

    :rtype: list
    
```

[Full module inspection](../modules/00039-requests.sessions.md)
