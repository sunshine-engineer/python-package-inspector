# requests.utils.address_in_network

[API index](../API_INDEX.md) · [Quick start](../QUICKSTART.md)

This function allows you to check if an IP belongs to a network subnet

Kind: **function**. Evidence: **source + runtime**. Discovery: **name heuristic**.

## Signature

```text
(ip, net)
```

## Inputs

| Parameter | Passing style | Required | Type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| ip | positional or keyword | Yes | Not provided | — | Not described in the docstring |
| net | positional or keyword | Yes | Not provided | — | Not described in the docstring |

## Returns and exceptions

Return annotation: `Not provided`.

Documented return/yield information:

- bool

No exception section was extracted. This does not mean the call cannot raise.

## Practice

No doctest-style usage example was supplied. Start with the inspection block below. Choose real inputs from the input table and original documentation; the generator does not invent valid values or expected results.

### Call template — edit before running

Generated from the signature, not a tested example. Replace every `...` placeholder with a valid value. Optional arguments use their declared defaults; add them from the input table when needed. Decorators or conditional definitions can affect runtime behavior.

```python
import importlib
m = importlib.import_module('requests.utils')
ip = ...  # TODO: supply a valid value from your application
net = ...  # TODO: supply a valid value from your application
result = m.address_in_network(ip=ip, net=net)
print(result)

```

### Inspect this exact API

```python
import importlib
import inspect

m = importlib.import_module('requests.utils')
obj = m
obj = inspect.getattr_static(obj, 'address_in_network')
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
This function allows you to check if an IP belongs to a network subnet

    Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
             returns False if ip = 192.168.1.1 and net = 192.168.100.0/24

    :rtype: bool
    
```

[Full module inspection](../modules/00042-requests.utils.md)
