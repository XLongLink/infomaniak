from .users import Users, AsyncUsers
from .aliases import Aliases, AsyncAliases
from .filters import Filters, AsyncFilters
from .folders import Folders, AsyncFolders
from .accesses import Accesses, AsyncAccesses
from .auto_reply import AutoReply, AsyncAutoReply
from .forwarding import Forwarding, AsyncForwarding
from .signatures import Signatures, AsyncSignatures
from infomaniak.resource import Resouce, AsyncResource


class Mailboxes(Resouce):
    """Mailboxes nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.accesses = Accesses(client)
        self.aliases = Aliases(client)
        self.auto_reply = AutoReply(client)
        self.filters = Filters(client)
        self.folders = Folders(client)
        self.forwarding = Forwarding(client)
        self.signatures = Signatures(client)
        self.users = Users(client)


class AsyncMailboxes(AsyncResource):
    """Async mailboxes nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.accesses = AsyncAccesses(client)
        self.aliases = AsyncAliases(client)
        self.auto_reply = AsyncAutoReply(client)
        self.filters = AsyncFilters(client)
        self.folders = AsyncFolders(client)
        self.forwarding = AsyncForwarding(client)
        self.signatures = AsyncSignatures(client)
        self.users = AsyncUsers(client)
