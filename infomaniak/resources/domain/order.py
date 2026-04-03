from infomaniak.resource import AsyncResource, Resouce


class Order(Resouce):
    """Domain order endpoints."""

    def check(self) -> None:
        """Check whether a domain can be ordered."""
        raise NotImplementedError("Domain.order.check is not implemented yet.")

    def create(self) -> None:
        """Create a domain order."""
        raise NotImplementedError("Domain.order.create is not implemented yet.")

    def transfer(self) -> None:
        """Transfer a domain."""
        raise NotImplementedError("Domain.order.transfer is not implemented yet.")


class AsyncOrder(AsyncResource):
    """Async domain order endpoints."""

    async def check(self) -> None:
        """Check whether a domain can be ordered."""
        raise NotImplementedError("AsyncDomain.order.check is not implemented yet.")

    async def create(self) -> None:
        """Create a domain order."""
        raise NotImplementedError("AsyncDomain.order.create is not implemented yet.")

    async def transfer(self) -> None:
        """Transfer a domain."""
        raise NotImplementedError("AsyncDomain.order.transfer is not implemented yet.")
