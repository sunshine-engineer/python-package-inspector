# requests.sessions.HTTPAdapter.cert_verify

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Verify a SSL certificate. This method should not be called from user

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, conn, url, verify, cert)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| conn | positional or keyword | Yes | Not provided | — | The urllib3 connection object associated with the cert. |
| url | positional or keyword | Yes | Not provided | — | The requested URL. |
| verify | positional or keyword | Yes | Not provided | — | Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use |
| cert | positional or keyword | Yes | Not provided | — | The SSL certificate to verify. |

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
m = importlib.import_module('requests.sessions')
conn = ...  # TODO: supply a valid value from your application
url = ...  # TODO: supply a valid value from your application
verify = ...  # TODO: supply a valid value from your application
cert = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.HTTPAdapter using its constructor page
result = instance.cert_verify(conn=conn, url=url, verify=verify, cert=cert)
print(result)

```

This is a class member. Construct `requests.sessions.HTTPAdapter` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.sessions.HTTPAdapter](00593-requests.sessions.HTTPAdapter.md) — The built-in HTTP Adapter for urllib3.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'HTTPAdapter')
obj = inspect.getattr_static(obj, 'cert_verify')
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
Verify a SSL certificate. This method should not be called from user
        code, and is only exposed for use when subclassing the
        :class:`HTTPAdapter <requests.adapters.HTTPAdapter>`.

        :param conn: The urllib3 connection object associated with the cert.
        :param url: The requested URL.
        :param verify: Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use
        :param cert: The SSL certificate to verify.
        
```

[Full module inspection](../modules/00039-requests.sessions.md)
