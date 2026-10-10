# requests.status_codes.LookupDict

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Dictionary lookup object.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.structures.LookupDict`.

## Signature

```text
(name=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| name | positional or keyword | No | Not provided | None | Not described in the docstring |

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
m = importlib.import_module('requests.status_codes')
result = m.LookupDict()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [clear](00706-requests.status_codes.LookupDict.clear.md) | function | Remove all items from the dict. |
| [copy](00707-requests.status_codes.LookupDict.copy.md) | function | Return a shallow copy of the dict. |
| [fromkeys](00708-requests.status_codes.LookupDict.fromkeys.md) | function | Create a new dictionary with keys from iterable and values set to value. |
| [get](00709-requests.status_codes.LookupDict.get.md) | function | Return the value for key if key is in the dictionary, else default. |
| [items](00710-requests.status_codes.LookupDict.items.md) | function | Return a set-like object providing a view on the dict's items. |
| [keys](00711-requests.status_codes.LookupDict.keys.md) | function | Return a set-like object providing a view on the dict's keys. |
| [pop](00712-requests.status_codes.LookupDict.pop.md) | function | D.pop(k&#91;,d&#93;) -> v, remove specified key and return the corresponding value. |
| [popitem](00713-requests.status_codes.LookupDict.popitem.md) | function | Remove and return a (key, value) pair as a 2-tuple. |
| [setdefault](00714-requests.status_codes.LookupDict.setdefault.md) | function | Insert key with a value of default if key is not in the dictionary. |
| [update](00715-requests.status_codes.LookupDict.update.md) | function | D.update(&#91;E, &#93;**F) -> None.  Update D from mapping/iterable E and F. |
| [values](00716-requests.status_codes.LookupDict.values.md) | function | Return an object providing a view on the dict's values. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.status_codes')
obj = m
obj = inspect.getattr_static(obj, 'LookupDict')
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
Dictionary lookup object.
```

[Full module inspection](../modules/00040-requests.status_codes.md)
