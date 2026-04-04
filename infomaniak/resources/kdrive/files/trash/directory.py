from infomaniak.resource import Resouce, AsyncResource


class Directory(Resouce):
    """kDrive resource for trashed directory endpoints."""

    def count(self) -> None:
        """Count items in a trashed directory."""
        raise NotImplementedError("kDrive files.trash.directory.count endpoint is not implemented yet.")

    def list(self) -> None:
        """List files in a trashed directory."""
        raise NotImplementedError("kDrive files.trash.directory.list endpoint is not implemented yet.")


class AsyncDirectory(AsyncResource):
    """Async kDrive resource for trashed directory endpoints."""

    async def count(self) -> None:
        """Count items in a trashed directory."""
        raise NotImplementedError("kDrive files.trash.directory.count endpoint is not implemented yet.")

    async def list(self) -> None:
        """List files in a trashed directory."""
        raise NotImplementedError("kDrive files.trash.directory.list endpoint is not implemented yet.")
