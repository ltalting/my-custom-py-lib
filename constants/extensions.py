from typing import TypedDict

TEXT_EXTENSIONS: set[str] = {".txt", ".py", ".log"}
VIDEO_EXTENSIONS: set[str] = {".mkv", ".avi", ".mp4"}
LINK_EXTENSIONS: set[str] = {".lnk"}
ROM_EXTENSIONS: set[str] = {".gb", ".gbc", ".gba", ".nds", ".cxi", ".3ds"}
ZIP_EXTENSIONS: set[str] = {".zip", ".7z"}
UNVRSLPKMNRNDMZR_EXTENSIONS: set[str] = {".rnqs"}

class CLS_APP_EXTENSIONS(TypedDict):
    universalpokemonrandomizer: set[str]

APP_EXTENSIONS: CLS_APP_EXTENSIONS = {
    "universalpokemonrandomizer": UNVRSLPKMNRNDMZR_EXTENSIONS
}