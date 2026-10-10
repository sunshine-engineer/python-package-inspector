# requests.models.requote_uri

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Re-quote the given URI.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.utils.requote_uri`.

## Signature

```text
(uri)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| uri | positional or keyword | Yes | Not provided | — | Not described in the docstring |

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
m = importlib.import_module('requests.models')
uri = ...  # TODO: supply a valid value from your application
result = m.requote_uri(uri=uri)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.models')
obj = m
obj = inspect.getattr_static(obj, 'requote_uri')
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
Re-quote the given URI.

    This function passes the given URI through an unquote/quote cycle to
    ensure that it is fully and consistently quoted.

    :rtype: str
    
```

[Full module inspection](../modules/00037-requests.models.md)
