from infomaniak.resource import AsyncResource, Resouce


class Address(Resouce):
    """eTickets address endpoints."""

    def list(self) -> None:
        """List all addresses for a group (GET /2/etickets/address)."""
        raise NotImplementedError("Etickets.address.list is not implemented yet.")


class AsyncAddress(AsyncResource):
    """Async eTickets address endpoints."""

    async def list(self) -> None:
        """List all addresses for a group (GET /2/etickets/address)."""
        raise NotImplementedError("AsyncEtickets.address.list is not implemented yet.")
