# classes/

OOP wrappers that provide a class-based interface to the library's filesystem functionality.

## `file.py` — `File`

A class representing a single file on disk. On instantiation it builds rich metadata and exposes utilities for counting lines and printing file contents.

### Constructor

```python
File(path: PathLike)
```

Accepts any `str` or `pathlib.Path`. Internally resolves the path and calls `_build_metadata()` to produce the appropriate `FileMetadata` subclass based on the file's extension.

### Class Methods

#### `File.from_path(path, raise_on_fail=True) -> File | None`

Safe alternative constructor. Returns `None` (or exits with an error) if the path is not a valid file.

```python
file = File.from_path("/some/path.txt", raise_on_fail=False)
if file:
    print(file.line_count())
```

### Instance Methods

| Method | Returns | Description |
|---|---|---|
| `line_count()` | `int` | Number of lines in the file |
| `print()` | `None` | Prints the file contents with line numbers to stdout |
| `__str__()` | `str` | JSON representation of the file's metadata |

### Metadata dispatch

The internal `_build_metadata()` method dispatches to one of three metadata types based on extension (sourced from `constants/extensions.py`):

| Extension group | Metadata type |
|---|---|
| `VIDEO_EXTENSIONS` (`.mkv`, `.avi`, `.mp4`) | `VideoFileMetadata` |
| `LINK_EXTENSIONS` (`.lnk`) | `LinkFileMetadata` |
| Everything else | `FileMetadata` |

### Notes

- `print()` is only implemented for text files (`TEXT_EXTENSIONS`). Video files log a warning; all other types exit with an error.
- Line numbers are left-padded to align with the total line count width.
