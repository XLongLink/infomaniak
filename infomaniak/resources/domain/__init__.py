from infomaniak.resource import AsyncResource, Resouce

from .dnssec import AsyncDNSSEC, DNSSEC
from .nameservers import AsyncNameservers, Nameservers
from .order import AsyncOrder, Order
from .zone import AsyncZone, Zone


class Domain(Resouce):
    """Domain resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.zone = Zone(client)
        self.order = Order(client)
        self.nameservers = Nameservers(client)
        self.dnssec = DNSSEC(client)

    def show(self) -> None:
        """Show a domain."""
        raise NotImplementedError("Domain.show is not implemented yet.")

    def list(self) -> None:
        """List domains."""
        raise NotImplementedError("Domain.list is not implemented yet.")


class AsyncDomain(AsyncResource):
    """Async domain resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.zone = AsyncZone(client)
        self.order = AsyncOrder(client)
        self.nameservers = AsyncNameservers(client)
        self.dnssec = AsyncDNSSEC(client)

    async def show(self) -> None:
        """Show a domain."""
        raise NotImplementedError("AsyncDomain.show is not implemented yet.")

    async def list(self) -> None:
        """List domains."""
        raise NotImplementedError("AsyncDomain.list is not implemented yet.")


__all__ = [
    "Domain",
    "AsyncDomain",
    "Zone",
    "AsyncZone",
    "Order",
    "AsyncOrder",
    "Nameservers",
    "AsyncNameservers",
    "DNSSEC",
    "AsyncDNSSEC",
]
