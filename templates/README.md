# templates/

Copy-paste boilerplate intended to be dropped into other scripts. Nothing here is imported as a module — these files are meant to be read and adapted.

## `set_project_root.py`

A self-contained `sys.path` bootstrapper. Paste the block between the `SET_PROJECT_ROOT` delimiters at the top of any script that needs to import from `custom_shared`.

**How it works:**

1. Walks up the directory tree from the script's own location.
2. Stops when it finds a directory whose name matches one of the entries in `PROJECT_ROOTS` (read from the environment variable of the same name, comma-separated; defaults to `"tor-dl"`).
3. Falls back to stopping at the parent of any directory named `custom_shared`.
4. Exits with a JSON error on stderr if neither condition is met.
5. Prepends the resolved root to `sys.path`.

**Configuration:**

| Env var | Default | Description |
|---|---|---|
| `PROJECT_ROOTS` | `tor-dl` | Comma-separated list of valid project root directory names |

**Usage:**

```python
################### SET_PROJECT_ROOT #########################
# ... paste block here ...
################# SET_PROJECT_ROOT ##########################

from custom_shared.log_util import log_msg  # now works
```

See [`examples/use_file_class.py`](../examples/use_file_class.py) for a working reference.
