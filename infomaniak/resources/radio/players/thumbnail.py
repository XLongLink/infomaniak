from infomaniak.resource import Resouce, AsyncResource


class Thumbnail(Resouce):
    """Radio players thumbnail endpoints."""

    def update(self) -> None:
        """Update a player's thumbnail."""
        raise NotImplementedError("Radio.players.thumbnail.update is not implemented yet.")

    def delete(self) -> None:
        """Delete a player's thumbnail."""
        raise NotImplementedError("Radio.players.thumbnail.delete is not implemented yet.")


class AsyncThumbnail(AsyncResource):
    """Async radio players thumbnail endpoints."""

    async def update(self) -> None:
        """Update a player's thumbnail."""
        raise NotImplementedError("AsyncRadio.players.thumbnail.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete a player's thumbnail."""
        raise NotImplementedError("AsyncRadio.players.thumbnail.delete is not implemented yet.")
