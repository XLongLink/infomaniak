from infomaniak.resource import Resouce, AsyncResource


class PlaylistsMedias(Resouce):
    """Radio AutoDJ playlists medias endpoints."""

    def list(self) -> None:
        """List media items in a playlist."""
        raise NotImplementedError("Radio.autodj.playlists.medias.list is not implemented yet.")


class AsyncPlaylistsMedias(AsyncResource):
    """Async radio AutoDJ playlists medias endpoints."""

    async def list(self) -> None:
        """List media items in a playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playlists.medias.list is not implemented yet.")


class Playlists(Resouce):
    """Radio AutoDJ playlists endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.medias = PlaylistsMedias(client)

    def list(self) -> None:
        """List playlists."""
        raise NotImplementedError("Radio.autodj.playlists.list is not implemented yet.")

    def create(self) -> None:
        """Create or store a playlist."""
        raise NotImplementedError("Radio.autodj.playlists.create is not implemented yet.")

    def get(self) -> None:
        """Display a playlist."""
        raise NotImplementedError("Radio.autodj.playlists.get is not implemented yet.")

    def update(self) -> None:
        """Update a playlist."""
        raise NotImplementedError("Radio.autodj.playlists.update is not implemented yet.")

    def delete(self) -> None:
        """Delete a playlist."""
        raise NotImplementedError("Radio.autodj.playlists.delete is not implemented yet.")

    def attach_media(self) -> None:
        """Attach media to a playlist."""
        raise NotImplementedError("Radio.autodj.playlists.attach_media is not implemented yet.")


class AsyncPlaylists(AsyncResource):
    """Async radio AutoDJ playlists endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.medias = AsyncPlaylistsMedias(client)

    async def list(self) -> None:
        """List playlists."""
        raise NotImplementedError("AsyncRadio.autodj.playlists.list is not implemented yet.")

    async def create(self) -> None:
        """Create or store a playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playlists.create is not implemented yet.")

    async def get(self) -> None:
        """Display a playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playlists.get is not implemented yet.")

    async def update(self) -> None:
        """Update a playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playlists.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete a playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playlists.delete is not implemented yet.")

    async def attach_media(self) -> None:
        """Attach media to a playlist."""
        raise NotImplementedError("AsyncRadio.autodj.playlists.attach_media is not implemented yet.")
