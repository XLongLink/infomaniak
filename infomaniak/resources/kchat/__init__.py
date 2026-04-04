from .bots import Bots, AsyncBots
from .emoji import Emoji, AsyncEmoji
from .files import Files, AsyncFiles
from .posts import Posts, AsyncPosts
from .roles import Roles, AsyncRoles
from .teams import Teams, AsyncTeams
from .users import Users, AsyncUsers
from .groups import Groups, AsyncGroups
from .status import Status, AsyncStatus
from .system import System, AsyncSystem
from .threads import Threads, AsyncThreads
from .channels import Channels, AsyncChannels
from .commands import Commands, AsyncCommands
from .insights import Insights, AsyncInsights
from .webhooks import Webhooks, AsyncWebhooks
from .reactions import Reactions, AsyncReactions
from .preferences import Preferences, AsyncPreferences
from infomaniak.resource import Resouce, AsyncResource


class Kchat(Resouce):
    """kChat resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.users = Users(client)
        self.bots = Bots(client)
        self.teams = Teams(client)
        self.channels = Channels(client)
        self.posts = Posts(client)
        self.threads = Threads(client)
        self.files = Files(client)
        self.preferences = Preferences(client)
        self.status = Status(client)
        self.emoji = Emoji(client)
        self.reactions = Reactions(client)
        self.webhooks = Webhooks(client)
        self.commands = Commands(client)
        self.system = System(client)
        self.groups = Groups(client)
        self.roles = Roles(client)
        self.insights = Insights(client)


class AsyncKchat(AsyncResource):
    """Async kChat resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.users = AsyncUsers(client)
        self.bots = AsyncBots(client)
        self.teams = AsyncTeams(client)
        self.channels = AsyncChannels(client)
        self.posts = AsyncPosts(client)
        self.threads = AsyncThreads(client)
        self.files = AsyncFiles(client)
        self.preferences = AsyncPreferences(client)
        self.status = AsyncStatus(client)
        self.emoji = AsyncEmoji(client)
        self.reactions = AsyncReactions(client)
        self.webhooks = AsyncWebhooks(client)
        self.commands = AsyncCommands(client)
        self.system = AsyncSystem(client)
        self.groups = AsyncGroups(client)
        self.roles = AsyncRoles(client)
        self.insights = AsyncInsights(client)


__all__ = [
    "Users",
    "Bots",
    "Teams",
    "Channels",
    "Posts",
    "Threads",
    "Files",
    "Preferences",
    "Status",
    "Emoji",
    "Reactions",
    "Webhooks",
    "Commands",
    "System",
    "Groups",
    "Roles",
    "Insights",
    "AsyncUsers",
    "AsyncBots",
    "AsyncTeams",
    "AsyncChannels",
    "AsyncPosts",
    "AsyncThreads",
    "AsyncFiles",
    "AsyncPreferences",
    "AsyncStatus",
    "AsyncEmoji",
    "AsyncReactions",
    "AsyncWebhooks",
    "AsyncCommands",
    "AsyncSystem",
    "AsyncGroups",
    "AsyncRoles",
    "AsyncInsights",
    "Kchat",
    "AsyncKchat",
]
