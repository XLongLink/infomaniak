from infomaniak.resource import Resouce, AsyncResource

# Import local resources
from .user import User, AsyncUser


class Core(Resouce):
    """Core resources for Infomaniak services."""

    def __init__(self, client):
        super().__init__(client)
        self.user = User(client)


class AsyncCore(AsyncResource):
    """Async core resources for Infomaniak services."""

    def __init__(self, client):
        super().__init__(client)
        self.user = AsyncUser(client)
