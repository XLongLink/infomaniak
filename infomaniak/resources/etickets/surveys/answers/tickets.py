from infomaniak.resource import AsyncResource, Resouce


class Tickets(Resouce):
    """eTickets survey answers for tickets endpoints."""

    def list(self) -> None:
        """List ticket survey answers (GET /2/etickets/surveys/answers/tickets)."""
        raise NotImplementedError("Etickets.surveys.answers.tickets.list is not implemented yet.")

    def update(self) -> None:
        """Create or update ticket survey answers (PATCH /2/etickets/surveys/answers/tickets)."""
        raise NotImplementedError("Etickets.surveys.answers.tickets.update is not implemented yet.")


class AsyncTickets(AsyncResource):
    """Async eTickets survey answers for tickets endpoints."""

    async def list(self) -> None:
        """List ticket survey answers (GET /2/etickets/surveys/answers/tickets)."""
        raise NotImplementedError("AsyncEtickets.surveys.answers.tickets.list is not implemented yet.")

    async def update(self) -> None:
        """Create or update ticket survey answers (PATCH /2/etickets/surveys/answers/tickets)."""
        raise NotImplementedError("AsyncEtickets.surveys.answers.tickets.update is not implemented yet.")
