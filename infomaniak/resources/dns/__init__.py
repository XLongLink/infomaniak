from .tld import TLD, AsyncTLD
from .zone import Zone, AsyncZone
from .domain import Domain, AsyncDomain
from infomaniak.resource import Resouce, AsyncResource


class DNS(Resouce):
    """DNS resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.domain = Domain(client)
        self.tld = TLD(client)
        self.zone = Zone(client)


class AsyncDNS(AsyncResource):
    """Async DNS resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.domain = AsyncDomain(client)
        self.tld = AsyncTLD(client)
        self.zone = AsyncZone(client)
