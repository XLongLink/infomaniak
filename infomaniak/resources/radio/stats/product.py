from infomaniak.resource import AsyncResource, Resouce


class Product(Resouce):
    """Radio statistics for product endpoints."""

    def listeners(self) -> None:
        """Get listeners."""
        raise NotImplementedError("Radio.stats.product.listeners is not implemented yet.")

    def listeners_per_minute(self) -> None:
        """Get listeners per minute."""
        raise NotImplementedError("Radio.stats.product.listeners_per_minute is not implemented yet.")

    def listeners_per_minute_grouped(self) -> None:
        """Get listeners per minute grouped by station."""
        raise NotImplementedError("Radio.stats.product.listeners_per_minute_grouped is not implemented yet.")

    def countries(self) -> None:
        """Get listeners by country."""
        raise NotImplementedError("Radio.stats.product.countries is not implemented yet.")

    def countries_continent(self) -> None:
        """Get listeners by continent."""
        raise NotImplementedError("Radio.stats.product.countries_continent is not implemented yet.")

    def station_listeners(self) -> None:
        """Get listeners by station."""
        raise NotImplementedError("Radio.stats.product.station_listeners is not implemented yet.")

    def consumption(self) -> None:
        """Get bandwidth consumption."""
        raise NotImplementedError("Radio.stats.product.consumption is not implemented yet.")

    def total_consumption(self) -> None:
        """Get total consumption."""
        raise NotImplementedError("Radio.stats.product.total_consumption is not implemented yet.")

    def station_consumption(self) -> None:
        """Get consumption by station."""
        raise NotImplementedError("Radio.stats.product.station_consumption is not implemented yet.")

    def players(self) -> None:
        """Get number of players."""
        raise NotImplementedError("Radio.stats.product.players is not implemented yet.")

    def total_players(self) -> None:
        """Get total players."""
        raise NotImplementedError("Radio.stats.product.total_players is not implemented yet.")

    def stats_by_station(self) -> None:
        """Get aggregated stats by station."""
        raise NotImplementedError("Radio.stats.product.stats_by_station is not implemented yet.")

    def export_csv(self) -> None:
        """Export statistics as CSV."""
        raise NotImplementedError("Radio.stats.product.export_csv is not implemented yet.")

    def export_csv_by_station(self) -> None:
        """Export station-level statistics as CSV."""
        raise NotImplementedError("Radio.stats.product.export_csv_by_station is not implemented yet.")


class AsyncProduct(AsyncResource):
    """Async radio statistics for product endpoints."""

    async def listeners(self) -> None:
        """Get listeners."""
        raise NotImplementedError("AsyncRadio.stats.product.listeners is not implemented yet.")

    async def listeners_per_minute(self) -> None:
        """Get listeners per minute."""
        raise NotImplementedError("AsyncRadio.stats.product.listeners_per_minute is not implemented yet.")

    async def listeners_per_minute_grouped(self) -> None:
        """Get listeners per minute grouped by station."""
        raise NotImplementedError("AsyncRadio.stats.product.listeners_per_minute_grouped is not implemented yet.")

    async def countries(self) -> None:
        """Get listeners by country."""
        raise NotImplementedError("AsyncRadio.stats.product.countries is not implemented yet.")

    async def countries_continent(self) -> None:
        """Get listeners by continent."""
        raise NotImplementedError("AsyncRadio.stats.product.countries_continent is not implemented yet.")

    async def station_listeners(self) -> None:
        """Get listeners by station."""
        raise NotImplementedError("AsyncRadio.stats.product.station_listeners is not implemented yet.")

    async def consumption(self) -> None:
        """Get bandwidth consumption."""
        raise NotImplementedError("AsyncRadio.stats.product.consumption is not implemented yet.")

    async def total_consumption(self) -> None:
        """Get total consumption."""
        raise NotImplementedError("AsyncRadio.stats.product.total_consumption is not implemented yet.")

    async def station_consumption(self) -> None:
        """Get consumption by station."""
        raise NotImplementedError("AsyncRadio.stats.product.station_consumption is not implemented yet.")

    async def players(self) -> None:
        """Get number of players."""
        raise NotImplementedError("AsyncRadio.stats.product.players is not implemented yet.")

    async def total_players(self) -> None:
        """Get total players."""
        raise NotImplementedError("AsyncRadio.stats.product.total_players is not implemented yet.")

    async def stats_by_station(self) -> None:
        """Get aggregated stats by station."""
        raise NotImplementedError("AsyncRadio.stats.product.stats_by_station is not implemented yet.")

    async def export_csv(self) -> None:
        """Export statistics as CSV."""
        raise NotImplementedError("AsyncRadio.stats.product.export_csv is not implemented yet.")

    async def export_csv_by_station(self) -> None:
        """Export station-level statistics as CSV."""
        raise NotImplementedError("AsyncRadio.stats.product.export_csv_by_station is not implemented yet.")
