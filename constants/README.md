# constants/

Shared constant definitions used throughout the library. Import directly from this package rather than hard-coding extension strings in calling code.

## `extensions.py`

Defines extension sets by file category, plus a typed app-extensions mapping.

### Extension Sets

| Name | Type | Values |
|---|---|---|
| `TEXT_EXTENSIONS` | `set[str]` | `.txt`, `.py`, `.log` |
| `VIDEO_EXTENSIONS` | `set[str]` | `.mkv`, `.avi`, `.mp4` |
| `LINK_EXTENSIONS` | `set[str]` | `.lnk` (Windows shortcuts) |
| `ROM_EXTENSIONS` | `set[str]` | `.gb`, `.gbc`, `.gba`, `.nds`, `.cxi`, `.3ds` |
| `ZIP_EXTENSIONS` | `set[str]` | `.zip`, `.7z` |
| `UNVRSLPKMNRNDMZR_EXTENSIONS` | `set[str]` | `.rnqs` (Universal Pokémon Randomizer) |

### App Extensions Mapping

```python
APP_EXTENSIONS: CLS_APP_EXTENSIONS = {
    "universalpokemonrandomizer": UNVRSLPKMNRNDMZR_EXTENSIONS
}
```

`CLS_APP_EXTENSIONS` is a `TypedDict` keying app names to their associated extension sets.

### Usage

```python
from custom_shared.constants import extensions

if path.suffix in extensions.VIDEO_EXTENSIONS:
    ...
```

### Extending

To add a new file category, add a new `set[str]` constant and, if needed, a new key to `CLS_APP_EXTENSIONS` and `APP_EXTENSIONS`.
