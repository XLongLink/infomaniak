from infomaniak.resource import AsyncResource, Resouce


class Ticket(Resouce):
    """eTickets ticket endpoints."""

    def update(self) -> None:
        """Update ticket data (method signature to be finalized from OpenAPI)."""
        raise NotImplementedError("Etickets.ticket.update is not implemented yet.")


class AsyncTicket(AsyncResource):
    """Async eTickets ticket endpoints."""

    async def update(self) -> None:
        """Update ticket data (method signature to be finalized from OpenAPI)."""
        raise NotImplementedError("AsyncEtickets.ticket.update is not implemented yet.")
