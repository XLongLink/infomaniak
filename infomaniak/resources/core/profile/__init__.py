from .info import ProfileInfo, AsyncProfileInfo
from .email import ProfileEmail, AsyncProfileEmail
from .phone import ProfilePhone, AsyncProfilePhone
from .avatar import ProfileAvatar, AsyncProfileAvatar
from .password import ProfilePassword, AsyncProfilePassword
from infomaniak.resource import Resouce, AsyncResource


class Profile(Resouce):
    """Core profile endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.password = ProfilePassword(client)
        self.email = ProfileEmail(client)
        self.phone = ProfilePhone(client)
        self.avatar = ProfileAvatar(client)
        self.info = ProfileInfo(client)


class AsyncProfile(AsyncResource):
    """Async core profile endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.password = AsyncProfilePassword(client)
        self.email = AsyncProfileEmail(client)
        self.phone = AsyncProfilePhone(client)
        self.avatar = AsyncProfileAvatar(client)
        self.info = AsyncProfileInfo(client)
