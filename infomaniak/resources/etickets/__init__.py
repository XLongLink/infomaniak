from infomaniak.resource import AsyncResource, Resouce

from .address import Address, AsyncAddress
from .customers import AsyncCustomers, Customers
from .date import AsyncDate, Date
from .reservations import AsyncReservations, Reservations
from .surveys import AsyncSurveys, Surveys
from .ticket import AsyncTicket, Ticket


class Etickets(Resouce):
    """eTickets resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.address = Address(client)
        self.customers = Customers(client)
        self.date = Date(client)
        self.reservations = Reservations(client)
        self.surveys = Surveys(client)
        self.ticket = Ticket(client)


class AsyncEtickets(AsyncResource):
    """Async eTickets resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.address = AsyncAddress(client)
        self.customers = AsyncCustomers(client)
        self.date = AsyncDate(client)
        self.reservations = AsyncReservations(client)
        self.surveys = AsyncSurveys(client)
        self.ticket = AsyncTicket(client)


__all__ = [
    "Etickets",
    "AsyncEtickets",
    "Address",
    "AsyncAddress",
    "Customers",
    "AsyncCustomers",
    "Date",
    "AsyncDate",
    "Reservations",
    "AsyncReservations",
    "Surveys",
    "AsyncSurveys",
    "Ticket",
    "AsyncTicket",
]
