from infomaniak.resource import AsyncResource, Resouce


class Data(Resouce):
    """Cloud database reference data resources."""

    def regions(self) -> None:
        """List available cloud database regions."""
        raise NotImplementedError("Cloud database data regions endpoint is not implemented yet.")

    def packs(self) -> None:
        """List available cloud database packs."""
        raise NotImplementedError("Cloud database data packs endpoint is not implemented yet.")

    def types(self) -> None:
        """List available cloud database types."""
        raise NotImplementedError("Cloud database data types endpoint is not implemented yet.")


class AsyncData(AsyncResource):
    """Async cloud database reference data resources."""

    async def regions(self) -> None:
        """List available cloud database regions."""
        raise NotImplementedError("Cloud database data regions endpoint is not implemented yet.")

    async def packs(self) -> None:
        """List available cloud database packs."""
        raise NotImplementedError("Cloud database data packs endpoint is not implemented yet.")

    async def types(self) -> None:
        """List available cloud database types."""
        raise NotImplementedError("Cloud database data types endpoint is not implemented yet.")


__all__ = ["Data", "AsyncData"]
