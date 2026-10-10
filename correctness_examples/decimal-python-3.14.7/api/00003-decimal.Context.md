# decimal.Context

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

The context affects almost all operations and controls rounding,

Kind: **class**. Evidence: **runtime**. Discovery: **runtime name heuristic**.

## Signature

```text
(prec=None, rounding=None, Emin=None, Emax=None, capitals=None, clamp=None, flags=None, traps=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| prec | positional or keyword | No | Not provided | None | Not described in the docstring |
| rounding | positional or keyword | No | Not provided | None | Not described in the docstring |
| Emin | positional or keyword | No | Not provided | None | Not described in the docstring |
| Emax | positional or keyword | No | Not provided | None | Not described in the docstring |
| capitals | positional or keyword | No | Not provided | None | Not described in the docstring |
| clamp | positional or keyword | No | Not provided | None | Not described in the docstring |
| flags | positional or keyword | No | Not provided | None | Not described in the docstring |
| traps | positional or keyword | No | Not provided | None | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
c = Context(prec=28, Emin=-425000000, Emax=425000000,
            rounding=ROUND_HALF_EVEN, capitals=1, clamp=1,
            traps=[InvalidOperation, DivisionByZero, Overflow],
            flags=[])
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('decimal')
result = m.Context()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [Etiny](00004-decimal.Context.Etiny.md) | function | Return a value equal to Emin - prec + 1, which is the minimum exponent value |
| [Etop](00005-decimal.Context.Etop.md) | function | Return a value equal to Emax - prec + 1.  This is the maximum exponent |
| [abs](00006-decimal.Context.abs.md) | function | Return the absolute value of x. |
| [add](00007-decimal.Context.add.md) | function | Return the sum of x and y. |
| [canonical](00008-decimal.Context.canonical.md) | function | Return a new instance of x. |
| [clear_flags](00009-decimal.Context.clear_flags.md) | function | Reset all flags to False. |
| [clear_traps](00010-decimal.Context.clear_traps.md) | function | Set all traps to False. |
| [compare](00011-decimal.Context.compare.md) | function | Compare x and y numerically. |
| [compare_signal](00012-decimal.Context.compare_signal.md) | function | Compare x and y numerically.  All NaNs signal. |
| [compare_total](00013-decimal.Context.compare_total.md) | function | Compare x and y using their abstract representation. |
| [compare_total_mag](00014-decimal.Context.compare_total_mag.md) | function | Compare x and y using their abstract representation, ignoring sign. |
| [copy](00015-decimal.Context.copy.md) | function | Return a duplicate of the context. |
| [copy_abs](00016-decimal.Context.copy_abs.md) | function | Return a copy of x with the sign set to 0. |
| [copy_decimal](00017-decimal.Context.copy_decimal.md) | function | Return a copy of Decimal x. |
| [copy_negate](00018-decimal.Context.copy_negate.md) | function | Return a copy of x with the sign inverted. |
| [copy_sign](00019-decimal.Context.copy_sign.md) | function | Copy the sign from y to x. |
| [create_decimal](00020-decimal.Context.create_decimal.md) | function | Create a new Decimal instance from num, using self as the context. Unlike the |
| [create_decimal_from_float](00021-decimal.Context.create_decimal_from_float.md) | function | Create a new Decimal instance from float f.  Unlike the Decimal.from_float() |
| [divide](00022-decimal.Context.divide.md) | function | Return x divided by y. |
| [divide_int](00023-decimal.Context.divide_int.md) | function | Return x divided by y, truncated to an integer. |
| [divmod](00024-decimal.Context.divmod.md) | function | Return quotient and remainder of the division x / y. |
| [exp](00025-decimal.Context.exp.md) | function | Return e ** x. |
| [fma](00026-decimal.Context.fma.md) | function | Return x multiplied by y, plus z. |
| [is_canonical](00027-decimal.Context.is_canonical.md) | function | Return True if x is canonical, False otherwise. |
| [is_finite](00028-decimal.Context.is_finite.md) | function | Return True if x is finite, False otherwise. |
| [is_infinite](00029-decimal.Context.is_infinite.md) | function | Return True if x is infinite, False otherwise. |
| [is_nan](00030-decimal.Context.is_nan.md) | function | Return True if x is a qNaN or sNaN, False otherwise. |
| [is_normal](00031-decimal.Context.is_normal.md) | function | Return True if x is a normal number, False otherwise. |
| [is_qnan](00032-decimal.Context.is_qnan.md) | function | Return True if x is a quiet NaN, False otherwise. |
| [is_signed](00033-decimal.Context.is_signed.md) | function | Return True if x is negative, False otherwise. |
| [is_snan](00034-decimal.Context.is_snan.md) | function | Return True if x is a signaling NaN, False otherwise. |
| [is_subnormal](00035-decimal.Context.is_subnormal.md) | function | Return True if x is subnormal, False otherwise. |
| [is_zero](00036-decimal.Context.is_zero.md) | function | Return True if x is a zero, False otherwise. |
| [ln](00037-decimal.Context.ln.md) | function | Return the natural (base e) logarithm of x. |
| [log10](00038-decimal.Context.log10.md) | function | Return the base 10 logarithm of x. |
| [logb](00039-decimal.Context.logb.md) | function | Return the exponent of the magnitude of the operand's MSD. |
| [logical_and](00040-decimal.Context.logical_and.md) | function | Applies the logical operation 'and' between each operand's digits. |
| [logical_invert](00041-decimal.Context.logical_invert.md) | function | Invert all the digits in the operand. |
| [logical_or](00042-decimal.Context.logical_or.md) | function | Applies the logical operation 'or' between each operand's digits. |
| [logical_xor](00043-decimal.Context.logical_xor.md) | function | Applies the logical operation 'xor' between each operand's digits. |
| [max](00044-decimal.Context.max.md) | function | Compare the values numerically and return the maximum. |
| [max_mag](00045-decimal.Context.max_mag.md) | function | Compare the values numerically with their sign ignored. |
| [min](00046-decimal.Context.min.md) | function | Compare the values numerically and return the minimum. |
| [min_mag](00047-decimal.Context.min_mag.md) | function | Compare the values numerically with their sign ignored. |
| [minus](00048-decimal.Context.minus.md) | function | Minus corresponds to the unary prefix minus operator in Python, but applies |
| [multiply](00049-decimal.Context.multiply.md) | function | Return the product of x and y. |
| [next_minus](00050-decimal.Context.next_minus.md) | function | Return the largest representable number smaller than x. |
| [next_plus](00051-decimal.Context.next_plus.md) | function | Return the smallest representable number larger than x. |
| [next_toward](00052-decimal.Context.next_toward.md) | function | Return the number closest to x, in the direction towards y. |
| [normalize](00053-decimal.Context.normalize.md) | function | Reduce x to its simplest form. Alias for reduce(x). |
| [number_class](00054-decimal.Context.number_class.md) | function | Return an indication of the class of x. |
| [plus](00055-decimal.Context.plus.md) | function | Plus corresponds to the unary prefix plus operator in Python, but applies |
| [power](00056-decimal.Context.power.md) | function | Compute a**b. If 'a' is negative, then 'b' must be integral. The result |
| [quantize](00057-decimal.Context.quantize.md) | function | Return a value equal to x (rounded), having the exponent of y. |
| [radix](00058-decimal.Context.radix.md) | function | Return 10. |
| [remainder](00059-decimal.Context.remainder.md) | function | Return the remainder from integer division.  The sign of the result, |
| [remainder_near](00060-decimal.Context.remainder_near.md) | function | Return x - y * n, where n is the integer nearest the exact value of x / y |
| [rotate](00061-decimal.Context.rotate.md) | function | Return a copy of x, rotated by y places. |
| [same_quantum](00062-decimal.Context.same_quantum.md) | function | Return True if the two operands have the same exponent. |
| [scaleb](00063-decimal.Context.scaleb.md) | function | Return the first operand after adding the second value to its exp. |
| [shift](00064-decimal.Context.shift.md) | function | Return a copy of x, shifted by y places. |
| [sqrt](00065-decimal.Context.sqrt.md) | function | Square root of a non-negative number to context precision. |
| [subtract](00066-decimal.Context.subtract.md) | function | Return the difference between x and y. |
| [to_eng_string](00067-decimal.Context.to_eng_string.md) | function | Convert a number to a string, using engineering notation. |
| [to_integral](00068-decimal.Context.to_integral.md) | function | Identical to to_integral_value(x). |
| [to_integral_exact](00069-decimal.Context.to_integral_exact.md) | function | Round to an integer. Signal if the result is rounded or inexact. |
| [to_integral_value](00070-decimal.Context.to_integral_value.md) | function | Round to an integer. |
| [to_sci_string](00071-decimal.Context.to_sci_string.md) | function | Convert a number to a string using scientific notation. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('decimal')
obj = m
obj = inspect.getattr_static(obj, 'Context')
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
The context affects almost all operations and controls rounding,
Over/Underflow, raising of exceptions and much more.  A new context
can be constructed as follows:

    >>> c = Context(prec=28, Emin=-425000000, Emax=425000000,
    ...             rounding=ROUND_HALF_EVEN, capitals=1, clamp=1,
    ...             traps=[InvalidOperation, DivisionByZero, Overflow],
    ...             flags=[])
    >>>
```

[Full module inspection](../modules/runtime-00000.md)
