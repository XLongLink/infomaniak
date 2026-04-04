from infomaniak.resource import AsyncResource, Resouce


class Users(Resouce):
    """kDrive resource for drive users endpoints."""

    def list(self) -> None:
        """List users of a drive."""
        raise NotImplementedError("kDrive drive.users.list endpoint is not implemented yet.")


class AsyncUsers(AsyncResource):
    """Async kDrive resource for drive users endpoints."""

    async def list(self) -> None:
        """List users of a drive."""
        raise NotImplementedError("kDrive drive.users.list endpoint is not implemented yet.")
