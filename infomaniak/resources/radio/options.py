from infomaniak.resource import AsyncResource, Resouce


class Options(Resouce):
    """Radio options endpoints."""

    def list(self) -> None:
        """List available options for radio products."""
        raise NotImplementedError("Radio.options.list is not implemented yet.")


class AsyncOptions(AsyncResource):
    """Async radio options endpoints."""

    async def list(self) -> None:
        """List available options for radio products."""
        raise NotImplementedError("AsyncRadio.options.list is not implemented yet.")
