from .product import Product, AsyncProduct
from .hls_stream import HlsStream, AsyncHlsStream
from infomaniak.resource import Resouce, AsyncResource


class Stats(Resouce):
    """Radio statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.hls_stream = HlsStream(client)
        self.product = Product(client)


class AsyncStats(AsyncResource):
    """Async radio statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.hls_stream = AsyncHlsStream(client)
        self.product = AsyncProduct(client)


__all__ = [
    "Stats",
    "AsyncStats",
    "HlsStream",
    "AsyncHlsStream",
    "Product",
    "AsyncProduct",
]
