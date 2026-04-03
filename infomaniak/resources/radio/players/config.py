from infomaniak.resource import AsyncResource, Resouce


class Config(Resouce):
    """Radio players configuration endpoints."""

    def get(self) -> None:
        """Retrieve a player's configuration."""
        raise NotImplementedError("Radio.players.config.get is not implemented yet.")

    def update(self) -> None:
        """Update a player's configuration."""
        raise NotImplementedError("Radio.players.config.update is not implemented yet.")


class AsyncConfig(AsyncResource):
    """Async radio players configuration endpoints."""

    async def get(self) -> None:
        """Retrieve a player's configuration."""
        raise NotImplementedError("AsyncRadio.players.config.get is not implemented yet.")

    async def update(self) -> None:
        """Update a player's configuration."""
        raise NotImplementedError("AsyncRadio.players.config.update is not implemented yet.")
