from .packs import Packs, AsyncPacks
from .stats import Stats, AsyncStats
from .autodj import Autodj, AsyncAutodj
from .options import Options, AsyncOptions
from .players import Players, AsyncPlayers
from .products import Products, AsyncProducts
from .hls_stream import HlsStream, AsyncHlsStream
from .mediapulse import Mediapulse, AsyncMediapulse
from .notifications import Notifications, AsyncNotifications
from .server_events import ServerEvents, AsyncServerEvents
from .encoder_events import EncoderEvents, AsyncEncoderEvents
from .product_options import ProductOptions, AsyncProductOptions
from infomaniak.resource import Resouce, AsyncResource


class Radio(Resouce):
    """Radio resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.autodj = Autodj(client)
        self.encoder_events = EncoderEvents(client)
        self.hls_stream = HlsStream(client)
        self.mediapulse = Mediapulse(client)
        self.notifications = Notifications(client)
        self.options = Options(client)
        self.packs = Packs(client)
        self.players = Players(client)
        self.product_options = ProductOptions(client)
        self.products = Products(client)
        self.server_events = ServerEvents(client)
        self.stats = Stats(client)


class AsyncRadio(AsyncResource):
    """Async radio resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.autodj = AsyncAutodj(client)
        self.encoder_events = AsyncEncoderEvents(client)
        self.hls_stream = AsyncHlsStream(client)
        self.mediapulse = AsyncMediapulse(client)
        self.notifications = AsyncNotifications(client)
        self.options = AsyncOptions(client)
        self.packs = AsyncPacks(client)
        self.players = AsyncPlayers(client)
        self.product_options = AsyncProductOptions(client)
        self.products = AsyncProducts(client)
        self.server_events = AsyncServerEvents(client)
        self.stats = AsyncStats(client)


__all__ = [
    "Radio",
    "AsyncRadio",
    "Autodj",
    "AsyncAutodj",
    "EncoderEvents",
    "AsyncEncoderEvents",
    "HlsStream",
    "AsyncHlsStream",
    "Mediapulse",
    "AsyncMediapulse",
    "Notifications",
    "AsyncNotifications",
    "Options",
    "AsyncOptions",
    "Packs",
    "AsyncPacks",
    "Players",
    "AsyncPlayers",
    "ProductOptions",
    "AsyncProductOptions",
    "Products",
    "AsyncProducts",
    "ServerEvents",
    "AsyncServerEvents",
    "Stats",
    "AsyncStats",
]
