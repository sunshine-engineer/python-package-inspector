# requests.utils.unquote_header_value

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Unquotes a header value.  (Reversal of :func:`quote_header_value`).

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(value, is_filename=False)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| value | positional or keyword | Yes | Not provided | — | the header value to unquote. |
| is_filename | positional or keyword | No | Not provided | False | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- str

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.utils')
value = ...  # TODO: supply a valid value from your application
result = m.unquote_header_value(value=value)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.utils')
obj = m
obj = inspect.getattr_static(obj, 'unquote_header_value')
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
Unquotes a header value.  (Reversal of :func:`quote_header_value`).
    This does not use the real unquoting but what browsers are actually
    using for quoting.

    :param value: the header value to unquote.
    :rtype: str
    
```

[Full module inspection](../modules/00042-requests.utils.md)
