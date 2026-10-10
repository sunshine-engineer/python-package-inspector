# Runtime: os.path

```text
Common pathname manipulations, WindowsNT/95 version.

Instead of importing this module directly, import os and refer to this
module as os.path.
```

## ALLOW_MISSING

```json
{
  "name": "ALLOW_MISSING",
  "kind": "ALLOW_MISSING",
  "origin": "genericpath"
}
```

```text
Special value for use in realpath().
```

## _LCMAP_LOWERCASE

```json
{
  "name": "_LCMAP_LOWERCASE",
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

## _LCMapStringEx

```json
{
  "name": "_LCMapStringEx",
  "kind": "function",
  "origin": "_winapi",
  "signature": "(locale, flags, src)",
  "parameters": [
    {
      "name": "locale",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "flags",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "src",
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

## _LOCALE_NAME_INVARIANT

```json
{
  "name": "_LOCALE_NAME_INVARIANT",
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

## __all__

```json
{
  "name": "__all__",
  "kind": "list",
  "origin": null
}
```

```text
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
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
  "kind": "class",
  "origin": "_frozen_importlib",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
Meta path import for frozen modules.

All methods are either class or static methods to avoid the need to
instantiate the class.
```

### _ORIGIN

```json
{
  "name": "_ORIGIN",
  "kind": "str",
  "binding": null,
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

### _SEP

```json
{
  "name": "_SEP",
  "kind": "str",
  "binding": null,
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

### __class__

```json
{
  "name": "__class__",
  "kind": "getset_descriptor",
  "binding": null,
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
  "binding": "instance",
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
  "binding": null,
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "binding": null,
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "binding": null,
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
  "binding": "instance",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "binding": "instance",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "binding": "instance",
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
  "binding": "instance",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "binding": null,
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "binding": "instance",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "binding": "instance",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "binding": "instance",
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "binding": null,
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
  "binding": "instance",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "binding": "instance",
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
  "binding": null,
  "decorators": [],
  "inherited": false
}
```

```text
list of weak references to the object
```

### _fix_up_module

```json
{
  "name": "_fix_up_module",
  "kind": "function",
  "binding": "class",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(cls, module)",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "module",
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

### _resolve_filename

```json
{
  "name": "_resolve_filename",
  "kind": "function",
  "binding": "class",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(cls, fullname, alias=None, ispkg=False)",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fullname",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "alias",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "ispkg",
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
No docstring available.
```

### create_module

```json
{
  "name": "create_module",
  "kind": "function",
  "binding": "static",
  "decorators": [
    "staticmethod"
  ],
  "inherited": false,
  "signature": "(spec)",
  "parameters": [
    {
      "name": "spec",
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
Set __file__, if able.
```

### exec_module

```json
{
  "name": "exec_module",
  "kind": "function",
  "binding": "static",
  "decorators": [
    "staticmethod"
  ],
  "inherited": false,
  "signature": "(module)",
  "parameters": [
    {
      "name": "module",
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

### find_spec

```json
{
  "name": "find_spec",
  "kind": "function",
  "binding": "class",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(cls, fullname, path=None, target=None)",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fullname",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "path",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "None",
      "required": false
    },
    {
      "name": "target",
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

### get_code

```json
{
  "name": "get_code",
  "kind": "function",
  "binding": "class",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(self, fullname)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fullname",
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
Return the code object for the frozen module.
```

### get_source

```json
{
  "name": "get_source",
  "kind": "function",
  "binding": "class",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(self, fullname)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fullname",
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
Return None as frozen modules do not have source code.
```

### is_package

```json
{
  "name": "is_package",
  "kind": "function",
  "binding": "class",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(self, fullname)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fullname",
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
Return True if the frozen module is a package.
```

### load_module

```json
{
  "name": "load_module",
  "kind": "function",
  "binding": "class",
  "decorators": [
    "classmethod"
  ],
  "inherited": false,
  "signature": "(cls, fullname)",
  "parameters": [
    {
      "name": "cls",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fullname",
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
Load a frozen module.

This method is deprecated.  Use exec_module() instead.
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

## _findfirstfile

```json
{
  "name": "_findfirstfile",
  "kind": "function",
  "origin": "nt",
  "signature": "(path, /)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
A function to get the real file name without accessing the file in Windows.
```

## _get_bothseps

```json
{
  "name": "_get_bothseps",
  "kind": "function",
  "origin": "ntpath",
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
No docstring available.
```

## _getfinalpathname

```json
{
  "name": "_getfinalpathname",
  "kind": "function",
  "origin": "nt",
  "signature": "(path, /)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    }
  ],
  "returns": null
}
```

```text
A helper function for samepath on windows.
```

## _getfinalpathname_nonstrict

```json
{
  "name": "_getfinalpathname_nonstrict",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(path, ignored_error=<class 'OSError'>)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "ignored_error",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "<class 'OSError'>",
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

## _getfullpathname

```json
{
  "name": "_getfullpathname",
  "kind": "function",
  "origin": "nt",
  "signature": "(path, /)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional only",
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

## _getvolumepathname

```json
{
  "name": "_getvolumepathname",
  "kind": "function",
  "origin": "nt",
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
A helper function for ismount on Win32.
```

## _isreservedname

```json
{
  "name": "_isreservedname",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(name)",
  "parameters": [
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
Return true if the filename is reserved by the system.
```

## _nt_readlink

```json
{
  "name": "_nt_readlink",
  "kind": "function",
  "origin": "nt",
  "signature": "(path, *, dir_fd=None)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "dir_fd",
      "kind": "keyword only",
      "annotation": null,
      "default": "None",
      "required": false
    }
  ],
  "returns": null
}
```

```text
Return a string representing the path to which the symbolic link points.

If dir_fd is not None, it should be a file descriptor open to
a directory, and path should be relative; path will then be relative to
that directory.

dir_fd may not be implemented on your platform.  If it is unavailable,
using it will raise a NotImplementedError.
```

## _path_isdevdrive

```json
{
  "name": "_path_isdevdrive",
  "kind": "function",
  "origin": "nt",
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
Determines whether the specified path is on a Windows Dev Drive.
```

## _readlink_deep

```json
{
  "name": "_readlink_deep",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(path, ignored_error=<class 'OSError'>)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "ignored_error",
      "kind": "positional or keyword",
      "annotation": null,
      "default": "<class 'OSError'>",
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

## _reserved_chars

```json
{
  "name": "_reserved_chars",
  "kind": "frozenset",
  "origin": null
}
```

```text
Build an immutable unordered collection of unique elements.
```

## _reserved_names

```json
{
  "name": "_reserved_names",
  "kind": "frozenset",
  "origin": null
}
```

```text
Build an immutable unordered collection of unique elements.
```

## _varpattern

```json
{
  "name": "_varpattern",
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

## _varsub

```json
{
  "name": "_varsub",
  "kind": "NoneType",
  "origin": null
}
```

```text
The type of the None singleton.
```

## _varsubb

```json
{
  "name": "_varsubb",
  "kind": "NoneType",
  "origin": null
}
```

```text
The type of the None singleton.
```

## abspath

```json
{
  "name": "abspath",
  "kind": "function",
  "origin": "ntpath",
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
Return the absolute version of a path.
```

## altsep

```json
{
  "name": "altsep",
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

## basename

```json
{
  "name": "basename",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(p)",
  "parameters": [
    {
      "name": "p",
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
Returns the final component of a pathname
```

## commonpath

```json
{
  "name": "commonpath",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(paths)",
  "parameters": [
    {
      "name": "paths",
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
Given an iterable of path names, returns the longest common sub-path.
```

## commonprefix

```json
{
  "name": "commonprefix",
  "kind": "function",
  "origin": "genericpath",
  "signature": "(m)",
  "parameters": [
    {
      "name": "m",
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
Given a list of pathnames, returns the longest common leading component
```

## curdir

```json
{
  "name": "curdir",
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

## defpath

```json
{
  "name": "defpath",
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

## devnull

```json
{
  "name": "devnull",
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

## dirname

```json
{
  "name": "dirname",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(p)",
  "parameters": [
    {
      "name": "p",
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
Returns the directory component of a pathname
```

## exists

```json
{
  "name": "exists",
  "kind": "function",
  "origin": "nt",
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
Test whether a path exists.  Returns False for broken symbolic links.
```

## expanduser

```json
{
  "name": "expanduser",
  "kind": "function",
  "origin": "ntpath",
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
Expand ~ and ~user constructs.

If user or home directory is unknown, do nothing.
```

## expandvars

```json
{
  "name": "expandvars",
  "kind": "function",
  "origin": "ntpath",
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
Expand shell variables of the forms $var, ${var} and %var%.

Unknown variables are left unchanged.
```

## extsep

```json
{
  "name": "extsep",
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

## genericpath

```json
{
  "name": "genericpath",
  "kind": "module",
  "origin": null
}
```

```text
Path operations common to more than one OS
Do not use directly.  The OS specific modules import the appropriate
functions from this module themselves.
```

## getatime

```json
{
  "name": "getatime",
  "kind": "function",
  "origin": "genericpath",
  "signature": "(filename)",
  "parameters": [
    {
      "name": "filename",
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
Return the last access time of a file, reported by os.stat().
```

## getctime

```json
{
  "name": "getctime",
  "kind": "function",
  "origin": "genericpath",
  "signature": "(filename)",
  "parameters": [
    {
      "name": "filename",
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
Return the metadata change time of a file, reported by os.stat().
```

## getmtime

```json
{
  "name": "getmtime",
  "kind": "function",
  "origin": "genericpath",
  "signature": "(filename)",
  "parameters": [
    {
      "name": "filename",
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
Return the last modification time of a file, reported by os.stat().
```

## getsize

```json
{
  "name": "getsize",
  "kind": "function",
  "origin": "genericpath",
  "signature": "(filename)",
  "parameters": [
    {
      "name": "filename",
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
Return the size of a file, reported by os.stat().
```

## isabs

```json
{
  "name": "isabs",
  "kind": "function",
  "origin": "ntpath",
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
Test whether a path is absolute
```

## isdevdrive

```json
{
  "name": "isdevdrive",
  "kind": "function",
  "origin": "ntpath",
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
Determines whether the specified path is on a Windows Dev Drive.
```

## isdir

```json
{
  "name": "isdir",
  "kind": "function",
  "origin": "nt",
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
Return true if the pathname refers to an existing directory.
```

## isfile

```json
{
  "name": "isfile",
  "kind": "function",
  "origin": "nt",
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
Test whether a path is a regular file
```

## isjunction

```json
{
  "name": "isjunction",
  "kind": "function",
  "origin": "nt",
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
Test whether a path is a junction
```

## islink

```json
{
  "name": "islink",
  "kind": "function",
  "origin": "nt",
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
Test whether a path is a symbolic link
```

## ismount

```json
{
  "name": "ismount",
  "kind": "function",
  "origin": "ntpath",
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
Test whether a path is a mount point (a drive root, the root of a
share, or a mounted volume)
```

## isreserved

```json
{
  "name": "isreserved",
  "kind": "function",
  "origin": "ntpath",
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
Return true if the pathname is reserved by the system.
```

## join

```json
{
  "name": "join",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(path, *paths)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "paths",
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

## lexists

```json
{
  "name": "lexists",
  "kind": "function",
  "origin": "nt",
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
Test whether a path exists.  Returns True for broken symbolic links.
```

## normcase

```json
{
  "name": "normcase",
  "kind": "function",
  "origin": "ntpath",
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
Normalize case of pathname.

Makes all characters lowercase and all slashes into backslashes.
```

## normpath

```json
{
  "name": "normpath",
  "kind": "function",
  "origin": "nt",
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
Normalize path, eliminating double slashes, etc.
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

## pardir

```json
{
  "name": "pardir",
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

## pathsep

```json
{
  "name": "pathsep",
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

## realpath

```json
{
  "name": "realpath",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(path, *, strict=False)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "strict",
      "kind": "keyword only",
      "annotation": null,
      "default": "False",
      "required": false
    }
  ],
  "returns": null
}
```

```text
No docstring available.
```

## relpath

```json
{
  "name": "relpath",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(path, start=None)",
  "parameters": [
    {
      "name": "path",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "start",
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
Return a relative version of a path
```

## samefile

```json
{
  "name": "samefile",
  "kind": "function",
  "origin": "genericpath",
  "signature": "(f1, f2)",
  "parameters": [
    {
      "name": "f1",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "f2",
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
Test whether two pathnames reference the same actual file or directory

This is determined by the device number and i-node number and
raises an exception if an os.stat() call on either pathname fails.
```

## sameopenfile

```json
{
  "name": "sameopenfile",
  "kind": "function",
  "origin": "genericpath",
  "signature": "(fp1, fp2)",
  "parameters": [
    {
      "name": "fp1",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "fp2",
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
Test whether two open file objects reference the same file
```

## samestat

```json
{
  "name": "samestat",
  "kind": "function",
  "origin": "genericpath",
  "signature": "(s1, s2)",
  "parameters": [
    {
      "name": "s1",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "s2",
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
Test whether two stat buffers reference the same file
```

## sep

```json
{
  "name": "sep",
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

## split

```json
{
  "name": "split",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(p)",
  "parameters": [
    {
      "name": "p",
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
Split a pathname.

Return tuple (head, tail) where tail is everything after the final
slash.  Either part may be empty.
```

## splitdrive

```json
{
  "name": "splitdrive",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(p)",
  "parameters": [
    {
      "name": "p",
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
Split a pathname into drive/UNC sharepoint and relative path specifiers.
Returns a 2-tuple (drive_or_unc, path); either part may be empty.

If you assign
    result = splitdrive(p)
It is always true that:
    result[0] + result[1] == p

If the path contained a drive letter, drive_or_unc will contain
everything up to and including the colon.  e.g. splitdrive("c:/dir")
returns ("c:", "/dir")

If the path contained a UNC path, the drive_or_unc will contain the
host name and share up to but not including the fourth directory
separator character.  e.g. splitdrive("//host/computer/dir") returns
("//host/computer", "/dir")

Paths cannot contain both a drive letter and a UNC path.
```

## splitext

```json
{
  "name": "splitext",
  "kind": "function",
  "origin": "ntpath",
  "signature": "(p)",
  "parameters": [
    {
      "name": "p",
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
Split the extension from a pathname.

Extension is everything from the last dot to the end, ignoring
leading dots.  Returns "(root, ext)"; ext may be empty.
```

## splitroot

```json
{
  "name": "splitroot",
  "kind": "function",
  "origin": "nt",
  "signature": "(p)",
  "parameters": [
    {
      "name": "p",
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
Split a pathname into drive, root and tail.

The tail contains anything after the root.
```

## supports_unicode_filenames

```json
{
  "name": "supports_unicode_filenames",
  "kind": "bool",
  "origin": null
}
```

```text
Returns True when the argument is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.
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
