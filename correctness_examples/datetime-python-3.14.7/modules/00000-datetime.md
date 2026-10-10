# datetime

Source: `datetime.py`

```text
Specific date/time and related types.

See https://data.iana.org/time-zones/tz-link.html for
time zone and DST data sources.

```

## Manual inspection

```python
import importlib, inspect
m = importlib.import_module('datetime')
dir(m)
help(m)
inspect.getmembers_static(m)
# For a discovered callable:
# inspect.signature(m.function_name)
# inspect.getdoc(m.function_name)
# inspect.getsource(m.function_name)
```

## from _datetime import *

```json
{
  "name": "from _datetime import *",
  "kind": "import",
  "line": 8,
  "from_module": "_datetime",
  "level": 0,
  "bindings": [
    {
      "imported": "*",
      "local": "*"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## from _pydatetime import *

```json
{
  "name": "from _pydatetime import *",
  "kind": "import",
  "line": 10,
  "from_module": "_pydatetime",
  "level": 0,
  "bindings": [
    {
      "imported": "*",
      "local": "*"
    }
  ],
  "conditional": true
}
```

```text
No docstring available.
```

## __all__

```json
{
  "name": "__all__",
  "kind": "assignment",
  "line": 12,
  "source": "__all__ = ('date', 'datetime', 'time', 'timedelta', 'timezone', 'tzinfo', 'MINYEAR', 'MAXYEAR', 'UTC')"
}
```

```text
No docstring available.
```
