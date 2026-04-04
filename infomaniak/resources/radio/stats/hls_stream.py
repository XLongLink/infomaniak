from infomaniak.resource import Resouce, AsyncResource


class HlsStream(Resouce):
    """Radio statistics for HLS stream endpoints."""

    def listeners(self) -> None:
        """Get listeners."""
        raise NotImplementedError("Radio.stats.hls_stream.listeners is not implemented yet.")

    def listeners_per_minute(self) -> None:
        """Get listeners per minute."""
        raise NotImplementedError("Radio.stats.hls_stream.listeners_per_minute is not implemented yet.")

    def countries(self) -> None:
        """Get listeners by country."""
        raise NotImplementedError("Radio.stats.hls_stream.countries is not implemented yet.")

    def countries_continent(self) -> None:
        """Get listeners by continent."""
        raise NotImplementedError("Radio.stats.hls_stream.countries_continent is not implemented yet.")

    def consumption(self) -> None:
        """Get bandwidth consumption."""
        raise NotImplementedError("Radio.stats.hls_stream.consumption is not implemented yet.")

    def total_consumption(self) -> None:
        """Get total consumption."""
        raise NotImplementedError("Radio.stats.hls_stream.total_consumption is not implemented yet.")

    def players(self) -> None:
        """Get number of players."""
        raise NotImplementedError("Radio.stats.hls_stream.players is not implemented yet.")

    def total_players(self) -> None:
        """Get total player count."""
        raise NotImplementedError("Radio.stats.hls_stream.total_players is not implemented yet.")

    def export_csv(self) -> None:
        """Export statistics as CSV."""
        raise NotImplementedError("Radio.stats.hls_stream.export_csv is not implemented yet.")


class AsyncHlsStream(AsyncResource):
    """Async radio statistics for HLS stream endpoints."""

    async def listeners(self) -> None:
        """Get listeners."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.listeners is not implemented yet.")

    async def listeners_per_minute(self) -> None:
        """Get listeners per minute."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.listeners_per_minute is not implemented yet.")

    async def countries(self) -> None:
        """Get listeners by country."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.countries is not implemented yet.")

    async def countries_continent(self) -> None:
        """Get listeners by continent."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.countries_continent is not implemented yet.")

    async def consumption(self) -> None:
        """Get bandwidth consumption."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.consumption is not implemented yet.")

    async def total_consumption(self) -> None:
        """Get total consumption."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.total_consumption is not implemented yet.")

    async def players(self) -> None:
        """Get number of players."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.players is not implemented yet.")

    async def total_players(self) -> None:
        """Get total player count."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.total_players is not implemented yet.")

    async def export_csv(self) -> None:
        """Export statistics as CSV."""
        raise NotImplementedError("AsyncRadio.stats.hls_stream.export_csv is not implemented yet.")
