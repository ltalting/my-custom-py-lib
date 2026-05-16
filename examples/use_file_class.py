################### SET_PROJECT_ROOT #########################
# Python compatibility:
# - Requires Python 3.8+
#     - pathlib.Path
#     - f-strings
# - Tested on: 3.8, 3.9, 3.10, 3.11, 3.12
# - May work on 3.7, but not officially supported
from json import dumps
from pathlib import Path
from sys import path as SysPath, stderr, exit
import os

# Absolute path of this file
FILE_PATH = Path(__file__)
abs_path = FILE_PATH.resolve()
current_dir = abs_path.parent
# Read from env (comma-separated), fallback to default
PROJECT_ROOTS = os.getenv("PROJECT_ROOTS")
if PROJECT_ROOTS:
    root_dir_names = [name.strip() for name in PROJECT_ROOTS.split(",") if name.strip()]
else:
    root_dir_names = ["tor-dl"]

# Walk up the directory tree until a matching root directory is found
while True:
    # Primary condition: directory name match
    if current_dir.name in root_dir_names:
        break

    # Fallback condition: contains a "custom_shared" directory
    if (current_dir / "custom_shared").is_dir():
        break

    # Reached filesystem root without finding a match
    if current_dir.parent == current_dir:
        stderr.write(
            dumps(
                {
                    "status": "errored",
                    "message": (
                        f"Did not find project root '{root_dir_names}' or a parent of "
                        f"'custom_shared' during imports in {FILE_PATH}"
                    ),
                }
            )
        )
        exit(1)

    current_dir = current_dir.parent

# Ensure project root is at the front of sys.path
if str(current_dir) not in SysPath:
    SysPath.insert(0, str(current_dir))

################# SET_PROJECT_ROOT ##########################
from custom_shared.classes.file import File

path = ""
file = File.from_path(path, False)
file.line_count()
file2 = File(path)
file2.line_count()

print(file)