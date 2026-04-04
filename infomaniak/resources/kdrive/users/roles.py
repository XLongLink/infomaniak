from infomaniak.resource import Resouce, AsyncResource


class Roles(Resouce):
    """kDrive resource for user roles endpoints."""

    def update(self) -> None:
        """Change user roles and permissions."""
        raise NotImplementedError("kDrive users.roles.update endpoint is not implemented yet.")


class AsyncRoles(AsyncResource):
    """Async kDrive resource for user roles endpoints."""

    async def update(self) -> None:
        """Change user roles and permissions."""
        raise NotImplementedError("kDrive users.roles.update endpoint is not implemented yet.")
