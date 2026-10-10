# Runtime: requests.sessions

```text
requests.sessions
~~~~~~~~~~~~~~~~~

This module provides a Session object to manage and persist settings across
requests (cookies, auth, proxies).
```

## CaseInsensitiveDict

```json
{
  "name": "CaseInsensitiveDict",
  "kind": "class",
  "origin": "requests.structures",
  "signature": "(data=None, **kwargs)",
  "parameters": [
    {
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
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

### _MutableMapping__marker

```json
{
  "name": "_MutableMapping__marker",
  "kind": "object",
  "decorators": [],
  "inherited": true
}
```

```text
The base class of the class hierarchy.

When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.
```

### __abstractmethods__

```json
{
  "name": "__abstractmethods__",
  "kind": "frozenset",
  "decorators": [],
  "inherited": false
}
```

```text
Build an immutable unordered collection of unique elements.
```

### __annotate_func__

```json
{
  "name": "__annotate_func__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": true
}
```

```text
The type of the None singleton.
```

### __annotations_cache__

```json
{
  "name": "__annotations_cache__",
  "kind": "dict",
  "decorators": [],
  "inherited": true
}
```

```text
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __class_getitem__

```json
{
  "name": "__class_getitem__",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": true,
  "signature": "(origin, args, /)",
  "parameters": [
    {
      "name": "origin",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Represent a PEP 585 generic type

For example, for t = list[int], t.__origin__ is list and t.__args__
is (int,).
```

### __contains__

```json
{
  "name": "__contains__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key)",
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

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __delitem__

```json
{
  "name": "__delitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key)",
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

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
dictionary for instance variables
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, other)",
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
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getitem__

```json
{
  "name": "__getitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key)",
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

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": false
}
```

```text
The type of the None singleton.
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, data=None, **kwargs)",
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
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __iter__

```json
{
  "name": "__iter__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __len__

```json
{
  "name": "__len__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Return repr(self).
```

### __reversed__

```json
{
  "name": "__reversed__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": true
}
```

```text
The type of the None singleton.
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setitem__

```json
{
  "name": "__setitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key, value)",
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

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __slots__

```json
{
  "name": "__slots__",
  "kind": "tuple",
  "decorators": [],
  "inherited": true
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": true,
  "signature": "(cls, C)",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "C",
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

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
list of weak references to the object
```

### _abc_impl

```json
{
  "name": "_abc_impl",
  "kind": "_abc_data",
  "decorators": [],
  "inherited": false
}
```

```text
Internal state held by ABC machinery.
```

### clear

```json
{
  "name": "clear",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
D.clear() -> None.  Remove all items from D.
```

### copy

```json
{
  "name": "copy",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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

### get

```json
{
  "name": "get",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key, default=None)",
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
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
```

### items

```json
{
  "name": "items",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
D.items() -> a set-like object providing a view on D's items
```

### keys

```json
{
  "name": "keys",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
D.keys() -> a set-like object providing a view on D's keys
```

### lower_items

```json
{
  "name": "lower_items",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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

### pop

```json
{
  "name": "pop",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key, default=<object object at 0x000001F8742901D0>)",
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
      "default": "<object object at 0x000001F8742901D0>",
      "required": false
    }
  ],
  "returns": null
}
```

```text
D.pop(k[,d]) -> v, remove specified key and return the corresponding
value.  If key is not found, d is returned if given, otherwise
KeyError is raised.
```

### popitem

```json
{
  "name": "popitem",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.
```

### setdefault

```json
{
  "name": "setdefault",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key, default=None)",
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
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
```

### update

```json
{
  "name": "update",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, other=(), /, **kwds)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "other",
      "kind": "positional only",
      "annotation": null,
      "default": "()",
      "required": false
    },
    {
      "name": "kwds",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:
    for k in E.keys(): D[k] = E[k]
If E present and lacks .keys() method, does:
    for (k, v) in E: D[k] = v
In either case, this is followed by:
    for k, v in F.items(): D[k] = v
```

### values

```json
{
  "name": "values",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
D.values() -> an object providing a view on D's values
```

## ChunkedEncodingError

```json
{
  "name": "ChunkedEncodingError",
  "kind": "class",
  "origin": "requests.exceptions",
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
The server declared chunked encoding but sent an invalid chunk.
```

### __cause__

```json
{
  "name": "__cause__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __context__

```json
{
  "name": "__context__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize RequestException with `request` and `response` objects.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, state, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "state",
      "kind": "positional only",
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

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __suppress_context__

```json
{
  "name": "__suppress_context__",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __traceback__

```json
{
  "name": "__traceback__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### add_note

```json
{
  "name": "add_note",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, note, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "note",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Add a note to the exception
```

### args

```json
{
  "name": "args",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### characters_written

```json
{
  "name": "characters_written",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### errno

```json
{
  "name": "errno",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
POSIX exception code
```

### filename

```json
{
  "name": "filename",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
exception filename
```

### filename2

```json
{
  "name": "filename2",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
second exception filename
```

### strerror

```json
{
  "name": "strerror",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
exception strerror
```

### winerror

```json
{
  "name": "winerror",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
Win32 exception code
```

### with_traceback

```json
{
  "name": "with_traceback",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, tb, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "tb",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Set self.__traceback__ to tb and return self.
```

## ContentDecodingError

```json
{
  "name": "ContentDecodingError",
  "kind": "class",
  "origin": "requests.exceptions",
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Failed to decode response content.
```

### __cause__

```json
{
  "name": "__cause__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __context__

```json
{
  "name": "__context__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize RequestException with `request` and `response` objects.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, state, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "state",
      "kind": "positional only",
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

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __suppress_context__

```json
{
  "name": "__suppress_context__",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __traceback__

```json
{
  "name": "__traceback__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### add_note

```json
{
  "name": "add_note",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, note, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "note",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Add a note to the exception
```

### args

```json
{
  "name": "args",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### characters_written

```json
{
  "name": "characters_written",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### errno

```json
{
  "name": "errno",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
POSIX exception code
```

### filename

```json
{
  "name": "filename",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
exception filename
```

### filename2

```json
{
  "name": "filename2",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
second exception filename
```

### strerror

```json
{
  "name": "strerror",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
exception strerror
```

### winerror

```json
{
  "name": "winerror",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
Win32 exception code
```

### with_traceback

```json
{
  "name": "with_traceback",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, tb, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "tb",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Set self.__traceback__ to tb and return self.
```

## DEFAULT_PORTS

```json
{
  "name": "DEFAULT_PORTS",
  "kind": "dict",
  "origin": null
}
```

```text
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
```

## DEFAULT_REDIRECT_LIMIT

```json
{
  "name": "DEFAULT_REDIRECT_LIMIT",
  "kind": "int",
  "origin": null
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

## HTTPAdapter

```json
{
  "name": "HTTPAdapter",
  "kind": "class",
  "origin": "requests.adapters",
  "signature": "(pool_connections=10, pool_maxsize=10, max_retries=0, pool_block=False)",
  "parameters": [
    {
      "name": "pool_connections",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "10",
      "required": false
    },
    {
      "name": "pool_maxsize",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "10",
      "required": false
    },
    {
      "name": "max_retries",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "0",
      "required": false
    },
    {
      "name": "pool_block",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    }
  ],
  "returns": null
}
```

```text
The built-in HTTP Adapter for urllib3.

Provides a general-case interface for Requests sessions to contact HTTP and
HTTPS urls by implementing the Transport Adapter interface. This class will
usually be created by the :class:`Session <Session>` class under the
covers.

:param pool_connections: The number of urllib3 connection pools to cache.
:param pool_maxsize: The maximum number of connections to save in the pool.
:param max_retries: The maximum number of retries each connection
    should attempt. Note, this applies only to failed DNS lookups, socket
    connections and connection timeouts, never to requests where data has
    made it to the server. By default, Requests does not retry failed
    connections. If you need granular control over the conditions under
    which we retry a request, import urllib3's ``Retry`` class and pass
    that instead.
:param pool_block: Whether the connection pool should block for connections.

Usage::

  >>> import requests
  >>> s = requests.Session()
  >>> a = requests.adapters.HTTPAdapter(max_retries=3)
  >>> s.mount('http://', a)
```

### __attrs__

```json
{
  "name": "__attrs__",
  "kind": "list",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
dictionary for instance variables
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, pool_connections=10, pool_maxsize=10, max_retries=0, pool_block=False)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pool_connections",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "10",
      "required": false
    },
    {
      "name": "pool_maxsize",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "10",
      "required": false
    },
    {
      "name": "max_retries",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "0",
      "required": false
    },
    {
      "name": "pool_block",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, state)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "state",
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

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### add_headers

```json
{
  "name": "add_headers",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, request, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Add any headers needed by the connection. As of v2.0 this does
nothing by default, but is left for overriding by users that subclass
the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

This should not be called from user code, and is only exposed for use
when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

:param request: The :class:`PreparedRequest <PreparedRequest>` to add headers to.
:param kwargs: The keyword arguments from the call to send().
```

### build_connection_pool_key_attributes

```json
{
  "name": "build_connection_pool_key_attributes",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, request, verify, cert=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cert",
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
Build the PoolKey attributes used by urllib3 to return a connection.

This looks at the PreparedRequest, the user-specified verify value,
and the value of the cert parameter to determine what PoolKey values
to use to select a connection from a given urllib3 Connection Pool.

The SSL related pool key arguments are not consistently set. As of
this writing, use the following to determine what keys may be in that
dictionary:

* If ``verify`` is ``True``, ``"ssl_context"`` will be set and will be the
  default Requests SSL Context
* If ``verify`` is ``False``, ``"ssl_context"`` will not be set but
  ``"cert_reqs"`` will be set
* If ``verify`` is a string, (i.e., it is a user-specified trust bundle)
  ``"ca_certs"`` will be set if the string is not a directory recognized
  by :py:func:`os.path.isdir`, otherwise ``"ca_certs_dir"`` will be
  set.
* If ``"cert"`` is specified, ``"cert_file"`` will always be set. If
  ``"cert"`` is a tuple with a second item, ``"key_file"`` will also
  be present

To override these settings, one may subclass this class, call this
method and use the above logic to change parameters as desired. For
example, if one wishes to use a custom :py:class:`ssl.SSLContext` one
must both set ``"ssl_context"`` and based on what else they require,
alter the other keys to ensure the desired behaviour.

:param request:
    The PreparedReqest being sent over the connection.
:type request:
    :class:`~requests.models.PreparedRequest`
:param verify:
    Either a boolean, in which case it controls whether
    we verify the server's TLS certificate, or a string, in which case it
    must be a path to a CA bundle to use.
:param cert:
    (optional) Any user-provided SSL certificate for client
    authentication (a.k.a., mTLS). This may be a string (i.e., just
    the path to a file which holds both certificate and key) or a
    tuple of length 2 with the certificate file path and key file
    path.
:returns:
    A tuple of two dictionaries. The first is the "host parameters"
    portion of the Pool Key including scheme, hostname, and port. The
    second is a dictionary of SSLContext related parameters.
```

### build_response

```json
{
  "name": "build_response",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, req, resp)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "req",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "resp",
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
Builds a :class:`Response <requests.Response>` object from a urllib3
response. This should not be called from user code, and is only exposed
for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`

:param req: The :class:`PreparedRequest <PreparedRequest>` used to generate the response.
:param resp: The urllib3 response object.
:rtype: requests.Response
```

### cert_verify

```json
{
  "name": "cert_verify",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, conn, url, verify, cert)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "conn",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cert",
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
Verify a SSL certificate. This method should not be called from user
code, and is only exposed for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

:param conn: The urllib3 connection object associated with the cert.
:param url: The requested URL.
:param verify: Either a boolean, in which case it controls whether we verify
    the server's TLS certificate, or a string, in which case it must be a path
    to a CA bundle to use
:param cert: The SSL certificate to verify.
```

### close

```json
{
  "name": "close",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Disposes of any internal state.

Currently, this closes the PoolManager and any active ProxyManager,
which closes any pooled connections.
```

### get_connection

```json
{
  "name": "get_connection",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, proxies=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
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
DEPRECATED: Users should move to `get_connection_with_tls_context`
for all subclasses of HTTPAdapter using Requests>=2.32.2.

Returns a urllib3 connection for the given URL. This should not be
called from user code, and is only exposed for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

:param url: The URL to connect to.
:param proxies: (optional) A Requests-style dictionary of proxies used on this request.
:rtype: urllib3.ConnectionPool
```

### get_connection_with_tls_context

```json
{
  "name": "get_connection_with_tls_context",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, request, verify, proxies=None, cert=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cert",
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
Returns a urllib3 connection for the given request and TLS settings.
This should not be called from user code, and is only exposed for use
when subclassing the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

:param request:
    The :class:`PreparedRequest <PreparedRequest>` object to be sent
    over the connection.
:param verify:
    Either a boolean, in which case it controls whether we verify the
    server's TLS certificate, or a string, in which case it must be a
    path to a CA bundle to use.
:param proxies:
    (optional) The proxies dictionary to apply to the request.
:param cert:
    (optional) Any user-provided SSL certificate to be used for client
    authentication (a.k.a., mTLS).
:rtype:
    urllib3.ConnectionPool
```

### init_poolmanager

```json
{
  "name": "init_poolmanager",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, connections, maxsize, block=False, **pool_kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "connections",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "maxsize",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "block",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "pool_kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initializes a urllib3 PoolManager.

This method should not be called from user code, and is only
exposed for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

:param connections: The number of urllib3 connection pools to cache.
:param maxsize: The maximum number of connections to save in the pool.
:param block: Block when no free connections are available.
:param pool_kwargs: Extra keyword arguments used to initialize the Pool Manager.
```

### proxy_headers

```json
{
  "name": "proxy_headers",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, proxy)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxy",
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
Returns a dictionary of the headers to add to any request sent
through a proxy. This works with urllib3 magic to ensure that they are
correctly sent to the proxy, rather than in a tunnelled request if
CONNECT is being used.

This should not be called from user code, and is only exposed for use
when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

:param proxy: The url of the proxy being used for this request.
:rtype: dict
```

### proxy_manager_for

```json
{
  "name": "proxy_manager_for",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, proxy, **proxy_kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxy",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxy_kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return urllib3 ProxyManager for the given proxy.

This method should not be called from user code, and is only
exposed for use when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

:param proxy: The proxy to return a urllib3 ProxyManager for.
:param proxy_kwargs: Extra keyword arguments used to configure the Proxy Manager.
:returns: ProxyManager
:rtype: urllib3.ProxyManager
```

### request_url

```json
{
  "name": "request_url",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, request, proxies)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
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
Obtain the url to use when making the final request.

If the message is being sent through a HTTP proxy, the full URL has to
be used. Otherwise, we should only use the path portion of the URL.

This should not be called from user code, and is only exposed for use
when subclassing the
:class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

:param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
:param proxies: A dictionary of schemes or schemes and hosts to proxy URLs.
:rtype: str
```

### send

```json
{
  "name": "send",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "stream",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "timeout",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    },
    {
      "name": "cert",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "proxies",
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
Sends PreparedRequest object. Returns Response object.

:param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
:param stream: (optional) Whether to stream the request content.
:param timeout: (optional) How long to wait for the server to send
    data before giving up, as a float, or a :ref:`(connect timeout,
    read timeout) <timeouts>` tuple.
:type timeout: float or tuple or urllib3 Timeout object
:param verify: (optional) Either a boolean, in which case it controls whether
    we verify the server's TLS certificate, or a string, in which case it
    must be a path to a CA bundle to use
:param cert: (optional) Any user-provided SSL certificate to be trusted.
:param proxies: (optional) The proxies dictionary to apply to the request.
:rtype: requests.Response
```

## InvalidSchema

```json
{
  "name": "InvalidSchema",
  "kind": "class",
  "origin": "requests.exceptions",
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
The URL scheme provided is either invalid or unsupported.
```

### __cause__

```json
{
  "name": "__cause__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __context__

```json
{
  "name": "__context__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize RequestException with `request` and `response` objects.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, state, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "state",
      "kind": "positional only",
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

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __suppress_context__

```json
{
  "name": "__suppress_context__",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __traceback__

```json
{
  "name": "__traceback__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### add_note

```json
{
  "name": "add_note",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, note, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "note",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Add a note to the exception
```

### args

```json
{
  "name": "args",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### characters_written

```json
{
  "name": "characters_written",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### errno

```json
{
  "name": "errno",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
POSIX exception code
```

### filename

```json
{
  "name": "filename",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
exception filename
```

### filename2

```json
{
  "name": "filename2",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
second exception filename
```

### strerror

```json
{
  "name": "strerror",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
exception strerror
```

### winerror

```json
{
  "name": "winerror",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
Win32 exception code
```

### with_traceback

```json
{
  "name": "with_traceback",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, tb, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "tb",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Set self.__traceback__ to tb and return self.
```

## Mapping

```json
{
  "name": "Mapping",
  "kind": "class",
  "origin": "collections.abc",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
A Mapping is a generic container for associating key/value
pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __iter__, and __len__.
```

### __abstractmethods__

```json
{
  "name": "__abstractmethods__",
  "kind": "frozenset",
  "decorators": [],
  "inherited": false
}
```

```text
Build an immutable unordered collection of unique elements.
```

### __annotate_func__

```json
{
  "name": "__annotate_func__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": false
}
```

```text
The type of the None singleton.
```

### __annotations_cache__

```json
{
  "name": "__annotations_cache__",
  "kind": "dict",
  "decorators": [],
  "inherited": false
}
```

```text
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __class_getitem__

```json
{
  "name": "__class_getitem__",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": true,
  "signature": "(origin, args, /)",
  "parameters": [
    {
      "name": "origin",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Represent a PEP 585 generic type

For example, for t = list[int], t.__origin__ is list and t.__args__
is (int,).
```

### __contains__

```json
{
  "name": "__contains__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key)",
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

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, other)",
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
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getitem__

```json
{
  "name": "__getitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key)",
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

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": false
}
```

```text
The type of the None singleton.
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __iter__

```json
{
  "name": "__iter__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __len__

```json
{
  "name": "__len__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __reversed__

```json
{
  "name": "__reversed__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": false
}
```

```text
The type of the None singleton.
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __slots__

```json
{
  "name": "__slots__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": true,
  "signature": "(cls, C)",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "C",
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

### _abc_impl

```json
{
  "name": "_abc_impl",
  "kind": "_abc_data",
  "decorators": [],
  "inherited": false
}
```

```text
Internal state held by ABC machinery.
```

### get

```json
{
  "name": "get",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key, default=None)",
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
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
```

### items

```json
{
  "name": "items",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
D.items() -> a set-like object providing a view on D's items
```

### keys

```json
{
  "name": "keys",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
D.keys() -> a set-like object providing a view on D's keys
```

### values

```json
{
  "name": "values",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
D.values() -> an object providing a view on D's values
```

## OrderedDict

```json
{
  "name": "OrderedDict",
  "kind": "class",
  "origin": "collections",
  "signature_error": "no signature found for builtin type <class 'collections.OrderedDict'>"
}
```

```text
Dictionary that remembers insertion order
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __class_getitem__

```json
{
  "name": "__class_getitem__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
dicts are generic over two types, signifying (respectively) the types of their keys and values
```

### __contains__

```json
{
  "name": "__contains__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
True if the dictionary has the specified key, else False.
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __delitem__

```json
{
  "name": "__delitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Delete self[key].
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
No docstring available.
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getitem__

```json
{
  "name": "__getitem__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self[key].
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": false
}
```

```text
The type of the None singleton.
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __ior__

```json
{
  "name": "__ior__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self|=value.
```

### __iter__

```json
{
  "name": "__iter__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement iter(self).
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __len__

```json
{
  "name": "__len__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return len(self).
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __or__

```json
{
  "name": "__or__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self|value.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return state information for pickling
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __reversed__

```json
{
  "name": "__reversed__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
od.__reversed__() <==> reversed(od)
```

### __ror__

```json
{
  "name": "__ror__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return value|self.
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setitem__

```json
{
  "name": "__setitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Set self[key] to value.
```

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return the size of the dict in memory, in bytes.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### clear

```json
{
  "name": "clear",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Remove all items from ordered dict.
```

### copy

```json
{
  "name": "copy",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
A shallow copy of ordered dict.
```

### fromkeys

```json
{
  "name": "fromkeys",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(type, /, iterable, value=None)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "iterable",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
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
Create a new ordered dictionary with keys from iterable and values set to value.
```

### get

```json
{
  "name": "get",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key, default=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "key",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "default",
      "kind": "positional only",
      "annotation": null,
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return the value for key if key is in the dictionary, else default.
```

### items

```json
{
  "name": "items",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a set-like object providing a view on the dict's items.
```

### keys

```json
{
  "name": "keys",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a set-like object providing a view on the dict's keys.
```

### move_to_end

```json
{
  "name": "move_to_end",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, key, last=True)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
      "name": "last",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Move an existing element to the end (or beginning if last is false).

Raise KeyError if the element does not exist.
```

### pop

```json
{
  "name": "pop",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'pop' of 'collections.OrderedDict' objects> builtin has invalid signature"
}
```

```text
od.pop(key[,default]) -> v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise,
raise a KeyError.
```

### popitem

```json
{
  "name": "popitem",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, last=True)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "last",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Remove and return a (key, value) pair from the dictionary.

Pairs are returned in LIFO order if last is true or FIFO order if
false.
```

### setdefault

```json
{
  "name": "setdefault",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, key, default=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.
```

### update

```json
{
  "name": "update",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "no signature found for builtin <method 'update' of 'collections.OrderedDict' objects>"
}
```

```text
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E is present and has a .keys() method, then does:  for k in E.keys(): D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]
```

### values

```json
{
  "name": "values",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return an object providing a view on the dict's values.
```

## PreparedRequest

```json
{
  "name": "PreparedRequest",
  "kind": "class",
  "origin": "requests.models",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
containing the exact bytes that will be sent to the server.

Instances are generated from a :class:`Request <Request>` object, and
should not be instantiated manually; doing so may produce undesirable
effects.

Usage::

  >>> import requests
  >>> req = requests.Request('GET', 'https://httpbin.org/get')
  >>> r = req.prepare()
  >>> r
  <PreparedRequest [GET]>

  >>> s = requests.Session()
  >>> s.send(r)
  <Response [200]>
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
dictionary for instance variables
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### _encode_files

```json
{
  "name": "_encode_files",
  "kind": "function",
  "decorators": [
    "staticmethod"
  ],
  "inherited": true,
  "signature": "(files, data)",
  "parameters": [
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "data",
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
Build the body for a multipart/form-data request.

Will successfully encode files when passed as a dict or a list of
tuples. Order is retained if data is a list of tuples but arbitrary
if parameters are supplied as a dict.
The tuples may be 2-tuples (filename, fileobj), 3-tuples (filename, fileobj, contentype)
or 4-tuples (filename, fileobj, contentype, custom_headers).
```

### _encode_params

```json
{
  "name": "_encode_params",
  "kind": "function",
  "decorators": [
    "staticmethod"
  ],
  "inherited": true,
  "signature": "(data)",
  "parameters": [
    {
      "name": "data",
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
Encode parameters in a piece of data.

Will successfully encode parameters when passed as a dict or a list of
2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
if parameters are supplied as a dict.
```

### _get_idna_encoded_host

```json
{
  "name": "_get_idna_encoded_host",
  "kind": "function",
  "decorators": [
    "staticmethod"
  ],
  "inherited": false,
  "signature": "(host)",
  "parameters": [
    {
      "name": "host",
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
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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

### deregister_hook

```json
{
  "name": "deregister_hook",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, event, hook)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "event",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hook",
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
Deregister a previously registered hook.
Returns True if the hook existed, False if not.
```

### path_url

```json
{
  "name": "path_url",
  "kind": "property",
  "decorators": [],
  "inherited": true
}
```

```text
Build the path URL to use.
```

### prepare

```json
{
  "name": "prepare",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "method",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "params",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "auth",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cookies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "json",
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
Prepares the entire request with the given parameters.
```

### prepare_auth

```json
{
  "name": "prepare_auth",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, auth, url='')",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "auth",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "''",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Prepares the given HTTP auth data.
```

### prepare_body

```json
{
  "name": "prepare_body",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, data, files, json=None)",
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
      "default": null,
      "required": true
    },
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "json",
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
Prepares the given HTTP body data.
```

### prepare_content_length

```json
{
  "name": "prepare_content_length",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, body)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "body",
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
Prepare Content-Length header based on request method and body
```

### prepare_cookies

```json
{
  "name": "prepare_cookies",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, cookies)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookies",
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
Prepares the given HTTP cookie data.

This function eventually generates a ``Cookie`` header from the
given cookies using cookielib. Due to cookielib's design, the header
will not be regenerated if it already exists, meaning this function
can only be called once for the life of the
:class:`PreparedRequest <PreparedRequest>` object. Any subsequent calls
to ``prepare_cookies`` will have no actual effect, unless the "Cookie"
header is removed beforehand.
```

### prepare_headers

```json
{
  "name": "prepare_headers",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, headers)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "headers",
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
Prepares the given HTTP headers.
```

### prepare_hooks

```json
{
  "name": "prepare_hooks",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, hooks)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hooks",
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
Prepares the given hooks.
```

### prepare_method

```json
{
  "name": "prepare_method",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, method)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "method",
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
Prepares the given HTTP method.
```

### prepare_url

```json
{
  "name": "prepare_url",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, params)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "params",
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
Prepares the given HTTP URL.
```

### register_hook

```json
{
  "name": "register_hook",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, event, hook)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "event",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hook",
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
Properly register a hook.
```

## REDIRECT_STATI

```json
{
  "name": "REDIRECT_STATI",
  "kind": "tuple",
  "origin": null
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

## Request

```json
{
  "name": "Request",
  "kind": "class",
  "origin": "requests.models",
  "signature": "(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)",
  "parameters": [
    {
      "name": "method",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "params",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "auth",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cookies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "json",
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
A user-created :class:`Request <Request>` object.

Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

:param method: HTTP method to use.
:param url: URL to send.
:param headers: dictionary of headers to send.
:param files: dictionary of {filename: fileobject} files to multipart upload.
:param data: the body to attach to the request. If a dictionary or
    list of tuples ``[(key, value)]`` is provided, form-encoding will
    take place.
:param json: json for the body to attach to the request (if files or data is not specified).
:param params: URL parameters to append to the URL. If a dictionary or
    list of tuples ``[(key, value)]`` is provided, form-encoding will
    take place.
:param auth: Auth handler or (user, pass) tuple.
:param cookies: dictionary or CookieJar of cookies to attach to this request.
:param hooks: dictionary of callback hooks, for internal usage.

Usage::

  >>> import requests
  >>> req = requests.Request('GET', 'https://httpbin.org/get')
  >>> req.prepare()
  <PreparedRequest [GET]>
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
dictionary for instance variables
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "method",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "params",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "auth",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cookies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "json",
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
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### deregister_hook

```json
{
  "name": "deregister_hook",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, event, hook)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "event",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hook",
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
Deregister a previously registered hook.
Returns True if the hook existed, False if not.
```

### prepare

```json
{
  "name": "prepare",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it.
```

### register_hook

```json
{
  "name": "register_hook",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, event, hook)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "event",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hook",
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
Properly register a hook.
```

## RequestsCookieJar

```json
{
  "name": "RequestsCookieJar",
  "kind": "class",
  "origin": "requests.cookies",
  "signature": "(policy=None)",
  "parameters": [
    {
      "name": "policy",
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
Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict
interface.

This is the CookieJar we create by default for requests and sessions that
don't specify one, since some clients may expect response.cookies and
session.cookies to support dict operations.

Requests does not use the dict interface internally; it's just for
compatibility with external client code. All requests code should work
out of the box with externally provided instances of ``CookieJar``, e.g.
``LWPCookieJar`` and ``FileCookieJar``.

Unlike a regular CookieJar, this class is pickleable.

.. warning:: dictionary operations that are normally O(1) may be O(n).
```

### _MutableMapping__marker

```json
{
  "name": "_MutableMapping__marker",
  "kind": "object",
  "decorators": [],
  "inherited": true
}
```

```text
The base class of the class hierarchy.

When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.
```

### __abstractmethods__

```json
{
  "name": "__abstractmethods__",
  "kind": "frozenset",
  "decorators": [],
  "inherited": false
}
```

```text
Build an immutable unordered collection of unique elements.
```

### __annotate_func__

```json
{
  "name": "__annotate_func__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": true
}
```

```text
The type of the None singleton.
```

### __annotations_cache__

```json
{
  "name": "__annotations_cache__",
  "kind": "dict",
  "decorators": [],
  "inherited": true
}
```

```text
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __class_getitem__

```json
{
  "name": "__class_getitem__",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": true,
  "signature": "(origin, args, /)",
  "parameters": [
    {
      "name": "origin",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Represent a PEP 585 generic type

For example, for t = list[int], t.__origin__ is list and t.__args__
is (int,).
```

### __contains__

```json
{
  "name": "__contains__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, name)",
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

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __delitem__

```json
{
  "name": "__delitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, name)",
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
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Deletes a cookie given a name. Wraps ``http.cookiejar.CookieJar``'s
``remove_cookie_by_name()``.
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
dictionary for instance variables
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, other)",
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
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getitem__

```json
{
  "name": "__getitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, name)",
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
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Dict-like __getitem__() for compatibility with client code. Throws
exception if there are more than one cookie with name. In that case,
use the more explicit get() method instead.

.. warning:: operation is O(n), not O(1).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Unlike a normal CookieJar, this class is pickleable.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": true
}
```

```text
The type of the None singleton.
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, policy=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "policy",
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
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __iter__

```json
{
  "name": "__iter__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __len__

```json
{
  "name": "__len__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
Return number of contained cookies.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
Return repr(self).
```

### __reversed__

```json
{
  "name": "__reversed__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": true
}
```

```text
The type of the None singleton.
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setitem__

```json
{
  "name": "__setitem__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, name, value)",
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
Dict-like __setitem__ for compatibility with client code. Throws
exception if there is already a cookie of that name in the jar. In that
case, use the more explicit set() method instead.
```

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, state)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "state",
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
Unlike a normal CookieJar, this class is pickleable.
```

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __slots__

```json
{
  "name": "__slots__",
  "kind": "tuple",
  "decorators": [],
  "inherited": true
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": true,
  "signature": "(cls, C)",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "C",
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

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### _abc_impl

```json
{
  "name": "_abc_impl",
  "kind": "_abc_data",
  "decorators": [],
  "inherited": false
}
```

```text
Internal state held by ABC machinery.
```

### _cookie_attrs

```json
{
  "name": "_cookie_attrs",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, cookies)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookies",
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
Return a list of cookie-attributes to be returned to server.

like ['foo="bar"; $Path="/"', ...]

The $Version attribute is also added when appropriate (currently only
once per request).
```

### _cookie_from_cookie_tuple

```json
{
  "name": "_cookie_from_cookie_tuple",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, tup, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "tup",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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

### _cookies_for_domain

```json
{
  "name": "_cookies_for_domain",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, domain, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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

### _cookies_for_request

```json
{
  "name": "_cookies_for_request",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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
Return a list of cookies to be returned to server.
```

### _cookies_from_attrs_set

```json
{
  "name": "_cookies_from_attrs_set",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, attrs_set, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "attrs_set",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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

### _find

```json
{
  "name": "_find",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, name, domain=None, path=None)",
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
      "default": null,
      "required": true
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Requests uses this method internally to get cookie values.

If there are conflicting cookies, _find arbitrarily chooses one.
See _find_no_duplicates if you want an exception thrown if there are
conflicting cookies.

:param name: a string containing name of cookie
:param domain: (optional) string containing domain of cookie
:param path: (optional) string containing path of cookie
:return: cookie.value
```

### _find_no_duplicates

```json
{
  "name": "_find_no_duplicates",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, name, domain=None, path=None)",
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
      "default": null,
      "required": true
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Both ``__get_item__`` and ``get`` call this function: it's never
used elsewhere in Requests.

:param name: a string containing name of cookie
:param domain: (optional) string containing domain of cookie
:param path: (optional) string containing path of cookie
:raises KeyError: if cookie is not found
:raises CookieConflictError: if there are multiple cookies
    that match name and optionally domain and path
:return: cookie.value
```

### _normalized_cookie_tuples

```json
{
  "name": "_normalized_cookie_tuples",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, attrs_set)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "attrs_set",
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
Return list of tuples containing normalised cookie information.

attrs_set is the list of lists of key,value pairs extracted from
the Set-Cookie or Set-Cookie2 headers.

Tuples are name, value, standard, rest, where name and value are the
cookie name and value, standard is a dictionary containing the standard
cookie-attributes (discard, secure, version, expires or max-age,
domain, path and port) and rest is a dictionary containing the rest of
the cookie-attributes.
```

### _process_rfc2109_cookies

```json
{
  "name": "_process_rfc2109_cookies",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, cookies)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookies",
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

### add_cookie_header

```json
{
  "name": "add_cookie_header",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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
Add correct Cookie: header to request (urllib.request.Request object).

The Cookie2 header is also added unless policy.hide_cookie2 is true.
```

### clear

```json
{
  "name": "clear",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, domain=None, path=None, name=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
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
Clear some cookies.

Invoking this method without arguments will clear all cookies.  If
given a single argument, only cookies belonging to that domain will be
removed.  If given two arguments, cookies belonging to the specified
path within that domain are removed.  If given three arguments, then
the cookie with the specified name, path and domain is removed.

Raises KeyError if no matching cookie exists.
```

### clear_expired_cookies

```json
{
  "name": "clear_expired_cookies",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
Discard all expired cookies.

You probably don't need to call this method: expired cookies are never
sent back to the server (provided you're using DefaultCookiePolicy),
this method is called by CookieJar itself every so often, and the
.save() method won't save expired cookies anyway (unless you ask
otherwise by passing a true ignore_expires argument).
```

### clear_session_cookies

```json
{
  "name": "clear_session_cookies",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
Discard all session cookies.

Note that the .save() method won't save session cookies anyway, unless
you ask otherwise by passing a true ignore_discard argument.
```

### copy

```json
{
  "name": "copy",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Return a copy of this RequestsCookieJar.
```

### domain_re

```json
{
  "name": "domain_re",
  "kind": "Pattern",
  "decorators": [],
  "inherited": true
}
```

```text
Compiled regular expression object.
```

### dots_re

```json
{
  "name": "dots_re",
  "kind": "Pattern",
  "decorators": [],
  "inherited": true
}
```

```text
Compiled regular expression object.
```

### extract_cookies

```json
{
  "name": "extract_cookies",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, response, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "response",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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
Extract cookies from response, where allowable given the request.
```

### get

```json
{
  "name": "get",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, name, default=None, domain=None, path=None)",
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
      "default": null,
      "required": true
    },
    {
      "name": "default",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Dict-like get() that also supports optional domain and path args in
order to resolve naming collisions from using one cookie jar over
multiple domains.

.. warning:: operation is O(n), not O(1).
```

### get_dict

```json
{
  "name": "get_dict",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, domain=None, path=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "domain",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "path",
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
Takes as an argument an optional domain and path and returns a plain
old Python dict of name-value pairs of cookies that meet the
requirements.

:rtype: dict
```

### get_policy

```json
{
  "name": "get_policy",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Return the CookiePolicy instance used.
```

### items

```json
{
  "name": "items",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Dict-like items() that returns a list of name-value tuples from the
jar. Allows client-code to call ``dict(RequestsCookieJar)`` and get a
vanilla python dict of key value pairs.

.. seealso:: keys() and values().
```

### iteritems

```json
{
  "name": "iteritems",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Dict-like iteritems() that returns an iterator of name-value tuples
from the jar.

.. seealso:: iterkeys() and itervalues().
```

### iterkeys

```json
{
  "name": "iterkeys",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Dict-like iterkeys() that returns an iterator of names of cookies
from the jar.

.. seealso:: itervalues() and iteritems().
```

### itervalues

```json
{
  "name": "itervalues",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Dict-like itervalues() that returns an iterator of values of cookies
from the jar.

.. seealso:: iterkeys() and iteritems().
```

### keys

```json
{
  "name": "keys",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Dict-like keys() that returns a list of names of cookies from the
jar.

.. seealso:: values() and items().
```

### list_domains

```json
{
  "name": "list_domains",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Utility method to list all the domains in the jar.
```

### list_paths

```json
{
  "name": "list_paths",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Utility method to list all the paths in the jar.
```

### magic_re

```json
{
  "name": "magic_re",
  "kind": "Pattern",
  "decorators": [],
  "inherited": true
}
```

```text
Compiled regular expression object.
```

### make_cookies

```json
{
  "name": "make_cookies",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, response, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "response",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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
Return sequence of Cookie objects extracted from response object.
```

### multiple_domains

```json
{
  "name": "multiple_domains",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Returns True if there are multiple domains in the jar.
Returns False otherwise.

:rtype: bool
```

### non_word_re

```json
{
  "name": "non_word_re",
  "kind": "Pattern",
  "decorators": [],
  "inherited": true
}
```

```text
Compiled regular expression object.
```

### pop

```json
{
  "name": "pop",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key, default=<object object at 0x000001F8742901D0>)",
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
      "default": "<object object at 0x000001F8742901D0>",
      "required": false
    }
  ],
  "returns": null
}
```

```text
D.pop(k[,d]) -> v, remove specified key and return the corresponding
value.  If key is not found, d is returned if given, otherwise
KeyError is raised.
```

### popitem

```json
{
  "name": "popitem",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self)",
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
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.
```

### quote_re

```json
{
  "name": "quote_re",
  "kind": "Pattern",
  "decorators": [],
  "inherited": true
}
```

```text
Compiled regular expression object.
```

### set

```json
{
  "name": "set",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, name, value, **kwargs)",
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
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Dict-like set() that also supports optional domain and path args in
order to resolve naming collisions from using one cookie jar over
multiple domains.
```

### set_cookie

```json
{
  "name": "set_cookie",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, cookie, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookie",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Set a cookie, without checking whether or not it should be set.
```

### set_cookie_if_ok

```json
{
  "name": "set_cookie_if_ok",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, cookie, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookie",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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
Set a cookie if policy says it's OK to do so.
```

### set_policy

```json
{
  "name": "set_policy",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, policy)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "policy",
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

### setdefault

```json
{
  "name": "setdefault",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, key, default=None)",
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
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
```

### strict_domain_re

```json
{
  "name": "strict_domain_re",
  "kind": "Pattern",
  "decorators": [],
  "inherited": true
}
```

```text
Compiled regular expression object.
```

### update

```json
{
  "name": "update",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, other)",
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
Updates this jar with cookies from another CookieJar or dict-like
```

### values

```json
{
  "name": "values",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Dict-like values() that returns a list of values of cookies from the
jar.

.. seealso:: keys() and items().
```

## Session

```json
{
  "name": "Session",
  "kind": "class",
  "origin": "requests.sessions",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
A Requests session.

Provides cookie persistence, connection-pooling, and configuration.

Basic Usage::

  >>> import requests
  >>> s = requests.Session()
  >>> s.get('https://httpbin.org/get')
  <Response [200]>

Or as a context manager::

  >>> with requests.Session() as s:
  ...     s.get('https://httpbin.org/get')
  <Response [200]>
```

### __attrs__

```json
{
  "name": "__attrs__",
  "kind": "list",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
dictionary for instance variables
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __enter__

```json
{
  "name": "__enter__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __exit__

```json
{
  "name": "__exit__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, *args)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
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

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, state)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "state",
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

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### close

```json
{
  "name": "close",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self)",
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
Closes all adapters and as such the session
```

### delete

```json
{
  "name": "delete",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Sends a DELETE request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response
```

### get

```json
{
  "name": "get",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Sends a GET request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response
```

### get_adapter

```json
{
  "name": "get_adapter",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
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
Returns the appropriate connection adapter for the given URL.

:rtype: requests.adapters.BaseAdapter
```

### get_redirect_target

```json
{
  "name": "get_redirect_target",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, resp)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "resp",
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
Receives a Response. Returns a redirect URI or ``None``
```

### head

```json
{
  "name": "head",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Sends a HEAD request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response
```

### merge_environment_settings

```json
{
  "name": "merge_environment_settings",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, proxies, stream, verify, cert)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "stream",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cert",
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
Check the environment and merge it with some settings.

:rtype: dict
```

### mount

```json
{
  "name": "mount",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, prefix, adapter)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prefix",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "adapter",
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
Registers a connection adapter to a prefix.

Adapters are sorted in descending order by prefix length.
```

### options

```json
{
  "name": "options",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Sends a OPTIONS request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response
```

### patch

```json
{
  "name": "patch",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, data=None, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
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
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Sends a PATCH request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response
```

### post

```json
{
  "name": "post",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, data=None, json=None, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
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
      "name": "json",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Sends a POST request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) json to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response
```

### prepare_request

```json
{
  "name": "prepare_request",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, request)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
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
Constructs a :class:`PreparedRequest <PreparedRequest>` for
transmission and returns it. The :class:`PreparedRequest` has settings
merged from the :class:`Request <Request>` instance and those of the
:class:`Session`.

:param request: :class:`Request` instance to prepare with this
    session's settings.
:rtype: requests.PreparedRequest
```

### put

```json
{
  "name": "put",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url, data=None, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
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
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Sends a PUT request. Returns :class:`Response` object.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:rtype: requests.Response
```

### rebuild_auth

```json
{
  "name": "rebuild_auth",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, prepared_request, response)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prepared_request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "response",
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
When being redirected we may want to strip authentication from the
request to avoid leaking credentials. This method intelligently removes
and reapplies authentication where possible to avoid credential loss.
```

### rebuild_method

```json
{
  "name": "rebuild_method",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, prepared_request, response)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prepared_request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "response",
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
When being redirected we may want to change the method of the request
based on certain specs or browser behavior.
```

### rebuild_proxies

```json
{
  "name": "rebuild_proxies",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, prepared_request, proxies)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prepared_request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
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
This method re-evaluates the proxy configuration by considering the
environment variables. If we are redirected to a URL covered by
NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
proxy keys for this URL (in case they were stripped by a previous
redirect).

This method also replaces the Proxy-Authorization header where
necessary.

:rtype: dict
```

### request

```json
{
  "name": "request",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "method",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "params",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cookies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "files",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "auth",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "timeout",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "allow_redirects",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    },
    {
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "stream",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "cert",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "json",
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
Constructs a :class:`Request <Request>`, prepares it and sends it.
Returns :class:`Response <Response>` object.

:param method: method for the new :class:`Request` object.
:param url: URL for the new :class:`Request` object.
:param params: (optional) Dictionary or bytes to be sent in the query
    string for the :class:`Request`.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) json to send in the body of the
    :class:`Request`.
:param headers: (optional) Dictionary of HTTP Headers to send with the
    :class:`Request`.
:param cookies: (optional) Dict or CookieJar object to send with the
    :class:`Request`.
:param files: (optional) Dictionary of ``'filename': file-like-objects``
    for multipart encoding upload.
:param auth: (optional) Auth tuple or callable to enable
    Basic/Digest/Custom HTTP Auth.
:param timeout: (optional) How long to wait for the server to send
    data before giving up, as a float, or a :ref:`(connect timeout,
    read timeout) <timeouts>` tuple.
:type timeout: float or tuple
:param allow_redirects: (optional) Set to True by default.
:type allow_redirects: bool
:param proxies: (optional) Dictionary mapping protocol or protocol and
    hostname to the URL of the proxy.
:param hooks: (optional) Dictionary mapping hook name to one event or
    list of events, event must be callable.
:param stream: (optional) whether to immediately download the response
    content. Defaults to ``False``.
:param verify: (optional) Either a boolean, in which case it controls whether we verify
    the server's TLS certificate, or a string, in which case it must be a path
    to a CA bundle to use. Defaults to ``True``. When set to
    ``False``, requests will accept any TLS certificate presented by
    the server, and will ignore hostname mismatches and/or expired
    certificates, which will make your application vulnerable to
    man-in-the-middle (MitM) attacks. Setting verify to ``False``
    may be useful during local development or testing.
:param cert: (optional) if String, path to ssl client cert file (.pem).
    If Tuple, ('cert', 'key') pair.
:rtype: requests.Response
```

### resolve_redirects

```json
{
  "name": "resolve_redirects",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "resp",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "req",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "stream",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "timeout",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    },
    {
      "name": "cert",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "yield_requests",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "adapter_kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Receives a Response. Returns a generator of Responses or Requests.
```

### send

```json
{
  "name": "send",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, request, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Send a given PreparedRequest.

:rtype: requests.Response
```

### should_strip_auth

```json
{
  "name": "should_strip_auth",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, old_url, new_url)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "old_url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "new_url",
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
Decide whether Authorization header should be removed when redirecting
```

## SessionRedirectMixin

```json
{
  "name": "SessionRedirectMixin",
  "kind": "class",
  "origin": "requests.sessions",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
No docstring available.
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
dictionary for instance variables
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "NoneType",
  "decorators": [],
  "inherited": false
}
```

```text
The type of the None singleton.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
list of weak references to the object
```

### get_redirect_target

```json
{
  "name": "get_redirect_target",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, resp)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "resp",
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
Receives a Response. Returns a redirect URI or ``None``
```

### rebuild_auth

```json
{
  "name": "rebuild_auth",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, prepared_request, response)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prepared_request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "response",
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
When being redirected we may want to strip authentication from the
request to avoid leaking credentials. This method intelligently removes
and reapplies authentication where possible to avoid credential loss.
```

### rebuild_method

```json
{
  "name": "rebuild_method",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, prepared_request, response)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prepared_request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "response",
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
When being redirected we may want to change the method of the request
based on certain specs or browser behavior.
```

### rebuild_proxies

```json
{
  "name": "rebuild_proxies",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, prepared_request, proxies)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prepared_request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
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
This method re-evaluates the proxy configuration by considering the
environment variables. If we are redirected to a URL covered by
NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
proxy keys for this URL (in case they were stripped by a previous
redirect).

This method also replaces the Proxy-Authorization header where
necessary.

:rtype: dict
```

### resolve_redirects

```json
{
  "name": "resolve_redirects",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "resp",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "req",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "stream",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "timeout",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    },
    {
      "name": "cert",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "yield_requests",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "adapter_kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Receives a Response. Returns a generator of Responses or Requests.
```

### should_strip_auth

```json
{
  "name": "should_strip_auth",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, old_url, new_url)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "old_url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "new_url",
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
Decide whether Authorization header should be removed when redirecting
```

## TooManyRedirects

```json
{
  "name": "TooManyRedirects",
  "kind": "class",
  "origin": "requests.exceptions",
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Too many redirects.
```

### __cause__

```json
{
  "name": "__cause__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __context__

```json
{
  "name": "__context__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dict__

```json
{
  "name": "__dict__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __firstlineno__

```json
{
  "name": "__firstlineno__",
  "kind": "int",
  "decorators": [],
  "inherited": false
}
```

```text
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating-point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer
iteral.
>>> int('0b100', base=0)
4
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize RequestException with `request` and `response` objects.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __module__

```json
{
  "name": "__module__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __setstate__

```json
{
  "name": "__setstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, state, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "state",
      "kind": "positional only",
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

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __static_attributes__

```json
{
  "name": "__static_attributes__",
  "kind": "tuple",
  "decorators": [],
  "inherited": false
}
```

```text
Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __suppress_context__

```json
{
  "name": "__suppress_context__",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __traceback__

```json
{
  "name": "__traceback__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### __weakref__

```json
{
  "name": "__weakref__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
list of weak references to the object
```

### add_note

```json
{
  "name": "add_note",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, note, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "note",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Add a note to the exception
```

### args

```json
{
  "name": "args",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### characters_written

```json
{
  "name": "characters_written",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
No docstring available.
```

### errno

```json
{
  "name": "errno",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
POSIX exception code
```

### filename

```json
{
  "name": "filename",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
exception filename
```

### filename2

```json
{
  "name": "filename2",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
second exception filename
```

### strerror

```json
{
  "name": "strerror",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
exception strerror
```

### winerror

```json
{
  "name": "winerror",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
Win32 exception code
```

### with_traceback

```json
{
  "name": "with_traceback",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, tb, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "tb",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Set self.__traceback__ to tb and return self.
```

## __builtins__

```json
{
  "name": "__builtins__",
  "kind": "dict",
  "origin": null
}
```

```text
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
    for k, v in iterable:
        d[k] = v
dict(**kwargs) -> new dictionary initialized with the name=value pairs
    in the keyword argument list.  For example:  dict(one=1, two=2)
```

## __cached__

```json
{
  "name": "__cached__",
  "kind": "str",
  "origin": null
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

## __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "origin": null
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

## __file__

```json
{
  "name": "__file__",
  "kind": "str",
  "origin": null
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

## __loader__

```json
{
  "name": "__loader__",
  "kind": "SourceFileLoader",
  "origin": "_frozen_importlib_external"
}
```

```text
Concrete implementation of SourceLoader using the file system.
```

## __name__

```json
{
  "name": "__name__",
  "kind": "str",
  "origin": null
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

## __package__

```json
{
  "name": "__package__",
  "kind": "str",
  "origin": null
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

## __spec__

```json
{
  "name": "__spec__",
  "kind": "ModuleSpec",
  "origin": "_frozen_importlib"
}
```

```text
The specification for a module, used for loading.

A module's spec is the source for information about the module.  For
data associated with the module, including source, use the spec's
loader.

`name` is the absolute name of the module.  `loader` is the loader
to use when loading the module.  `parent` is the name of the
package the module is in.  The parent is derived from the name.

`is_package` determines if the module is considered a package or
not.  On modules this is reflected by the `__path__` attribute.

`origin` is the specific location used by the loader from which to
load the module, if that information is available.  When filename is
set, origin will match.

`has_location` indicates that a spec's "origin" reflects a location.
When this is True, `__file__` attribute of the module is set.

`cached` is the location of the cached bytecode file, if any.  It
corresponds to the `__cached__` attribute.

`submodule_search_locations` is the sequence of path entries to
search when importing submodules.  If set, is_package should be
True--and False otherwise.

Packages are simply modules that (may) have submodules.  If a spec
has a non-None value in `submodule_search_locations`, the import
system will consider modules loaded from the spec as packages.

Only finders (see importlib.abc.MetaPathFinder and
importlib.abc.PathEntryFinder) should modify ModuleSpec instances.
```

## _basic_auth_str

```json
{
  "name": "_basic_auth_str",
  "kind": "function",
  "origin": "requests.auth",
  "signature": "(username, password)",
  "parameters": [
    {
      "name": "username",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "password",
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
Returns a Basic Auth string.
```

## codes

```json
{
  "name": "codes",
  "kind": "LookupDict",
  "origin": "requests.structures"
}
```

```text
Dictionary lookup object.
```

## cookiejar_from_dict

```json
{
  "name": "cookiejar_from_dict",
  "kind": "function",
  "origin": "requests.cookies",
  "signature": "(cookie_dict, cookiejar=None, overwrite=True)",
  "parameters": [
    {
      "name": "cookie_dict",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookiejar",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "overwrite",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Returns a CookieJar from a key/value dictionary.

:param cookie_dict: Dict of key/values to insert into CookieJar.
:param cookiejar: (optional) A cookiejar to add the cookies to.
:param overwrite: (optional) If False, will not replace cookies
    already in the jar with new ones.
:rtype: CookieJar
```

## cookielib

```json
{
  "name": "cookielib",
  "kind": "module",
  "origin": null
}
```

```text
HTTP cookie handling for web clients.

This module has (now fairly distant) origins in Gisle Aas' Perl module
HTTP::Cookies, from the libwww-perl library.

Docstrings, comments and debug strings in this code refer to the
attributes of the HTTP cookie system as cookie-attributes, to distinguish
them clearly from Python attributes.

Class diagram (note that BSDDBCookieJar and the MSIE* classes are not
distributed with the Python standard library, but are available from
http://wwwsearch.sf.net/):

                        CookieJar____
                        /     \      \
            FileCookieJar      \      \
             /    |   \         \      \
 MozillaCookieJar | LWPCookieJar \      \
                  |               |      \
                  |   ---MSIEBase |       \
                  |  /      |     |        \
                  | /   MSIEDBCookieJar BSDDBCookieJar
                  |/
               MSIECookieJar
```

## default_headers

```json
{
  "name": "default_headers",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
:rtype: requests.structures.CaseInsensitiveDict
```

## default_hooks

```json
{
  "name": "default_hooks",
  "kind": "function",
  "origin": "requests.hooks",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
No docstring available.
```

## dispatch_hook

```json
{
  "name": "dispatch_hook",
  "kind": "function",
  "origin": "requests.hooks",
  "signature": "(key, hooks, hook_data, **kwargs)",
  "parameters": [
    {
      "name": "key",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hook_data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Dispatches a hook dictionary on a given piece of data.
```

## extract_cookies_to_jar

```json
{
  "name": "extract_cookies_to_jar",
  "kind": "function",
  "origin": "requests.cookies",
  "signature": "(jar, request, response)",
  "parameters": [
    {
      "name": "jar",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "response",
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
Extract the cookies from the response into a CookieJar.

:param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)
:param request: our own requests.Request object
:param response: urllib3.HTTPResponse object
```

## get_auth_from_url

```json
{
  "name": "get_auth_from_url",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(url)",
  "parameters": [
    {
      "name": "url",
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
Given a url with authentication components, extract them into a tuple of
username,password.

:rtype: (str,str)
```

## get_environ_proxies

```json
{
  "name": "get_environ_proxies",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(url, no_proxy=None)",
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "no_proxy",
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
Return a dict of environment proxies.

:rtype: dict
```

## get_netrc_auth

```json
{
  "name": "get_netrc_auth",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(url, raise_errors=False)",
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "raise_errors",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Returns the Requests tuple auth for a given url from netrc.
```

## merge_cookies

```json
{
  "name": "merge_cookies",
  "kind": "function",
  "origin": "requests.cookies",
  "signature": "(cookiejar, cookies)",
  "parameters": [
    {
      "name": "cookiejar",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "cookies",
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
Add cookies to cookiejar and returns a merged CookieJar.

:param cookiejar: CookieJar object to add the cookies to.
:param cookies: Dictionary or CookieJar object to be added.
:rtype: CookieJar
```

## merge_hooks

```json
{
  "name": "merge_hooks",
  "kind": "function",
  "origin": "requests.sessions",
  "signature": "(request_hooks, session_hooks, dict_class=<class 'collections.OrderedDict'>)",
  "parameters": [
    {
      "name": "request_hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "session_hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "dict_class",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "<class 'collections.OrderedDict'>",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Properly merges both requests and session hooks.

This is necessary because when request_hooks == {'response': []}, the
merge breaks Session hooks entirely.
```

## merge_setting

```json
{
  "name": "merge_setting",
  "kind": "function",
  "origin": "requests.sessions",
  "signature": "(request_setting, session_setting, dict_class=<class 'collections.OrderedDict'>)",
  "parameters": [
    {
      "name": "request_setting",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "session_setting",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "dict_class",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "<class 'collections.OrderedDict'>",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Determines appropriate setting for a given request, taking into account
the explicit setting on that request, and the setting in the session. If a
setting is a dictionary, they will be merged together using `dict_class`
```

## os

```json
{
  "name": "os",
  "kind": "module",
  "origin": null
}
```

```text
OS routines for NT or Posix depending on what system we're on.

This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)

Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir), and leave all pathname manipulation to os.path
(e.g., split and join).
```

## preferred_clock

```json
{
  "name": "preferred_clock",
  "kind": "function",
  "origin": "time",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
perf_counter() -> float

Performance counter for benchmarking.
```

## requote_uri

```json
{
  "name": "requote_uri",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(uri)",
  "parameters": [
    {
      "name": "uri",
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
Re-quote the given URI.

This function passes the given URI through an unquote/quote cycle to
ensure that it is fully and consistently quoted.

:rtype: str
```

## resolve_proxies

```json
{
  "name": "resolve_proxies",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(request, proxies, trust_env=True)",
  "parameters": [
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "proxies",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "trust_env",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    }
  ],
  "returns": null
}
```

```text
This method takes proxy information from a request and configuration
input to resolve a mapping of target proxies. This will consider settings
such as NO_PROXY to strip proxy configurations.

:param request: Request or PreparedRequest
:param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
:param trust_env: Boolean declaring whether to trust environment configs

:rtype: dict
```

## rewind_body

```json
{
  "name": "rewind_body",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(prepared_request)",
  "parameters": [
    {
      "name": "prepared_request",
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
Move file pointer back to its recorded starting position
so it can be read again on redirect.
```

## session

```json
{
  "name": "session",
  "kind": "function",
  "origin": "requests.sessions",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
Returns a :class:`Session` for context-management.

.. deprecated:: 1.0.0

    This method has been deprecated since version 1.0.0 and is only kept for
    backwards compatibility. New code should use :class:`~requests.sessions.Session`
    to create a session. This may be removed at a future date.

:rtype: Session
```

## should_bypass_proxies

```json
{
  "name": "should_bypass_proxies",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(url, no_proxy)",
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "no_proxy",
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
Returns whether we should bypass proxies or not.

:rtype: bool
```

## sys

```json
{
  "name": "sys",
  "kind": "module",
  "origin": null
}
```

```text
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_exc - the last uncaught exception
  Only available in an interactive session after a
  traceback has been printed.
last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are the (deprecated) legacy representation of last_exc.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
_enablelegacywindowsfsencoding -- [Windows only]
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exception() -- return the current thread's active exception
exc_info() -- return information about the current thread's active exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
```

## time

```json
{
  "name": "time",
  "kind": "module",
  "origin": null
}
```

```text
This module provides various functions to manipulate time values.

There are two standard representations of time.  One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
or a floating-point number (to represent fractions of seconds).
The epoch is the point where the time starts, the return value of time.gmtime(0).
It is January 1, 1970, 00:00:00 (UTC) on all platforms.

The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (including century, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
If the DST flag is 0, the time is given in the regular time zone;
if it is 1, the time is given in the DST time zone;
if it is -1, mktime() should guess based on the date and time.
```

## timedelta

```json
{
  "name": "timedelta",
  "kind": "class",
  "origin": "datetime",
  "signature_error": "no signature found for builtin type <class 'datetime.timedelta'>"
}
```

```text
Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.
```

### __abs__

```json
{
  "name": "__abs__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
abs(self)
```

### __add__

```json
{
  "name": "__add__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self+value.
```

### __bool__

```json
{
  "name": "__bool__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
True if self else False
```

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
the object's class
```

### __delattr__

```json
{
  "name": "__delattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement delattr(self, name).
```

### __dir__

```json
{
  "name": "__dir__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default dir() implementation.
```

### __divmod__

```json
{
  "name": "__divmod__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return divmod(self, value).
```

### __doc__

```json
{
  "name": "__doc__",
  "kind": "str",
  "decorators": [],
  "inherited": false
}
```

```text
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.
```

### __eq__

```json
{
  "name": "__eq__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self==value.
```

### __floordiv__

```json
{
  "name": "__floordiv__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self//value.
```

### __format__

```json
{
  "name": "__format__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, format_spec, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "format_spec",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.
```

### __ge__

```json
{
  "name": "__ge__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>=value.
```

### __getattribute__

```json
{
  "name": "__getattribute__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return getattr(self, name).
```

### __getstate__

```json
{
  "name": "__getstate__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __gt__

```json
{
  "name": "__gt__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self>value.
```

### __hash__

```json
{
  "name": "__hash__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return hash(self).
```

### __init__

```json
{
  "name": "__init__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /, *args, **kwargs)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Initialize self.  See help(type(self)) for accurate signature.
```

### __init_subclass__

```json
{
  "name": "__init_subclass__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
This method is called when a class is subclassed.

The default implementation does nothing. It may be
overridden to extend subclasses.
```

### __le__

```json
{
  "name": "__le__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<=value.
```

### __lt__

```json
{
  "name": "__lt__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self<value.
```

### __mod__

```json
{
  "name": "__mod__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self%value.
```

### __mul__

```json
{
  "name": "__mul__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self*value.
```

### __ne__

```json
{
  "name": "__ne__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self!=value.
```

### __neg__

```json
{
  "name": "__neg__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
-self
```

### __new__

```json
{
  "name": "__new__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(*args, **kwargs)",
  "parameters": [
    {
      "name": "args",
      "kind": "var positional",
      "annotation": null,
      "default": null,
      "required": false
    },
    {
      "name": "kwargs",
      "kind": "var keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Create and return a new object.  See help(type) for accurate signature.
```

### __pos__

```json
{
  "name": "__pos__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
+self
```

### __radd__

```json
{
  "name": "__radd__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return value+self.
```

### __rdivmod__

```json
{
  "name": "__rdivmod__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return divmod(value, self).
```

### __reduce__

```json
{
  "name": "__reduce__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
__reduce__() -> (cls, state)
```

### __reduce_ex__

```json
{
  "name": "__reduce_ex__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, protocol, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "protocol",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Helper for pickle.
```

### __repr__

```json
{
  "name": "__repr__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return repr(self).
```

### __rfloordiv__

```json
{
  "name": "__rfloordiv__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return value//self.
```

### __rmod__

```json
{
  "name": "__rmod__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return value%self.
```

### __rmul__

```json
{
  "name": "__rmul__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return value*self.
```

### __rsub__

```json
{
  "name": "__rsub__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return value-self.
```

### __rtruediv__

```json
{
  "name": "__rtruediv__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return value/self.
```

### __setattr__

```json
{
  "name": "__setattr__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, name, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Implement setattr(self, name, value).
```

### __sizeof__

```json
{
  "name": "__sizeof__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Size of object in memory, in bytes.
```

### __str__

```json
{
  "name": "__str__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return str(self).
```

### __sub__

```json
{
  "name": "__sub__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self-value.
```

### __subclasshook__

```json
{
  "name": "__subclasshook__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, object, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "object",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__().
It should return True, False or NotImplemented.  If it returns
NotImplemented, the normal algorithm is used.  Otherwise, it
overrides the normal algorithm (and the outcome is cached).
```

### __truediv__

```json
{
  "name": "__truediv__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return self/value.
```

### days

```json
{
  "name": "days",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
Number of days.
```

### max

```json
{
  "name": "max",
  "kind": "timedelta",
  "decorators": [],
  "inherited": false
}
```

```text
Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.
```

### microseconds

```json
{
  "name": "microseconds",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
Number of microseconds (>= 0 and less than 1 second).
```

### min

```json
{
  "name": "min",
  "kind": "timedelta",
  "decorators": [],
  "inherited": false
}
```

```text
Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.
```

### resolution

```json
{
  "name": "resolution",
  "kind": "timedelta",
  "decorators": [],
  "inherited": false
}
```

```text
Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.
```

### seconds

```json
{
  "name": "seconds",
  "kind": "member_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
Number of seconds (>= 0 and less than 1 day).
```

### total_seconds

```json
{
  "name": "total_seconds",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Total seconds in the duration.
```

## to_key_val_list

```json
{
  "name": "to_key_val_list",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(value)",
  "parameters": [
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

## to_native_string

```json
{
  "name": "to_native_string",
  "kind": "function",
  "origin": "requests._internal_utils",
  "signature": "(string, encoding='ascii')",
  "parameters": [
    {
      "name": "string",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "encoding",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'ascii'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Given a string object, regardless of type, returns a representation of
that string in the native string type, encoding and decoding where
necessary. This assumes ASCII unless told otherwise.
```

## urljoin

```json
{
  "name": "urljoin",
  "kind": "function",
  "origin": "urllib.parse",
  "signature": "(base, url, allow_fragments=True)",
  "parameters": [
    {
      "name": "base",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "allow_fragments",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Join a base URL and a possibly relative URL to form an absolute
interpretation of the latter.
```

## urlparse

```json
{
  "name": "urlparse",
  "kind": "function",
  "origin": "urllib.parse",
  "signature": "(url, scheme='', allow_fragments=True)",
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "scheme",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "''",
      "required": false
    },
    {
      "name": "allow_fragments",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "True",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Parse a URL into 6 components:
<scheme>://<netloc>/<path>;<params>?<query>#<fragment>

The result is a named 6-tuple with fields corresponding to the
above. It is either a ParseResult or ParseResultBytes object,
depending on the type of the url parameter.

The username, password, hostname, and port sub-components of netloc
can also be accessed as attributes of the returned object.

The scheme argument provides the default value of the scheme
component when no scheme is found in url.

If allow_fragments is False, no attempt is made to separate the
fragment component from the previous component, which can be either
path or query.

Note that % escapes are not expanded.

urlsplit() should generally be used instead of urlparse().
```
