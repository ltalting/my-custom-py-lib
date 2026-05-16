# types/filesystem/

Dataclasses representing filesystem artifacts (files and directories) with rich metadata. All types serialize to JSON via a `to_dict()` / `__str__()` interface.

## Type Hierarchy

```
FilesystemArtifact          (base: path, name, timestamps)
├── FileMetadata            (adds: extension, size_in_bytes)
│   ├── VideoFileMetadata   (adds: duration, codec, dimensions, framerate, audio_codec, bitrate)
│   └── LinkFileMetadata    (adds: Windows shortcut target, working_directory, arguments, etc.)
└── DirectoryMetadata       (adds: contained_bytes, sub_directories, files)
```

---

## `filesystem_artifact.py` — `FilesystemArtifact`

Base dataclass for any path on disk. Validates existence on `__post_init__` and populates common metadata.

**Fields:**

| Field | Type | Description |
|---|---|---|
| `path` | `Path` | Resolved `pathlib.Path` |
| `name` | `str` | Stem (filename without extension) |
| `ext_name` | `str` | Full filename including extension |
| `created` | `datetime` | `ctime` of the path |
| `modified` | `datetime` | `mtime` of the path |
| `obtained_at` | `datetime` | When this object was instantiated |

Raises `FileNotFoundError` if the path does not exist.

---

## `file_metadata.py` — `FileMetadata`

Extends `FilesystemArtifact` with file-specific fields. Raises `ValueError` if the path is not a file.

**Additional fields:**

| Field | Type | Description |
|---|---|---|
| `extension` | `str` | File suffix (e.g. `".txt"`) |
| `size_in_bytes` | `int` | File size from `stat()` |

---

## `video_file_metadata.py` — `VideoFileMetadata`

Extends `FileMetadata` for video files. The video-specific fields (`duration`, `codec`, `bitrate`, `width`, `height`, `framerate`, `audio_codec`) are declared but **not populated automatically** — callers are responsible for filling them in after construction (e.g. via `ffprobe` or a media library).

**Additional fields:**

| Field | Type | Description |
|---|---|---|
| `duration` | `float \| None` | Duration in seconds |
| `codec` | `str \| None` | Video codec name |
| `bitrate` | `int \| None` | Bitrate in bits/s |
| `width` | `int \| None` | Frame width in pixels |
| `height` | `int \| None` | Frame height in pixels |
| `framerate` | `float \| None` | Frames per second |
| `audio_codec` | `str \| None` | Audio codec name |

---

## `link_file_metadata.py` — `LinkFileMetadata`

Extends `FileMetadata` for Windows shortcut (`.lnk`) files. Requires the `winshell` package.

**Additional fields:**

| Field | Type | Description |
|---|---|---|
| `target_path` | `str \| None` | Path the shortcut points to |
| `working_directory` | `str \| None` | Working directory of the shortcut |
| `arguments` | `str \| None` | Command-line arguments |
| `description` | `str \| None` | Shortcut description |
| `icon_location` | `str \| None` | Path to the icon |

Raises `ValueError` if the path is not a `.lnk` file.

---

## `directory_metadata.py` — `DirectoryMetadata`

Extends `FilesystemArtifact` for directories. Raises `ValueError` if the path is not a directory.

**Additional fields:**

| Field | Type | Description |
|---|---|---|
| `contained_bytes` | `int \| None` | Total size of all contained files (recursive) |
| `sub_directories` | `list[Path]` | Direct child directories |
| `files` | `list[Path]` | Direct child files |

---

## `path_like.py` — `PathLike`

A type alias:

```python
PathLike = Union[str, Path]
```

Used throughout the library as the accepted input type for any path argument.

---

## `file_like.py` — `FileLike`

A union type alias for any file metadata variant:

```python
FileLike = Union[FileMetadata, VideoFileMetadata]
```

Used as a return type in `filesystem_functions.py` when the exact subtype isn't known at call time.
