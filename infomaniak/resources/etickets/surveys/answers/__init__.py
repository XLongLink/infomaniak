from .passes import Passes, AsyncPasses
from .tickets import Tickets, AsyncTickets
from infomaniak.resource import Resouce, AsyncResource


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


__all__ = [
    "Answers",
    "AsyncAnswers",
    "Passes",
    "AsyncPasses",
    "Tickets",
    "AsyncTickets",
]
