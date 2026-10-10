# requests.utils.parse_dict_header

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Parse lists of key, value pairs as described by RFC 2068 Section 2 and

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(value)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| value | positional or keyword | Yes | Not provided | — | a string with a dict header. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- :class:`dict`
- dict

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
d = parse_dict_header('foo="is a fish", bar="as well"')
```

```python
type(d) is dict
```

Expected output recorded in the docstring:

```text
True
```

```python
sorted(d.items())
```

Expected output recorded in the docstring:

```text
[('bar', 'as well'), ('foo', 'is a fish')]
```

```python
parse_dict_header('key_without_value')
```

Expected output recorded in the docstring:

```text
{'key_without_value': None}
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.utils')
value = ...  # TODO: supply a valid value from your application
result = m.parse_dict_header(value=value)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.utils')
obj = m
obj = inspect.getattr_static(obj, 'parse_dict_header')
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
Parse lists of key, value pairs as described by RFC 2068 Section 2 and
    convert them into a python dict:

    >>> d = parse_dict_header('foo="is a fish", bar="as well"')
    >>> type(d) is dict
    True
    >>> sorted(d.items())
    [('bar', 'as well'), ('foo', 'is a fish')]

    If there is no value for a key it will be `None`:

    >>> parse_dict_header('key_without_value')
    {'key_without_value': None}

    To create a header from the :class:`dict` again, use the
    :func:`dump_header` function.

    :param value: a string with a dict header.
    :return: :class:`dict`
    :rtype: dict
    
```

[Full module inspection](../modules/00042-requests.utils.md)
