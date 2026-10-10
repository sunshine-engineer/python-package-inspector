# requests.hooks

Source: `requests/hooks.py`

```text

requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.hooks')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## HOOKS

```json
{
  "name": "HOOKS",
  "kind": "assignment",
  "line": 12,
  "source": "HOOKS = ['response']"
}
```

```text
No docstring available.
```

## default_hooks

```json
{
  "name": "default_hooks",
  "kind": "function",
  "signature": "default_hooks()",
  "line": 15,
  "decorators": [],
  "parameters": [],
  "returns": null
}
```

```text
No docstring available.
```

## dispatch_hook

```json
{
  "name": "dispatch_hook",
  "kind": "function",
  "signature": "dispatch_hook(key, hooks, hook_data, **kwargs)",
  "line": 22,
  "decorators": [],
  "parameters": [
    {
      "name": "key",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hooks",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "hook_data",
      "kind": "positional or keyword",
      "annotation": null,
      "default": null,
      "required": true
    },
    {
      "name": "kwargs",
      "kind": "variadic keyword",
      "annotation": null,
      "default": null,
      "required": false
    }
  ],
  "returns": null
}
```

```text
Dispatches a hook dictionary on a given piece of data.
```
