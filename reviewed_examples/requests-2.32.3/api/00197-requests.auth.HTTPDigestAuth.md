# requests.auth.HTTPDigestAuth

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

Attaches HTTP Digest Authentication to the given Request object.

Kind: **class**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(username, password)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| username | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| password | positional or keyword | Yes | Not provided | — | Not described in the docstring |

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
m = importlib.import_module('requests.auth')
username = ...  # TODO: supply a valid value from your application
password = ...  # TODO: supply a valid value from your application
result = m.HTTPDigestAuth(username=username, password=password)
print(result)

```

## Public members

| Member | Kind | Purpose |
| --- | --- | --- |
| [build_digest_header](00198-requests.auth.HTTPDigestAuth.build_digest_header.md) | function | :rtype: str |
| [handle_401](00199-requests.auth.HTTPDigestAuth.handle_401.md) | function | Takes the given response and tries digest-auth, if needed. |
| [handle_redirect](00200-requests.auth.HTTPDigestAuth.handle_redirect.md) | function | Reset num_401_calls counter on redirects. |
| [init_per_thread_state](00201-requests.auth.HTTPDigestAuth.init_per_thread_state.md) | function | No description supplied by the package. |

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.auth')
obj = m
obj = inspect.getattr_static(obj, 'HTTPDigestAuth')
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
Attaches HTTP Digest Authentication to the given Request object.
```

[Full module inspection](../modules/00030-requests.auth.md)
