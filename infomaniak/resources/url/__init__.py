from .short import Short, AsyncShort
from infomaniak.resource import Resouce, AsyncResource


class Url(Resouce):
    """URL resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.short = Short(client)


class AsyncUrl(AsyncResource):
    """Async URL resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.short = AsyncShort(client)
