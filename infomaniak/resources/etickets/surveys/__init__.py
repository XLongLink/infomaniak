from .answers import Answers, AsyncAnswers
from infomaniak.resource import Resouce, AsyncResource


class Surveys(Resouce):
    """eTickets surveys endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.answers = Answers(client)

    def list(self) -> None:
        """List surveys (GET /2/etickets/surveys)."""
        raise NotImplementedError("Etickets.surveys.list is not implemented yet.")


class AsyncSurveys(AsyncResource):
    """Async eTickets surveys endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.answers = AsyncAnswers(client)

    async def list(self) -> None:
        """List surveys (GET /2/etickets/surveys)."""
        raise NotImplementedError("AsyncEtickets.surveys.list is not implemented yet.")


__all__ = [
    "Surveys",
    "AsyncSurveys",
    "Answers",
    "AsyncAnswers",
]
