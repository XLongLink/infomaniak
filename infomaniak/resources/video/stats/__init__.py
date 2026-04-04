from .channel import ChannelStats, AsyncChannelStats
from .globals_ import GlobalStats, AsyncGlobalStats
from infomaniak.resource import Resouce, AsyncResource


class Stats(Resouce):
    """Video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.channel = ChannelStats(client)
        self.globals = GlobalStats(client)


class AsyncStats(AsyncResource):
    """Async video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.channel = AsyncChannelStats(client)
        self.globals = AsyncGlobalStats(client)


__all__ = [
    "Stats",
    "AsyncStats",
    "ChannelStats",
    "AsyncChannelStats",
    "GlobalStats",
    "AsyncGlobalStats",
]
