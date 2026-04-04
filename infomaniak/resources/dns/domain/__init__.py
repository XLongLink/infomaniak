from .order import Order, AsyncOrder
from .dnssec import DNSSEC, AsyncDNSSEC
from .nameservers import Nameservers, AsyncNameservers
from infomaniak.resource import Resouce, AsyncResource


class Domain(Resouce):
    """DNS domain endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.dnssec = DNSSEC(client)
        self.nameservers = Nameservers(client)
        self.order = Order(client)

    def list(self) -> None:
        """List domains."""
        raise NotImplementedError("DNS.domain.list is not implemented yet.")

    def display(self) -> None:
        """Display one domain."""
        raise NotImplementedError("DNS.domain.display is not implemented yet.")


class AsyncDomain(AsyncResource):
    """Async DNS domain endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.dnssec = AsyncDNSSEC(client)
        self.nameservers = AsyncNameservers(client)
        self.order = AsyncOrder(client)

    async def list(self) -> None:
        """List domains."""
        raise NotImplementedError("AsyncDNS.domain.list is not implemented yet.")

    async def display(self) -> None:
        """Display one domain."""
        raise NotImplementedError("AsyncDNS.domain.display is not implemented yet.")


__all__ = [
    "Domain",
    "AsyncDomain",
    "DNSSEC",
    "AsyncDNSSEC",
    "Nameservers",
    "AsyncNameservers",
    "Order",
    "AsyncOrder",
]
