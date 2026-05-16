# my-custom-py-lib

A personal Python utility library (`custom_shared`) providing reusable tools for filesystem introspection, shell execution, FTP transfers, logging, interactive prompts, and more.

## Requirements

- Python 3.8+
- `winshell` (only required for Windows shortcut `.lnk` support via `LinkFileMetadata`)

## Installation

Place this directory somewhere accessible and ensure its parent is on `sys.path`. See [`templates/set_project_root.py`](templates/set_project_root.py) for a copy-paste snippet that auto-resolves the project root at import time.

## Structure

```
my-custom-py-lib/
├── __init__.py                 # Top-level package exports
├── common_functs.py            # Small general-purpose helpers
├── control_functions.py        # Shell execution and VM lifecycle helpers
├── filesystem_functions.py     # Functional API for filesystem operations
├── ftp_conn.py                 # FTP connection and recursive download
├── la_vista_baby.py            # Safe script exit helpers
├── log_util.py                 # Colored terminal logging
├── parsers.py                  # .env file parser
├── question_master.py          # Interactive CLI prompt helpers
│
├── classes/                    # OOP wrappers
│   └── file.py                 # File class with metadata and print support
│
├── constants/                  # Shared constant definitions
│   └── extensions.py           # Extension sets by file type
│
├── examples/                   # Usage demonstrations
│   └── use_file_class.py       # Example: using the File class
│
├── templates/                  # Copy-paste boilerplate snippets
│   └── set_project_root.py     # sys.path bootstrapper
│
└── types/                      # Type definitions and dataclasses
    └── filesystem/             # Filesystem metadata types
```

## Module Overview

| Module | Purpose |
|---|---|
| `log_util` | Print colored, optionally indented messages to stdout/stderr |
| `common_functs` | General helpers (`dict_values_to_keys`, `any_to_str`) |
| `control_functions` | Run shell commands, manage Vagrant VMs, handle exit routines |
| `filesystem_functions` | Get/print metadata for files and directories |
| `ftp_conn` | Connect to FTP servers and recursively download directory trees |
| `la_vista_baby` | Validate and execute clean script exits |
| `parsers` | Parse `.env` files into `os.environ` |
| `question_master` | Ask validated CLI questions with range and case-sensitivity support |
| `classes/` | OOP wrappers around the functional filesystem API |
| `constants/` | Extension sets used across the library |
| `types/` | Dataclasses representing filesystem metadata |

## Quick Example

```python
from custom_shared.classes.file import File
from custom_shared.log_util import log_msg

file = File.from_path("/path/to/file.txt")
log_msg(f"Lines: {file.line_count()}", "green")
print(file)  # JSON metadata
```
