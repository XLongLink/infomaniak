from infomaniak.resource import AsyncResource, Resouce


class HlsStream(Resouce):
    """Radio HLS stream endpoints."""

    def get(self) -> None:
        """Get HLS stream configuration."""
        raise NotImplementedError("Radio.hls_stream.get is not implemented yet.")

    def update(self) -> None:
        """Update HLS stream configuration."""
        raise NotImplementedError("Radio.hls_stream.update is not implemented yet.")

    def delete(self) -> None:
        """Delete an HLS stream."""
        raise NotImplementedError("Radio.hls_stream.delete is not implemented yet.")

    def add(self) -> None:
        """Add a new HLS stream."""
        raise NotImplementedError("Radio.hls_stream.add is not implemented yet.")


class AsyncHlsStream(AsyncResource):
    """Async radio HLS stream endpoints."""

    async def get(self) -> None:
        """Get HLS stream configuration."""
        raise NotImplementedError("AsyncRadio.hls_stream.get is not implemented yet.")

    async def update(self) -> None:
        """Update HLS stream configuration."""
        raise NotImplementedError("AsyncRadio.hls_stream.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete an HLS stream."""
        raise NotImplementedError("AsyncRadio.hls_stream.delete is not implemented yet.")

    async def add(self) -> None:
        """Add a new HLS stream."""
        raise NotImplementedError("AsyncRadio.hls_stream.add is not implemented yet.")
