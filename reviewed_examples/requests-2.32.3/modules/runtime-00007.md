# Runtime: requests.compat

```text
requests.compat
~~~~~~~~~~~~~~~

This module previously handled import compatibility issues
between Python 2 and Python 3. It remains for backwards
compatibility until the next major version.
```

## Callable

```json
{
  "name": "Callable",
  "kind": "class",
  "origin": "collections.abc",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
No docstring available.
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

### __call__

```json
{
  "name": "__call__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, *args, **kwds)",
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
Call self as a function.
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
  "inherited": false,
  "signature": "(origin, args)",
  "parameters": [
    {
      "name": "origin",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "args",
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
Represent `Callable[argtypes, resulttype]`.

This sets ``__args__`` to a tuple containing the flattened
``argtypes`` followed by ``resulttype``.

Example: ``Callable[[int, str], float]`` sets ``__args__`` to
``(int, str, float)``.
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
  "inherited": false,
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

## JSONDecodeError

```json
{
  "name": "JSONDecodeError",
  "kind": "class",
  "origin": "json.decoder",
  "signature": "(msg, doc, pos)",
  "parameters": [
    {
      "name": "msg",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "doc",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pos",
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
Subclass of ValueError with the following additional properties:

msg: The unformatted error message
doc: The JSON document being parsed
pos: The start index of doc where parsing failed
lineno: The line corresponding to pos
colno: The column corresponding to pos
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
  "signature": "(self, msg, doc, pos)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "msg",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "doc",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pos",
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

## Morsel

```json
{
  "name": "Morsel",
  "kind": "class",
  "origin": "http.cookies",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
A class to hold ONE (key, value) pair.

In a cookie, each such pair may have several attributes, so this class is
used to keep the attributes associated with the appropriate key,value pair.
This class also includes a coded_value attribute, which is used to hold
the network representation of the value.
```

### OutputString

```json
{
  "name": "OutputString",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, attrs=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "attrs",
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
  "inherited": false,
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
  "signature": "(self, morsel)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "morsel",
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

### __ior__

```json
{
  "name": "__ior__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, values)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "values",
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
Return self|=value.
```

### __iter__

```json
{
  "name": "__iter__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
Return self|value.
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
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a reverse iterator over the dict keys.
```

### __ror__

```json
{
  "name": "__ror__",
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
  "signature": "(self, K, V)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "K",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "V",
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
Set self[key] to value.
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
Return the size of the dict in memory, in bytes.
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
  "signature": "(self, attrs=None, header='Set-Cookie:')",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "attrs",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "header",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'Set-Cookie:'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
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

### _flags

```json
{
  "name": "_flags",
  "kind": "set",
  "decorators": [],
  "inherited": false
}
```

```text
Build an unordered collection of unique elements.
```

### _reserved

```json
{
  "name": "_reserved",
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

### _reserved_defaults

```json
{
  "name": "_reserved_defaults",
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

### clear

```json
{
  "name": "clear",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Remove all items from the dict.
```

### coded_value

```json
{
  "name": "coded_value",
  "kind": "property",
  "decorators": [],
  "inherited": false
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
Return a shallow copy of the dict.
```

### fromkeys

```json
{
  "name": "fromkeys",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(type, iterable, value=None, /)",
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
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
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
Create a new dictionary with keys from iterable and values set to value.
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

### isReservedKey

```json
{
  "name": "isReservedKey",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, K)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "K",
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

### items

```json
{
  "name": "items",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### js_output

```json
{
  "name": "js_output",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, attrs=None)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "attrs",
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

### key

```json
{
  "name": "key",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
No docstring available.
```

### keys

```json
{
  "name": "keys",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### output

```json
{
  "name": "output",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, attrs=None, header='Set-Cookie:')",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "attrs",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "header",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'Set-Cookie:'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

### pop

```json
{
  "name": "pop",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "inspection_error": "<method 'pop' of 'dict' objects> builtin has invalid signature"
}
```

```text
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise,
raise a KeyError.
```

### popitem

```json
{
  "name": "popitem",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.
```

### set

```json
{
  "name": "set",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key, val, coded_val)",
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
      "name": "val",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "coded_val",
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
  "inherited": false,
  "signature": "(self, key, val=None)",
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
      "name": "val",
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
  "signature": "(self, values)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "values",
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
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E is present and has a .keys() method, then does:  for k in E.keys(): D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]
```

### value

```json
{
  "name": "value",
  "kind": "property",
  "decorators": [],
  "inherited": false
}
```

```text
No docstring available.
```

### values

```json
{
  "name": "values",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

## MutableMapping

```json
{
  "name": "MutableMapping",
  "kind": "class",
  "origin": "collections.abc",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
A MutableMapping is a generic container for associating
key/value pairs.

This class provides concrete generic implementations of all
methods except for __getitem__, __setitem__, __delitem__,
__iter__, and __len__.
```

### _MutableMapping__marker

```json
{
  "name": "_MutableMapping__marker",
  "kind": "object",
  "decorators": [],
  "inherited": false
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

### clear

```json
{
  "name": "clear",
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
D.clear() -> None.  Remove all items from D.
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

### pop

```json
{
  "name": "pop",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, key, default=<object object at 0x00000163C7B501D0>)",
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
      "default": "<object object at 0x00000163C7B501D0>",
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
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.
```

### setdefault

```json
{
  "name": "setdefault",
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
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
```

### update

```json
{
  "name": "update",
  "kind": "function",
  "decorators": [],
  "inherited": false,
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

## StringIO

```json
{
  "name": "StringIO",
  "kind": "class",
  "origin": "_io",
  "signature": "(initial_value='', newline='\\n')",
  "parameters": [
    {
      "name": "initial_value",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "''",
      "required": false
    },
    {
      "name": "newline",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'\\n'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Text I/O implementation using an in-memory buffer.

The initial_value argument sets the value of object.  The newline
argument is like the one of TextIOWrapper's constructor.
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

### __del__

```json
{
  "name": "__del__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Called when the instance is about to be destroyed.
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

### __enter__

```json
{
  "name": "__enter__",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "inherited": true,
  "inspection_error": "no signature found for builtin <method '__exit__' of '_io._IOBase' objects>"
}
```

```text
No docstring available.
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
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### __next__

```json
{
  "name": "__next__",
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
Implement next(self).
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

### _checkClosed

```json
{
  "name": "_checkClosed",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### _checkReadable

```json
{
  "name": "_checkReadable",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### _checkSeekable

```json
{
  "name": "_checkSeekable",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### _checkWritable

```json
{
  "name": "_checkWritable",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### close

```json
{
  "name": "close",
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
Close the IO object.

Attempting any further operation after the object is closed
will raise a ValueError.

This method has no effect if the file is already closed.
```

### closed

```json
{
  "name": "closed",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
No docstring available.
```

### detach

```json
{
  "name": "detach",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Separate the underlying buffer from the TextIOBase and return it.

After the underlying buffer has been detached, the TextIO is in
an unusable state.
```

### encoding

```json
{
  "name": "encoding",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
Encoding of the text stream.

Subclasses should override.
```

### errors

```json
{
  "name": "errors",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": true
}
```

```text
The error setting of the decoder or encoder.

Subclasses should override.
```

### fileno

```json
{
  "name": "fileno",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return underlying file descriptor if one exists.

Raise OSError if the IO object does not use a file descriptor.
```

### flush

```json
{
  "name": "flush",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Flush write buffers, if applicable.

This is not implemented for read-only and non-blocking streams.
```

### getvalue

```json
{
  "name": "getvalue",
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
Retrieve the entire contents of the object.
```

### isatty

```json
{
  "name": "isatty",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return whether this is an 'interactive' stream.

Return False if it can't be determined.
```

### line_buffering

```json
{
  "name": "line_buffering",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
No docstring available.
```

### newlines

```json
{
  "name": "newlines",
  "kind": "getset_descriptor",
  "decorators": [],
  "inherited": false
}
```

```text
Line endings translated so far.

Only line endings translated during reading are considered.

Subclasses should override.
```

### read

```json
{
  "name": "read",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, size=-1, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "size",
      "kind": "positional only",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Read at most size characters, returned as a string.

If the argument is negative or omitted, read until EOF
is reached. Return an empty string at EOF.
```

### readable

```json
{
  "name": "readable",
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
Returns True if the IO object can be read.
```

### readline

```json
{
  "name": "readline",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, size=-1, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "size",
      "kind": "positional only",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Read until newline or EOF.

Returns an empty string if EOF is hit immediately.
```

### readlines

```json
{
  "name": "readlines",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, hint=-1, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hint",
      "kind": "positional only",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a list of lines from the stream.

hint can be specified to control the number of lines read: no more
lines will be read if the total size (in bytes/characters) of all
lines so far exceeds hint.
```

### seek

```json
{
  "name": "seek",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, pos, whence=0, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pos",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "whence",
      "kind": "positional only",
      "annotation": null,
      "default": "0",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Change stream position.

Seek to character offset pos relative to position indicated by
whence:
    0  Start of stream (the default).  pos should be >= 0;
    1  Current position - pos must be 0;
    2  End of stream - pos must be 0.
Returns the new absolute position.
```

### seekable

```json
{
  "name": "seekable",
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
Returns True if the IO object can be seeked.
```

### tell

```json
{
  "name": "tell",
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
Tell the current file position.
```

### truncate

```json
{
  "name": "truncate",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, pos=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "pos",
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
Truncate size to pos.

The pos argument defaults to the current file position, as
returned by tell().  The current file position is unchanged.
Returns the new absolute position.
```

### writable

```json
{
  "name": "writable",
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
Returns True if the IO object can be written.
```

### write

```json
{
  "name": "write",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, s, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "s",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Write string to file.

Returns the number of characters written, which is always equal to
the length of the string.
```

### writelines

```json
{
  "name": "writelines",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, lines, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "lines",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Write a list of lines to stream.

Line separators are not added, so it is usual for each of the
lines provided to have a line separator at the end.
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

## _resolve_char_detection

```json
{
  "name": "_resolve_char_detection",
  "kind": "function",
  "origin": "requests.compat",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
Find supported character detection libraries.
```

## _ver

```json
{
  "name": "_ver",
  "kind": "version_info",
  "origin": null
}
```

```text
sys.version_info

Version information as a named tuple.
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

## builtin_str

```json
{
  "name": "builtin_str",
  "kind": "class",
  "origin": "builtins",
  "signature_error": "no signature found for builtin type <class 'str'>"
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

### __contains__

```json
{
  "name": "__contains__",
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
Return bool(key in self).
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
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "inherited": false,
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
Return a formatted version of the string as described by format_spec.
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
Return self[key].
```

### __getnewargs__

```json
{
  "name": "__getnewargs__",
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
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
Return the size of the string in memory, in bytes.
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

### capitalize

```json
{
  "name": "capitalize",
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
Return a capitalized version of the string.

More specifically, make the first character have upper case and the
rest lower case.
```

### casefold

```json
{
  "name": "casefold",
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
Return a version of the string suitable for caseless comparisons.
```

### center

```json
{
  "name": "center",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a centered string of length width.

Padding is done using the specified fill character (default is
a space).
```

### count

```json
{
  "name": "count",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'count' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the number of non-overlapping occurrences of substring sub in string S[start:end].

Optional arguments start and end are interpreted as in slice
notation.
```

### encode

```json
{
  "name": "encode",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, encoding='utf-8', errors='strict')",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "encoding",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'utf-8'",
      "required": false
    },
    {
      "name": "errors",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'strict'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Encode the string using the codec registered for encoding.

encoding
  The encoding in which to encode the string.
errors
  The error handling scheme to use for encoding errors.
  The default is 'strict' meaning that encoding errors raise a
  UnicodeEncodeError.  Other possible values are 'ignore', 'replace'
  and 'xmlcharrefreplace' as well as any other name registered with
  codecs.register_error that can handle UnicodeEncodeErrors.
```

### endswith

```json
{
  "name": "endswith",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'endswith' of 'str' objects> builtin has invalid signature"
}
```

```text
Return True if the string ends with the specified suffix, False otherwise.

suffix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.
```

### expandtabs

```json
{
  "name": "expandtabs",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, tabsize=8)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "tabsize",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "8",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.
```

### find

```json
{
  "name": "find",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'find' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice
notation.  Return -1 on failure.
```

### format

```json
{
  "name": "format",
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
Return a formatted version of the string, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
```

### format_map

```json
{
  "name": "format_map",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, mapping, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "mapping",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a formatted version of the string, using substitutions from mapping.
The substitutions are identified by braces ('{' and '}').
```

### index

```json
{
  "name": "index",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'index' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice
notation.  Raises ValueError when the substring is not found.
```

### isalnum

```json
{
  "name": "isalnum",
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
Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are
alpha-numeric and there is at least one character in the string.
```

### isalpha

```json
{
  "name": "isalpha",
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
Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are
alphabetic and there is at least one character in the string.
```

### isascii

```json
{
  "name": "isascii",
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
Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.
```

### isdecimal

```json
{
  "name": "isdecimal",
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
Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are
decimal and there is at least one character in the string.
```

### isdigit

```json
{
  "name": "isdigit",
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
Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are
digits and there is at least one character in the string.
```

### isidentifier

```json
{
  "name": "isidentifier",
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
Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved
identifier, such as "def" or "class".
```

### islower

```json
{
  "name": "islower",
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
Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are
lowercase and there is at least one cased character in the string.
```

### isnumeric

```json
{
  "name": "isnumeric",
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
Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and
there is at least one character in the string.
```

### isprintable

```json
{
  "name": "isprintable",
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
Return True if all characters in the string are printable, False otherwise.

A character is printable if repr() may use it in its output.
```

### isspace

```json
{
  "name": "isspace",
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
Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are
whitespace and there is at least one character in the string.
```

### istitle

```json
{
  "name": "istitle",
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
Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.
```

### isupper

```json
{
  "name": "isupper",
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
Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are
uppercase and there is at least one cased character in the string.
```

### join

```json
{
  "name": "join",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, iterable, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "iterable",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Concatenate any number of strings.

The string whose method is called is inserted in between each given
string.  The result is returned as a new string.

Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
```

### ljust

```json
{
  "name": "ljust",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a left-justified string of length width.

Padding is done using the specified fill character (default is
a space).
```

### lower

```json
{
  "name": "lower",
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
Return a copy of the string converted to lowercase.
```

### lstrip

```json
{
  "name": "lstrip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, chars=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chars",
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
Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.
```

### maketrans

```json
{
  "name": "maketrans",
  "kind": "function",
  "decorators": [
    "staticmethod"
  ],
  "inherited": false,
  "inspection_error": "<built-in method maketrans of type object at 0x00007FF8B16AD5B0> builtin has invalid signature"
}
```

```text
Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping
Unicode ordinals (integers) or characters to Unicode ordinals,
strings or None.  Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length,
and in the resulting dictionary, each character in x will be mapped
to the character at the same position in y.  If there is a third
argument, it must be a string, whose characters will be mapped to
None in the result.
```

### partition

```json
{
  "name": "partition",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, sep, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Partition the string into three parts using the given separator.

This will search for the separator in the string.  If the separator
is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing
the original string and two empty strings.
```

### removeprefix

```json
{
  "name": "removeprefix",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, prefix, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prefix",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return
string[len(prefix):].  Otherwise, return a copy of the original
string.
```

### removesuffix

```json
{
  "name": "removesuffix",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, suffix, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "suffix",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not
empty, return string[:-len(suffix)].  Otherwise, return a copy of
the original string.
```

### replace

```json
{
  "name": "replace",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, old, new, /, count=-1)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "old",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "new",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "count",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a copy with all occurrences of substring old replaced by new.

  count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.
```

### rfind

```json
{
  "name": "rfind",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'rfind' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice
notation.  Return -1 on failure.
```

### rindex

```json
{
  "name": "rindex",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'rindex' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice
notation.  Raises ValueError when the substring is not found.
```

### rjust

```json
{
  "name": "rjust",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a right-justified string of length width.

Padding is done using the specified fill character (default is
a space).
```

### rpartition

```json
{
  "name": "rpartition",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, sep, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the
end.  If the separator is found, returns a 3-tuple containing the
part before the separator, the separator itself, and the part after
it.

If the separator is not found, returns a 3-tuple containing two
empty strings and the original string.
```

### rsplit

```json
{
  "name": "rsplit",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, sep=None, maxsplit=-1)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "maxsplit",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any
    whitespace character (including \n \r \t \f and spaces) and
    will discard empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.
```

### rstrip

```json
{
  "name": "rstrip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, chars=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chars",
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
Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.
```

### split

```json
{
  "name": "split",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, sep=None, maxsplit=-1)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "maxsplit",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any
    whitespace character (including \n \r \t \f and spaces) and
    will discard empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been
intentionally delimited.  With natural text that includes
punctuation, consider using the regular expression module.
```

### splitlines

```json
{
  "name": "splitlines",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, keepends=False)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "keepends",
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
Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends
is given and true.
```

### startswith

```json
{
  "name": "startswith",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'startswith' of 'str' objects> builtin has invalid signature"
}
```

```text
Return True if the string starts with the specified prefix, False otherwise.

prefix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.
```

### strip

```json
{
  "name": "strip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, chars=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chars",
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
Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.
```

### swapcase

```json
{
  "name": "swapcase",
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
Convert uppercase characters to lowercase and lowercase characters to uppercase.
```

### title

```json
{
  "name": "title",
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
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all
remaining cased characters have lower case.
```

### translate

```json
{
  "name": "translate",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, table, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "table",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Replace each character in the string using the given translation table.

  table
    Translation table, which must be a mapping of Unicode ordinals
    to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for
instance a dictionary or list.  If this operation raises
LookupError, the character is left untouched.  Characters mapped to
None are deleted.
```

### upper

```json
{
  "name": "upper",
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
Return a copy of the string converted to uppercase.
```

### zfill

```json
{
  "name": "zfill",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.
```

## bytes

```json
{
  "name": "bytes",
  "kind": "class",
  "origin": "builtins",
  "signature_error": "no signature found for builtin type <class 'bytes'>"
}
```

```text
bytes(iterable_of_ints) -> bytes
bytes(string, encoding[, errors]) -> bytes
bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
bytes(int) -> bytes object of size given by the parameter initialized with null bytes
bytes() -> empty bytes object

Construct an immutable array of bytes from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - any object implementing the buffer API.
  - an integer
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

### __buffer__

```json
{
  "name": "__buffer__",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, flags, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "flags",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a buffer object that exposes the underlying memory of the object.
```

### __bytes__

```json
{
  "name": "__bytes__",
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
Convert this value to exact type bytes.
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

### __contains__

```json
{
  "name": "__contains__",
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
Return bool(key in self).
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
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
Return self[key].
```

### __getnewargs__

```json
{
  "name": "__getnewargs__",
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
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### capitalize

```json
{
  "name": "capitalize",
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
B.capitalize() -> copy of B

Return a copy of B with only its first character capitalized (ASCII)
and the rest lower-cased.
```

### center

```json
{
  "name": "center",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=b' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "b' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a centered string of length width.

Padding is done using the specified fill character.
```

### count

```json
{
  "name": "count",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'count' of 'bytes' objects> builtin has invalid signature"
}
```

```text
Return the number of non-overlapping occurrences of subsection 'sub' in bytes B[start:end].

start
  Optional start position. Default: start of the bytes.
end
  Optional stop position. Default: end of the bytes.
```

### decode

```json
{
  "name": "decode",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, encoding='utf-8', errors='strict')",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "encoding",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'utf-8'",
      "required": false
    },
    {
      "name": "errors",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'strict'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Decode the bytes using the codec registered for encoding.

encoding
  The encoding with which to decode the bytes.
errors
  The error handling scheme to use for the handling of decoding
  errors.  The default is 'strict' meaning that decoding errors
  raise a UnicodeDecodeError.  Other possible values are 'ignore'
  and 'replace' as well as any other name registered with
  codecs.register_error that can handle UnicodeDecodeErrors.
```

### endswith

```json
{
  "name": "endswith",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'endswith' of 'bytes' objects> builtin has invalid signature"
}
```

```text
Return True if the bytes ends with the specified suffix, False otherwise.

suffix
  A bytes or a tuple of bytes to try.
start
  Optional start position. Default: start of the bytes.
end
  Optional stop position. Default: end of the bytes.
```

### expandtabs

```json
{
  "name": "expandtabs",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, tabsize=8)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "tabsize",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "8",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.
```

### find

```json
{
  "name": "find",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'find' of 'bytes' objects> builtin has invalid signature"
}
```

```text
Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end].

  start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Return -1 on failure.
```

### fromhex

```json
{
  "name": "fromhex",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(type, string, /)",
  "parameters": [
    {
      "name": "type",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "string",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Create a bytes object from a string of hexadecimal numbers.

Spaces between two numbers are accepted.
Example: bytes.fromhex('B9 01EF') -> b'\\xb9\\x01\\xef'.
```

### hex

```json
{
  "name": "hex",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'hex' of 'bytes' objects> builtin has invalid signature"
}
```

```text
Create a string of hexadecimal numbers from a bytes object.

  sep
    An optional single character or byte to separate hex bytes.
  bytes_per_sep
    How many bytes between separators.  Positive values count from
    the right, negative values count from the left.

Example:
>>> value = b'\xb9\x01\xef'
>>> value.hex()
'b901ef'
>>> value.hex(':')
'b9:01:ef'
>>> value.hex(':', 2)
'b9:01ef'
>>> value.hex(':', -2)
'b901:ef'
```

### index

```json
{
  "name": "index",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'index' of 'bytes' objects> builtin has invalid signature"
}
```

```text
Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end].

  start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Raise ValueError if the subsection is not found.
```

### isalnum

```json
{
  "name": "isalnum",
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
B.isalnum() -> bool

Return True if all characters in B are alphanumeric
and there is at least one character in B, False otherwise.
```

### isalpha

```json
{
  "name": "isalpha",
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
B.isalpha() -> bool

Return True if all characters in B are alphabetic
and there is at least one character in B, False otherwise.
```

### isascii

```json
{
  "name": "isascii",
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
B.isascii() -> bool

Return True if B is empty or all characters in B are ASCII,
False otherwise.
```

### isdigit

```json
{
  "name": "isdigit",
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
B.isdigit() -> bool

Return True if all characters in B are digits
and there is at least one character in B, False otherwise.
```

### islower

```json
{
  "name": "islower",
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
B.islower() -> bool

Return True if all cased characters in B are lowercase and there is
at least one cased character in B, False otherwise.
```

### isspace

```json
{
  "name": "isspace",
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
B.isspace() -> bool

Return True if all characters in B are whitespace
and there is at least one character in B, False otherwise.
```

### istitle

```json
{
  "name": "istitle",
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
B.istitle() -> bool

Return True if B is a titlecased string and there is at least one
character in B, i.e. uppercase characters may only follow uncased
characters and lowercase characters only cased ones. Return False
otherwise.
```

### isupper

```json
{
  "name": "isupper",
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
B.isupper() -> bool

Return True if all cased characters in B are uppercase and there is
at least one cased character in B, False otherwise.
```

### join

```json
{
  "name": "join",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, iterable_of_bytes, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "iterable_of_bytes",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Concatenate any number of bytes objects.

The bytes whose method is called is inserted in between each pair.

The result is returned as a new bytes object.

Example: b'.'.join([b'ab', b'pq', b'rs']) -> b'ab.pq.rs'.
```

### ljust

```json
{
  "name": "ljust",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=b' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "b' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a left-justified string of length width.

Padding is done using the specified fill character.
```

### lower

```json
{
  "name": "lower",
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
B.lower() -> copy of B

Return a copy of B with all ASCII characters converted to lowercase.
```

### lstrip

```json
{
  "name": "lstrip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, bytes=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "bytes",
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
Strip leading bytes contained in the argument.

If the argument is omitted or None, strip leading  ASCII whitespace.
```

### maketrans

```json
{
  "name": "maketrans",
  "kind": "function",
  "decorators": [
    "staticmethod"
  ],
  "inherited": false,
  "signature": "(frm, to, /)",
  "parameters": [
    {
      "name": "frm",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "to",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a translation table usable for the bytes or bytearray translate method.

The returned table will be one where each byte in frm is mapped to
the byte at the same position in to.

The bytes objects frm and to must be of the same length.
```

### partition

```json
{
  "name": "partition",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, sep, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Partition the bytes into three parts using the given separator.

This will search for the separator sep in the bytes.  If the
separator is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the
original bytes object and two empty bytes objects.
```

### removeprefix

```json
{
  "name": "removeprefix",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, prefix, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prefix",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a bytes object with the given prefix string removed if present.

If the bytes starts with the prefix string, return
bytes[len(prefix):].  Otherwise, return a copy of the original
bytes.
```

### removesuffix

```json
{
  "name": "removesuffix",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, suffix, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "suffix",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a bytes object with the given suffix string removed if present.

If the bytes ends with the suffix string and that suffix is not
empty, return bytes[:-len(prefix)].  Otherwise, return a copy of the
original bytes.
```

### replace

```json
{
  "name": "replace",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, old, new, count=-1, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "old",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "new",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "count",
      "kind": "positional only",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a copy with all occurrences of substring old replaced by new.

  count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.
```

### rfind

```json
{
  "name": "rfind",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'rfind' of 'bytes' objects> builtin has invalid signature"
}
```

```text
Return the highest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end].

  start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Return -1 on failure.
```

### rindex

```json
{
  "name": "rindex",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'rindex' of 'bytes' objects> builtin has invalid signature"
}
```

```text
Return the highest index in B where subsection 'sub' is found, such that 'sub' is contained within B[start,end].

  start
    Optional start position. Default: start of the bytes.
  end
    Optional stop position. Default: end of the bytes.

Raise ValueError if the subsection is not found.
```

### rjust

```json
{
  "name": "rjust",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=b' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "b' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a right-justified string of length width.

Padding is done using the specified fill character.
```

### rpartition

```json
{
  "name": "rpartition",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, sep, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Partition the bytes into three parts using the given separator.

This will search for the separator sep in the bytes, starting at the
end.  If the separator is found, returns a 3-tuple containing the
part before the separator, the separator itself, and the part after
it.

If the separator is not found, returns a 3-tuple containing two
empty bytes objects and the original bytes object.
```

### rsplit

```json
{
  "name": "rsplit",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, sep=None, maxsplit=-1)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "maxsplit",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a list of the sections in the bytes, using sep as the delimiter.

  sep
    The delimiter according which to split the bytes.
    None (the default value) means split on ASCII whitespace
    characters (space, tab, return, newline, formfeed, vertical tab).
  maxsplit
    Maximum number of splits to do.
    -1 (the default value) means no limit.

Splitting is done starting at the end of the bytes and working to
the front.
```

### rstrip

```json
{
  "name": "rstrip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, bytes=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "bytes",
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
Strip trailing bytes contained in the argument.

If the argument is omitted or None, strip trailing ASCII whitespace.
```

### split

```json
{
  "name": "split",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, sep=None, maxsplit=-1)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "maxsplit",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a list of the sections in the bytes, using sep as the delimiter.

sep
  The delimiter according which to split the bytes.
  None (the default value) means split on ASCII whitespace
  characters (space, tab, return, newline, formfeed, vertical tab).
maxsplit
  Maximum number of splits to do.
  -1 (the default value) means no limit.
```

### splitlines

```json
{
  "name": "splitlines",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, keepends=False)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "keepends",
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
Return a list of the lines in the bytes, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends
is given and true.
```

### startswith

```json
{
  "name": "startswith",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'startswith' of 'bytes' objects> builtin has invalid signature"
}
```

```text
Return True if the bytes starts with the specified prefix, False otherwise.

prefix
  A bytes or a tuple of bytes to try.
start
  Optional start position. Default: start of the bytes.
end
  Optional stop position. Default: end of the bytes.
```

### strip

```json
{
  "name": "strip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, bytes=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "bytes",
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
Strip leading and trailing bytes contained in the argument.

If the argument is omitted or None, strip leading and trailing ASCII
whitespace.
```

### swapcase

```json
{
  "name": "swapcase",
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
B.swapcase() -> copy of B

Return a copy of B with uppercase ASCII characters converted
to lowercase ASCII and vice versa.
```

### title

```json
{
  "name": "title",
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
B.title() -> copy of B

Return a titlecased version of B, i.e. ASCII words start with
uppercase characters, all remaining cased characters have lowercase.
```

### translate

```json
{
  "name": "translate",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, table, /, delete=b'')",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "table",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "delete",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "b''",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a copy with each character mapped by the given translation table.

  table
    Translation table, which must be a bytes object of length 256.

All characters occurring in the optional argument delete are
removed.  The remaining characters are mapped through the given
translation table.
```

### upper

```json
{
  "name": "upper",
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
B.upper() -> copy of B

Return a copy of B with all ASCII characters converted to uppercase.
```

### zfill

```json
{
  "name": "zfill",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Pad a numeric string with zeros on the left, to fill a field of the given width.

The original string is never truncated.
```

## chardet

```json
{
  "name": "chardet",
  "kind": "module",
  "origin": null
}
```

```text
Charset-Normalizer
~~~~~~~~~~~~~~
The Real First Universal Charset Detector.
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, This package is trying to resolve the issue by taking a new approach.
All IANA character set names for which the Python core library provides codecs are supported.

Basic usage:
   >>> from charset_normalizer import from_bytes
   >>> results = from_bytes('Bсеки човек има право на образование. Oбразованието!'.encode('utf_8'))
   >>> best_guess = results.best()
   >>> str(best_guess)
   'Bсеки човек има право на образование. Oбразованието!'

Others methods and usages are available - see the full documentation
at <https://github.com/Ousret/charset_normalizer>.
:copyright: (c) Ahmed TAHRI
:license: MIT, see LICENSE for more details.
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

## getproxies

```json
{
  "name": "getproxies",
  "kind": "function",
  "origin": "urllib.request",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
Return a dictionary of scheme -> proxy server URL mappings.

Returns settings gathered from the environment, if specified,
or the registry.
```

## getproxies_environment

```json
{
  "name": "getproxies_environment",
  "kind": "function",
  "origin": "urllib.request",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
Return a dictionary of scheme -> proxy server URL mappings.

Scan the environment for variables named <scheme>_proxy;
this seems to be the standard convention.
```

## has_simplejson

```json
{
  "name": "has_simplejson",
  "kind": "bool",
  "origin": null
}
```

```text
Returns True when the argument is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.
```

## importlib

```json
{
  "name": "importlib",
  "kind": "module",
  "origin": null
}
```

```text
A pure Python implementation of import.
```

## integer_types

```json
{
  "name": "integer_types",
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

## is_py2

```json
{
  "name": "is_py2",
  "kind": "bool",
  "origin": null
}
```

```text
Returns True when the argument is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.
```

## is_py3

```json
{
  "name": "is_py3",
  "kind": "bool",
  "origin": null
}
```

```text
Returns True when the argument is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.
```

## json

```json
{
  "name": "json",
  "kind": "module",
  "origin": null
}
```

```text
JSON (JavaScript Object Notation) <https://json.org> is a subset of
JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
interchange format.

:mod:`json` exposes an API familiar to users of the standard library
:mod:`marshal` and :mod:`pickle` modules.  It is derived from a
version of the externally maintained simplejson library.

Encoding basic Python object hierarchies::

    >>> import json
    >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    '["foo", {"bar": ["baz", null, 1.0, 2]}]'
    >>> print(json.dumps("\"foo\bar"))
    "\"foo\bar"
    >>> print(json.dumps('\u1234'))
    "\u1234"
    >>> print(json.dumps('\\'))
    "\\"
    >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
    {"a": 0, "b": 0, "c": 0}
    >>> from io import StringIO
    >>> io = StringIO()
    >>> json.dump(['streaming API'], io)
    >>> io.getvalue()
    '["streaming API"]'

Compact encoding::

    >>> import json
    >>> mydict = {'4': 5, '6': 7}
    >>> json.dumps([1,2,3,mydict], separators=(',', ':'))
    '[1,2,3,{"4":5,"6":7}]'

Pretty printing::

    >>> import json
    >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
    {
        "4": 5,
        "6": 7
    }

Decoding JSON::

    >>> import json
    >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
    >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
    True
    >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
    True
    >>> from io import StringIO
    >>> io = StringIO('["streaming API"]')
    >>> json.load(io)[0] == 'streaming API'
    True

Specializing JSON object decoding::

    >>> import json
    >>> def as_complex(dct):
    ...     if '__complex__' in dct:
    ...         return complex(dct['real'], dct['imag'])
    ...     return dct
    ...
    >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
    ...     object_hook=as_complex)
    (1+2j)
    >>> from decimal import Decimal
    >>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
    True

Specializing JSON object encoding::

    >>> import json
    >>> def encode_complex(obj):
    ...     if isinstance(obj, complex):
    ...         return [obj.real, obj.imag]
    ...     raise TypeError(f'Object of type {obj.__class__.__name__} '
    ...                     f'is not JSON serializable')
    ...
    >>> json.dumps(2 + 1j, default=encode_complex)
    '[2.0, 1.0]'
    >>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
    '[2.0, 1.0]'
    >>> ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
    '[2.0, 1.0]'


Using json from the shell to validate and pretty-print::

    $ echo '{"json":"obj"}' | python -m json
    {
        "json": "obj"
    }
    $ echo '{ 1.2:3.4}' | python -m json
    Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
```

## numeric_types

```json
{
  "name": "numeric_types",
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

## parse_http_list

```json
{
  "name": "parse_http_list",
  "kind": "function",
  "origin": "urllib.request",
  "signature": "(s)",
  "parameters": [
    {
      "name": "s",
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
Parse lists as described by RFC 2068 Section 2.

In particular, parse comma-separated lists where the elements of
the list may include quoted-strings.  A quoted-string could
contain a comma.  A non-quoted string could have quotes in the
middle.  Neither commas nor quotes count if they are escaped.
Only double-quotes count, not single-quotes.
```

## proxy_bypass

```json
{
  "name": "proxy_bypass",
  "kind": "function",
  "origin": "urllib.request",
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
Return True, if host should be bypassed.

Checks proxy settings gathered from the environment, if specified,
or the registry.
```

## proxy_bypass_environment

```json
{
  "name": "proxy_bypass_environment",
  "kind": "function",
  "origin": "urllib.request",
  "signature": "(host, proxies=None)",
  "parameters": [
    {
      "name": "host",
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
Test if proxies should not be used for a particular host.

Checks the proxy dict for the value of no_proxy, which should
be a list of comma separated DNS suffixes, or '*' for all hosts.
```

## quote

```json
{
  "name": "quote",
  "kind": "function",
  "origin": "urllib.parse",
  "signature": "(string, safe='/', encoding=None, errors=None)",
  "parameters": [
    {
      "name": "string",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "safe",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'/'",
      "required": false
    },
    {
      "name": "encoding",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "errors",
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
quote('abc def') -> 'abc%20def'

Each part of a URL, e.g. the path info, the query, etc., has a
different set of reserved characters that must be quoted. The
quote function offers a cautious (not minimal) way to quote a
string for most of these parts.

RFC 3986 Uniform Resource Identifier (URI): Generic Syntax lists
the following (un)reserved characters.

unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
reserved      = gen-delims / sub-delims
gen-delims    = ":" / "/" / "?" / "#" / "[" / "]" / "@"
sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
              / "*" / "+" / "," / ";" / "="

Each of the reserved characters is reserved in some component of a URL,
but not necessarily in all of them.

The quote function %-escapes all characters that are neither in the
unreserved chars ("always safe") nor the additional chars set via the
safe arg.

The default for the safe arg is '/'. The character is reserved, but in
typical usage the quote function is being called on a path where the
existing slash characters are to be preserved.

Python 3.7 updates from using RFC 2396 to RFC 3986 to quote URL strings.
Now, "~" is included in the set of unreserved characters.

string and safe may be either str or bytes objects. encoding and errors
must not be specified if string is a bytes object.

The optional encoding and errors parameters specify how to deal with
non-ASCII characters, as accepted by the str.encode method.
By default, encoding='utf-8' (characters are encoded with UTF-8), and
errors='strict' (unsupported characters raise a UnicodeEncodeError).
```

## quote_plus

```json
{
  "name": "quote_plus",
  "kind": "function",
  "origin": "urllib.parse",
  "signature": "(string, safe='', encoding=None, errors=None)",
  "parameters": [
    {
      "name": "string",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "safe",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "''",
      "required": false
    },
    {
      "name": "encoding",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "errors",
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
Like quote(), but also replace ' ' with '+', as required for quoting
HTML form values. Plus signs in the original string are escaped unless
they are included in safe. It also does not have safe default to '/'.
```

## str

```json
{
  "name": "str",
  "kind": "class",
  "origin": "builtins",
  "signature_error": "no signature found for builtin type <class 'str'>"
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

### __contains__

```json
{
  "name": "__contains__",
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
Return bool(key in self).
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
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "inherited": false,
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
Return a formatted version of the string as described by format_spec.
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
Return self[key].
```

### __getnewargs__

```json
{
  "name": "__getnewargs__",
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
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
Return the size of the string in memory, in bytes.
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

### capitalize

```json
{
  "name": "capitalize",
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
Return a capitalized version of the string.

More specifically, make the first character have upper case and the
rest lower case.
```

### casefold

```json
{
  "name": "casefold",
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
Return a version of the string suitable for caseless comparisons.
```

### center

```json
{
  "name": "center",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a centered string of length width.

Padding is done using the specified fill character (default is
a space).
```

### count

```json
{
  "name": "count",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'count' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the number of non-overlapping occurrences of substring sub in string S[start:end].

Optional arguments start and end are interpreted as in slice
notation.
```

### encode

```json
{
  "name": "encode",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, encoding='utf-8', errors='strict')",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "encoding",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'utf-8'",
      "required": false
    },
    {
      "name": "errors",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'strict'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Encode the string using the codec registered for encoding.

encoding
  The encoding in which to encode the string.
errors
  The error handling scheme to use for encoding errors.
  The default is 'strict' meaning that encoding errors raise a
  UnicodeEncodeError.  Other possible values are 'ignore', 'replace'
  and 'xmlcharrefreplace' as well as any other name registered with
  codecs.register_error that can handle UnicodeEncodeErrors.
```

### endswith

```json
{
  "name": "endswith",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'endswith' of 'str' objects> builtin has invalid signature"
}
```

```text
Return True if the string ends with the specified suffix, False otherwise.

suffix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.
```

### expandtabs

```json
{
  "name": "expandtabs",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, tabsize=8)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "tabsize",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "8",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.
```

### find

```json
{
  "name": "find",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'find' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice
notation.  Return -1 on failure.
```

### format

```json
{
  "name": "format",
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
Return a formatted version of the string, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
```

### format_map

```json
{
  "name": "format_map",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, mapping, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "mapping",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a formatted version of the string, using substitutions from mapping.
The substitutions are identified by braces ('{' and '}').
```

### index

```json
{
  "name": "index",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'index' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice
notation.  Raises ValueError when the substring is not found.
```

### isalnum

```json
{
  "name": "isalnum",
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
Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are
alpha-numeric and there is at least one character in the string.
```

### isalpha

```json
{
  "name": "isalpha",
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
Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are
alphabetic and there is at least one character in the string.
```

### isascii

```json
{
  "name": "isascii",
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
Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F.
Empty string is ASCII too.
```

### isdecimal

```json
{
  "name": "isdecimal",
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
Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are
decimal and there is at least one character in the string.
```

### isdigit

```json
{
  "name": "isdigit",
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
Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are
digits and there is at least one character in the string.
```

### isidentifier

```json
{
  "name": "isidentifier",
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
Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved
identifier, such as "def" or "class".
```

### islower

```json
{
  "name": "islower",
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
Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are
lowercase and there is at least one cased character in the string.
```

### isnumeric

```json
{
  "name": "isnumeric",
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
Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and
there is at least one character in the string.
```

### isprintable

```json
{
  "name": "isprintable",
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
Return True if all characters in the string are printable, False otherwise.

A character is printable if repr() may use it in its output.
```

### isspace

```json
{
  "name": "isspace",
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
Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are
whitespace and there is at least one character in the string.
```

### istitle

```json
{
  "name": "istitle",
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
Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only
follow uncased characters and lowercase characters only cased ones.
```

### isupper

```json
{
  "name": "isupper",
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
Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are
uppercase and there is at least one cased character in the string.
```

### join

```json
{
  "name": "join",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, iterable, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "iterable",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Concatenate any number of strings.

The string whose method is called is inserted in between each given
string.  The result is returned as a new string.

Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
```

### ljust

```json
{
  "name": "ljust",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a left-justified string of length width.

Padding is done using the specified fill character (default is
a space).
```

### lower

```json
{
  "name": "lower",
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
Return a copy of the string converted to lowercase.
```

### lstrip

```json
{
  "name": "lstrip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, chars=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chars",
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
Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.
```

### maketrans

```json
{
  "name": "maketrans",
  "kind": "function",
  "decorators": [
    "staticmethod"
  ],
  "inherited": false,
  "inspection_error": "<built-in method maketrans of type object at 0x00007FF8B16AD5B0> builtin has invalid signature"
}
```

```text
Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping
Unicode ordinals (integers) or characters to Unicode ordinals,
strings or None.  Character keys will be then converted to ordinals.
If there are two arguments, they must be strings of equal length,
and in the resulting dictionary, each character in x will be mapped
to the character at the same position in y.  If there is a third
argument, it must be a string, whose characters will be mapped to
None in the result.
```

### partition

```json
{
  "name": "partition",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, sep, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Partition the string into three parts using the given separator.

This will search for the separator in the string.  If the separator
is found, returns a 3-tuple containing the part before the
separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing
the original string and two empty strings.
```

### removeprefix

```json
{
  "name": "removeprefix",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, prefix, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "prefix",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return
string[len(prefix):].  Otherwise, return a copy of the original
string.
```

### removesuffix

```json
{
  "name": "removesuffix",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, suffix, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "suffix",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not
empty, return string[:-len(suffix)].  Otherwise, return a copy of
the original string.
```

### replace

```json
{
  "name": "replace",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, old, new, /, count=-1)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "old",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "new",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "count",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a copy with all occurrences of substring old replaced by new.

  count
    Maximum number of occurrences to replace.
    -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are
replaced.
```

### rfind

```json
{
  "name": "rfind",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'rfind' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice
notation.  Return -1 on failure.
```

### rindex

```json
{
  "name": "rindex",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'rindex' of 'str' objects> builtin has invalid signature"
}
```

```text
Return the highest index in S where substring sub is found, such that sub is contained within S[start:end].

Optional arguments start and end are interpreted as in slice
notation.  Raises ValueError when the substring is not found.
```

### rjust

```json
{
  "name": "rjust",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, fillchar=' ', /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fillchar",
      "kind": "positional only",
      "annotation": null,
      "default": "' '",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a right-justified string of length width.

Padding is done using the specified fill character (default is
a space).
```

### rpartition

```json
{
  "name": "rpartition",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, sep, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the
end.  If the separator is found, returns a 3-tuple containing the
part before the separator, the separator itself, and the part after
it.

If the separator is not found, returns a 3-tuple containing two
empty strings and the original string.
```

### rsplit

```json
{
  "name": "rsplit",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, sep=None, maxsplit=-1)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "maxsplit",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any
    whitespace character (including \n \r \t \f and spaces) and
    will discard empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.
```

### rstrip

```json
{
  "name": "rstrip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, chars=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chars",
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
Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.
```

### split

```json
{
  "name": "split",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, sep=None, maxsplit=-1)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "sep",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "maxsplit",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "-1",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any
    whitespace character (including \n \r \t \f and spaces) and
    will discard empty strings from the result.
  maxsplit
    Maximum number of splits.
    -1 (the default value) means no limit.

Splitting starts at the front of the string and works to the end.

Note, str.split() is mainly useful for data that has been
intentionally delimited.  With natural text that includes
punctuation, consider using the regular expression module.
```

### splitlines

```json
{
  "name": "splitlines",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, /, keepends=False)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "keepends",
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
Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends
is given and true.
```

### startswith

```json
{
  "name": "startswith",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "inspection_error": "<method 'startswith' of 'str' objects> builtin has invalid signature"
}
```

```text
Return True if the string starts with the specified prefix, False otherwise.

prefix
  A string or a tuple of strings to try.
start
  Optional start position. Default: start of the string.
end
  Optional stop position. Default: end of the string.
```

### strip

```json
{
  "name": "strip",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, chars=None, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "chars",
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
Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.
```

### swapcase

```json
{
  "name": "swapcase",
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
Convert uppercase characters to lowercase and lowercase characters to uppercase.
```

### title

```json
{
  "name": "title",
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
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all
remaining cased characters have lower case.
```

### translate

```json
{
  "name": "translate",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, table, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "table",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Replace each character in the string using the given translation table.

  table
    Translation table, which must be a mapping of Unicode ordinals
    to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via __getitem__, for
instance a dictionary or list.  If this operation raises
LookupError, the character is left untouched.  Characters mapped to
None are deleted.
```

### upper

```json
{
  "name": "upper",
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
Return a copy of the string converted to uppercase.
```

### zfill

```json
{
  "name": "zfill",
  "kind": "function",
  "decorators": [],
  "inherited": false,
  "signature": "(self, width, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "width",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.
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

## unquote

```json
{
  "name": "unquote",
  "kind": "function",
  "origin": "urllib.parse",
  "signature": "(string, encoding='utf-8', errors='replace')",
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
      "default": "'utf-8'",
      "required": false
    },
    {
      "name": "errors",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'replace'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Replace %xx escapes by their single-character equivalent. The optional
encoding and errors parameters specify how to decode percent-encoded
sequences into Unicode characters, as accepted by the bytes.decode()
method.
By default, percent-encoded sequences are decoded with UTF-8, and invalid
sequences are replaced by a placeholder character.

unquote('abc%20def') -> 'abc def'.
```

## unquote_plus

```json
{
  "name": "unquote_plus",
  "kind": "function",
  "origin": "urllib.parse",
  "signature": "(string, encoding='utf-8', errors='replace')",
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
      "default": "'utf-8'",
      "required": false
    },
    {
      "name": "errors",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "'replace'",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Like unquote(), but also replace plus signs by spaces, as required for
unquoting HTML form values.

unquote_plus('%7e/abc+def') -> '~/abc def'
```

## urldefrag

```json
{
  "name": "urldefrag",
  "kind": "function",
  "origin": "urllib.parse",
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
Removes any existing fragment from URL.

Returns a tuple of the defragmented URL and the fragment.  If
the URL contained no fragments, the second element is the
empty string.
```

## urlencode

```json
{
  "name": "urlencode",
  "kind": "function",
  "origin": "urllib.parse",
  "signature": "(query, doseq=False, safe='', encoding=None, errors=None, quote_via=<function quote_plus at 0x00000163C8A7FA00>)",
  "parameters": [
    {
      "name": "query",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "doseq",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "False",
      "required": false
    },
    {
      "name": "safe",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "''",
      "required": false
    },
    {
      "name": "encoding",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "errors",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "quote_via",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "<function quote_plus at 0x00000163C8A7FA00>",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Encode a dict or sequence of two-element tuples into a URL query string.

If any values in the query arg are sequences and doseq is true, each
sequence element is converted to a separate parameter.

If the query arg is a sequence of two-element tuples, the order of the
parameters in the output will match the order of parameters in the
input.

The components of a query arg may each be either a string or a bytes type.

The safe, encoding, and errors parameters are passed down to the function
specified by quote_via (encoding and errors only if a component is a str).
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

## urlsplit

```json
{
  "name": "urlsplit",
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
Parse a URL into 5 components:
<scheme>://<netloc>/<path>?<query>#<fragment>

The result is a named 5-tuple with fields corresponding to the
above. It is either a SplitResult or SplitResultBytes object,
depending on the type of the url parameter.

The username, password, hostname, and port sub-components of netloc
can also be accessed as attributes of the returned object.

The scheme argument provides the default value of the scheme
component when no scheme is found in url.

If allow_fragments is False, no attempt is made to separate the
fragment component from the previous component, which can be either
path or query.

Note that % escapes are not expanded.
```

## urlunparse

```json
{
  "name": "urlunparse",
  "kind": "function",
  "origin": "urllib.parse",
  "signature": "(components)",
  "parameters": [
    {
      "name": "components",
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
Put a parsed URL back together again.  This may result in a
slightly different, but equivalent URL, if the URL that was parsed
originally had redundant delimiters, e.g. a ? with an empty query
(the draft states that these are equivalent).
```
