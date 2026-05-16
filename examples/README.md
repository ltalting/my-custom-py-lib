# examples/

Runnable scripts demonstrating how to use the library. Each file is self-contained and includes the `set_project_root` bootstrapper so it can be executed directly without manual `sys.path` setup.

## `use_file_class.py`

Demonstrates basic usage of the `File` class from `custom_shared.classes.file`.

**What it shows:**
- Using `File.from_path()` (safe, returns `None` on failure) vs. `File()` (raises on failure)
- Calling `line_count()` on an instance
- Printing a `File` instance to get its JSON metadata

**To run:**

1. Set the `path` variable to a real file path.
2. Optionally set the `PROJECT_ROOTS` environment variable to your project root directory name (defaults to `"tor-dl"`), or ensure a `custom_shared/` directory exists somewhere up the tree from this file.
3. Execute:
   ```bash
   python examples/use_file_class.py
   ```

## Adding Examples

Drop new `.py` files here. Copy the `SET_PROJECT_ROOT` block from any existing example (or from `templates/set_project_root.py`) to the top so the script can locate the library regardless of where it's run from.
