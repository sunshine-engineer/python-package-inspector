# requests.adapters.CaseInsensitiveDict

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

A case-insensitive ``dict``-like object.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.structures.CaseInsensitiveDict`.

## Signature

```text
(data=None, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| data | positional or keyword | No | Not provided | None | Not described in the docstring |
| kwargs | var keyword | No | Not provided | Collects extra arguments | Not described in the docstring |

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
m = importlib.import_module('requests.adapters')
result = m.CaseInsensitiveDict()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [clear](00100-requests.adapters.CaseInsensitiveDict.clear.md) | function | D.clear() -> None.  Remove all items from D. |
| [copy](00101-requests.adapters.CaseInsensitiveDict.copy.md) | function | No description supplied by the package. |
| [get](00102-requests.adapters.CaseInsensitiveDict.get.md) | function | D.get(k&#91;,d&#93;) -> D&#91;k&#93; if k in D, else d.  d defaults to None. |
| [items](00103-requests.adapters.CaseInsensitiveDict.items.md) | function | D.items() -> a set-like object providing a view on D's items |
| [keys](00104-requests.adapters.CaseInsensitiveDict.keys.md) | function | D.keys() -> a set-like object providing a view on D's keys |
| [lower_items](00105-requests.adapters.CaseInsensitiveDict.lower_items.md) | function | Like iteritems(), but with all lowercase keys. |
| [pop](00106-requests.adapters.CaseInsensitiveDict.pop.md) | function | D.pop(k&#91;,d&#93;) -> v, remove specified key and return the corresponding |
| [popitem](00107-requests.adapters.CaseInsensitiveDict.popitem.md) | function | D.popitem() -> (k, v), remove and return some (key, value) pair |
| [setdefault](00108-requests.adapters.CaseInsensitiveDict.setdefault.md) | function | D.setdefault(k&#91;,d&#93;) -> D.get(k,d), also set D&#91;k&#93;=d if k not in D |
| [update](00109-requests.adapters.CaseInsensitiveDict.update.md) | function | D.update(&#91;E, &#93;**F) -> None.  Update D from mapping/iterable E and F. |
| [values](00110-requests.adapters.CaseInsensitiveDict.values.md) | function | D.values() -> an object providing a view on D's values |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'CaseInsensitiveDict')
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
A case-insensitive ``dict``-like object.

    Implements all methods and operations of
    ``MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.

    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive::

        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True

    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.

    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.
    
```

[Full module inspection](../modules/00028-requests.adapters.md)
