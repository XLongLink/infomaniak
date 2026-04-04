from .mailboxes import Mailboxes, AsyncMailboxes
from infomaniak.resource import Resouce, AsyncResource
from .mailbox_management import MailboxManagement, AsyncMailboxManagement


class Mail(Resouce):
    """Mail resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.mailbox_management = MailboxManagement(client)
        self.mailboxes = Mailboxes(client)


class AsyncMail(AsyncResource):
    """Async mail resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.mailbox_management = AsyncMailboxManagement(client)
        self.mailboxes = AsyncMailboxes(client)
