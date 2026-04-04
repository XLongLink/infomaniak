from infomaniak.resource import Resouce, AsyncResource


class Users(Resouce):
    """Radio products users endpoints."""

    def list(self) -> None:
        """List users linked to a radio product."""
        raise NotImplementedError("Radio.products.users.list is not implemented yet.")


class AsyncUsers(AsyncResource):
    """Async radio products users endpoints."""

    async def list(self) -> None:
        """List users linked to a radio product."""
        raise NotImplementedError("AsyncRadio.products.users.list is not implemented yet.")
