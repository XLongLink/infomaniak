from infomaniak.resource import Resouce, AsyncResource


class Ip(Resouce):
    """Cloud database IP allowlist resources."""

    def list(self) -> None:
        """List allowed IP addresses for a managed cloud database."""
        raise NotImplementedError("Cloud database IP list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create an allowed IP address for a managed cloud database."""
        raise NotImplementedError("Cloud database IP create endpoint is not implemented yet.")

    def remove(self) -> None:
        """Remove an allowed IP address for a managed cloud database."""
        raise NotImplementedError("Cloud database IP remove endpoint is not implemented yet.")


class AsyncIp(AsyncResource):
    """Async cloud database IP allowlist resources."""

    async def list(self) -> None:
        """List allowed IP addresses for a managed cloud database."""
        raise NotImplementedError("Cloud database IP list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create an allowed IP address for a managed cloud database."""
        raise NotImplementedError("Cloud database IP create endpoint is not implemented yet.")

    async def remove(self) -> None:
        """Remove an allowed IP address for a managed cloud database."""
        raise NotImplementedError("Cloud database IP remove endpoint is not implemented yet.")
