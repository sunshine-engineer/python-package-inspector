# requests.structures

Source: `requests/structures.py`

```text

requests.structures
~~~~~~~~~~~~~~~~~~~

Data structures that power Requests.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.structures')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## from collections import OrderedDict

```json
{
  "name": "from collections import OrderedDict",
  "kind": "import",
  "line": 8,
  "from_module": "collections",
  "level": 0,
  "bindings": [
    {
      "imported": "OrderedDict",
      "local": "OrderedDict"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import Mapping, MutableMapping

```json
{
  "name": "from .compat import Mapping, MutableMapping",
  "kind": "import",
  "line": 10,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "Mapping",
      "local": "Mapping"
    },
    {
      "imported": "MutableMapping",
      "local": "MutableMapping"
    }
  ]
}
```

```text
No docstring available.
```

## CaseInsensitiveDict

```json
{
  "name": "CaseInsensitiveDict",
  "kind": "class",
  "line": 13,
  "bases": [
    "MutableMapping"
  ],
  "decorators": []
}
```

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

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, data=None, **kwargs)",
  "line": 40,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "variadic keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __setitem__

```json
{
  "name": "__setitem__",
  "kind": "function",
  "signature": "__setitem__(self, key, value)",
  "line": 46,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __getitem__

```json
{
  "name": "__getitem__",
  "kind": "function",
  "signature": "__getitem__(self, key)",
  "line": 51,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __delitem__

```json
{
  "name": "__delitem__",
  "kind": "function",
  "signature": "__delitem__(self, key)",
  "line": 54,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __iter__

```json
{
  "name": "__iter__",
  "kind": "function",
  "signature": "__iter__(self)",
  "line": 57,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __len__

```json
{
  "name": "__len__",
  "kind": "function",
  "signature": "__len__(self)",
  "line": 60,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### lower_items

```json
{
  "name": "lower_items",
  "kind": "function",
  "signature": "lower_items(self)",
  "line": 63,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Like iteritems(), but with all lowercase keys.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "signature": "__eq__(self, other)",
  "line": 67,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "other",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### copy

```json
{
  "name": "copy",
  "kind": "function",
  "signature": "copy(self)",
  "line": 76,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "signature": "__repr__(self)",
  "line": 79,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

## LookupDict

```json
{
  "name": "LookupDict",
  "kind": "class",
  "line": 83,
  "bases": [
    "dict"
  ],
  "decorators": []
}
```

```text
Dictionary lookup object.
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "signature": "__init__(self, name=None)",
  "line": 86,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "signature": "__repr__(self)",
  "line": 90,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### __getitem__

```json
{
  "name": "__getitem__",
  "kind": "function",
  "signature": "__getitem__(self, key)",
  "line": 93,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### get

```json
{
  "name": "get",
  "kind": "function",
  "signature": "get(self, key, default=None)",
  "line": 98,
  "decorators": [],
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "default",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```
