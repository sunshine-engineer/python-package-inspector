# requests._internal_utils

Source: `requests/_internal_utils.py`

```text

requests._internal_utils
~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by Requests
which depend on extremely few external helpers (such as compat)

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests._internal_utils')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import re

```json
{
  "name": "import re",
  "kind": "import",
  "line": 8,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "re",
      "local": "re"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import builtin_str

```json
{
  "name": "from .compat import builtin_str",
  "kind": "import",
  "line": 10,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "builtin_str",
      "local": "builtin_str"
    }
  ]
}
```

```text
No docstring available.
```

## _VALID_HEADER_NAME_RE_BYTE

```json
{
  "name": "_VALID_HEADER_NAME_RE_BYTE",
  "kind": "assignment",
  "line": 12,
  "source": "_VALID_HEADER_NAME_RE_BYTE = re.compile(b'^[^:\\\\s][^:\\\\r\\\\n]*$')"
}
```

```text
No docstring available.
```

## _VALID_HEADER_NAME_RE_STR

```json
{
  "name": "_VALID_HEADER_NAME_RE_STR",
  "kind": "assignment",
  "line": 13,
  "source": "_VALID_HEADER_NAME_RE_STR = re.compile('^[^:\\\\s][^:\\\\r\\\\n]*$')"
}
```

```text
No docstring available.
```

## _VALID_HEADER_VALUE_RE_BYTE

```json
{
  "name": "_VALID_HEADER_VALUE_RE_BYTE",
  "kind": "assignment",
  "line": 14,
  "source": "_VALID_HEADER_VALUE_RE_BYTE = re.compile(b'^\\\\S[^\\\\r\\\\n]*$|^$')"
}
```

```text
No docstring available.
```

## _VALID_HEADER_VALUE_RE_STR

```json
{
  "name": "_VALID_HEADER_VALUE_RE_STR",
  "kind": "assignment",
  "line": 15,
  "source": "_VALID_HEADER_VALUE_RE_STR = re.compile('^\\\\S[^\\\\r\\\\n]*$|^$')"
}
```

```text
No docstring available.
```

## _HEADER_VALIDATORS_STR

```json
{
  "name": "_HEADER_VALIDATORS_STR",
  "kind": "assignment",
  "line": 17,
  "source": "_HEADER_VALIDATORS_STR = (_VALID_HEADER_NAME_RE_STR, _VALID_HEADER_VALUE_RE_STR)"
}
```

```text
No docstring available.
```

## _HEADER_VALIDATORS_BYTE

```json
{
  "name": "_HEADER_VALIDATORS_BYTE",
  "kind": "assignment",
  "line": 18,
  "source": "_HEADER_VALIDATORS_BYTE = (_VALID_HEADER_NAME_RE_BYTE, _VALID_HEADER_VALUE_RE_BYTE)"
}
```

```text
No docstring available.
```

## HEADER_VALIDATORS

```json
{
  "name": "HEADER_VALIDATORS",
  "kind": "assignment",
  "line": 19,
  "source": "HEADER_VALIDATORS = {bytes: _HEADER_VALIDATORS_BYTE, str: _HEADER_VALIDATORS_STR}"
}
```

```text
No docstring available.
```

## to_native_string

```json
{
  "name": "to_native_string",
  "kind": "function",
  "signature": "to_native_string(string, encoding='ascii')",
  "line": 25,
  "decorators": [],
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
  "signature": "unicode_is_ascii(u_string)",
  "line": 38,
  "decorators": [],
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
