# requests.api.request

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Constructs and sends a :class:`Request <Request>`.

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(method, url, **kwargs)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| method | positional or keyword | Yes | Not provided | — | method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``. |
| url | positional or keyword | Yes | Not provided | — | URL for the new :class:`Request` object. |
| kwargs | var keyword | No | Not provided | Collects extra arguments | Not described in the docstring |

### Additional inputs documented by the package

These names appear in the docstring but not as explicit signature parameters. They may be forwarded through `**kwargs`; verify the documented call path before passing them. Required status and defaults are not inferred.

| Name | Documented type | Description |
| --- | --- | --- |
| params | Not provided | (optional) Dictionary, list of tuples or bytes to send in the query string for the :class:`Request`. |
| data | Not provided | (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the :class:`Request`. |
| json | Not provided | (optional) A JSON serializable Python object to send in the body of the :class:`Request`. |
| headers | Not provided | (optional) Dictionary of HTTP Headers to send with the :class:`Request`. |
| cookies | Not provided | (optional) Dict or CookieJar object to send with the :class:`Request`. |
| files | Not provided | (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload. ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')`` or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers to add for the file. |
| auth | Not provided | (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth. |
| timeout | float or tuple | (optional) How many seconds to wait for the server to send data before giving up, as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple. |
| allow_redirects | bool | (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``. |
| proxies | Not provided | (optional) Dictionary mapping protocol to the URL of the proxy. |
| verify | Not provided | (optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to ``True``. |
| stream | Not provided | (optional) if ``False``, the response content will be immediately downloaded. |
| cert | Not provided | (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair. |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- :class:`Response <Response>` object
- requests.Response
- Usage::
- >>> import requests
- >>> req = requests.request('GET', 'https://httpbin.org/get')
- >>> req
- <Response &#91;200&#93;>

No exception section was extracted. This does not mean the call cannot raise.

## Practice

Examples copied from the installed docstring. Package-authored; not executed by the generator. Preserve any setup/context from the original documentation.

```python
import requests
```

```python
req = requests.request('GET', 'https://httpbin.org/get')
```

```python
req
```

Expected output recorded in the docstring:

```text
<Response [200]>
```

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.api')
method = ...  # TODO: supply a valid value from your application
url = ...  # TODO: supply a valid value from your application
result = m.request(method=method, url=url)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.api')
obj = m
obj = inspect.getattr_static(obj, 'request')
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
Constructs and sends a :class:`Request <Request>`.

    :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How many seconds to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    Usage::

      >>> import requests
      >>> req = requests.request('GET', 'https://httpbin.org/get')
      >>> req
      <Response [200]>
    
```

[Full module inspection](../modules/00029-requests.api.md)
