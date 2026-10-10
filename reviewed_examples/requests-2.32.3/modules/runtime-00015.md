# Runtime: requests.status_codes

```text
The ``codes`` object defines a mapping from common names for HTTP statuses
to their numerical codes, accessible either as attributes or as dictionary
items.

Example::

    >>> import requests
    >>> requests.codes['temporary_redirect']
    307
    >>> requests.codes.teapot
    418
    >>> requests.codes['\o/']
    200

Some codes have multiple names, and both upper- and lower-case versions of
the names are allowed. For example, ``codes.ok``, ``codes.OK``, and
``codes.okay`` all correspond to the HTTP status code 200.

* 100: ``continue``
* 101: ``switching_protocols``
* 102: ``processing``, ``early-hints``
* 103: ``checkpoint``
* 122: ``uri_too_long``, ``request_uri_too_long``
* 200: ``ok``, ``okay``, ``all_ok``, ``all_okay``, ``all_good``, ``\o/``, ``✓``
* 201: ``created``
* 202: ``accepted``
* 203: ``non_authoritative_info``, ``non_authoritative_information``
* 204: ``no_content``
* 205: ``reset_content``, ``reset``
* 206: ``partial_content``, ``partial``
* 207: ``multi_status``, ``multiple_status``, ``multi_stati``, ``multiple_stati``
* 208: ``already_reported``
* 226: ``im_used``
* 300: ``multiple_choices``
* 301: ``moved_permanently``, ``moved``, ``\o-``
* 302: ``found``
* 303: ``see_other``, ``other``
* 304: ``not_modified``
* 305: ``use_proxy``
* 306: ``switch_proxy``
* 307: ``temporary_redirect``, ``temporary_moved``, ``temporary``
* 308: ``permanent_redirect``, ``resume_incomplete``, ``resume``
* 400: ``bad_request``, ``bad``
* 401: ``unauthorized``
* 402: ``payment_required``, ``payment``
* 403: ``forbidden``
* 404: ``not_found``, ``-o-``
* 405: ``method_not_allowed``, ``not_allowed``
* 406: ``not_acceptable``
* 407: ``proxy_authentication_required``, ``proxy_auth``, ``proxy_authentication``
* 408: ``request_timeout``, ``timeout``
* 409: ``conflict``
* 410: ``gone``
* 411: ``length_required``
* 412: ``precondition_failed``, ``precondition``
* 413: ``request_entity_too_large``, ``content_too_large``
* 414: ``request_uri_too_large``, ``uri_too_long``
* 415: ``unsupported_media_type``, ``unsupported_media``, ``media_type``
* 416: ``requested_range_not_satisfiable``, ``requested_range``, ``range_not_satisfiable``
* 417: ``expectation_failed``
* 418: ``im_a_teapot``, ``teapot``, ``i_am_a_teapot``
* 421: ``misdirected_request``
* 422: ``unprocessable_entity``, ``unprocessable``, ``unprocessable_content``
* 423: ``locked``
* 424: ``failed_dependency``, ``dependency``
* 425: ``unordered_collection``, ``unordered``, ``too_early``
* 426: ``upgrade_required``, ``upgrade``
* 428: ``precondition_required``, ``precondition``
* 429: ``too_many_requests``, ``too_many``
* 431: ``header_fields_too_large``, ``fields_too_large``
* 444: ``no_response``, ``none``
* 449: ``retry_with``, ``retry``
* 450: ``blocked_by_windows_parental_controls``, ``parental_controls``
* 451: ``unavailable_for_legal_reasons``, ``legal_reasons``
* 499: ``client_closed_request``
* 500: ``internal_server_error``, ``server_error``, ``/o\``, ``✗``
* 501: ``not_implemented``
* 502: ``bad_gateway``
* 503: ``service_unavailable``, ``unavailable``
* 504: ``gateway_timeout``
* 505: ``http_version_not_supported``, ``http_version``
* 506: ``variant_also_negotiates``
* 507: ``insufficient_storage``
* 509: ``bandwidth_limit_exceeded``, ``bandwidth``
* 510: ``not_extended``
* 511: ``network_authentication_required``, ``network_auth``, ``network_authentication``
```

## LookupDict

```json
{
  "name": "LookupDict",
  "kind": "class",
  "origin": "requests.structures",
  "signature": "(name=None)",
  "parameters": [
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
Dictionary lookup object.
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
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "inherited": false,
  "signature": "(self, name=None)",
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
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "inherited": true,
  "signature": "(self, value, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "value",
      "kind": "positional only",
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
  "inherited": true,
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
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

### copy

```json
{
  "name": "copy",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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
Return the value for key if key is in the dictionary, else default.
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

### setdefault

```json
{
  "name": "setdefault",
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
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.
```

### update

```json
{
  "name": "update",
  "kind": "function",
  "decorators": [],
  "inherited": true,
  "inspection_error": "no signature found for builtin <method 'update' of 'dict' objects>"
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
  "inherited": true,
  "signature": "(self, /)",
  "parameters": [
    {
      "name": "self",
      "kind": "positional only",
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

## _codes

```json
{
  "name": "_codes",
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

## _init

```json
{
  "name": "_init",
  "kind": "function",
  "origin": "requests.status_codes",
  "signature": "()",
  "parameters": [],
  "returns": null
}
```

```text
No docstring available.
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
