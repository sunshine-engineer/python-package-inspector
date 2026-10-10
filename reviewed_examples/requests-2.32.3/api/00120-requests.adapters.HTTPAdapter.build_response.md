# requests.adapters.HTTPAdapter.build_response

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Builds a :class:`Response <requests.Response>` object from a urllib3

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, req, resp)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| req | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| resp | positional or keyword | Yes | Not provided | — | The urllib3 response object. |

### Additional inputs documented by the package

These names appear in the docstring but not as explicit signature parameters. They may be forwarded through `**kwargs`; verify the documented call path before passing them. Required status and defaults are not inferred.

| Name | Documented type | Description |
| --- | --- | --- |
| The | req: | class:`PreparedRequest <PreparedRequest>` used to generate the response. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- requests.Response

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.adapters')
req = ...  # TODO: supply a valid value from your application
resp = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.HTTPAdapter using its constructor page
result = instance.build_response(req=req, resp=resp)
print(result)

```

This is a class member. Construct `requests.adapters.HTTPAdapter` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.adapters.HTTPAdapter](00117-requests.adapters.HTTPAdapter.md) — The built-in HTTP Adapter for urllib3.
- [requests.adapters.PreparedRequest](00142-requests.adapters.PreparedRequest.md) — The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
- [requests.adapters.Response](00159-requests.adapters.Response.md) — The :class:`Response <Response>` object, which contains a

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'HTTPAdapter')
obj = inspect.getattr_static(obj, 'build_response')
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
Builds a :class:`Response <requests.Response>` object from a urllib3
        response. This should not be called from user code, and is only exposed
        for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`

        :param req: The :class:`PreparedRequest <PreparedRequest>` used to generate the response.
        :param resp: The urllib3 response object.
        :rtype: requests.Response
        
```

[Full module inspection](../modules/00028-requests.adapters.md)
