# requests.Response

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

The :class:`Response <Response>` object, which contains a

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

Re-export of `requests.models.Response`.

## Signature

```text
()
```

## Inputs

No caller-supplied parameters are declared.

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
m = importlib.import_module('requests')
result = m.Response()
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [apparent_encoding](00043-requests.Response.apparent_encoding.md) | property | The apparent encoding, provided by the charset_normalizer or chardet libraries. |
| [close](00044-requests.Response.close.md) | function | Releases the connection back to the pool. Once this method has been |
| [content](00045-requests.Response.content.md) | property | Content of the response, in bytes. |
| [is_permanent_redirect](00046-requests.Response.is_permanent_redirect.md) | property | True if this Response one of the permanent versions of redirect. |
| [is_redirect](00047-requests.Response.is_redirect.md) | property | True if this Response is a well-formed HTTP redirect that could have |
| [iter_content](00048-requests.Response.iter_content.md) | function | Iterates over the response data.  When stream=True is set on the |
| [iter_lines](00049-requests.Response.iter_lines.md) | function | Iterates over the response data, one line at a time.  When |
| [json](00050-requests.Response.json.md) | function | Returns the json-encoded content of a response, if any. |
| [links](00051-requests.Response.links.md) | property | Returns the parsed header links of the response, if any. |
| [next](00052-requests.Response.next.md) | property | Returns a PreparedRequest for the next request in a redirect chain, if there is one. |
| [ok](00053-requests.Response.ok.md) | property | Returns True if :attr:`status_code` is less than 400, False if not. |
| [raise_for_status](00054-requests.Response.raise_for_status.md) | function | Raises :class:`HTTPError`, if one occurred. |
| [text](00055-requests.Response.text.md) | property | Content of the response, in unicode. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests')
obj = m
obj = inspect.getattr_static(obj, 'Response')
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
The :class:`Response <Response>` object, which contains a
    server's response to an HTTP request.
    
```

[Full module inspection](../modules/00007-requests.md)
