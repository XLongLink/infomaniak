from .date import Date, AsyncDate
from .ticket import Ticket, AsyncTicket
from .address import Address, AsyncAddress
from .surveys import Surveys, AsyncSurveys
from .customers import Customers, AsyncCustomers
from .reservations import Reservations, AsyncReservations
from infomaniak.resource import Resouce, AsyncResource


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
