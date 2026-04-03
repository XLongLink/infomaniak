from infomaniak.resource import AsyncResource, Resouce

from .autodj import AsyncAutodj, Autodj
from .encoder_events import AsyncEncoderEvents, EncoderEvents
from .hls_stream import AsyncHlsStream, HlsStream
from .mediapulse import AsyncMediapulse, Mediapulse
from .notifications import AsyncNotifications, Notifications
from .options import AsyncOptions, Options
from .packs import AsyncPacks, Packs
from .players import AsyncPlayers, Players
from .product_options import AsyncProductOptions, ProductOptions
from .products import AsyncProducts, Products
from .server_events import AsyncServerEvents, ServerEvents
from .stats import AsyncStats, Stats


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
