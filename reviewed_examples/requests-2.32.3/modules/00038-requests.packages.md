# requests.packages

Source: `requests/packages.py`

```text
No module docstring.
```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('requests.packages')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## import sys

```json
{
  "name": "import sys",
  "kind": "import",
  "line": 1,
  "from_module": null,
  "level": 0,
  "bindings": [
    {
      "imported": "sys",
      "local": "sys"
    }
  ]
}
```

```text
No docstring available.
```

## from .compat import chardet

```json
{
  "name": "from .compat import chardet",
  "kind": "import",
  "line": 3,
  "from_module": "compat",
  "level": 1,
  "bindings": [
    {
      "imported": "chardet",
      "local": "chardet"
    }
  ]
}
```

```text
No docstring available.
```

## target

```json
{
  "name": "target",
  "kind": "assignment",
  "line": 17,
  "source": "target = chardet.__name__",
  "conditional": true
}
```

```text
No docstring available.
```
