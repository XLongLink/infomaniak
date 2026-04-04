from infomaniak.resource import Resouce, AsyncResource


class Statistics(Resouce):
    """kDrive resource for statistics endpoints."""

    def usage(self) -> None:
        """Get drive usage statistics."""
        raise NotImplementedError("kDrive statistics.usage endpoint is not implemented yet.")

    def files(self) -> None:
        """Get file statistics."""
        raise NotImplementedError("kDrive statistics.files endpoint is not implemented yet.")


class AsyncStatistics(AsyncResource):
    """Async kDrive resource for statistics endpoints."""

    async def usage(self) -> None:
        """Get drive usage statistics."""
        raise NotImplementedError("kDrive statistics.usage endpoint is not implemented yet.")

    async def files(self) -> None:
        """Get file statistics."""
        raise NotImplementedError("kDrive statistics.files endpoint is not implemented yet.")
