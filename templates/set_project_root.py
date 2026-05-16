################### SET_PROJECT_ROOT #########################

from json import dumps
from pathlib import Path
from sys import path as SysPath, stderr, exit
import os

# Absolute path of this file
FILE_PATH = Path(__file__)
current_dir = FILE_PATH.resolve().parent
# Read from env (comma-separated), fallback to default
PROJECT_ROOTS = os.getenv("PROJECT_ROOTS")
if PROJECT_ROOTS:
    root_dir_names = [name.strip() for name in PROJECT_ROOTS.split(",") if name.strip()]
else:
    root_dir_names = ["tor-dl"]

project_root = None

# Walk upward once, resolving project_root directly
while True:
    # Primary: explicit root match
    if current_dir.name in root_dir_names:
        project_root = current_dir
        break
    # Fallback: parent of "custom_shared"
    if current_dir.name == "custom_shared":
        project_root = current_dir.parent
        break
    # Reached filesystem root
    if current_dir.parent == current_dir:
        break
    current_dir = current_dir.parent
# Validate result
if project_root is None:
    stderr.write(
        dumps(
            {
                "status": "errored",
                "message": (
                    f"Did not find project root '{root_dir_names}' or a "
                    f"'custom_shared' ancestor during imports in {FILE_PATH}"
                ),
            }
        )
    )
    exit(1)
# Ensure project root is at the front of sys.path
if str(project_root) not in SysPath:
    SysPath.insert(0, str(project_root))

################# SET_PROJECT_ROOT ##########################