from infomaniak.resource import AsyncResource, Resouce

from .search import AsyncSearch, Search
from .trash import AsyncTrash, Trash
from .upload import AsyncUpload, Upload


class Files(Resouce):
    """kDrive resource for file and directory endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.upload = Upload(client)
        self.trash = Trash(client)
        self.search = Search(client)

    def display(self) -> None:
        """Get file or directory details."""
        raise NotImplementedError("kDrive files.display endpoint is not implemented yet.")

    def list(self) -> None:
        """List files and directories in a folder."""
        raise NotImplementedError("kDrive files.list endpoint is not implemented yet.")

    def get_by_filename(self) -> None:
        """Get a child by filename."""
        raise NotImplementedError("kDrive files.get_by_filename endpoint is not implemented yet.")

    def count(self) -> None:
        """Count elements in a directory."""
        raise NotImplementedError("kDrive files.count endpoint is not implemented yet.")

    def create_directory(self) -> None:
        """Create a directory."""
        raise NotImplementedError("kDrive files.create_directory endpoint is not implemented yet.")

    def create_default_file(self) -> None:
        """Create a default file."""
        raise NotImplementedError("kDrive files.create_default_file endpoint is not implemented yet.")

    def rename(self) -> None:
        """Rename a file or directory."""
        raise NotImplementedError("kDrive files.rename endpoint is not implemented yet.")

    def move(self) -> None:
        """Move a file or directory."""
        raise NotImplementedError("kDrive files.move endpoint is not implemented yet.")

    def copy_to_drive(self) -> None:
        """Copy a file to another drive."""
        raise NotImplementedError("kDrive files.copy_to_drive endpoint is not implemented yet.")

    def copy_to_directory(self) -> None:
        """Copy a file into a directory."""
        raise NotImplementedError("kDrive files.copy_to_directory endpoint is not implemented yet.")

    def duplicate(self) -> None:
        """Duplicate a file or directory."""
        raise NotImplementedError("kDrive files.duplicate endpoint is not implemented yet.")

    def convert(self) -> None:
        """Convert a file to another format."""
        raise NotImplementedError("kDrive files.convert endpoint is not implemented yet.")

    def delete(self) -> None:
        """Move a file or directory to the trash."""
        raise NotImplementedError("kDrive files.delete endpoint is not implemented yet.")

    def unlock(self) -> None:
        """Unlock a file or directory."""
        raise NotImplementedError("kDrive files.unlock endpoint is not implemented yet.")

    def update_modification_date(self) -> None:
        """Update the modification date of a file."""
        raise NotImplementedError("kDrive files.update_modification_date endpoint is not implemented yet.")

    def download(self) -> None:
        """Download a file."""
        raise NotImplementedError("kDrive files.download endpoint is not implemented yet.")

    def preview(self) -> None:
        """Get a file preview."""
        raise NotImplementedError("kDrive files.preview endpoint is not implemented yet.")

    def thumbnail(self) -> None:
        """Get a file thumbnail."""
        raise NotImplementedError("kDrive files.thumbnail endpoint is not implemented yet.")

    def size(self) -> None:
        """Get file size."""
        raise NotImplementedError("kDrive files.size endpoint is not implemented yet.")

    def hash(self) -> None:
        """Get file hash."""
        raise NotImplementedError("kDrive files.hash endpoint is not implemented yet.")

    def temp_url(self) -> None:
        """Get a temporary download URL."""
        raise NotImplementedError("kDrive files.temp_url endpoint is not implemented yet.")


class AsyncFiles(AsyncResource):
    """Async kDrive resource for file and directory endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.upload = AsyncUpload(client)
        self.trash = AsyncTrash(client)
        self.search = AsyncSearch(client)

    async def display(self) -> None:
        """Get file or directory details."""
        raise NotImplementedError("kDrive files.display endpoint is not implemented yet.")

    async def list(self) -> None:
        """List files and directories in a folder."""
        raise NotImplementedError("kDrive files.list endpoint is not implemented yet.")

    async def get_by_filename(self) -> None:
        """Get a child by filename."""
        raise NotImplementedError("kDrive files.get_by_filename endpoint is not implemented yet.")

    async def count(self) -> None:
        """Count elements in a directory."""
        raise NotImplementedError("kDrive files.count endpoint is not implemented yet.")

    async def create_directory(self) -> None:
        """Create a directory."""
        raise NotImplementedError("kDrive files.create_directory endpoint is not implemented yet.")

    async def create_default_file(self) -> None:
        """Create a default file."""
        raise NotImplementedError("kDrive files.create_default_file endpoint is not implemented yet.")

    async def rename(self) -> None:
        """Rename a file or directory."""
        raise NotImplementedError("kDrive files.rename endpoint is not implemented yet.")

    async def move(self) -> None:
        """Move a file or directory."""
        raise NotImplementedError("kDrive files.move endpoint is not implemented yet.")

    async def copy_to_drive(self) -> None:
        """Copy a file to another drive."""
        raise NotImplementedError("kDrive files.copy_to_drive endpoint is not implemented yet.")

    async def copy_to_directory(self) -> None:
        """Copy a file into a directory."""
        raise NotImplementedError("kDrive files.copy_to_directory endpoint is not implemented yet.")

    async def duplicate(self) -> None:
        """Duplicate a file or directory."""
        raise NotImplementedError("kDrive files.duplicate endpoint is not implemented yet.")

    async def convert(self) -> None:
        """Convert a file to another format."""
        raise NotImplementedError("kDrive files.convert endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Move a file or directory to the trash."""
        raise NotImplementedError("kDrive files.delete endpoint is not implemented yet.")

    async def unlock(self) -> None:
        """Unlock a file or directory."""
        raise NotImplementedError("kDrive files.unlock endpoint is not implemented yet.")

    async def update_modification_date(self) -> None:
        """Update the modification date of a file."""
        raise NotImplementedError("kDrive files.update_modification_date endpoint is not implemented yet.")

    async def download(self) -> None:
        """Download a file."""
        raise NotImplementedError("kDrive files.download endpoint is not implemented yet.")

    async def preview(self) -> None:
        """Get a file preview."""
        raise NotImplementedError("kDrive files.preview endpoint is not implemented yet.")

    async def thumbnail(self) -> None:
        """Get a file thumbnail."""
        raise NotImplementedError("kDrive files.thumbnail endpoint is not implemented yet.")

    async def size(self) -> None:
        """Get file size."""
        raise NotImplementedError("kDrive files.size endpoint is not implemented yet.")

    async def hash(self) -> None:
        """Get file hash."""
        raise NotImplementedError("kDrive files.hash endpoint is not implemented yet.")

    async def temp_url(self) -> None:
        """Get a temporary download URL."""
        raise NotImplementedError("kDrive files.temp_url endpoint is not implemented yet.")


__all__ = ["Upload", "Trash", "Search", "AsyncUpload", "AsyncTrash", "AsyncSearch", "Files", "AsyncFiles"]
