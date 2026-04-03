from infomaniak.resource import AsyncResource, Resouce


class Nameservers(Resouce):
    """Domain nameserver endpoints."""

    def update(self) -> None:
        """Update nameservers for a domain."""
        raise NotImplementedError("Domain.nameservers.update is not implemented yet.")


class AsyncNameservers(AsyncResource):
    """Async domain nameserver endpoints."""

    async def update(self) -> None:
        """Update nameservers for a domain."""
        raise NotImplementedError(
            "AsyncDomain.nameservers.update is not implemented yet."
        )
