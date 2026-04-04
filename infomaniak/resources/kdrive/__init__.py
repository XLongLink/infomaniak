from infomaniak.resource import AsyncResource, Resouce

from .drive import AsyncDrive, Drive
from .files import AsyncFiles, Files
from .invitations import AsyncInvitations, Invitations
from .settings import AsyncSettings, Settings
from .statistics import AsyncStatistics, Statistics
from .users import AsyncUsers, Users


class Kdrive(Resouce):
    """kDrive resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.drive = Drive(client)
        self.files = Files(client)
        self.invitations = Invitations(client)
        self.settings = Settings(client)
        self.statistics = Statistics(client)
        self.users = Users(client)


class AsyncKdrive(AsyncResource):
    """Async kDrive resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.drive = AsyncDrive(client)
        self.files = AsyncFiles(client)
        self.invitations = AsyncInvitations(client)
        self.settings = AsyncSettings(client)
        self.statistics = AsyncStatistics(client)
        self.users = AsyncUsers(client)


__all__ = [
    "Drive",
    "Files",
    "Invitations",
    "Settings",
    "Statistics",
    "Users",
    "AsyncDrive",
    "AsyncFiles",
    "AsyncInvitations",
    "AsyncSettings",
    "AsyncStatistics",
    "AsyncUsers",
    "Kdrive",
    "AsyncKdrive",
]
