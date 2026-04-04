from infomaniak.resource import Resouce, AsyncResource


class ServerEvents(Resouce):
    """Radio server events endpoints."""

    def list(self) -> None:
        """List server events."""
        raise NotImplementedError("Radio.server_events.list is not implemented yet.")


class AsyncServerEvents(AsyncResource):
    """Async radio server events endpoints."""

    async def list(self) -> None:
        """List server events."""
        raise NotImplementedError("AsyncRadio.server_events.list is not implemented yet.")
