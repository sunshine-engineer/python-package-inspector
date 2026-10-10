# requests.models.Request

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

A user-created :class:`Request <Request>` object.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| method | positional or keyword | No | Not provided | None | HTTP method to use. |
| url | positional or keyword | No | Not provided | None | URL to send. |
| headers | positional or keyword | No | Not provided | None | dictionary of headers to send. |
| files | positional or keyword | No | Not provided | None | dictionary of {filename: fileobject} files to multipart upload. |
| data | positional or keyword | No | Not provided | None | the body to attach to the request. If a dictionary or list of tuples ``&#91;(key, value)&#93;`` is provided, form-encoding will take place. |
| params | positional or keyword | No | Not provided | None | URL parameters to append to the URL. If a dictionary or list of tuples ``&#91;(key, value)&#93;`` is provided, form-encoding will take place. |
| auth | positional or keyword | No | Not provided | None | Auth handler or (user, pass) tuple. |
| cookies | positional or keyword | No | Not provided | None | dictionary or CookieJar of cookies to attach to this request. |
| hooks | positional or keyword | No | Not provided | None | dictionary of callback hooks, for internal usage. |
| json | positional or keyword | No | Not provided | None | json for the body to attach to the request (if files or data is not specified). |

### Additional inputs documented by the package

These names appear in the docstring but not as explicit signature parameters. They may be forwarded through `**kwargs`; verify the documented call path before passing them. Required status and defaults are not inferred.

| Name | Documented type | Description |
| --- | --- | --- |
| Usage | Not provided | : >>> import requests >>> req = requests.Request('GET', 'https://httpbin.org/get') >>> req.prepare() <PreparedRequest &#91;GET&#93;> |

## Returns and exceptions

Return annotation: `Not provided`.

Return behavior is not separately documented; consult the original docstring below.

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
import requests
```

```python
req = requests.Request('GET', 'https://httpbin.org/get')
```

```python
req.prepare()
```

Expected output recorded in the docstring:

```text
<PreparedRequest [GET]>
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.models')
result = m.Request()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [deregister_hook](00529-requests.models.Request.deregister_hook.md) | function | Deregister a previously registered hook. |
| [prepare](00530-requests.models.Request.prepare.md) | function | Constructs a :class:`PreparedRequest <PreparedRequest>` for transmission and returns it. |
| [register_hook](00531-requests.models.Request.register_hook.md) | function | Properly register a hook. |

## Related APIs mentioned in the docstring

- [requests.models.PreparedRequest](00514-requests.models.PreparedRequest.md) — The fully mutable :class:`PreparedRequest <PreparedRequest>` object,

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.models')
obj = m
obj = inspect.getattr_static(obj, 'Request')
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
A user-created :class:`Request <Request>` object.

    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

    :param method: HTTP method to use.
    :param url: URL to send.
    :param headers: dictionary of headers to send.
    :param files: dictionary of {filename: fileobject} files to multipart upload.
    :param data: the body to attach to the request. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param json: json for the body to attach to the request (if files or data is not specified).
    :param params: URL parameters to append to the URL. If a dictionary or
        list of tuples ``[(key, value)]`` is provided, form-encoding will
        take place.
    :param auth: Auth handler or (user, pass) tuple.
    :param cookies: dictionary or CookieJar of cookies to attach to this request.
    :param hooks: dictionary of callback hooks, for internal usage.

    Usage::

      >>> import requests
      >>> req = requests.Request('GET', 'https://httpbin.org/get')
      >>> req.prepare()
      <PreparedRequest [GET]>
    
```

[Full module inspection](../modules/00037-requests.models.md)
