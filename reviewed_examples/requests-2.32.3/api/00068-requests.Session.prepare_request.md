# requests.Session.prepare_request

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Constructs a :class:`PreparedRequest <PreparedRequest>` for

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, request)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| request | positional or keyword | Yes | Not provided | — | :class:`Request` instance to prepare with this session's settings. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- requests.PreparedRequest

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests')
request = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Session using its constructor page
result = instance.prepare_request(request=request)
print(result)

```

This is a class member. Construct `requests.Session` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.PreparedRequest](00015-requests.PreparedRequest.md) — The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
- [requests.Request](00032-requests.Request.md) — A user-created :class:`Request <Request>` object.
- [requests.Session](00056-requests.Session.md) — A Requests session.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests')
obj = m
obj = inspect.getattr_static(obj, 'Session')
obj = inspect.getattr_static(obj, 'prepare_request')
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
Constructs a :class:`PreparedRequest <PreparedRequest>` for
        transmission and returns it. The :class:`PreparedRequest` has settings
        merged from the :class:`Request <Request>` instance and those of the
        :class:`Session`.

        :param request: :class:`Request` instance to prepare with this
            session's settings.
        :rtype: requests.PreparedRequest
        
```

[Full module inspection](../modules/00007-requests.md)
