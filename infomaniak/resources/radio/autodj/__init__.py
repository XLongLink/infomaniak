from .media import Media, AsyncMedia
from .events import Events, AsyncEvents
from .playlists import Playlists, AsyncPlaylists
from .playing_playlist import PlayingPlaylist, AsyncPlayingPlaylist
from infomaniak.resource import Resouce, AsyncResource


class Autodj(Resouce):
    """Radio AutoDJ endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.events = Events(client)
        self.media = Media(client)
        self.playing_playlist = PlayingPlaylist(client)
        self.playlists = Playlists(client)

    def get(self) -> None:
        """Fetch AutoDJ settings."""
        raise NotImplementedError("Radio.autodj.get is not implemented yet.")

    def update(self) -> None:
        """Update AutoDJ settings."""
        raise NotImplementedError("Radio.autodj.update is not implemented yet.")

    def create(self) -> None:
        """Create or store AutoDJ settings."""
        raise NotImplementedError("Radio.autodj.create is not implemented yet.")

    def restart(self) -> None:
        """Restart AutoDJ."""
        raise NotImplementedError("Radio.autodj.restart is not implemented yet.")


class AsyncAutodj(AsyncResource):
    """Async radio AutoDJ endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.events = AsyncEvents(client)
        self.media = AsyncMedia(client)
        self.playing_playlist = AsyncPlayingPlaylist(client)
        self.playlists = AsyncPlaylists(client)

    async def get(self) -> None:
        """Fetch AutoDJ settings."""
        raise NotImplementedError("AsyncRadio.autodj.get is not implemented yet.")

    async def update(self) -> None:
        """Update AutoDJ settings."""
        raise NotImplementedError("AsyncRadio.autodj.update is not implemented yet.")

    async def create(self) -> None:
        """Create or store AutoDJ settings."""
        raise NotImplementedError("AsyncRadio.autodj.create is not implemented yet.")

    async def restart(self) -> None:
        """Restart AutoDJ."""
        raise NotImplementedError("AsyncRadio.autodj.restart is not implemented yet.")
