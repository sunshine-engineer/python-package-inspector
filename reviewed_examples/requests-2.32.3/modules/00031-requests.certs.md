# requests.certs

Source: `requests/certs.py`

```text

requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.certs')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## from certifi import where

```json
{
  "name": "from certifi import where",
  "kind": "import",
  "line": 14,
  "from_module": "certifi",
  "level": 0,
  "bindings": [
    {
      "imported": "where",
      "local": "where"
    }
  ]
}
```

```text
No docstring available.
```
