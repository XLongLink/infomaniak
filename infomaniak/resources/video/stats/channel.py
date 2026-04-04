from .viewers import StatsViewers, AsyncStatsViewers
from .viewing import StatsViewing, AsyncStatsViewing
from .geolocation import StatsGeolocation, AsyncStatsGeolocation
from infomaniak.resource import Resouce, AsyncResource


class ChannelStats(Resouce):
    """Per-channel video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.geolocation = StatsGeolocation(client)
        self.viewers = StatsViewers(client)
        self.viewing = StatsViewing(client)

    def consumption(self) -> None:
        raise NotImplementedError("Video.stats.channel.consumption is not implemented yet.")

    def consumption_histogram(self) -> None:
        raise NotImplementedError("Video.stats.channel.consumption_histogram is not implemented yet.")


class AsyncChannelStats(AsyncResource):
    """Async per-channel video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.geolocation = AsyncStatsGeolocation(client)
        self.viewers = AsyncStatsViewers(client)
        self.viewing = AsyncStatsViewing(client)

    async def consumption(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.channel.consumption is not implemented yet.")

    async def consumption_histogram(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.channel.consumption_histogram is not implemented yet.")
