from infomaniak.resource import AsyncResource, Resouce

from .scheduled import AsyncScheduled, Scheduled


class Backups(Resouce):
    """Cloud database backups resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.scheduled = Scheduled(client)

    def list(self) -> None:
        """List backups for a managed cloud database."""
        raise NotImplementedError("Cloud database backups list endpoint is not implemented yet.")

    def get(self) -> None:
        """Retrieve a backup for a managed cloud database."""
        raise NotImplementedError("Cloud database backups get endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a backup for a managed cloud database."""
        raise NotImplementedError("Cloud database backups delete endpoint is not implemented yet.")


class AsyncBackups(AsyncResource):
    """Async cloud database backups resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.scheduled = AsyncScheduled(client)

    async def list(self) -> None:
        """List backups for a managed cloud database."""
        raise NotImplementedError("Cloud database backups list endpoint is not implemented yet.")

    async def get(self) -> None:
        """Retrieve a backup for a managed cloud database."""
        raise NotImplementedError("Cloud database backups get endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a backup for a managed cloud database."""
        raise NotImplementedError("Cloud database backups delete endpoint is not implemented yet.")


__all__ = ["Scheduled", "AsyncScheduled", "Backups", "AsyncBackups"]
