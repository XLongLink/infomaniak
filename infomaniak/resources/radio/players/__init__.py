from .config import Config, AsyncConfig
from .thumbnail import Thumbnail, AsyncThumbnail
from infomaniak.resource import Resouce, AsyncResource


class Players(Resouce):
    """Radio players endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.config = Config(client)
        self.thumbnail = Thumbnail(client)

    def station_list(self) -> None:
        """List players for a specific station."""
        raise NotImplementedError("Radio.players.station_list is not implemented yet.")

    def product_list(self) -> None:
        """List players for a radio product."""
        raise NotImplementedError("Radio.players.product_list is not implemented yet.")

    def create(self) -> None:
        """Create or store a player."""
        raise NotImplementedError("Radio.players.create is not implemented yet.")

    def get(self) -> None:
        """Display a player."""
        raise NotImplementedError("Radio.players.get is not implemented yet.")

    def update(self) -> None:
        """Update a player."""
        raise NotImplementedError("Radio.players.update is not implemented yet.")

    def delete(self) -> None:
        """Delete a player."""
        raise NotImplementedError("Radio.players.delete is not implemented yet.")

    def check_ip_access(self) -> None:
        """Check if an IP can access a mountpoint."""
        raise NotImplementedError("Radio.players.check_ip_access is not implemented yet.")

    def check_domain_access(self) -> None:
        """Check if a domain can access a player."""
        raise NotImplementedError("Radio.players.check_domain_access is not implemented yet.")

    def duplicate(self) -> None:
        """Duplicate an existing player."""
        raise NotImplementedError("Radio.players.duplicate is not implemented yet.")

    def reset(self) -> None:
        """Reset a player."""
        raise NotImplementedError("Radio.players.reset is not implemented yet.")


class AsyncPlayers(AsyncResource):
    """Async radio players endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.config = AsyncConfig(client)
        self.thumbnail = AsyncThumbnail(client)

    async def station_list(self) -> None:
        """List players for a specific station."""
        raise NotImplementedError("AsyncRadio.players.station_list is not implemented yet.")

    async def product_list(self) -> None:
        """List players for a radio product."""
        raise NotImplementedError("AsyncRadio.players.product_list is not implemented yet.")

    async def create(self) -> None:
        """Create or store a player."""
        raise NotImplementedError("AsyncRadio.players.create is not implemented yet.")

    async def get(self) -> None:
        """Display a player."""
        raise NotImplementedError("AsyncRadio.players.get is not implemented yet.")

    async def update(self) -> None:
        """Update a player."""
        raise NotImplementedError("AsyncRadio.players.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete a player."""
        raise NotImplementedError("AsyncRadio.players.delete is not implemented yet.")

    async def check_ip_access(self) -> None:
        """Check if an IP can access a mountpoint."""
        raise NotImplementedError("AsyncRadio.players.check_ip_access is not implemented yet.")

    async def check_domain_access(self) -> None:
        """Check if a domain can access a player."""
        raise NotImplementedError("AsyncRadio.players.check_domain_access is not implemented yet.")

    async def duplicate(self) -> None:
        """Duplicate an existing player."""
        raise NotImplementedError("AsyncRadio.players.duplicate is not implemented yet.")

    async def reset(self) -> None:
        """Reset a player."""
        raise NotImplementedError("AsyncRadio.players.reset is not implemented yet.")


__all__ = [
    "Players",
    "AsyncPlayers",
    "Config",
    "AsyncConfig",
    "Thumbnail",
    "AsyncThumbnail",
]
