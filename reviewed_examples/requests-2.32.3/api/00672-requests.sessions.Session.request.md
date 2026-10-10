# requests.sessions.Session.request

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Constructs a :class:`Request <Request>`, prepares it and sends it.

Kind: **function**. Evidence: **source + runtime**. Discovery: **public member name**.

## Signature

```text
(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| method | positional or keyword | Yes | Not provided | — | method for the new :class:`Request` object. |
| url | positional or keyword | Yes | Not provided | — | URL for the new :class:`Request` object. |
| params | positional or keyword | No | Not provided | None | (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`. |
| data | positional or keyword | No | Not provided | None | (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the :class:`Request`. |
| headers | positional or keyword | No | Not provided | None | (optional) Dictionary of HTTP Headers to send with the |
| cookies | positional or keyword | No | Not provided | None | (optional) Dict or CookieJar object to send with the |
| files | positional or keyword | No | Not provided | None | (optional) Dictionary of ``'filename': file-like-objects`` for multipart encoding upload. |
| auth | positional or keyword | No | Not provided | None | (optional) Auth tuple or callable to enable Basic/Digest/Custom HTTP Auth. |
| timeout | positional or keyword | No | float or tuple | None | (optional) How long to wait for the server to send data before giving up, as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple. |
| allow_redirects | positional or keyword | No | bool | True | (optional) Set to True by default. |
| proxies | positional or keyword | No | Not provided | None | (optional) Dictionary mapping protocol or protocol and hostname to the URL of the proxy. |
| hooks | positional or keyword | No | Not provided | None | (optional) Dictionary mapping hook name to one event or list of events, event must be callable. |
| stream | positional or keyword | No | Not provided | None | (optional) whether to immediately download the response content. Defaults to ``False``. |
| verify | positional or keyword | No | Not provided | None | (optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to ``True``. When set to ``False``, requests will accept any TLS certificate presented by the server, and will ignore hostname mismatches and/or expired certificates, which will make your application vulnerable to man-in-the-middle (MitM) attacks. Setting verify to ``False`` may be useful during local development or testing. |
| cert | positional or keyword | No | Not provided | None | (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair. |
| json | positional or keyword | No | Not provided | None | (optional) json to send in the body of the |

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
m = importlib.import_module('requests.sessions')
method = ...  # TODO: supply a valid value from your application
url = ...  # TODO: supply a valid value from your application
instance = ...  # TODO: construct m.Session using its constructor page
result = instance.request(method=method, url=url)
print(result)

```

This is a class member. Construct `requests.sessions.Session` using its documented constructor before calling an instance method. `self`/`cls` are receiver parameters. Static/class methods and properties are identified by their decorators when available.

## Related APIs mentioned in the docstring

- [requests.sessions.Request](00623-requests.sessions.Request.md) — A user-created :class:`Request <Request>` object.

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'Session')
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
Constructs a :class:`Request <Request>`, prepares it and sends it.
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param hooks: (optional) Dictionary mapping hook name to one event or
            list of events, event must be callable.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``. When set to
            ``False``, requests will accept any TLS certificate presented by
            the server, and will ignore hostname mismatches and/or expired
            certificates, which will make your application vulnerable to
            man-in-the-middle (MitM) attacks. Setting verify to ``False``
            may be useful during local development or testing.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        
```

[Full module inspection](../modules/00039-requests.sessions.md)
