# decimal.Decimal

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Construct a new Decimal object. 'value' can be an integer, string, tuple,

Kind: **class**. Evidence: **runtime**. Discovery: **runtime name heuristic**.

## Signature

```text
(value='0', context=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| value | positional or keyword | No | Not provided | '0' | Not described in the docstring |
| context | positional or keyword | No | Not provided | None | Not described in the docstring |

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
result = m.Decimal()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [adjusted](00076-decimal.Decimal.adjusted.md) | function | Return the adjusted exponent of the number.  Defined as exp + digits - 1. |
| [as_integer_ratio](00077-decimal.Decimal.as_integer_ratio.md) | function | Decimal.as_integer_ratio() -> (int, int) |
| [as_tuple](00078-decimal.Decimal.as_tuple.md) | function | Return a tuple representation of the number. |
| [canonical](00079-decimal.Decimal.canonical.md) | function | Return the canonical encoding of the argument.  Currently, the encoding |
| [compare](00080-decimal.Decimal.compare.md) | function | Compare self to other.  Return a decimal value: |
| [compare_signal](00081-decimal.Decimal.compare_signal.md) | function | Identical to compare, except that all NaNs signal. |
| [compare_total](00082-decimal.Decimal.compare_total.md) | function | Compare two operands using their abstract representation rather than |
| [compare_total_mag](00083-decimal.Decimal.compare_total_mag.md) | function | Compare two operands using their abstract representation rather than their |
| [conjugate](00084-decimal.Decimal.conjugate.md) | function | Return self. |
| [copy_abs](00085-decimal.Decimal.copy_abs.md) | function | Return the absolute value of the argument.  This operation is unaffected by |
| [copy_negate](00086-decimal.Decimal.copy_negate.md) | function | Return the negation of the argument.  This operation is unaffected by context |
| [copy_sign](00087-decimal.Decimal.copy_sign.md) | function | Return a copy of the first operand with the sign set to be the same as the |
| [exp](00088-decimal.Decimal.exp.md) | function | Return the value of the (natural) exponential function e**x at the given |
| [fma](00089-decimal.Decimal.fma.md) | function | Fused multiply-add.  Return self*other+third with no rounding of the |
| [from_float](00090-decimal.Decimal.from_float.md) | function | Class method that converts a float to a decimal number, exactly. |
| [from_number](00091-decimal.Decimal.from_number.md) | function | Class method that converts a real number to a decimal number, exactly. |
| [is_canonical](00092-decimal.Decimal.is_canonical.md) | function | Return True if the argument is canonical and False otherwise.  Currently, |
| [is_finite](00093-decimal.Decimal.is_finite.md) | function | Return True if the argument is a finite number, and False if the argument |
| [is_infinite](00094-decimal.Decimal.is_infinite.md) | function | Return True if the argument is either positive or negative infinity and |
| [is_nan](00095-decimal.Decimal.is_nan.md) | function | Return True if the argument is a (quiet or signaling) NaN and False |
| [is_normal](00096-decimal.Decimal.is_normal.md) | function | Return True if the argument is a normal finite non-zero number with an |
| [is_qnan](00097-decimal.Decimal.is_qnan.md) | function | Return True if the argument is a quiet NaN, and False otherwise. |
| [is_signed](00098-decimal.Decimal.is_signed.md) | function | Return True if the argument has a negative sign and False otherwise. |
| [is_snan](00099-decimal.Decimal.is_snan.md) | function | Return True if the argument is a signaling NaN and False otherwise. |
| [is_subnormal](00100-decimal.Decimal.is_subnormal.md) | function | Return True if the argument is subnormal, and False otherwise. A number is |
| [is_zero](00101-decimal.Decimal.is_zero.md) | function | Return True if the argument is a (positive or negative) zero and False |
| [ln](00102-decimal.Decimal.ln.md) | function | Return the natural (base e) logarithm of the operand. The function always |
| [log10](00103-decimal.Decimal.log10.md) | function | Return the base ten logarithm of the operand. The function always uses the |
| [logb](00104-decimal.Decimal.logb.md) | function | For a non-zero number, return the adjusted exponent of the operand as a |
| [logical_and](00105-decimal.Decimal.logical_and.md) | function | Applies an 'and' operation between self and other's digits. |
| [logical_invert](00106-decimal.Decimal.logical_invert.md) | function | Invert all its digits. |
| [logical_or](00107-decimal.Decimal.logical_or.md) | function | Applies an 'or' operation between self and other's digits. |
| [logical_xor](00108-decimal.Decimal.logical_xor.md) | function | Applies an 'xor' operation between self and other's digits. |
| [max](00109-decimal.Decimal.max.md) | function | Maximum of self and other.  If one operand is a quiet NaN and the other is |
| [max_mag](00110-decimal.Decimal.max_mag.md) | function | Similar to the max() method, but the comparison is done using the absolute |
| [min](00111-decimal.Decimal.min.md) | function | Minimum of self and other. If one operand is a quiet NaN and the other is |
| [min_mag](00112-decimal.Decimal.min_mag.md) | function | Similar to the min() method, but the comparison is done using the absolute |
| [next_minus](00113-decimal.Decimal.next_minus.md) | function | Return the largest number representable in the given context (or in the |
| [next_plus](00114-decimal.Decimal.next_plus.md) | function | Return the smallest number representable in the given context (or in the |
| [next_toward](00115-decimal.Decimal.next_toward.md) | function | If the two operands are unequal, return the number closest to the first |
| [normalize](00116-decimal.Decimal.normalize.md) | function | Normalize the number by stripping the rightmost trailing zeros and |
| [number_class](00117-decimal.Decimal.number_class.md) | function | Return a string describing the class of the operand.  The returned value |
| [quantize](00118-decimal.Decimal.quantize.md) | function | Return a value equal to the first operand after rounding and having the |
| [radix](00119-decimal.Decimal.radix.md) | function | Return Decimal(10), the radix (base) in which the Decimal class does |
| [remainder_near](00120-decimal.Decimal.remainder_near.md) | function | Return the remainder from dividing self by other.  This differs from |
| [rotate](00121-decimal.Decimal.rotate.md) | function | Return the result of rotating the digits of the first operand by an amount |
| [same_quantum](00122-decimal.Decimal.same_quantum.md) | function | Test whether self and other have the same exponent or whether both are NaN. |
| [scaleb](00123-decimal.Decimal.scaleb.md) | function | Return the first operand with the exponent adjusted the second.  Equivalently, |
| [shift](00124-decimal.Decimal.shift.md) | function | Return the result of shifting the digits of the first operand by an amount |
| [sqrt](00125-decimal.Decimal.sqrt.md) | function | Return the square root of the argument to full precision. The result is |
| [to_eng_string](00126-decimal.Decimal.to_eng_string.md) | function | Convert to an engineering-type string.  Engineering notation has an exponent |
| [to_integral](00127-decimal.Decimal.to_integral.md) | function | Identical to the to_integral_value() method.  The to_integral() name has been |
| [to_integral_exact](00128-decimal.Decimal.to_integral_exact.md) | function | Round to the nearest integer, signaling Inexact or Rounded as appropriate if |
| [to_integral_value](00129-decimal.Decimal.to_integral_value.md) | function | Round to the nearest integer without signaling Inexact or Rounded.  The |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('decimal')
obj = m
obj = inspect.getattr_static(obj, 'Decimal')
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
Construct a new Decimal object. 'value' can be an integer, string, tuple,
or another Decimal object. If no value is given, return Decimal('0'). The
context does not affect the conversion and is only passed to determine if
the InvalidOperation trap is active.
```

[Full module inspection](../modules/runtime-00000.md)
