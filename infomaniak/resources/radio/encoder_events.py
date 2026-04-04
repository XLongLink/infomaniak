from infomaniak.resource import Resouce, AsyncResource


class EncoderEvents(Resouce):
    """Radio encoder events endpoints."""

    def list(self) -> None:
        """List encoder events."""
        raise NotImplementedError("Radio.encoder_events.list is not implemented yet.")


class AsyncEncoderEvents(AsyncResource):
    """Async radio encoder events endpoints."""

    async def list(self) -> None:
        """List encoder events."""
        raise NotImplementedError("AsyncRadio.encoder_events.list is not implemented yet.")
