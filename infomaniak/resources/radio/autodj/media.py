from infomaniak.resource import AsyncResource, Resouce


class Media(Resouce):
    """Radio AutoDJ media endpoints."""

    def list(self) -> None:
        """List AutoDJ media."""
        raise NotImplementedError("Radio.autodj.media.list is not implemented yet.")

    def create(self) -> None:
        """Upload or store an AutoDJ media item."""
        raise NotImplementedError("Radio.autodj.media.create is not implemented yet.")

    def get(self) -> None:
        """Display a specific AutoDJ media item."""
        raise NotImplementedError("Radio.autodj.media.get is not implemented yet.")

    def update(self) -> None:
        """Update an AutoDJ media item."""
        raise NotImplementedError("Radio.autodj.media.update is not implemented yet.")

    def delete(self) -> None:
        """Delete an AutoDJ media item."""
        raise NotImplementedError("Radio.autodj.media.delete is not implemented yet.")


class AsyncMedia(AsyncResource):
    """Async radio AutoDJ media endpoints."""

    async def list(self) -> None:
        """List AutoDJ media."""
        raise NotImplementedError("AsyncRadio.autodj.media.list is not implemented yet.")

    async def create(self) -> None:
        """Upload or store an AutoDJ media item."""
        raise NotImplementedError("AsyncRadio.autodj.media.create is not implemented yet.")

    async def get(self) -> None:
        """Display a specific AutoDJ media item."""
        raise NotImplementedError("AsyncRadio.autodj.media.get is not implemented yet.")

    async def update(self) -> None:
        """Update an AutoDJ media item."""
        raise NotImplementedError("AsyncRadio.autodj.media.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete an AutoDJ media item."""
        raise NotImplementedError("AsyncRadio.autodj.media.delete is not implemented yet.")
