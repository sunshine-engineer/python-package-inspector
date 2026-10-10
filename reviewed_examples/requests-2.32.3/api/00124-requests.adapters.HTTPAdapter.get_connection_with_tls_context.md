# requests.adapters.HTTPAdapter.get_connection_with_tls_context

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Returns a urllib3 connection for the given request and TLS settings.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, request, verify, proxies=None, cert=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| request | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| verify | positional or keyword | Yes | Not provided | — | Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. |
| proxies | positional or keyword | No | Not provided | None | (optional) The proxies dictionary to apply to the request. |
| cert | positional or keyword | No | Not provided | None | (optional) Any user-provided SSL certificate to be used for client authentication (a.k.a., mTLS). |

### Additional inputs documented by the package

These names appear in the docstring but not as explicit signature parameters. They may be forwarded through `**kwargs`; verify the documented call path before passing them. Required status and defaults are not inferred.

| Name | Documented type | Description |
| --- | --- | --- |
| The | class:`PreparedRequest <PreparedRequest>` object to be sent | over the connection. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- 
- urllib3.ConnectionPool

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.adapters')
request = ...  # TODO: supply a valid value from your application
verify = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.HTTPAdapter using its constructor page
result = instance.get_connection_with_tls_context(request=request, verify=verify)
print(result)

```

This is a class member. Construct `requests.adapters.HTTPAdapter` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.adapters.HTTPAdapter](00117-requests.adapters.HTTPAdapter.md) — The built-in HTTP Adapter for urllib3.
- [requests.adapters.PreparedRequest](00142-requests.adapters.PreparedRequest.md) — The fully mutable :class:`PreparedRequest <PreparedRequest>` object,

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.adapters')
obj = m
obj = inspect.getattr_static(obj, 'HTTPAdapter')
obj = inspect.getattr_static(obj, 'get_connection_with_tls_context')
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
Returns a urllib3 connection for the given request and TLS settings.
        This should not be called from user code, and is only exposed for use
        when subclassing the :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param request:
            The :class:`PreparedRequest <PreparedRequest>` object to be sent
            over the connection.
        :param verify:
            Either a boolean, in which case it controls whether we verify the
            server's TLS certificate, or a string, in which case it must be a
            path to a CA bundle to use.
        :param proxies:
            (optional) The proxies dictionary to apply to the request.
        :param cert:
            (optional) Any user-provided SSL certificate to be used for client
            authentication (a.k.a., mTLS).
        :rtype:
            urllib3.ConnectionPool
        
```

[Full module inspection](../modules/00028-requests.adapters.md)
