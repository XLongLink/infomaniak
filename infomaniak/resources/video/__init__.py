from .live import Live, AsyncLive
from .event import Event, AsyncEvent
from .order import Order, AsyncOrder
from .stats import Stats, AsyncStats
from .prices import Prices, AsyncPrices
from .stream import Stream, AsyncStream
from .channel import Channel, AsyncChannel
from .options import Options, AsyncOptions
from .players import Players, AsyncPlayers
from .countries import Countries, AsyncCountries
from .thumbnail import Thumbnail, AsyncThumbnail
from .timezones import Timezones, AsyncTimezones
from .integrations import Integrations, AsyncIntegrations
from .restrictions import Restrictions, AsyncRestrictions
from infomaniak.resource import Resouce, AsyncResource


class Video(Resouce):
    """Video resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.channel = Channel(client)
        self.countries = Countries(client)
        self.event = Event(client)
        self.integrations = Integrations(client)
        self.live = Live(client)
        self.options = Options(client)
        self.order = Order(client)
        self.players = Players(client)
        self.prices = Prices(client)
        self.restrictions = Restrictions(client)
        self.stats = Stats(client)
        self.stream = Stream(client)
        self.thumbnail = Thumbnail(client)
        self.timezones = Timezones(client)


class AsyncVideo(AsyncResource):
    """Async video resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.channel = AsyncChannel(client)
        self.countries = AsyncCountries(client)
        self.event = AsyncEvent(client)
        self.integrations = AsyncIntegrations(client)
        self.live = AsyncLive(client)
        self.options = AsyncOptions(client)
        self.order = AsyncOrder(client)
        self.players = AsyncPlayers(client)
        self.prices = AsyncPrices(client)
        self.restrictions = AsyncRestrictions(client)
        self.stats = AsyncStats(client)
        self.stream = AsyncStream(client)
        self.thumbnail = AsyncThumbnail(client)
        self.timezones = AsyncTimezones(client)
