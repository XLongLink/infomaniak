from infomaniak.resource import Resouce, AsyncResource


class Zone(Resouce):
    """Domain zone endpoints."""

    def list(self) -> None:
        """List DNS zones."""
        raise NotImplementedError("Domain.zone.list is not implemented yet.")


class AsyncZone(AsyncResource):
    """Async domain zone endpoints."""

    async def list(self) -> None:
        """List DNS zones."""
        raise NotImplementedError("AsyncDomain.zone.list is not implemented yet.")
