from .team import Team, AsyncTeam
from .user import User, AsyncUser
from infomaniak.resource import Resouce, AsyncResource


class Webmail(Resouce):
    """Mailbox webmail access nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.team = Team(client)
        self.user = User(client)


class AsyncWebmail(AsyncResource):
    """Async mailbox webmail access nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.team = AsyncTeam(client)
        self.user = AsyncUser(client)


__all__ = [
    "Webmail",
    "AsyncWebmail",
    "Team",
    "AsyncTeam",
    "User",
    "AsyncUser",
]
