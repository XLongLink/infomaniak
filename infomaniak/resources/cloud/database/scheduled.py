from infomaniak.resource import AsyncResource, Resouce


class Scheduled(Resouce):
    """Cloud database scheduled backups resources."""

    def list(self) -> None:
        """List scheduled backups for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a scheduled backup for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups create endpoint is not implemented yet.")

    def get(self) -> None:
        """Retrieve a scheduled backup for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups get endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a scheduled backup for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups delete endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a scheduled backup for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups update endpoint is not implemented yet.")


class AsyncScheduled(AsyncResource):
    """Async cloud database scheduled backups resources."""

    async def list(self) -> None:
        """List scheduled backups for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a scheduled backup for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups create endpoint is not implemented yet.")

    async def get(self) -> None:
        """Retrieve a scheduled backup for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups get endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a scheduled backup for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups delete endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a scheduled backup for a managed cloud database."""
        raise NotImplementedError("Cloud database scheduled backups update endpoint is not implemented yet.")


__all__ = ["Scheduled", "AsyncScheduled"]
