from pathlib import Path
from ..log_util import log_msg
from ..constants import extensions
from ..types.filesystem.file_metadata import FileMetadata
from ..types.filesystem.video_file_metadata import VideoFileMetadata
from ..types.filesystem.link_file_metadata import LinkFileMetadata
from ..types.filesystem.path_like import PathLike

class File:
    def __init__(self, path: PathLike):
        self.path: Path = Path(path)
        self.metadata: FileMetadata = self._build_metadata()
    
    def __str__(self) -> str:
        return str(self.metadata)

    @classmethod
    def from_path(cls, path: PathLike, raise_on_fail: bool = True) -> "File | None":
        p = Path(path)
        if p.is_file():
            return cls(p)
        if raise_on_fail:
            log_msg(f"Not a file: {p}", "red", exit = 1)
        return None

    def _build_metadata(self) -> FileMetadata:
        ext = self.path.suffix

        if ext in extensions.VIDEO_EXTENSIONS:
            return VideoFileMetadata(path = self.path, extension = ext)
        elif ext in extensions.LINK_EXTENSIONS:
            return LinkFileMetadata(path = self.path, extension = ext)
        else:
            return FileMetadata(path = self.path, extension = ext)

    def line_count(self) -> int:
        with self.path.open("r") as f:
            return sum(1 for _ in f)

    def print(self) -> None:
        if self.metadata.extension in extensions.TEXT_EXTENSIONS:
            line_count = self.line_count()
            pad_width = len(str(line_count)) + 2

            with self.path.open("r", encoding="utf-8", errors="replace") as f:
                for line_number, line in enumerate(f, start=1):
                    padded = str(line_number).ljust(pad_width, " ")
                    log_msg(f"{padded}{line.rstrip()}")

        elif self.metadata.extension in extensions.VIDEO_EXTENSIONS:
            log_msg("VIDEO FILE DETECTED: print() not implemented.", "yellow")

        else:
            log_msg(
                f"ERROR: File with extension {self.extension} is not printable",
                "red",
                1,
            )