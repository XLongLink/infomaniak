from infomaniak.resource import AsyncResource, Resouce

from .passes import AsyncPasses, Passes
from .tickets import AsyncTickets, Tickets


class Answers(Resouce):
    """eTickets survey answers endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.passes = Passes(client)
        self.tickets = Tickets(client)


class AsyncAnswers(AsyncResource):
    """Async eTickets survey answers endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.passes = AsyncPasses(client)
        self.tickets = AsyncTickets(client)


__all__ = ["Answers", "AsyncAnswers", "Passes", "AsyncPasses", "Tickets", "AsyncTickets"]
