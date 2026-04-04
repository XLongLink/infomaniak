from infomaniak.resource import Resouce, AsyncResource


class Passes(Resouce):
    """eTickets survey answers for passes endpoints."""

    def list(self) -> None:
        """List pass survey answers (GET /2/etickets/surveys/answers/passes)."""
        raise NotImplementedError("Etickets.surveys.answers.passes.list is not implemented yet.")

    def update(self) -> None:
        """Update or clear pass survey answers (PATCH /2/etickets/surveys/answers/passes)."""
        raise NotImplementedError("Etickets.surveys.answers.passes.update is not implemented yet.")


class AsyncPasses(AsyncResource):
    """Async eTickets survey answers for passes endpoints."""

    async def list(self) -> None:
        """List pass survey answers (GET /2/etickets/surveys/answers/passes)."""
        raise NotImplementedError("AsyncEtickets.surveys.answers.passes.list is not implemented yet.")

    async def update(self) -> None:
        """Update or clear pass survey answers (PATCH /2/etickets/surveys/answers/passes)."""
        raise NotImplementedError("AsyncEtickets.surveys.answers.passes.update is not implemented yet.")
