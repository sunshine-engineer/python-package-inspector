# Runtime: requests.adapters

```text
requests.adapters
~~~~~~~~~~~~~~~~~

This module contains the transport adapters that Requests uses to define
and maintain connections.
```

## BaseAdapter

```json
{
  "name": "BaseAdapter",
  "kind": "class",
  "origin": "requests.adapters",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
The Base Transport Adapter
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
Cleans up adapter specific items.
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
:type timeout: float or tuple
:param verify: (optional) Either a boolean, in which case it controls whether we verify
    the server's TLS certificate, or a string, in which case it must be a path
    to a CA bundle to use
:param cert: (optional) Any user-provided SSL certificate to be trusted.
:param proxies: (optional) The proxies dictionary to apply to the request.
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
  "signature": "(self, key, default=<object object at 0x0000027593C501D0>)",
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
      "default": "<object object at 0x0000027593C501D0>",
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

## ClosedPoolError

```json
{
  "name": "ClosedPoolError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature": "(pool: 'ConnectionPool', message: 'str') -> 'None'",
  "parameters": [
    {
      "name": "pool",
      "kind": "positional or keyword",
      "annotation": "'ConnectionPool'",
      "default": null,
      "required": true
    },
    {
      "name": "message",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
}
```

```text
Raised when a request enters a pool after the pool has been closed.
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
  "signature": "(self, pool: 'ConnectionPool', message: 'str') -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pool",
      "kind": "positional or keyword",
      "annotation": "'ConnectionPool'",
      "default": null,
      "required": true
    },
    {
      "name": "message",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
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
  "signature": "(self) -> '_TYPE_REDUCE_RESULT'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'_TYPE_REDUCE_RESULT'"
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

## ConnectTimeout

```json
{
  "name": "ConnectTimeout",
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
The request timed out while trying to connect to the remote server.

Requests that produced this error are safe to retry.
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

## ConnectTimeoutError

```json
{
  "name": "ConnectTimeoutError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature_error": "no signature found for builtin type <class 'urllib3.exceptions.ConnectTimeoutError'>"
}
```

```text
Raised when a socket timeout occurs while connecting to a server
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

## ConnectionError

```json
{
  "name": "ConnectionError",
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
A Connection error occurred.
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

## DEFAULT_CA_BUNDLE_PATH

```json
{
  "name": "DEFAULT_CA_BUNDLE_PATH",
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

## DEFAULT_POOLBLOCK

```json
{
  "name": "DEFAULT_POOLBLOCK",
  "kind": "bool",
  "origin": null
}
```

```text
Returns True when the argument is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.
```

## DEFAULT_POOLSIZE

```json
{
  "name": "DEFAULT_POOLSIZE",
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

## DEFAULT_POOL_TIMEOUT

```json
{
  "name": "DEFAULT_POOL_TIMEOUT",
  "kind": "NoneType",
  "origin": null
}
```

```text
The type of the None singleton.
```

## DEFAULT_RETRIES

```json
{
  "name": "DEFAULT_RETRIES",
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

## InvalidHeader

```json
{
  "name": "InvalidHeader",
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
The header value provided was somehow invalid.
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

## InvalidProxyURL

```json
{
  "name": "InvalidProxyURL",
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
The proxy URL provided is invalid.
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

## InvalidURL

```json
{
  "name": "InvalidURL",
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
The URL provided was somehow invalid.
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

## LocationValueError

```json
{
  "name": "LocationValueError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature_error": "no signature found for builtin type <class 'urllib3.exceptions.LocationValueError'>"
}
```

```text
Raised when there is something wrong with a given URL input.
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
  "inherited": false
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

## MaxRetryError

```json
{
  "name": "MaxRetryError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature": "(pool: 'ConnectionPool', url: 'str | None', reason: 'Exception | None' = None) -> 'None'",
  "parameters": [
    {
      "name": "pool",
      "kind": "positional or keyword",
      "annotation": "'ConnectionPool'",
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "reason",
      "kind": "positional or keyword",
      "annotation": "'Exception | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'None'"
}
```

```text
Raised when the maximum number of retries is exceeded.

:param pool: The connection pool
:type pool: :class:`~urllib3.connectionpool.HTTPConnectionPool`
:param str url: The requested Url
:param reason: The underlying error
:type reason: :class:`Exception`
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
  "inherited": false,
  "signature": "(self, pool: 'ConnectionPool', url: 'str | None', reason: 'Exception | None' = None) -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pool",
      "kind": "positional or keyword",
      "annotation": "'ConnectionPool'",
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "reason",
      "kind": "positional or keyword",
      "annotation": "'Exception | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'None'"
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
  "inherited": false,
  "signature": "(self) -> '_TYPE_REDUCE_RESULT'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'_TYPE_REDUCE_RESULT'"
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

## NewConnectionError

```json
{
  "name": "NewConnectionError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature": "(conn: 'HTTPConnection', message: 'str') -> 'None'",
  "parameters": [
    {
      "name": "conn",
      "kind": "positional or keyword",
      "annotation": "'HTTPConnection'",
      "default": null,
      "required": true
    },
    {
      "name": "message",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
}
```

```text
Raised when we fail to establish a new connection. Usually ECONNREFUSED.
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
  "inherited": false,
  "signature": "(self, conn: 'HTTPConnection', message: 'str') -> 'None'",
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
      "annotation": "'HTTPConnection'",
      "default": null,
      "required": true
    },
    {
      "name": "message",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
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
  "inherited": false,
  "signature": "(self) -> '_TYPE_REDUCE_RESULT'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'_TYPE_REDUCE_RESULT'"
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

### pool

```json
{
  "name": "pool",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
No docstring available.
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

## PoolManager

```json
{
  "name": "PoolManager",
  "kind": "class",
  "origin": "urllib3.poolmanager",
  "signature": "(num_pools: 'int' = 10, headers: 'typing.Mapping[str, str] | None' = None, **connection_pool_kw: 'typing.Any') -> 'None'",
  "parameters": [
    {
      "name": "num_pools",
      "kind": "positional or keyword",
      "annotation": "'int'",
      "default": "10",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": "'typing.Mapping[str, str] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "connection_pool_kw",
      "kind": "var keyword",
      "annotation": "'typing.Any'",
      "default": null,
      "required": false
    }
  ],
  "returns": "'None'"
}
```

```text
Allows for arbitrary requests while transparently keeping track of
necessary connection pools for you.

:param num_pools:
    Number of connection pools to cache before discarding the least
    recently used pool.

:param headers:
    Headers to include with all requests, unless other headers are given
    explicitly.

:param \**connection_pool_kw:
    Additional parameters are used to create fresh
    :class:`urllib3.connectionpool.ConnectionPool` instances.

Example:

.. code-block:: python

    import urllib3

    http = urllib3.PoolManager(num_pools=2)

    resp1 = http.request("GET", "https://google.com/")
    resp2 = http.request("GET", "https://google.com/mail")
    resp3 = http.request("GET", "https://yahoo.com/")

    print(len(http.pools))
    # 2
```

### __annotations__

```json
{
  "name": "__annotations__",
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
  "signature": "(self) -> 'Self'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'Self'"
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
  "signature": "(self, exc_type: 'type[BaseException] | None', exc_val: 'BaseException | None', exc_tb: 'TracebackType | None') -> 'typing.Literal[False]'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "exc_type",
      "kind": "positional or keyword",
      "annotation": "'type[BaseException] | None'",
      "default": null,
      "required": true
    },
    {
      "name": "exc_val",
      "kind": "positional or keyword",
      "annotation": "'BaseException | None'",
      "default": null,
      "required": true
    },
    {
      "name": "exc_tb",
      "kind": "positional or keyword",
      "annotation": "'TracebackType | None'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'typing.Literal[False]'"
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
  "signature": "(self, num_pools: 'int' = 10, headers: 'typing.Mapping[str, str] | None' = None, **connection_pool_kw: 'typing.Any') -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "num_pools",
      "kind": "positional or keyword",
      "annotation": "'int'",
      "default": "10",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": "'typing.Mapping[str, str] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "connection_pool_kw",
      "kind": "var keyword",
      "annotation": "'typing.Any'",
      "default": null,
      "required": false
    }
  ],
  "returns": "'None'"
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
  "inherited": true
}
```

```text
list of weak references to the object
```

### _encode_url_methods

```json
{
  "name": "_encode_url_methods",
  "kind": "set",
  "decorators": [],
  "inherited": true
}
```

```text
Build an unordered collection of unique elements.
```

### _merge_pool_kwargs

```json
{
  "name": "_merge_pool_kwargs",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, override: 'dict[str, typing.Any] | None') -> 'dict[str, typing.Any]'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "override",
      "kind": "positional or keyword",
      "annotation": "'dict[str, typing.Any] | None'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'dict[str, typing.Any]'"
}
```

```text
Merge a dictionary of override values for self.connection_pool_kw.

This does not modify self.connection_pool_kw and returns a new dict.
Any keys in the override dictionary with a value of ``None`` are
removed from the merged dictionary.
```

### _new_pool

```json
{
  "name": "_new_pool",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, scheme: 'str', host: 'str', port: 'int', request_context: 'dict[str, typing.Any] | None' = None) -> 'HTTPConnectionPool'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "scheme",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "host",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "port",
      "kind": "positional or keyword",
      "annotation": "'int'",
      "default": null,
      "required": true
    },
    {
      "name": "request_context",
      "kind": "positional or keyword",
      "annotation": "'dict[str, typing.Any] | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'HTTPConnectionPool'"
}
```

```text
Create a new :class:`urllib3.connectionpool.ConnectionPool` based on host, port, scheme, and
any additional pool keyword arguments.

If ``request_context`` is provided, it is provided as keyword arguments
to the pool class used. This method is used to actually create the
connection pools handed out by :meth:`connection_from_url` and
companion methods. It is intended to be overridden for customization.
```

### _proxy_requires_url_absolute_form

```json
{
  "name": "_proxy_requires_url_absolute_form",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, parsed_url: 'Url') -> 'bool'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "parsed_url",
      "kind": "positional or keyword",
      "annotation": "'Url'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'bool'"
}
```

```text
Indicates if the proxy requires the complete destination URL in the
request.  Normally this is only needed when not using an HTTP CONNECT
tunnel.
```

### clear

```json
{
  "name": "clear",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self) -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
}
```

```text
Empty our store of pools and direct them all to close.

This will not affect in-flight connections, but they will not be
re-used after completion.
```

### connection_from_context

```json
{
  "name": "connection_from_context",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, request_context: 'dict[str, typing.Any]') -> 'HTTPConnectionPool'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "request_context",
      "kind": "positional or keyword",
      "annotation": "'dict[str, typing.Any]'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'HTTPConnectionPool'"
}
```

```text
Get a :class:`urllib3.connectionpool.ConnectionPool` based on the request context.

``request_context`` must at least contain the ``scheme`` key and its
value must be a key in ``key_fn_by_scheme`` instance variable.
```

### connection_from_host

```json
{
  "name": "connection_from_host",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, host: 'str | None', port: 'int | None' = None, scheme: 'str | None' = 'http', pool_kwargs: 'dict[str, typing.Any] | None' = None) -> 'HTTPConnectionPool'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "host",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "port",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "scheme",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": "'http'",
      "required": false
    },
    {
      "name": "pool_kwargs",
      "kind": "positional or keyword",
      "annotation": "'dict[str, typing.Any] | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'HTTPConnectionPool'"
}
```

```text
Get a :class:`urllib3.connectionpool.ConnectionPool` based on the host, port, and scheme.

If ``port`` isn't given, it will be derived from the ``scheme`` using
``urllib3.connectionpool.port_by_scheme``. If ``pool_kwargs`` is
provided, it is merged with the instance's ``connection_pool_kw``
variable and used to create the new connection pool, if one is
needed.
```

### connection_from_pool_key

```json
{
  "name": "connection_from_pool_key",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, pool_key: 'PoolKey', request_context: 'dict[str, typing.Any]') -> 'HTTPConnectionPool'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pool_key",
      "kind": "positional or keyword",
      "annotation": "'PoolKey'",
      "default": null,
      "required": true
    },
    {
      "name": "request_context",
      "kind": "positional or keyword",
      "annotation": "'dict[str, typing.Any]'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'HTTPConnectionPool'"
}
```

```text
Get a :class:`urllib3.connectionpool.ConnectionPool` based on the provided pool key.

``pool_key`` should be a namedtuple that only contains immutable
objects. At a minimum it must have the ``scheme``, ``host``, and
``port`` fields.
```

### connection_from_url

```json
{
  "name": "connection_from_url",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, url: 'str', pool_kwargs: 'dict[str, typing.Any] | None' = None) -> 'HTTPConnectionPool'",
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
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "pool_kwargs",
      "kind": "positional or keyword",
      "annotation": "'dict[str, typing.Any] | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'HTTPConnectionPool'"
}
```

```text
Similar to :func:`urllib3.connectionpool.connection_from_url`.

If ``pool_kwargs`` is not provided and a new pool needs to be
constructed, ``self.connection_pool_kw`` is used to initialize
the :class:`urllib3.connectionpool.ConnectionPool`. If ``pool_kwargs``
is provided, it is used instead. Note that if a new pool does not
need to be created for the request, the provided ``pool_kwargs`` are
not used.
```

### proxy

```json
{
  "name": "proxy",
  "kind": "NoneType",
  "decorators": [],
  "inherited": false
}
```

```text
The type of the None singleton.
```

### proxy_config

```json
{
  "name": "proxy_config",
  "kind": "NoneType",
  "decorators": [],
  "inherited": false
}
```

```text
The type of the None singleton.
```

### request

```json
{
  "name": "request",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, method: 'str', url: 'str', body: '_TYPE_BODY | None' = None, fields: '_TYPE_FIELDS | None' = None, headers: 'typing.Mapping[str, str] | None' = None, json: 'typing.Any | None' = None, **urlopen_kw: 'typing.Any') -> 'BaseHTTPResponse'",
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
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "body",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_BODY | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "fields",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_FIELDS | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": "'typing.Mapping[str, str] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "json",
      "kind": "positional or keyword",
      "annotation": "'typing.Any | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "urlopen_kw",
      "kind": "var keyword",
      "annotation": "'typing.Any'",
      "default": null,
      "required": false
    }
  ],
  "returns": "'BaseHTTPResponse'"
}
```

```text
Make a request using :meth:`urlopen` with the appropriate encoding of
``fields`` based on the ``method`` used.

This is a convenience method that requires the least amount of manual
effort. It can be used in most situations, while still having the
option to drop down to more specific methods when necessary, such as
:meth:`request_encode_url`, :meth:`request_encode_body`,
or even the lowest level :meth:`urlopen`.

:param method:
    HTTP request method (such as GET, POST, PUT, etc.)

:param url:
    The URL to perform the request on.

:param body:
    Data to send in the request body, either :class:`str`, :class:`bytes`,
    an iterable of :class:`str`/:class:`bytes`, or a file-like object.

:param fields:
    Data to encode and send in the URL or request body, depending on ``method``.

:param headers:
    Dictionary of custom headers to send, such as User-Agent,
    If-None-Match, etc. If None, pool headers are used. If provided,
    these headers completely replace any pool-specific headers.

:param json:
    Data to encode and send as JSON with UTF-encoded in the request body.
    The ``"Content-Type"`` header will be set to ``"application/json"``
    unless specified otherwise.
```

### request_encode_body

```json
{
  "name": "request_encode_body",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, method: 'str', url: 'str', fields: '_TYPE_FIELDS | None' = None, headers: 'typing.Mapping[str, str] | None' = None, encode_multipart: 'bool' = True, multipart_boundary: 'str | None' = None, **urlopen_kw: 'str') -> 'BaseHTTPResponse'",
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
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "fields",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_FIELDS | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": "'typing.Mapping[str, str] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "encode_multipart",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "True",
      "required": false
    },
    {
      "name": "multipart_boundary",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "urlopen_kw",
      "kind": "var keyword",
      "annotation": "'str'",
      "default": null,
      "required": false
    }
  ],
  "returns": "'BaseHTTPResponse'"
}
```

```text
Make a request using :meth:`urlopen` with the ``fields`` encoded in
the body. This is useful for request methods like POST, PUT, PATCH, etc.

When ``encode_multipart=True`` (default), then
:func:`urllib3.encode_multipart_formdata` is used to encode
the payload with the appropriate content type. Otherwise
:func:`urllib.parse.urlencode` is used with the
'application/x-www-form-urlencoded' content type.

Multipart encoding must be used when posting files, and it's reasonably
safe to use it in other times too. However, it may break request
signing, such as with OAuth.

Supports an optional ``fields`` parameter of key/value strings AND
key/filetuple. A filetuple is a (filename, data, MIME type) tuple where
the MIME type is optional. For example::

    fields = {
        'foo': 'bar',
        'fakefile': ('foofile.txt', 'contents of foofile'),
        'realfile': ('barfile.txt', open('realfile').read()),
        'typedfile': ('bazfile.bin', open('bazfile').read(),
                      'image/jpeg'),
        'nonamefile': 'contents of nonamefile field',
    }

When uploading a file, providing a filename (the first parameter of the
tuple) is optional but recommended to best mimic behavior of browsers.

Note that if ``headers`` are supplied, the 'Content-Type' header will
be overwritten because it depends on the dynamic random boundary string
which is used to compose the body of the request. The random boundary
string can be explicitly set with the ``multipart_boundary`` parameter.

:param method:
    HTTP request method (such as GET, POST, PUT, etc.)

:param url:
    The URL to perform the request on.

:param fields:
    Data to encode and send in the request body.

:param headers:
    Dictionary of custom headers to send, such as User-Agent,
    If-None-Match, etc. If None, pool headers are used. If provided,
    these headers completely replace any pool-specific headers.

:param encode_multipart:
    If True, encode the ``fields`` using the multipart/form-data MIME
    format.

:param multipart_boundary:
    If not specified, then a random boundary will be generated using
    :func:`urllib3.filepost.choose_boundary`.
```

### request_encode_url

```json
{
  "name": "request_encode_url",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, method: 'str', url: 'str', fields: '_TYPE_ENCODE_URL_FIELDS | None' = None, headers: 'typing.Mapping[str, str] | None' = None, **urlopen_kw: 'str') -> 'BaseHTTPResponse'",
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
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "fields",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_ENCODE_URL_FIELDS | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "headers",
      "kind": "positional or keyword",
      "annotation": "'typing.Mapping[str, str] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "urlopen_kw",
      "kind": "var keyword",
      "annotation": "'str'",
      "default": null,
      "required": false
    }
  ],
  "returns": "'BaseHTTPResponse'"
}
```

```text
Make a request using :meth:`urlopen` with the ``fields`` encoded in
the url. This is useful for request methods like GET, HEAD, DELETE, etc.

:param method:
    HTTP request method (such as GET, POST, PUT, etc.)

:param url:
    The URL to perform the request on.

:param fields:
    Data to encode and send in the URL.

:param headers:
    Dictionary of custom headers to send, such as User-Agent,
    If-None-Match, etc. If None, pool headers are used. If provided,
    these headers completely replace any pool-specific headers.
```

### urlopen

```json
{
  "name": "urlopen",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, method: 'str', url: 'str', redirect: 'bool' = True, **kw: 'typing.Any') -> 'BaseHTTPResponse'",
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
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "redirect",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "True",
      "required": false
    },
    {
      "name": "kw",
      "kind": "var keyword",
      "annotation": "'typing.Any'",
      "default": null,
      "required": false
    }
  ],
  "returns": "'BaseHTTPResponse'"
}
```

```text
Same as :meth:`urllib3.HTTPConnectionPool.urlopen`
with custom cross-host redirect logic and only sends the request-uri
portion of the ``url``.

The given ``url`` parameter must be absolute, such that an appropriate
:class:`urllib3.connectionpool.ConnectionPool` can be chosen for it.
```

## ProtocolError

```json
{
  "name": "ProtocolError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature_error": "no signature found for builtin type <class 'urllib3.exceptions.ProtocolError'>"
}
```

```text
Raised when something unexpected happens mid-request/response.
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

## ProxyError

```json
{
  "name": "ProxyError",
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
A proxy error occurred.
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

## ReadTimeout

```json
{
  "name": "ReadTimeout",
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
The server did not send any data in the allotted amount of time.
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

## ReadTimeoutError

```json
{
  "name": "ReadTimeoutError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature": "(pool: 'ConnectionPool', url: 'str | None', message: 'str') -> 'None'",
  "parameters": [
    {
      "name": "pool",
      "kind": "positional or keyword",
      "annotation": "'ConnectionPool'",
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "message",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
}
```

```text
Raised when a socket timeout occurs while receiving data from a server
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
  "signature": "(self, pool: 'ConnectionPool', url: 'str | None', message: 'str') -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pool",
      "kind": "positional or keyword",
      "annotation": "'ConnectionPool'",
      "default": null,
      "required": true
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "message",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
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
  "signature": "(self) -> '_TYPE_REDUCE_RESULT'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'_TYPE_REDUCE_RESULT'"
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

## Response

```json
{
  "name": "Response",
  "kind": "class",
  "origin": "requests.models",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
The :class:`Response <Response>` object, which contains a
server's response to an HTTP request.
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

### __bool__

```json
{
  "name": "__bool__",
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
Returns True if :attr:`status_code` is less than 400.

This attribute checks if the status code of the response is between
400 and 600 to see if there was a client error or a server error. If
the status code, is between 200 and 400, this will return True. This
is **not** a check to see if the response code is ``200 OK``.
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
Allows you to use a response as an iterator.
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

### __nonzero__

```json
{
  "name": "__nonzero__",
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
Returns True if :attr:`status_code` is less than 400.

This attribute checks if the status code of the response is between
400 and 600 to see if there was a client error or a server error. If
the status code, is between 200 and 400, this will return True. This
is **not** a check to see if the response code is ``200 OK``.
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
  "inherited": false
}
```

```text
list of weak references to the object
```

### apparent_encoding

```json
{
  "name": "apparent_encoding",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
The apparent encoding, provided by the charset_normalizer or chardet libraries.
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
Releases the connection back to the pool. Once this method has been
called the underlying ``raw`` object must not be accessed again.

*Note: Should not normally need to be called explicitly.*
```

### content

```json
{
  "name": "content",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
Content of the response, in bytes.
```

### is_permanent_redirect

```json
{
  "name": "is_permanent_redirect",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
True if this Response one of the permanent versions of redirect.
```

### is_redirect

```json
{
  "name": "is_redirect",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
True if this Response is a well-formed HTTP redirect that could have
been processed automatically (by :meth:`Session.resolve_redirects`).
```

### iter_content

```json
{
  "name": "iter_content",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, chunk_size=1, decode_unicode=False)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chunk_size",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "1",
      "required": false
    },
    {
      "name": "decode_unicode",
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
Iterates over the response data.  When stream=True is set on the
request, this avoids reading the content at once into memory for
large responses.  The chunk size is the number of bytes it should
read into memory.  This is not necessarily the length of each item
returned as decoding can take place.

chunk_size must be of type int or None. A value of None will
function differently depending on the value of `stream`.
stream=True will read data as it arrives in whatever size the
chunks are received. If stream=False, data is returned as
a single chunk.

If decode_unicode is True, content will be decoded using the best
available encoding based on the response.
```

### iter_lines

```json
{
  "name": "iter_lines",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, chunk_size=512, decode_unicode=False, delimiter=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chunk_size",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "512",
      "required": false
    },
    {
      "name": "decode_unicode",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "delimiter",
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
Iterates over the response data, one line at a time.  When
stream=True is set on the request, this avoids reading the
content at once into memory for large responses.

.. note:: This method is not reentrant safe.
```

### json

```json
{
  "name": "json",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, **kwargs)",
  "parameters": [
    {
      "name": "self",
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
Returns the json-encoded content of a response, if any.

:param \*\*kwargs: Optional arguments that ``json.loads`` takes.
:raises requests.exceptions.JSONDecodeError: If the response body does not
    contain valid json.
```

### links

```json
{
  "name": "links",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
Returns the parsed header links of the response, if any.
```

### next

```json
{
  "name": "next",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
Returns a PreparedRequest for the next request in a redirect chain, if there is one.
```

### ok

```json
{
  "name": "ok",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
Returns True if :attr:`status_code` is less than 400, False if not.

This attribute checks if the status code of the response is between
400 and 600 to see if there was a client error or a server error. If
the status code is between 200 and 400, this will return True. This
is **not** a check to see if the response code is ``200 OK``.
```

### raise_for_status

```json
{
  "name": "raise_for_status",
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
Raises :class:`HTTPError`, if one occurred.
```

### text

```json
{
  "name": "text",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
Content of the response, in unicode.

If Response.encoding is None, encoding will be guessed using
``charset_normalizer`` or ``chardet``.

The encoding of the response content is determined based solely on HTTP
headers, following RFC 2616 to the letter. If you can take advantage of
non-HTTP knowledge to make a better guess at the encoding, you should
set ``r.encoding`` appropriately before accessing this property.
```

## ResponseError

```json
{
  "name": "ResponseError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature_error": "no signature found for builtin type <class 'urllib3.exceptions.ResponseError'>"
}
```

```text
Used as a container for an error reason supplied in a MaxRetryError.
```

### GENERIC_ERROR

```json
{
  "name": "GENERIC_ERROR",
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

### SPECIFIC_ERROR

```json
{
  "name": "SPECIFIC_ERROR",
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

## Retry

```json
{
  "name": "Retry",
  "kind": "class",
  "origin": "urllib3.util.retry",
  "signature": "(total: 'bool | int | None' = 10, connect: 'int | None' = None, read: 'int | None' = None, redirect: 'bool | int | None' = None, status: 'int | None' = None, other: 'int | None' = None, allowed_methods: 'typing.Collection[str] | None' = frozenset({'TRACE', 'HEAD', 'PUT', 'GET', 'DELETE', 'OPTIONS'}), status_forcelist: 'typing.Collection[int] | None' = None, backoff_factor: 'float' = 0, backoff_max: 'float' = 120, raise_on_redirect: 'bool' = True, raise_on_status: 'bool' = True, history: 'tuple[RequestHistory, ...] | None' = None, respect_retry_after_header: 'bool' = True, remove_headers_on_redirect: 'typing.Collection[str]' = frozenset({'Cookie', 'Proxy-Authorization', 'Authorization'}), backoff_jitter: 'float' = 0.0, retry_after_max: 'int' = 21600) -> 'None'",
  "parameters": [
    {
      "name": "total",
      "kind": "positional or keyword",
      "annotation": "'bool | int | None'",
      "default": "10",
      "required": false
    },
    {
      "name": "connect",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "read",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "redirect",
      "kind": "positional or keyword",
      "annotation": "'bool | int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "status",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "other",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "allowed_methods",
      "kind": "positional or keyword",
      "annotation": "'typing.Collection[str] | None'",
      "default": "frozenset({'TRACE', 'HEAD', 'PUT', 'GET', 'DELETE', 'OPTIONS'})",
      "required": false
    },
    {
      "name": "status_forcelist",
      "kind": "positional or keyword",
      "annotation": "'typing.Collection[int] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "backoff_factor",
      "kind": "positional or keyword",
      "annotation": "'float'",
      "default": "0",
      "required": false
    },
    {
      "name": "backoff_max",
      "kind": "positional or keyword",
      "annotation": "'float'",
      "default": "120",
      "required": false
    },
    {
      "name": "raise_on_redirect",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "True",
      "required": false
    },
    {
      "name": "raise_on_status",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "True",
      "required": false
    },
    {
      "name": "history",
      "kind": "positional or keyword",
      "annotation": "'tuple[RequestHistory, ...] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "respect_retry_after_header",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "True",
      "required": false
    },
    {
      "name": "remove_headers_on_redirect",
      "kind": "positional or keyword",
      "annotation": "'typing.Collection[str]'",
      "default": "frozenset({'Cookie', 'Proxy-Authorization', 'Authorization'})",
      "required": false
    },
    {
      "name": "backoff_jitter",
      "kind": "positional or keyword",
      "annotation": "'float'",
      "default": "0.0",
      "required": false
    },
    {
      "name": "retry_after_max",
      "kind": "positional or keyword",
      "annotation": "'int'",
      "default": "21600",
      "required": false
    }
  ],
  "returns": "'None'"
}
```

```text
Retry configuration.

Each retry attempt will create a new Retry object with updated values, so
they can be safely reused.

Retries can be defined as a default for a pool:

.. code-block:: python

    retries = Retry(connect=5, read=2, redirect=5)
    http = PoolManager(retries=retries)
    response = http.request("GET", "https://example.com/")

Or per-request (which overrides the default for the pool):

.. code-block:: python

    response = http.request("GET", "https://example.com/", retries=Retry(10))

Retries can be disabled by passing ``False``:

.. code-block:: python

    response = http.request("GET", "https://example.com/", retries=False)

Errors will be wrapped in :class:`~urllib3.exceptions.MaxRetryError` unless
retries are disabled, in which case the causing exception will be raised.

:param int total:
    Total number of retries to allow. Takes precedence over other counts.

    Set to ``None`` to remove this constraint and fall back on other
    counts.

    Set to ``0`` to fail on the first retry.

    Set to ``False`` to disable and imply ``raise_on_redirect=False``.

:param int connect:
    How many connection-related errors to retry on.

    These are errors raised before the request is sent to the remote server,
    which we assume has not triggered the server to process the request.

    Set to ``0`` to fail on the first retry of this type.

:param int read:
    How many times to retry on read errors.

    These errors are raised after the request was sent to the server, so the
    request may have side-effects.

    Set to ``0`` to fail on the first retry of this type.

:param int redirect:
    How many redirects to perform. Limit this to avoid infinite redirect
    loops.

    A redirect is a HTTP response with a status code 301, 302, 303, 307 or
    308.

    Set to ``0`` to fail on the first retry of this type.

    Set to ``False`` to disable and imply ``raise_on_redirect=False``.

:param int status:
    How many times to retry on bad status codes.

    These are retries made on responses, where status code matches
    ``status_forcelist``.

    Set to ``0`` to fail on the first retry of this type.

:param int other:
    How many times to retry on other errors.

    Other errors are errors that are not connect, read, redirect or status errors.
    These errors might be raised after the request was sent to the server, so the
    request might have side-effects.

    Set to ``0`` to fail on the first retry of this type.

    If ``total`` is not set, it's a good idea to set this to 0 to account
    for unexpected edge cases and avoid infinite retry loops.

:param Collection allowed_methods:
    Set of uppercased HTTP method verbs that we should retry on.

    By default, we only retry on methods which are considered to be
    idempotent (multiple requests with the same parameters end with the
    same state). See :attr:`Retry.DEFAULT_ALLOWED_METHODS`.

    Set to a ``None`` value to retry on any verb.

:param Collection status_forcelist:
    A set of integer HTTP status codes that we should force a retry on.
    A retry is initiated if the request method is in ``allowed_methods``
    and the response status code is in ``status_forcelist``.

    By default, this is disabled with ``None``.

:param float backoff_factor:
    A backoff factor to apply between attempts after the second try
    (most errors are resolved immediately by a second try without a
    delay). urllib3 will sleep for::

        {backoff factor} * (2 ** ({number of previous retries}))

    seconds. If `backoff_jitter` is non-zero, this sleep is extended by::

        random.uniform(0, {backoff jitter})

    seconds. For example, if the backoff_factor is 0.1, then :func:`Retry.sleep` will
    sleep for [0.0s, 0.2s, 0.4s, 0.8s, ...] between retries. No backoff will ever
    be longer than `backoff_max`.

    By default, backoff is disabled (factor set to 0).

:param float backoff_max:
    The maximum backoff time (in seconds) between retry attempts.
    This value caps the computed backoff from `backoff_factor`.

:param float backoff_jitter:
    Random jitter amount (in seconds) added to the computed backoff.
    Jitter is sampled uniformly from `0` to `backoff_jitter`.

:param bool raise_on_redirect: Whether, if the number of redirects is
    exhausted, to raise a MaxRetryError, or to return a response with a
    response code in the 3xx range.

:param bool raise_on_status: Similar meaning to ``raise_on_redirect``:
    whether we should raise an exception, or return a response,
    if status falls in ``status_forcelist`` range and retries have
    been exhausted.

:param tuple history: The history of the request encountered during
    each call to :meth:`~Retry.increment`. The list is in the order
    the requests occurred. Each list item is of class :class:`RequestHistory`.

:param bool respect_retry_after_header:
    Whether to respect Retry-After header on status codes defined as
    :attr:`Retry.RETRY_AFTER_STATUS_CODES` or not.

:param Collection remove_headers_on_redirect:
    Sequence of headers to remove from the request when a response
    indicating a redirect is returned before firing off the redirected
    request.

:param int retry_after_max: Number of seconds to allow as the maximum for
    Retry-After headers. Defaults to :attr:`Retry.DEFAULT_RETRY_AFTER_MAX`.
    Any Retry-After headers larger than this value will be limited to this
    value.
```

### DEFAULT

```json
{
  "name": "DEFAULT",
  "kind": "Retry",
  "decorators": [],
  "inherited": false
}
```

```text
Retry configuration.

Each retry attempt will create a new Retry object with updated values, so
they can be safely reused.

Retries can be defined as a default for a pool:

.. code-block:: python

    retries = Retry(connect=5, read=2, redirect=5)
    http = PoolManager(retries=retries)
    response = http.request("GET", "https://example.com/")

Or per-request (which overrides the default for the pool):

.. code-block:: python

    response = http.request("GET", "https://example.com/", retries=Retry(10))

Retries can be disabled by passing ``False``:

.. code-block:: python

    response = http.request("GET", "https://example.com/", retries=False)

Errors will be wrapped in :class:`~urllib3.exceptions.MaxRetryError` unless
retries are disabled, in which case the causing exception will be raised.

:param int total:
    Total number of retries to allow. Takes precedence over other counts.

    Set to ``None`` to remove this constraint and fall back on other
    counts.

    Set to ``0`` to fail on the first retry.

    Set to ``False`` to disable and imply ``raise_on_redirect=False``.

:param int connect:
    How many connection-related errors to retry on.

    These are errors raised before the request is sent to the remote server,
    which we assume has not triggered the server to process the request.

    Set to ``0`` to fail on the first retry of this type.

:param int read:
    How many times to retry on read errors.

    These errors are raised after the request was sent to the server, so the
    request may have side-effects.

    Set to ``0`` to fail on the first retry of this type.

:param int redirect:
    How many redirects to perform. Limit this to avoid infinite redirect
    loops.

    A redirect is a HTTP response with a status code 301, 302, 303, 307 or
    308.

    Set to ``0`` to fail on the first retry of this type.

    Set to ``False`` to disable and imply ``raise_on_redirect=False``.

:param int status:
    How many times to retry on bad status codes.

    These are retries made on responses, where status code matches
    ``status_forcelist``.

    Set to ``0`` to fail on the first retry of this type.

:param int other:
    How many times to retry on other errors.

    Other errors are errors that are not connect, read, redirect or status errors.
    These errors might be raised after the request was sent to the server, so the
    request might have side-effects.

    Set to ``0`` to fail on the first retry of this type.

    If ``total`` is not set, it's a good idea to set this to 0 to account
    for unexpected edge cases and avoid infinite retry loops.

:param Collection allowed_methods:
    Set of uppercased HTTP method verbs that we should retry on.

    By default, we only retry on methods which are considered to be
    idempotent (multiple requests with the same parameters end with the
    same state). See :attr:`Retry.DEFAULT_ALLOWED_METHODS`.

    Set to a ``None`` value to retry on any verb.

:param Collection status_forcelist:
    A set of integer HTTP status codes that we should force a retry on.
    A retry is initiated if the request method is in ``allowed_methods``
    and the response status code is in ``status_forcelist``.

    By default, this is disabled with ``None``.

:param float backoff_factor:
    A backoff factor to apply between attempts after the second try
    (most errors are resolved immediately by a second try without a
    delay). urllib3 will sleep for::

        {backoff factor} * (2 ** ({number of previous retries}))

    seconds. If `backoff_jitter` is non-zero, this sleep is extended by::

        random.uniform(0, {backoff jitter})

    seconds. For example, if the backoff_factor is 0.1, then :func:`Retry.sleep` will
    sleep for [0.0s, 0.2s, 0.4s, 0.8s, ...] between retries. No backoff will ever
    be longer than `backoff_max`.

    By default, backoff is disabled (factor set to 0).

:param float backoff_max:
    The maximum backoff time (in seconds) between retry attempts.
    This value caps the computed backoff from `backoff_factor`.

:param float backoff_jitter:
    Random jitter amount (in seconds) added to the computed backoff.
    Jitter is sampled uniformly from `0` to `backoff_jitter`.

:param bool raise_on_redirect: Whether, if the number of redirects is
    exhausted, to raise a MaxRetryError, or to return a response with a
    response code in the 3xx range.

:param bool raise_on_status: Similar meaning to ``raise_on_redirect``:
    whether we should raise an exception, or return a response,
    if status falls in ``status_forcelist`` range and retries have
    been exhausted.

:param tuple history: The history of the request encountered during
    each call to :meth:`~Retry.increment`. The list is in the order
    the requests occurred. Each list item is of class :class:`RequestHistory`.

:param bool respect_retry_after_header:
    Whether to respect Retry-After header on status codes defined as
    :attr:`Retry.RETRY_AFTER_STATUS_CODES` or not.

:param Collection remove_headers_on_redirect:
    Sequence of headers to remove from the request when a response
    indicating a redirect is returned before firing off the redirected
    request.

:param int retry_after_max: Number of seconds to allow as the maximum for
    Retry-After headers. Defaults to :attr:`Retry.DEFAULT_RETRY_AFTER_MAX`.
    Any Retry-After headers larger than this value will be limited to this
    value.
```

### DEFAULT_ALLOWED_METHODS

```json
{
  "name": "DEFAULT_ALLOWED_METHODS",
  "kind": "frozenset",
  "decorators": [],
  "inherited": false
}
```

```text
Build an immutable unordered collection of unique elements.
```

### DEFAULT_BACKOFF_MAX

```json
{
  "name": "DEFAULT_BACKOFF_MAX",
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

### DEFAULT_REMOVE_HEADERS_ON_REDIRECT

```json
{
  "name": "DEFAULT_REMOVE_HEADERS_ON_REDIRECT",
  "kind": "frozenset",
  "decorators": [],
  "inherited": false
}
```

```text
Build an immutable unordered collection of unique elements.
```

### DEFAULT_RETRY_AFTER_MAX

```json
{
  "name": "DEFAULT_RETRY_AFTER_MAX",
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

### RETRY_AFTER_STATUS_CODES

```json
{
  "name": "RETRY_AFTER_STATUS_CODES",
  "kind": "frozenset",
  "decorators": [],
  "inherited": false
}
```

```text
Build an immutable unordered collection of unique elements.
```

### __annotations__

```json
{
  "name": "__annotations__",
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
  "signature": "(self, total: 'bool | int | None' = 10, connect: 'int | None' = None, read: 'int | None' = None, redirect: 'bool | int | None' = None, status: 'int | None' = None, other: 'int | None' = None, allowed_methods: 'typing.Collection[str] | None' = frozenset({'TRACE', 'HEAD', 'PUT', 'GET', 'DELETE', 'OPTIONS'}), status_forcelist: 'typing.Collection[int] | None' = None, backoff_factor: 'float' = 0, backoff_max: 'float' = 120, raise_on_redirect: 'bool' = True, raise_on_status: 'bool' = True, history: 'tuple[RequestHistory, ...] | None' = None, respect_retry_after_header: 'bool' = True, remove_headers_on_redirect: 'typing.Collection[str]' = frozenset({'Cookie', 'Proxy-Authorization', 'Authorization'}), backoff_jitter: 'float' = 0.0, retry_after_max: 'int' = 21600) -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "total",
      "kind": "positional or keyword",
      "annotation": "'bool | int | None'",
      "default": "10",
      "required": false
    },
    {
      "name": "connect",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "read",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "redirect",
      "kind": "positional or keyword",
      "annotation": "'bool | int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "status",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "other",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "allowed_methods",
      "kind": "positional or keyword",
      "annotation": "'typing.Collection[str] | None'",
      "default": "frozenset({'TRACE', 'HEAD', 'PUT', 'GET', 'DELETE', 'OPTIONS'})",
      "required": false
    },
    {
      "name": "status_forcelist",
      "kind": "positional or keyword",
      "annotation": "'typing.Collection[int] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "backoff_factor",
      "kind": "positional or keyword",
      "annotation": "'float'",
      "default": "0",
      "required": false
    },
    {
      "name": "backoff_max",
      "kind": "positional or keyword",
      "annotation": "'float'",
      "default": "120",
      "required": false
    },
    {
      "name": "raise_on_redirect",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "True",
      "required": false
    },
    {
      "name": "raise_on_status",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "True",
      "required": false
    },
    {
      "name": "history",
      "kind": "positional or keyword",
      "annotation": "'tuple[RequestHistory, ...] | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "respect_retry_after_header",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "True",
      "required": false
    },
    {
      "name": "remove_headers_on_redirect",
      "kind": "positional or keyword",
      "annotation": "'typing.Collection[str]'",
      "default": "frozenset({'Cookie', 'Proxy-Authorization', 'Authorization'})",
      "required": false
    },
    {
      "name": "backoff_jitter",
      "kind": "positional or keyword",
      "annotation": "'float'",
      "default": "0.0",
      "required": false
    },
    {
      "name": "retry_after_max",
      "kind": "positional or keyword",
      "annotation": "'int'",
      "default": "21600",
      "required": false
    }
  ],
  "returns": "'None'"
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
  "signature": "(self) -> 'str'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'str'"
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

### _is_connection_error

```json
{
  "name": "_is_connection_error",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, err: 'Exception') -> 'bool'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "err",
      "kind": "positional or keyword",
      "annotation": "'Exception'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'bool'"
}
```

```text
Errors when we're fairly sure that the server did not receive the
request, so it should be safe to retry.
```

### _is_method_retryable

```json
{
  "name": "_is_method_retryable",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, method: 'str') -> 'bool'",
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
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'bool'"
}
```

```text
Checks if a given HTTP method should be retried upon, depending if
it is included in the allowed_methods
```

### _is_read_error

```json
{
  "name": "_is_read_error",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, err: 'Exception') -> 'bool'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "err",
      "kind": "positional or keyword",
      "annotation": "'Exception'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'bool'"
}
```

```text
Errors that occur after the request has been started, so we should
assume that the server began processing it.
```

### _sleep_backoff

```json
{
  "name": "_sleep_backoff",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self) -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
}
```

```text
No docstring available.
```

### from_int

```json
{
  "name": "from_int",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(cls, retries: 'Retry | bool | int | None', redirect: 'bool | int | None' = True, default: 'Retry | bool | int | None' = None) -> 'Retry'",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "retries",
      "kind": "positional or keyword",
      "annotation": "'Retry | bool | int | None'",
      "default": null,
      "required": true
    },
    {
      "name": "redirect",
      "kind": "positional or keyword",
      "annotation": "'bool | int | None'",
      "default": "True",
      "required": false
    },
    {
      "name": "default",
      "kind": "positional or keyword",
      "annotation": "'Retry | bool | int | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'Retry'"
}
```

```text
Backwards-compatibility for the old retries format.
```

### get_backoff_time

```json
{
  "name": "get_backoff_time",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self) -> 'float'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'float'"
}
```

```text
Formula for computing the current backoff

:rtype: float
```

### get_retry_after

```json
{
  "name": "get_retry_after",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, response: 'BaseHTTPResponse') -> 'float | None'",
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
      "annotation": "'BaseHTTPResponse'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'float | None'"
}
```

```text
Get the value of Retry-After in seconds.
```

### increment

```json
{
  "name": "increment",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, method: 'str | None' = None, url: 'str | None' = None, response: 'BaseHTTPResponse | None' = None, error: 'Exception | None' = None, _pool: 'ConnectionPool | None' = None, _stacktrace: 'TracebackType | None' = None) -> 'Self'",
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
      "annotation": "'str | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "response",
      "kind": "positional or keyword",
      "annotation": "'BaseHTTPResponse | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "error",
      "kind": "positional or keyword",
      "annotation": "'Exception | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "_pool",
      "kind": "positional or keyword",
      "annotation": "'ConnectionPool | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "_stacktrace",
      "kind": "positional or keyword",
      "annotation": "'TracebackType | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'Self'"
}
```

```text
Return a new Retry object with incremented retry counters.

:param response: A response object, or None, if the server did not
    return a response.
:type response: :class:`~urllib3.response.BaseHTTPResponse`
:param Exception error: An error encountered during the request, or
    None if the response was received successfully.

:return: A new ``Retry`` object.
```

### is_exhausted

```json
{
  "name": "is_exhausted",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self) -> 'bool'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'bool'"
}
```

```text
Are we out of retries?
```

### is_retry

```json
{
  "name": "is_retry",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, method: 'str', status_code: 'int', has_retry_after: 'bool' = False) -> 'bool'",
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
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "status_code",
      "kind": "positional or keyword",
      "annotation": "'int'",
      "default": null,
      "required": true
    },
    {
      "name": "has_retry_after",
      "kind": "positional or keyword",
      "annotation": "'bool'",
      "default": "False",
      "required": false
    }
  ],
  "returns": "'bool'"
}
```

```text
Is this method/status code retryable? (Based on allowlists and control
variables such as the number of total retries to allow, whether to
respect the Retry-After header, whether this header is present, and
whether the returned status code is on the list of status codes to
be retried upon on the presence of the aforementioned header)
```

### new

```json
{
  "name": "new",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, **kw: 'typing.Any') -> 'Self'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kw",
      "kind": "var keyword",
      "annotation": "'typing.Any'",
      "default": null,
      "required": false
    }
  ],
  "returns": "'Self'"
}
```

```text
No docstring available.
```

### parse_retry_after

```json
{
  "name": "parse_retry_after",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, retry_after: 'str') -> 'float'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "retry_after",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'float'"
}
```

```text
No docstring available.
```

### sleep

```json
{
  "name": "sleep",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, response: 'BaseHTTPResponse | None' = None) -> 'None'",
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
      "annotation": "'BaseHTTPResponse | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'None'"
}
```

```text
Sleep between retry attempts.

This method will respect a server's ``Retry-After`` response header
and sleep the duration of the time requested. If that is not present, it
will use an exponential backoff. By default, the backoff factor is 0 and
this method will return immediately.
```

### sleep_for_retry

```json
{
  "name": "sleep_for_retry",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, response: 'BaseHTTPResponse') -> 'bool'",
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
      "annotation": "'BaseHTTPResponse'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'bool'"
}
```

```text
No docstring available.
```

## RetryError

```json
{
  "name": "RetryError",
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
Custom retries logic failed
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

## SOCKSProxyManager

```json
{
  "name": "SOCKSProxyManager",
  "kind": "function",
  "origin": "requests.adapters",
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
No docstring available.
```

## SSLError

```json
{
  "name": "SSLError",
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
An SSL error occurred.
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

## TimeoutSauce

```json
{
  "name": "TimeoutSauce",
  "kind": "class",
  "origin": "urllib3.util.timeout",
  "signature": "(total: '_TYPE_TIMEOUT' = None, connect: '_TYPE_TIMEOUT' = <_TYPE_DEFAULT.token: -1>, read: '_TYPE_TIMEOUT' = <_TYPE_DEFAULT.token: -1>) -> 'None'",
  "parameters": [
    {
      "name": "total",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": "None",
      "required": false
    },
    {
      "name": "connect",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": "<_TYPE_DEFAULT.token: -1>",
      "required": false
    },
    {
      "name": "read",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": "<_TYPE_DEFAULT.token: -1>",
      "required": false
    }
  ],
  "returns": "'None'"
}
```

```text
Timeout configuration.

Timeouts can be defined as a default for a pool:

.. code-block:: python

    import urllib3

    timeout = urllib3.util.Timeout(connect=2.0, read=7.0)

    http = urllib3.PoolManager(timeout=timeout)

    resp = http.request("GET", "https://example.com/")

    print(resp.status)

Or per-request (which overrides the default for the pool):

.. code-block:: python

   response = http.request("GET", "https://example.com/", timeout=Timeout(10))

Timeouts can be disabled by setting all the parameters to ``None``:

.. code-block:: python

   no_timeout = Timeout(connect=None, read=None)
   response = http.request("GET", "https://example.com/", timeout=no_timeout)


:param total:
    This combines the connect and read timeouts into one; the read timeout
    will be set to the time leftover from the connect attempt. In the
    event that both a connect timeout and a total are specified, or a read
    timeout and a total are specified, the shorter timeout will be applied.

    Defaults to None.

:type total: int, float, or None

:param connect:
    The maximum amount of time (in seconds) to wait for a connection
    attempt to a server to succeed. Omitting the parameter will default the
    connect timeout to the system default, probably `the global default
    timeout in socket.py
    <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
    None will set an infinite timeout for connection attempts.

:type connect: int, float, or None

:param read:
    The maximum amount of time (in seconds) to wait between consecutive
    read operations for a response from the server. Omitting the parameter
    will default the read timeout to the system default, probably `the
    global default timeout in socket.py
    <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
    None will set an infinite timeout.

:type read: int, float, or None

.. note::

    Many factors can affect the total amount of time for urllib3 to return
    an HTTP response.

    For example, Python's DNS resolver does not obey the timeout specified
    on the socket. Other factors that can affect total request time include
    high CPU load, high swap, the program running at a low priority level,
    or other behaviors.

    In addition, the read and total timeouts only measure the time between
    read operations on the socket connecting the client and the server,
    not the total amount of time for the request to return a complete
    response. For most requests, the timeout is raised because the server
    has not sent the first byte in the specified time. This is not always
    the case; if a server streams one byte every fifteen seconds, a timeout
    of 20 seconds will not trigger, even though the request will take
    several minutes to complete.
```

### DEFAULT_TIMEOUT

```json
{
  "name": "DEFAULT_TIMEOUT",
  "kind": "_TYPE_DEFAULT",
  "decorators": [],
  "inherited": false
}
```

```text
No docstring available.
```

### __annotations__

```json
{
  "name": "__annotations__",
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
  "signature": "(self, total: '_TYPE_TIMEOUT' = None, connect: '_TYPE_TIMEOUT' = <_TYPE_DEFAULT.token: -1>, read: '_TYPE_TIMEOUT' = <_TYPE_DEFAULT.token: -1>) -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "total",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": "None",
      "required": false
    },
    {
      "name": "connect",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": "<_TYPE_DEFAULT.token: -1>",
      "required": false
    },
    {
      "name": "read",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": "<_TYPE_DEFAULT.token: -1>",
      "required": false
    }
  ],
  "returns": "'None'"
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
  "signature": "(self) -> 'str'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'str'"
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
  "inherited": false,
  "signature": "(self) -> 'str'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'str'"
}
```

```text
Return repr(self).
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

### _validate_timeout

```json
{
  "name": "_validate_timeout",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(cls, value: '_TYPE_TIMEOUT', name: 'str') -> '_TYPE_TIMEOUT'",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": null,
      "required": true
    },
    {
      "name": "name",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'_TYPE_TIMEOUT'"
}
```

```text
Check that a timeout attribute is valid.

:param value: The timeout value to validate
:param name: The name of the timeout attribute to validate. This is
    used to specify in error messages.
:return: The validated and casted version of the given value.
:raises ValueError: If it is a numeric value less than or equal to
    zero, or the type is not an integer, float, or None.
```

### clone

```json
{
  "name": "clone",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self) -> 'Timeout'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'Timeout'"
}
```

```text
Create a copy of the timeout object

Timeout properties are stored per-pool but each request needs a fresh
Timeout object to ensure each one has its own start/stop configured.

:return: a copy of the timeout object
:rtype: :class:`Timeout`
```

### connect_timeout

```json
{
  "name": "connect_timeout",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
Get the value to use when setting a connection timeout.

This will be a positive float or integer, the value None
(never timeout), or the default system timeout.

:return: Connect timeout.
:rtype: int, float, :attr:`Timeout.DEFAULT_TIMEOUT` or None
```

### from_float

```json
{
  "name": "from_float",
  "kind": "function",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(cls, timeout: '_TYPE_TIMEOUT') -> 'Timeout'",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "timeout",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'Timeout'"
}
```

```text
Create a new Timeout from a legacy timeout value.

The timeout value used by httplib.py sets the same timeout on the
connect(), and recv() socket requests. This creates a :class:`Timeout`
object that sets the individual timeouts to the ``timeout`` value
passed to this function.

:param timeout: The legacy timeout value.
:type timeout: integer, float, :attr:`urllib3.util.Timeout.DEFAULT_TIMEOUT`, or None
:return: Timeout object
:rtype: :class:`Timeout`
```

### get_connect_duration

```json
{
  "name": "get_connect_duration",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self) -> 'float'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'float'"
}
```

```text
Gets the time elapsed since the call to :meth:`start_connect`.

:return: Elapsed time in seconds.
:rtype: float
:raises urllib3.exceptions.TimeoutStateError: if you attempt
    to get duration for a timer that hasn't been started.
```

### read_timeout

```json
{
  "name": "read_timeout",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
Get the value for the read timeout.

This assumes some time has elapsed in the connection timeout and
computes the read timeout appropriately.

If self.total is set, the read timeout is dependent on the amount of
time taken by the connect timeout. If the connection time has not been
established, a :exc:`~urllib3.exceptions.TimeoutStateError` will be
raised.

:return: Value to use for the read timeout.
:rtype: int, float or None
:raises urllib3.exceptions.TimeoutStateError: If :meth:`start_connect`
    has not yet been called on this object.
```

### resolve_default_timeout

```json
{
  "name": "resolve_default_timeout",
  "kind": "function",
  "decorators": [
    "staticmethod"
  ],
  "inherited": false,
  "signature": "(timeout: '_TYPE_TIMEOUT') -> 'float | None'",
  "parameters": [
    {
      "name": "timeout",
      "kind": "positional or keyword",
      "annotation": "'_TYPE_TIMEOUT'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'float | None'"
}
```

```text
No docstring available.
```

### start_connect

```json
{
  "name": "start_connect",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self) -> 'float'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": "'float'"
}
```

```text
Start the timeout clock, used during a connect() attempt

:raises urllib3.exceptions.TimeoutStateError: if you attempt
    to start a timer that has been started already.
```

## _HTTPError

```json
{
  "name": "_HTTPError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature_error": "no signature found for builtin type <class 'urllib3.exceptions.HTTPError'>"
}
```

```text
Base exception used by this module.
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
  "inherited": false
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

## _InvalidHeader

```json
{
  "name": "_InvalidHeader",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature_error": "no signature found for builtin type <class 'urllib3.exceptions.InvalidHeader'>"
}
```

```text
The header provided was somehow invalid.
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

## _ProxyError

```json
{
  "name": "_ProxyError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature": "(message: 'str', error: 'Exception') -> 'None'",
  "parameters": [
    {
      "name": "message",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "error",
      "kind": "positional or keyword",
      "annotation": "'Exception'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
}
```

```text
Raised when the connection to a proxy fails.
```

### __annotations__

```json
{
  "name": "__annotations__",
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
  "inherited": false,
  "signature": "(self, message: 'str', error: 'Exception') -> 'None'",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "message",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "error",
      "kind": "positional or keyword",
      "annotation": "'Exception'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'None'"
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

## _SSLError

```json
{
  "name": "_SSLError",
  "kind": "class",
  "origin": "urllib3.exceptions",
  "signature_error": "no signature found for builtin type <class 'urllib3.exceptions.SSLError'>"
}
```

```text
Raised when SSL certificate fails in an HTTPS connection.
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

## _preloaded_ssl_context

```json
{
  "name": "_preloaded_ssl_context",
  "kind": "SSLContext",
  "origin": "ssl"
}
```

```text
An SSLContext holds various SSL-related configuration options and
data, such as certificates and possibly a private key.
```

## _urllib3_request_context

```json
{
  "name": "_urllib3_request_context",
  "kind": "function",
  "origin": "requests.adapters",
  "signature": "(request: 'PreparedRequest', verify: 'bool | str | None', client_cert: 'typing.Tuple[str, str] | str | None', poolmanager: 'PoolManager') -> '(typing.Dict[str, typing.Any], typing.Dict[str, typing.Any])'",
  "parameters": [
    {
      "name": "request",
      "kind": "positional or keyword",
      "annotation": "'PreparedRequest'",
      "default": null,
      "required": true
    },
    {
      "name": "verify",
      "kind": "positional or keyword",
      "annotation": "'bool | str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "client_cert",
      "kind": "positional or keyword",
      "annotation": "'typing.Tuple[str, str] | str | None'",
      "default": null,
      "required": true
    },
    {
      "name": "poolmanager",
      "kind": "positional or keyword",
      "annotation": "'PoolManager'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'(typing.Dict[str, typing.Any], typing.Dict[str, typing.Any])'"
}
```

```text
No docstring available.
```

## basestring

```json
{
  "name": "basestring",
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

## create_urllib3_context

```json
{
  "name": "create_urllib3_context",
  "kind": "function",
  "origin": "urllib3.util.ssl_",
  "signature": "(ssl_version: 'int | None' = None, cert_reqs: 'int | None' = None, options: 'int | None' = None, ciphers: 'str | None' = None, ssl_minimum_version: 'int | None' = None, ssl_maximum_version: 'int | None' = None, verify_flags: 'int | None' = None) -> 'ssl.SSLContext'",
  "parameters": [
    {
      "name": "ssl_version",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "cert_reqs",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "options",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "ciphers",
      "kind": "positional or keyword",
      "annotation": "'str | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "ssl_minimum_version",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "ssl_maximum_version",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    },
    {
      "name": "verify_flags",
      "kind": "positional or keyword",
      "annotation": "'int | None'",
      "default": "None",
      "required": false
    }
  ],
  "returns": "'ssl.SSLContext'"
}
```

```text
Creates and configures an :class:`ssl.SSLContext` instance for use with urllib3.

:param ssl_version:
    The desired protocol version to use. This will default to
    PROTOCOL_SSLv23 which will negotiate the highest protocol that both
    the server and your installation of OpenSSL support.

    This parameter is deprecated instead use 'ssl_minimum_version'.
:param ssl_minimum_version:
    The minimum version of TLS to be used. Use the 'ssl.TLSVersion' enum for specifying the value.
:param ssl_maximum_version:
    The maximum version of TLS to be used. Use the 'ssl.TLSVersion' enum for specifying the value.
    Not recommended to set to anything other than 'ssl.TLSVersion.MAXIMUM_SUPPORTED' which is the
    default value.
:param cert_reqs:
    Whether to require the certificate verification. This defaults to
    ``ssl.CERT_REQUIRED``.
:param options:
    Specific OpenSSL options. These default to ``ssl.OP_NO_SSLv2``,
    ``ssl.OP_NO_SSLv3``, ``ssl.OP_NO_COMPRESSION``, and ``ssl.OP_NO_TICKET``.
:param ciphers:
    Which cipher suites to allow the server to select. Defaults to either system configured
    ciphers if OpenSSL 1.1.1+, otherwise uses a secure default set of ciphers.
:param verify_flags:
    The flags for certificate verification operations. These default to
    ``ssl.VERIFY_X509_PARTIAL_CHAIN`` and ``ssl.VERIFY_X509_STRICT`` for Python 3.13+.
:returns:
    Constructed SSLContext object with specified options
:rtype: SSLContext
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

## extract_zipped_paths

```json
{
  "name": "extract_zipped_paths",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(path)",
  "parameters": [
    {
      "name": "path",
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
Replace nonexistent paths that look like they refer to a member of a zip
archive with the location of an extracted copy of the target, or else
just return the provided path unchanged.
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

## get_encoding_from_headers

```json
{
  "name": "get_encoding_from_headers",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(headers)",
  "parameters": [
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
Returns encodings from given HTTP Header Dict.

:param headers: dictionary to extract encoding from.
:rtype: str
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

## parse_url

```json
{
  "name": "parse_url",
  "kind": "function",
  "origin": "urllib3.util.url",
  "signature": "(url: 'str') -> 'Url'",
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    }
  ],
  "returns": "'Url'"
}
```

```text
Given a url, return a parsed :class:`.Url` namedtuple. Best-effort is
performed to parse incomplete urls. Fields not provided will be None.
This parser is RFC 3986 and RFC 6874 compliant.

The parser logic and helper functions are based heavily on
work done in the ``rfc3986`` module.

:param str url: URL to parse into a :class:`.Url` namedtuple.

Partly backwards-compatible with :mod:`urllib.parse`.

Example:

.. code-block:: python

    import urllib3

    print( urllib3.util.parse_url('http://google.com/mail/'))
    # Url(scheme='http', host='google.com', port=None, path='/mail/', ...)

    print( urllib3.util.parse_url('google.com:80'))
    # Url(scheme=None, host='google.com', port=80, path=None, ...)

    print( urllib3.util.parse_url('/foo?bar'))
    # Url(scheme=None, host=None, port=None, path='/foo', query='bar', ...)
```

## prepend_scheme_if_needed

```json
{
  "name": "prepend_scheme_if_needed",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(url, new_scheme)",
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "new_scheme",
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
Given a URL that may or may not have a scheme, prepend the given scheme.
Does not replace a present scheme with the one provided as an argument.

:rtype: str
```

## proxy_from_url

```json
{
  "name": "proxy_from_url",
  "kind": "function",
  "origin": "urllib3.poolmanager",
  "signature": "(url: 'str', **kw: 'typing.Any') -> 'ProxyManager'",
  "parameters": [
    {
      "name": "url",
      "kind": "positional or keyword",
      "annotation": "'str'",
      "default": null,
      "required": true
    },
    {
      "name": "kw",
      "kind": "var keyword",
      "annotation": "'typing.Any'",
      "default": null,
      "required": false
    }
  ],
  "returns": "'ProxyManager'"
}
```

```text
No docstring available.
```

## select_proxy

```json
{
  "name": "select_proxy",
  "kind": "function",
  "origin": "requests.utils",
  "signature": "(url, proxies)",
  "parameters": [
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
    }
  ],
  "returns": null
}
```

```text
Select a proxy for the url, if applicable.

:param url: The url being for the request
:param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
```

## socket

```json
{
  "name": "socket",
  "kind": "module",
  "origin": null
}
```

```text
This module provides socket operations and some related functions.
On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
On other systems, it only supports IP. Functions specific for a
socket are available as methods of the socket object.

Functions:

socket() -- create a new socket object
socketpair() -- create a pair of new socket objects [*]
fromfd() -- create a socket object from an open file descriptor [*]
send_fds() -- Send file descriptor to the socket.
recv_fds() -- Receive file descriptors from the socket.
fromshare() -- create a socket object from data received from socket.share() [*]
gethostname() -- return the current hostname
gethostbyname() -- map a hostname to its IP number
gethostbyaddr() -- map an IP number or hostname to DNS info
getservbyname() -- map a service name and a protocol name to a port number
getprotobyname() -- map a protocol name (e.g. 'tcp') to a number
ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
htons(), htonl() -- convert 16, 32 bit int from host to network byte order
inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)
socket.getdefaulttimeout() -- get the default timeout value
socket.setdefaulttimeout() -- set the default timeout value
create_connection() -- connects to an address, with an optional timeout and
                       optional source address.
create_server() -- create a TCP socket and bind it to a specified address.

 [*] not available on all platforms!

Special objects:

SocketType -- type object for socket objects
error -- exception raised for I/O errors
has_ipv6 -- boolean value indicating if IPv6 is supported

IntEnum constants:

AF_INET, AF_UNIX -- socket domains (first argument to socket() call)
SOCK_STREAM, SOCK_DGRAM, SOCK_RAW -- socket types (second argument)

Integer constants:

Many other constants may be defined; these may be used in calls to
the setsockopt() and getsockopt() methods.
```

## ssl

```json
{
  "name": "ssl",
  "kind": "module",
  "origin": null
}
```

```text
This module provides some more Pythonic support for SSL.

Object types:

  SSLSocket -- subtype of socket.socket which does SSL over the socket

Exceptions:

  SSLError -- exception raised for I/O errors

Functions:

  cert_time_to_seconds -- convert time string used for certificate
                          notBefore and notAfter functions to integer
                          seconds past the Epoch (the time values
                          returned from time.time())

  get_server_certificate (addr, ssl_version, ca_certs, timeout) -- Retrieve the
                          certificate from the server at the specified
                          address and return it as a PEM-encoded string


Integer constants:

SSL_ERROR_ZERO_RETURN
SSL_ERROR_WANT_READ
SSL_ERROR_WANT_WRITE
SSL_ERROR_WANT_X509_LOOKUP
SSL_ERROR_SYSCALL
SSL_ERROR_SSL
SSL_ERROR_WANT_CONNECT

SSL_ERROR_EOF
SSL_ERROR_INVALID_ERROR_CODE

The following group define certificate requirements that one side is
allowing/requiring from the other side:

CERT_NONE - no certificates from the other side are required (or will
            be looked at if provided)
CERT_OPTIONAL - certificates are not required, but if provided will be
                validated, and if validation fails, the connection will
                also fail
CERT_REQUIRED - certificates are required, and will be validated, and
                if validation fails, the connection will also fail

The following constants identify various SSL protocol variants:

PROTOCOL_SSLv2
PROTOCOL_SSLv3
PROTOCOL_SSLv23
PROTOCOL_TLS
PROTOCOL_TLS_CLIENT
PROTOCOL_TLS_SERVER
PROTOCOL_TLSv1
PROTOCOL_TLSv1_1
PROTOCOL_TLSv1_2

The following constants identify various SSL alert message descriptions as per
http://www.iana.org/assignments/tls-parameters/tls-parameters.xml#tls-parameters-6

ALERT_DESCRIPTION_CLOSE_NOTIFY
ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
ALERT_DESCRIPTION_BAD_RECORD_MAC
ALERT_DESCRIPTION_RECORD_OVERFLOW
ALERT_DESCRIPTION_DECOMPRESSION_FAILURE
ALERT_DESCRIPTION_HANDSHAKE_FAILURE
ALERT_DESCRIPTION_BAD_CERTIFICATE
ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE
ALERT_DESCRIPTION_CERTIFICATE_REVOKED
ALERT_DESCRIPTION_CERTIFICATE_EXPIRED
ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN
ALERT_DESCRIPTION_ILLEGAL_PARAMETER
ALERT_DESCRIPTION_UNKNOWN_CA
ALERT_DESCRIPTION_ACCESS_DENIED
ALERT_DESCRIPTION_DECODE_ERROR
ALERT_DESCRIPTION_DECRYPT_ERROR
ALERT_DESCRIPTION_PROTOCOL_VERSION
ALERT_DESCRIPTION_INSUFFICIENT_SECURITY
ALERT_DESCRIPTION_INTERNAL_ERROR
ALERT_DESCRIPTION_USER_CANCELLED
ALERT_DESCRIPTION_NO_RENEGOTIATION
ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE
ALERT_DESCRIPTION_UNRECOGNIZED_NAME
ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE
ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
```

## typing

```json
{
  "name": "typing",
  "kind": "module",
  "origin": null
}
```

```text
The typing module: Support for gradual typing as defined by PEP 484 and subsequent PEPs.

Among other things, the module includes the following:
* Generic, Protocol, and internal machinery to support generic aliases.
  All subscripted types like X[int], Union[int, str] are generic aliases.
* Various "special forms" that have unique meanings in type annotations:
  Any, Never, ClassVar, Self, Concatenate, Unpack, and others.
* Classes whose instances can be type arguments to generic classes and functions:
  TypeVar, ParamSpec, TypeVarTuple.
* Public helper functions: get_type_hints, overload, cast, final, and others.
* Several protocols to support duck-typing:
  SupportsFloat, SupportsIndex, SupportsAbs, and others.
* Special types: NewType, NamedTuple, TypedDict.
* Deprecated aliases for builtin types and collections.abc ABCs.

Any name not present in __all__ is an implementation detail
that may be changed without notice. Use at your own risk!
```

## urldefragauth

```json
{
  "name": "urldefragauth",
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
Given a url remove the fragment and the authentication part.

:rtype: str
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

## warnings

```json
{
  "name": "warnings",
  "kind": "module",
  "origin": null
}
```

```text
No docstring available.
```
