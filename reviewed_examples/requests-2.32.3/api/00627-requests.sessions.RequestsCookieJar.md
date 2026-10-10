# requests.sessions.RequestsCookieJar

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.cookies.RequestsCookieJar`.

## Signature

```text
(policy=None)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| policy | positional or keyword | No | Not provided | None | Not described in the docstring |

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
result = m.RequestsCookieJar()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [add_cookie_header](00628-requests.sessions.RequestsCookieJar.add_cookie_header.md) | function | Add correct Cookie: header to request (urllib.request.Request object). |
| [clear](00629-requests.sessions.RequestsCookieJar.clear.md) | function | Clear some cookies. |
| [clear_expired_cookies](00630-requests.sessions.RequestsCookieJar.clear_expired_cookies.md) | function | Discard all expired cookies. |
| [clear_session_cookies](00631-requests.sessions.RequestsCookieJar.clear_session_cookies.md) | function | Discard all session cookies. |
| [copy](00632-requests.sessions.RequestsCookieJar.copy.md) | function | Return a copy of this RequestsCookieJar. |
| [extract_cookies](00633-requests.sessions.RequestsCookieJar.extract_cookies.md) | function | Extract cookies from response, where allowable given the request. |
| [get](00634-requests.sessions.RequestsCookieJar.get.md) | function | Dict-like get() that also supports optional domain and path args in |
| [get_dict](00635-requests.sessions.RequestsCookieJar.get_dict.md) | function | Takes as an argument an optional domain and path and returns a plain |
| [get_policy](00636-requests.sessions.RequestsCookieJar.get_policy.md) | function | Return the CookiePolicy instance used. |
| [items](00637-requests.sessions.RequestsCookieJar.items.md) | function | Dict-like items() that returns a list of name-value tuples from the |
| [iteritems](00638-requests.sessions.RequestsCookieJar.iteritems.md) | function | Dict-like iteritems() that returns an iterator of name-value tuples |
| [iterkeys](00639-requests.sessions.RequestsCookieJar.iterkeys.md) | function | Dict-like iterkeys() that returns an iterator of names of cookies |
| [itervalues](00640-requests.sessions.RequestsCookieJar.itervalues.md) | function | Dict-like itervalues() that returns an iterator of values of cookies |
| [keys](00641-requests.sessions.RequestsCookieJar.keys.md) | function | Dict-like keys() that returns a list of names of cookies from the |
| [list_domains](00642-requests.sessions.RequestsCookieJar.list_domains.md) | function | Utility method to list all the domains in the jar. |
| [list_paths](00643-requests.sessions.RequestsCookieJar.list_paths.md) | function | Utility method to list all the paths in the jar. |
| [make_cookies](00644-requests.sessions.RequestsCookieJar.make_cookies.md) | function | Return sequence of Cookie objects extracted from response object. |
| [multiple_domains](00645-requests.sessions.RequestsCookieJar.multiple_domains.md) | function | Returns True if there are multiple domains in the jar. |
| [pop](00646-requests.sessions.RequestsCookieJar.pop.md) | function | D.pop(k&#91;,d&#93;) -> v, remove specified key and return the corresponding |
| [popitem](00647-requests.sessions.RequestsCookieJar.popitem.md) | function | D.popitem() -> (k, v), remove and return some (key, value) pair |
| [set](00648-requests.sessions.RequestsCookieJar.set.md) | function | Dict-like set() that also supports optional domain and path args in |
| [set_cookie](00649-requests.sessions.RequestsCookieJar.set_cookie.md) | function | Set a cookie, without checking whether or not it should be set. |
| [set_cookie_if_ok](00650-requests.sessions.RequestsCookieJar.set_cookie_if_ok.md) | function | Set a cookie if policy says it's OK to do so. |
| [set_policy](00651-requests.sessions.RequestsCookieJar.set_policy.md) | function | No description supplied by the package. |
| [setdefault](00652-requests.sessions.RequestsCookieJar.setdefault.md) | function | D.setdefault(k&#91;,d&#93;) -> D.get(k,d), also set D&#91;k&#93;=d if k not in D |
| [update](00653-requests.sessions.RequestsCookieJar.update.md) | function | Updates this jar with cookies from another CookieJar or dict-like |
| [values](00654-requests.sessions.RequestsCookieJar.values.md) | function | Dict-like values() that returns a list of values of cookies from the |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.sessions')
obj = m
obj = inspect.getattr_static(obj, 'RequestsCookieJar')
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
Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict
    interface.

    This is the CookieJar we create by default for requests and sessions that
    don't specify one, since some clients may expect response.cookies and
    session.cookies to support dict operations.

    Requests does not use the dict interface internally; it's just for
    compatibility with external client code. All requests code should work
    out of the box with externally provided instances of ``CookieJar``, e.g.
    ``LWPCookieJar`` and ``FileCookieJar``.

    Unlike a regular CookieJar, this class is pickleable.

    .. warning:: dictionary operations that are normally O(1) may be O(n).
    
```

[Full module inspection](../modules/00039-requests.sessions.md)
