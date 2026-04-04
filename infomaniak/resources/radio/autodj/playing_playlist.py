from infomaniak.resource import Resouce, AsyncResource


class PlayingPlaylistMedias(Resouce):
    """Radio AutoDJ playing playlist medias endpoints."""

    def get(self) -> None:
        """Get media entries in the playing playlist."""
        raise NotImplementedError("Radio.autodj.playing_playlist.medias.get is not implemented yet.")

    def insert(self) -> None:
        """Insert a media after the current item."""
        raise NotImplementedError("Radio.autodj.playing_playlist.medias.insert is not implemented yet.")

    def move(self) -> None:
        """Move a media item within the playing playlist."""
        raise NotImplementedError("Radio.autodj.playing_playlist.medias.move is not implemented yet.")

    def remove(self) -> None:
        """Remove a media item from the playing playlist."""
        raise NotImplementedError("Radio.autodj.playing_playlist.medias.remove is not implemented yet.")


class AsyncPlayingPlaylistMedias(AsyncResource):
    """Async radio AutoDJ playing playlist medias endpoints."""

    async def get(self) -> None:
        """Get media entries in the playing playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playing_playlist.medias.get is not implemented yet.")

    async def insert(self) -> None:
        """Insert a media after the current item."""
        raise NotImplementedError("AsyncRadio.autodj.playing_playlist.medias.insert is not implemented yet.")

    async def move(self) -> None:
        """Move a media item within the playing playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playing_playlist.medias.move is not implemented yet.")

    async def remove(self) -> None:
        """Remove a media item from the playing playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playing_playlist.medias.remove is not implemented yet.")


class PlayingPlaylist(Resouce):
    """Radio AutoDJ playing playlist endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.medias = PlayingPlaylistMedias(client)

    def get(self) -> None:
        """Get the current playing playlist."""
        raise NotImplementedError("Radio.autodj.playing_playlist.get is not implemented yet.")

    def generate(self) -> None:
        """Generate a playing playlist."""
        raise NotImplementedError("Radio.autodj.playing_playlist.generate is not implemented yet.")


class AsyncPlayingPlaylist(AsyncResource):
    """Async radio AutoDJ playing playlist endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.medias = AsyncPlayingPlaylistMedias(client)

    async def get(self) -> None:
        """Get the current playing playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playing_playlist.get is not implemented yet.")

    async def generate(self) -> None:
        """Generate a playing playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playing_playlist.generate is not implemented yet.")
