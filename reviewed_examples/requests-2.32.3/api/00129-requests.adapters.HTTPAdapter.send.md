# requests.adapters.HTTPAdapter.send

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Sends PreparedRequest object. Returns Response object.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| request | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| stream | positional or keyword | No | Not provided | False | (optional) Whether to stream the request content. |
| timeout | positional or keyword | No | float or tuple or urllib3 Timeout object | None | (optional) How long to wait for the server to send data before giving up, as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple. |
| verify | positional or keyword | No | Not provided | True | (optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use |
| cert | positional or keyword | No | Not provided | None | (optional) Any user-provided SSL certificate to be trusted. |
| proxies | positional or keyword | No | Not provided | None | (optional) The proxies dictionary to apply to the request. |

### Additional inputs documented by the package

These names appear in the docstring but not as explicit signature parameters. They may be forwarded through `**kwargs`; verify the documented call path before passing them. Required status and defaults are not inferred.

| Name | Documented type | Description |
| --- | --- | --- |
| The | request: | class:`PreparedRequest <PreparedRequest>` being sent. |

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
request = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.HTTPAdapter using its constructor page
result = instance.send(request=request)
print(result)

```

This is a class member. Construct `requests.adapters.HTTPAdapter` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.adapters.PreparedRequest](00142-requests.adapters.PreparedRequest.md) — The fully mutable :class:`PreparedRequest <PreparedRequest>` object,

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'HTTPAdapter')
obj = inspect.getattr_static(obj, 'send')
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
Sends PreparedRequest object. Returns Response object.

        :param request: The :class:`PreparedRequest <PreparedRequest>` being sent.
        :param stream: (optional) Whether to stream the request content.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple or urllib3 Timeout object
        :param verify: (optional) Either a boolean, in which case it controls whether
            we verify the server's TLS certificate, or a string, in which case it
            must be a path to a CA bundle to use
        :param cert: (optional) Any user-provided SSL certificate to be trusted.
        :param proxies: (optional) The proxies dictionary to apply to the request.
        :rtype: requests.Response
        
```

[Full module inspection](../modules/00028-requests.adapters.md)
