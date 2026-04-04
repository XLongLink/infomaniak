from infomaniak.resource import Resouce, AsyncResource


class Date(Resouce):
    """eTickets date endpoints."""

    def list(self) -> None:
        """List all dates within a period (GET /2/etickets/date)."""
        raise NotImplementedError("Etickets.date.list is not implemented yet.")


class AsyncDate(AsyncResource):
    """Async eTickets date endpoints."""

    async def list(self) -> None:
        """List all dates within a period (GET /2/etickets/date)."""
        raise NotImplementedError("AsyncEtickets.date.list is not implemented yet.")
