# requests.cookies.RequestsCookieJar.clear_expired_cookies

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Discard all expired cookies.

Kind: **function**. Evidence: **runtime**. Discovery: **public member name**.

Inherited class member.

## Signature

```text
(self)
```

## Inputs

No caller-supplied parameters are declared.

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
m = importlib.import_module('requests.cookies')
instance = ...  # TODO: construct m.RequestsCookieJar using its constructor page
result = instance.clear_expired_cookies()
print(result)

```

This is a class member. Construct `requests.cookies.RequestsCookieJar` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
obj = m
obj = inspect.getattr_static(obj, 'RequestsCookieJar')
obj = inspect.getattr_static(obj, 'clear_expired_cookies')
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
Discard all expired cookies.

You probably don't need to call this method: expired cookies are never
sent back to the server (provided you're using DefaultCookiePolicy),
this method is called by CookieJar itself every so often, and the
.save() method won't save expired cookies anyway (unless you ask
otherwise by passing a true ignore_expires argument).
```

[Full module inspection](../modules/runtime-00008.md)
