# decimal.Context.power

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Compute a**b. If 'a' is negative, then 'b' must be integral. The result

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

## Signature

```text
(self, /, a, b, modulo=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| a | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| b | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| modulo | positional or keyword | No | Not provided | None | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('decimal')
a = ...  # TODO: supply a valid value from your application
b = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Context using its constructor page
result = instance.power(a=a, b=b)
print(result)

```

Construct `decimal.Context` using its constructor page before using this instance member. Its first positional receiver is supplied by the instance, regardless of the receiver name.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('decimal')
obj = m
obj = inspect.getattr_static(obj, 'Context')
obj = inspect.getattr_static(obj, 'power')
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
Compute a**b. If 'a' is negative, then 'b' must be integral. The result
will be inexact unless 'a' is integral and the result is finite and can
be expressed exactly in 'precision' digits.  In the Python version the
result is always correctly rounded, in the C version the result is almost
always correctly rounded.

If modulo is given, compute (a**b) % modulo. The following restrictions
hold:

    * all three arguments must be integral
    * 'b' must be nonnegative
    * at least one of 'a' or 'b' must be nonzero
    * modulo must be nonzero and less than 10**prec in absolute value
```

[Full module inspection](../modules/runtime-00000.md)
