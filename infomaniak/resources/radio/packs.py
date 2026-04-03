from infomaniak.resource import AsyncResource, Resouce


class Packs(Resouce):
    """Radio packs endpoints."""

    def list(self) -> None:
        """List available radio packs."""
        raise NotImplementedError("Radio.packs.list is not implemented yet.")


class AsyncPacks(AsyncResource):
    """Async radio packs endpoints."""

    async def list(self) -> None:
        """List available radio packs."""
        raise NotImplementedError("AsyncRadio.packs.list is not implemented yet.")
