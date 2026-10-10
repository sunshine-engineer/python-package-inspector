# requests.cookies.RequestsCookieJar

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

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
m = importlib.import_module('requests.cookies')
result = m.RequestsCookieJar()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [add_cookie_header](00366-requests.cookies.RequestsCookieJar.add_cookie_header.md) | function | Add correct Cookie: header to request (urllib.request.Request object). |
| [clear](00367-requests.cookies.RequestsCookieJar.clear.md) | function | Clear some cookies. |
| [clear_expired_cookies](00368-requests.cookies.RequestsCookieJar.clear_expired_cookies.md) | function | Discard all expired cookies. |
| [clear_session_cookies](00369-requests.cookies.RequestsCookieJar.clear_session_cookies.md) | function | Discard all session cookies. |
| [copy](00370-requests.cookies.RequestsCookieJar.copy.md) | function | Return a copy of this RequestsCookieJar. |
| [extract_cookies](00371-requests.cookies.RequestsCookieJar.extract_cookies.md) | function | Extract cookies from response, where allowable given the request. |
| [get](00372-requests.cookies.RequestsCookieJar.get.md) | function | Dict-like get() that also supports optional domain and path args in |
| [get_dict](00373-requests.cookies.RequestsCookieJar.get_dict.md) | function | Takes as an argument an optional domain and path and returns a plain |
| [get_policy](00374-requests.cookies.RequestsCookieJar.get_policy.md) | function | Return the CookiePolicy instance used. |
| [items](00375-requests.cookies.RequestsCookieJar.items.md) | function | Dict-like items() that returns a list of name-value tuples from the |
| [iteritems](00376-requests.cookies.RequestsCookieJar.iteritems.md) | function | Dict-like iteritems() that returns an iterator of name-value tuples |
| [iterkeys](00377-requests.cookies.RequestsCookieJar.iterkeys.md) | function | Dict-like iterkeys() that returns an iterator of names of cookies |
| [itervalues](00378-requests.cookies.RequestsCookieJar.itervalues.md) | function | Dict-like itervalues() that returns an iterator of values of cookies |
| [keys](00379-requests.cookies.RequestsCookieJar.keys.md) | function | Dict-like keys() that returns a list of names of cookies from the |
| [list_domains](00380-requests.cookies.RequestsCookieJar.list_domains.md) | function | Utility method to list all the domains in the jar. |
| [list_paths](00381-requests.cookies.RequestsCookieJar.list_paths.md) | function | Utility method to list all the paths in the jar. |
| [make_cookies](00382-requests.cookies.RequestsCookieJar.make_cookies.md) | function | Return sequence of Cookie objects extracted from response object. |
| [multiple_domains](00383-requests.cookies.RequestsCookieJar.multiple_domains.md) | function | Returns True if there are multiple domains in the jar. |
| [pop](00384-requests.cookies.RequestsCookieJar.pop.md) | function | D.pop(k&#91;,d&#93;) -> v, remove specified key and return the corresponding |
| [popitem](00385-requests.cookies.RequestsCookieJar.popitem.md) | function | D.popitem() -> (k, v), remove and return some (key, value) pair |
| [set](00386-requests.cookies.RequestsCookieJar.set.md) | function | Dict-like set() that also supports optional domain and path args in |
| [set_cookie](00387-requests.cookies.RequestsCookieJar.set_cookie.md) | function | Set a cookie, without checking whether or not it should be set. |
| [set_cookie_if_ok](00388-requests.cookies.RequestsCookieJar.set_cookie_if_ok.md) | function | Set a cookie if policy says it's OK to do so. |
| [set_policy](00389-requests.cookies.RequestsCookieJar.set_policy.md) | function | No description supplied by the package. |
| [setdefault](00390-requests.cookies.RequestsCookieJar.setdefault.md) | function | D.setdefault(k&#91;,d&#93;) -> D.get(k,d), also set D&#91;k&#93;=d if k not in D |
| [update](00391-requests.cookies.RequestsCookieJar.update.md) | function | Updates this jar with cookies from another CookieJar or dict-like |
| [values](00392-requests.cookies.RequestsCookieJar.values.md) | function | Dict-like values() that returns a list of values of cookies from the |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.cookies')
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

[Full module inspection](../modules/00033-requests.cookies.md)
