# requests.compat.bytes.hex

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Create a string of hexadecimal numbers from a bytes object.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Signature unavailable. Inspect the docstring before calling this API.

## Inputs

Parameter details unavailable.

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
value = b'\xb9\x01\xef'
```

```python
value.hex()
```

Expected output recorded in the docstring:

```text
'b901ef'
```

```python
value.hex(':')
```

Expected output recorded in the docstring:

```text
'b9:01:ef'
```

```python
value.hex(':', 2)
```

Expected output recorded in the docstring:

```text
'b9:01ef'
```

```python
value.hex(':', -2)
```

Expected output recorded in the docstring:

```text
'b901:ef'
```

This is a class member. Construct `requests.compat.bytes` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.compat')
obj = m
obj = inspect.getattr_static(obj, 'bytes')
obj = inspect.getattr_static(obj, 'hex')
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

[Full module inspection](../modules/runtime-00007.md)
