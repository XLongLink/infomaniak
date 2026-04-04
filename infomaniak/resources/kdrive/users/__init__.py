from .roles import Roles, AsyncRoles
from infomaniak.resource import Resouce, AsyncResource


class Users(Resouce):
    """kDrive resource for users endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.roles = Roles(client)

    def invite(self) -> None:
        """Invite a user to kDrive."""
        raise NotImplementedError("kDrive users.invite endpoint is not implemented yet.")

    def remove(self) -> None:
        """Remove a user from kDrive."""
        raise NotImplementedError("kDrive users.remove endpoint is not implemented yet.")


class AsyncUsers(AsyncResource):
    """Async kDrive resource for users endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.roles = AsyncRoles(client)

    async def invite(self) -> None:
        """Invite a user to kDrive."""
        raise NotImplementedError("kDrive users.invite endpoint is not implemented yet.")

    async def remove(self) -> None:
        """Remove a user from kDrive."""
        raise NotImplementedError("kDrive users.remove endpoint is not implemented yet.")


__all__ = ["Roles", "AsyncRoles", "Users", "AsyncUsers"]
