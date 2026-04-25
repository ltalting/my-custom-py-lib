from os import environ
from pathlib import Path
from custom_shared.log_util import log_msg
from custom_shared.control_functions import exit_script
from custom_shared.filesystem_functions import is_file

def parse_env_file(env_file_path: Path):
    if is_file(env_file_path):
        for line in env_file_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, _, value = line.partition("=")
            environ.setdefault(key, value)
    else:
        log_msg("ERROR: Could not find .env file. It should be placed in the directory the script is being executed from.", "red")
        exit_script(1)