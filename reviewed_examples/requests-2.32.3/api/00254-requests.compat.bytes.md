# requests.compat.bytes

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

bytes(iterable_of_ints) -> bytes

Kind: **class**. Evidence: **runtime**. Discovery: **runtime name heuristic**.

Signature unavailable. Inspect the docstring before calling this API.

## Inputs

Parameter details unavailable.

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [capitalize](00255-requests.compat.bytes.capitalize.md) | function | B.capitalize() -> copy of B |
| [center](00256-requests.compat.bytes.center.md) | function | Return a centered string of length width. |
| [count](00257-requests.compat.bytes.count.md) | function | Return the number of non-overlapping occurrences of subsection 'sub' in bytes B&#91;start:end&#93;. |
| [decode](00258-requests.compat.bytes.decode.md) | function | Decode the bytes using the codec registered for encoding. |
| [endswith](00259-requests.compat.bytes.endswith.md) | function | Return True if the bytes ends with the specified suffix, False otherwise. |
| [expandtabs](00260-requests.compat.bytes.expandtabs.md) | function | Return a copy where all tab characters are expanded using spaces. |
| [find](00261-requests.compat.bytes.find.md) | function | Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B&#91;start,end&#93;. |
| [fromhex](00262-requests.compat.bytes.fromhex.md) | function | Create a bytes object from a string of hexadecimal numbers. |
| [hex](00263-requests.compat.bytes.hex.md) | function | Create a string of hexadecimal numbers from a bytes object. |
| [index](00264-requests.compat.bytes.index.md) | function | Return the lowest index in B where subsection 'sub' is found, such that 'sub' is contained within B&#91;start,end&#93;. |
| [isalnum](00265-requests.compat.bytes.isalnum.md) | function | B.isalnum() -> bool |
| [isalpha](00266-requests.compat.bytes.isalpha.md) | function | B.isalpha() -> bool |
| [isascii](00267-requests.compat.bytes.isascii.md) | function | B.isascii() -> bool |
| [isdigit](00268-requests.compat.bytes.isdigit.md) | function | B.isdigit() -> bool |
| [islower](00269-requests.compat.bytes.islower.md) | function | B.islower() -> bool |
| [isspace](00270-requests.compat.bytes.isspace.md) | function | B.isspace() -> bool |
| [istitle](00271-requests.compat.bytes.istitle.md) | function | B.istitle() -> bool |
| [isupper](00272-requests.compat.bytes.isupper.md) | function | B.isupper() -> bool |
| [join](00273-requests.compat.bytes.join.md) | function | Concatenate any number of bytes objects. |
| [ljust](00274-requests.compat.bytes.ljust.md) | function | Return a left-justified string of length width. |
| [lower](00275-requests.compat.bytes.lower.md) | function | B.lower() -> copy of B |
| [lstrip](00276-requests.compat.bytes.lstrip.md) | function | Strip leading bytes contained in the argument. |
| [maketrans](00277-requests.compat.bytes.maketrans.md) | function | Return a translation table usable for the bytes or bytearray translate method. |
| [partition](00278-requests.compat.bytes.partition.md) | function | Partition the bytes into three parts using the given separator. |
| [removeprefix](00279-requests.compat.bytes.removeprefix.md) | function | Return a bytes object with the given prefix string removed if present. |
| [removesuffix](00280-requests.compat.bytes.removesuffix.md) | function | Return a bytes object with the given suffix string removed if present. |
| [replace](00281-requests.compat.bytes.replace.md) | function | Return a copy with all occurrences of substring old replaced by new. |
| [rfind](00282-requests.compat.bytes.rfind.md) | function | Return the highest index in B where subsection 'sub' is found, such that 'sub' is contained within B&#91;start,end&#93;. |
| [rindex](00283-requests.compat.bytes.rindex.md) | function | Return the highest index in B where subsection 'sub' is found, such that 'sub' is contained within B&#91;start,end&#93;. |
| [rjust](00284-requests.compat.bytes.rjust.md) | function | Return a right-justified string of length width. |
| [rpartition](00285-requests.compat.bytes.rpartition.md) | function | Partition the bytes into three parts using the given separator. |
| [rsplit](00286-requests.compat.bytes.rsplit.md) | function | Return a list of the sections in the bytes, using sep as the delimiter. |
| [rstrip](00287-requests.compat.bytes.rstrip.md) | function | Strip trailing bytes contained in the argument. |
| [split](00288-requests.compat.bytes.split.md) | function | Return a list of the sections in the bytes, using sep as the delimiter. |
| [splitlines](00289-requests.compat.bytes.splitlines.md) | function | Return a list of the lines in the bytes, breaking at line boundaries. |
| [startswith](00290-requests.compat.bytes.startswith.md) | function | Return True if the bytes starts with the specified prefix, False otherwise. |
| [strip](00291-requests.compat.bytes.strip.md) | function | Strip leading and trailing bytes contained in the argument. |
| [swapcase](00292-requests.compat.bytes.swapcase.md) | function | B.swapcase() -> copy of B |
| [title](00293-requests.compat.bytes.title.md) | function | B.title() -> copy of B |
| [translate](00294-requests.compat.bytes.translate.md) | function | Return a copy with each character mapped by the given translation table. |
| [upper](00295-requests.compat.bytes.upper.md) | function | B.upper() -> copy of B |
| [zfill](00296-requests.compat.bytes.zfill.md) | function | Pad a numeric string with zeros on the left, to fill a field of the given width. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.compat')
obj = m
obj = inspect.getattr_static(obj, 'bytes')
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

[Full module inspection](../modules/runtime-00007.md)
