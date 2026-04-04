from .directory import Directory, AsyncDirectory
from infomaniak.resource import Resouce, AsyncResource


class Trash(Resouce):
    """kDrive resource for trash endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.directory = Directory(client)

    def empty(self) -> None:
        """Empty the trash."""
        raise NotImplementedError("kDrive files.trash.empty endpoint is not implemented yet.")

    def count(self) -> None:
        """Count trashed items."""
        raise NotImplementedError("kDrive files.trash.count endpoint is not implemented yet.")

    def remove(self) -> None:
        """Permanently remove a trashed file."""
        raise NotImplementedError("kDrive files.trash.remove endpoint is not implemented yet.")

    def restore(self) -> None:
        """Restore a trashed file."""
        raise NotImplementedError("kDrive files.trash.restore endpoint is not implemented yet.")

    def thumbnail(self) -> None:
        """Get thumbnail of a trashed file."""
        raise NotImplementedError("kDrive files.trash.thumbnail endpoint is not implemented yet.")

    def list(self) -> None:
        """List files in trash."""
        raise NotImplementedError("kDrive files.trash.list endpoint is not implemented yet.")

    def display(self) -> None:
        """Get a specific trashed file."""
        raise NotImplementedError("kDrive files.trash.display endpoint is not implemented yet.")


class AsyncTrash(AsyncResource):
    """Async kDrive resource for trash endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.directory = AsyncDirectory(client)

    async def empty(self) -> None:
        """Empty the trash."""
        raise NotImplementedError("kDrive files.trash.empty endpoint is not implemented yet.")

    async def count(self) -> None:
        """Count trashed items."""
        raise NotImplementedError("kDrive files.trash.count endpoint is not implemented yet.")

    async def remove(self) -> None:
        """Permanently remove a trashed file."""
        raise NotImplementedError("kDrive files.trash.remove endpoint is not implemented yet.")

    async def restore(self) -> None:
        """Restore a trashed file."""
        raise NotImplementedError("kDrive files.trash.restore endpoint is not implemented yet.")

    async def thumbnail(self) -> None:
        """Get thumbnail of a trashed file."""
        raise NotImplementedError("kDrive files.trash.thumbnail endpoint is not implemented yet.")

    async def list(self) -> None:
        """List files in trash."""
        raise NotImplementedError("kDrive files.trash.list endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get a specific trashed file."""
        raise NotImplementedError("kDrive files.trash.display endpoint is not implemented yet.")
