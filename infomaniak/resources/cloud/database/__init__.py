from infomaniak.resource import AsyncResource, Resouce

from .backups import AsyncBackups, Backups
from .config import AsyncConfig, Config
from .data import AsyncData, Data
from .ip import AsyncIp, Ip
from .restore import AsyncRestore, Restore


class Database(Resouce):
    """Cloud database resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.backups = Backups(client)
        self.config = Config(client)
        self.data = Data(client)
        self.ip = Ip(client)
        self.restore = Restore(client)

    def list(self) -> None:
        """List managed cloud databases."""
        raise NotImplementedError("Cloud database list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a managed cloud database."""
        raise NotImplementedError("Cloud database create endpoint is not implemented yet.")

    def get(self) -> None:
        """Retrieve a managed cloud database."""
        raise NotImplementedError("Cloud database get endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a managed cloud database."""
        raise NotImplementedError("Cloud database delete endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a managed cloud database."""
        raise NotImplementedError("Cloud database update endpoint is not implemented yet.")

    def password(self) -> None:
        """Rotate or update a managed cloud database password."""
        raise NotImplementedError("Cloud database password endpoint is not implemented yet.")


class AsyncDatabase(AsyncResource):
    """Async cloud database resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.backups = AsyncBackups(client)
        self.config = AsyncConfig(client)
        self.data = AsyncData(client)
        self.ip = AsyncIp(client)
        self.restore = AsyncRestore(client)

    async def list(self) -> None:
        """List managed cloud databases."""
        raise NotImplementedError("Cloud database list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a managed cloud database."""
        raise NotImplementedError("Cloud database create endpoint is not implemented yet.")

    async def get(self) -> None:
        """Retrieve a managed cloud database."""
        raise NotImplementedError("Cloud database get endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a managed cloud database."""
        raise NotImplementedError("Cloud database delete endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a managed cloud database."""
        raise NotImplementedError("Cloud database update endpoint is not implemented yet.")

    async def password(self) -> None:
        """Rotate or update a managed cloud database password."""
        raise NotImplementedError("Cloud database password endpoint is not implemented yet.")


__all__ = [
    "Backups",
    "Config",
    "Data",
    "Ip",
    "Restore",
    "AsyncBackups",
    "AsyncConfig",
    "AsyncData",
    "AsyncIp",
    "AsyncRestore",
    "Database",
    "AsyncDatabase",
]
