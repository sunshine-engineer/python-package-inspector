# requests.sessions.session

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Returns a :class:`Session` for context-management.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
()
```

## Inputs

No caller-supplied parameters are declared.

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- Session

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.sessions')
result = m.session()
print(result)

```

## Related APIs mentioned in the docstring

- [requests.sessions.Session](00655-requests.sessions.Session.md) — A Requests session.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'session')
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

    Returns a :class:`Session` for context-management.

    .. deprecated:: 1.0.0

        This method has been deprecated since version 1.0.0 and is only kept for
        backwards compatibility. New code should use :class:`~requests.sessions.Session`
        to create a session. This may be removed at a future date.

    :rtype: Session
    
```

[Full module inspection](../modules/00039-requests.sessions.md)
