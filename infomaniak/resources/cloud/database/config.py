from infomaniak.resource import AsyncResource, Resouce


class Config(Resouce):
    """Cloud database configuration resources."""

    def get(self) -> None:
        """Retrieve a database configuration entry."""
        raise NotImplementedError("Cloud database config get endpoint is not implemented yet.")

    def list(self) -> None:
        """List database configuration entries."""
        raise NotImplementedError("Cloud database config list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a database configuration entry."""
        raise NotImplementedError("Cloud database config create endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a database configuration entry."""
        raise NotImplementedError("Cloud database config update endpoint is not implemented yet.")

    def remove(self) -> None:
        """Remove a database configuration entry."""
        raise NotImplementedError("Cloud database config remove endpoint is not implemented yet.")


class AsyncConfig(AsyncResource):
    """Async cloud database configuration resources."""

    async def get(self) -> None:
        """Retrieve a database configuration entry."""
        raise NotImplementedError("Cloud database config get endpoint is not implemented yet.")

    async def list(self) -> None:
        """List database configuration entries."""
        raise NotImplementedError("Cloud database config list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a database configuration entry."""
        raise NotImplementedError("Cloud database config create endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a database configuration entry."""
        raise NotImplementedError("Cloud database config update endpoint is not implemented yet.")

    async def remove(self) -> None:
        """Remove a database configuration entry."""
        raise NotImplementedError("Cloud database config remove endpoint is not implemented yet.")


__all__ = ["Config", "AsyncConfig"]
