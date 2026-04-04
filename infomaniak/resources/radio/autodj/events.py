from infomaniak.resource import Resouce, AsyncResource


class Events(Resouce):
    """Radio AutoDJ events endpoints."""

    def list(self) -> None:
        """List all AutoDJ events."""
        raise NotImplementedError("Radio.autodj.events.list is not implemented yet.")

    def create(self) -> None:
        """Create or store an AutoDJ event."""
        raise NotImplementedError("Radio.autodj.events.create is not implemented yet.")

    def get(self) -> None:
        """Display a specific AutoDJ event."""
        raise NotImplementedError("Radio.autodj.events.get is not implemented yet.")

    def update(self) -> None:
        """Update an AutoDJ event."""
        raise NotImplementedError("Radio.autodj.events.update is not implemented yet.")

    def delete(self) -> None:
        """Delete an AutoDJ event."""
        raise NotImplementedError("Radio.autodj.events.delete is not implemented yet.")


class AsyncEvents(AsyncResource):
    """Async radio AutoDJ events endpoints."""

    async def list(self) -> None:
        """List all AutoDJ events."""
        raise NotImplementedError("AsyncRadio.autodj.events.list is not implemented yet.")

    async def create(self) -> None:
        """Create or store an AutoDJ event."""
        raise NotImplementedError("AsyncRadio.autodj.events.create is not implemented yet.")

    async def get(self) -> None:
        """Display a specific AutoDJ event."""
        raise NotImplementedError("AsyncRadio.autodj.events.get is not implemented yet.")

    async def update(self) -> None:
        """Update an AutoDJ event."""
        raise NotImplementedError("AsyncRadio.autodj.events.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete an AutoDJ event."""
        raise NotImplementedError("AsyncRadio.autodj.events.delete is not implemented yet.")
