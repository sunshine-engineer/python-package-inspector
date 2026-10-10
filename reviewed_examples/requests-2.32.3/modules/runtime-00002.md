# Runtime: requests._internal_utils

```text
requests._internal_utils
~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by Requests
which depend on extremely few external helpers (such as compat)
```

## HEADER_VALIDATORS

```json
{
  "name": "HEADER_VALIDATORS",
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

## _HEADER_VALIDATORS_BYTE

```json
{
  "name": "_HEADER_VALIDATORS_BYTE",
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

## _HEADER_VALIDATORS_STR

```json
{
  "name": "_HEADER_VALIDATORS_STR",
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

## _VALID_HEADER_NAME_RE_BYTE

```json
{
  "name": "_VALID_HEADER_NAME_RE_BYTE",
  "kind": "Pattern",
  "origin": "re"
}
```

```text
Compiled regular expression object.
```

## _VALID_HEADER_NAME_RE_STR

```json
{
  "name": "_VALID_HEADER_NAME_RE_STR",
  "kind": "Pattern",
  "origin": "re"
}
```

```text
Compiled regular expression object.
```

## _VALID_HEADER_VALUE_RE_BYTE

```json
{
  "name": "_VALID_HEADER_VALUE_RE_BYTE",
  "kind": "Pattern",
  "origin": "re"
}
```

```text
Compiled regular expression object.
```

## _VALID_HEADER_VALUE_RE_STR

```json
{
  "name": "_VALID_HEADER_VALUE_RE_STR",
  "kind": "Pattern",
  "origin": "re"
}
```

```text
Compiled regular expression object.
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

## re

```json
{
  "name": "re",
  "kind": "module",
  "origin": null
}
```

```text
Support for regular expressions (RE).

This module provides regular expression matching operations similar to
those found in Perl.  It supports both 8-bit and Unicode strings; both
the pattern and the strings being processed can contain null bytes and
characters outside the US ASCII range.

Regular expressions can contain both special and ordinary characters.
Most ordinary characters, like "A", "a", or "0", are the simplest
regular expressions; they simply match themselves.  You can
concatenate ordinary characters, so last matches the string 'last'.

The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?aiLmsux) The letters set the corresponding flags defined below.
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                       the (optional) no pattern otherwise.

The special sequences consist of "\\" and a character from the list
below.  If the ordinary character is not on the list, then the
resulting RE will match the second character.
    \number  Matches the contents of the group of the same number.
    \A       Matches only at the start of the string.
    \z       Matches only at the end of the string.
    \b       Matches the empty string, but only at the start or end of a word.
    \B       Matches the empty string, but not at the start or end of a word.
    \d       Matches any decimal digit; equivalent to the set [0-9] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode digits.
    \D       Matches any non-digit character; equivalent to [^\d].
    \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode whitespace characters.
    \S       Matches any non-whitespace character; equivalent to [^\s].
    \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
             in bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the
             range of Unicode alphanumeric characters (letters plus digits
             plus underscore).
             With LOCALE, it will match the set [0-9_] plus characters defined
             as letters for the current locale.
    \W       Matches the complement of \w.
    \\       Matches a literal backslash.

This module exports the following functions:
    match     Match a regular expression pattern to the beginning of a string.
    fullmatch Match a regular expression pattern to all of a string.
    search    Search a string for the presence of a pattern.
    sub       Substitute occurrences of a pattern found in a string.
    subn      Same as sub, but also return the number of substitutions made.
    split     Split a string by the occurrences of a pattern.
    findall   Find all occurrences of a pattern in a string.
    finditer  Return an iterator yielding a Match object for each match.
    compile   Compile a pattern into a Pattern object.
    purge     Clear the regular expression cache.
    escape    Backslash all non-alphanumerics in a string.

Each function other than purge and escape can take an optional 'flags' argument
consisting of one or more of the following module constants, joined by "|".
A, L, and U are mutually exclusive.
    A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                   match the corresponding ASCII character categories
                   (rather than the whole Unicode categories, which is the
                   default).
                   For bytes patterns, this flag is the only available
                   behaviour and needn't be specified.
    I  IGNORECASE  Perform case-insensitive matching.
    L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
    M  MULTILINE   "^" matches the beginning of lines (after a newline)
                   as well as the string.
                   "$" matches the end of lines (before a newline) as well
                   as the end of the string.
    S  DOTALL      "." matches any character at all, including the newline.
    X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
    U  UNICODE     For compatibility only. Ignored for string patterns (it
                   is the default), and forbidden for bytes patterns.

This module also defines exception 'PatternError', aliased to 'error' for
backward compatibility.
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

## unicode_is_ascii

```json
{
  "name": "unicode_is_ascii",
  "kind": "function",
  "origin": "requests._internal_utils",
  "signature": "(u_string)",
  "parameters": [
    {
      "name": "u_string",
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
Determine if unicode string only contains ASCII characters.

:param str u_string: unicode string to check. Must be unicode
    and not Python 2 `str`.
:rtype: bool
```
