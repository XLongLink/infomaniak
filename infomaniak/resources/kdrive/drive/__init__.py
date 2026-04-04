from .users import Users, AsyncUsers
from infomaniak.resource import Resouce, AsyncResource


class Drive(Resouce):
    """kDrive resource for drive endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.users = Users(client)

    def list(self) -> None:
        """List accessible drives."""
        raise NotImplementedError("kDrive drive.list endpoint is not implemented yet.")

    def display(self) -> None:
        """Get drive information."""
        raise NotImplementedError("kDrive drive.display endpoint is not implemented yet.")

    def update(self) -> None:
        """Update drive details."""
        raise NotImplementedError("kDrive drive.update endpoint is not implemented yet.")

    def wake(self) -> None:
        """Wake a sleeping drive."""
        raise NotImplementedError("kDrive drive.wake endpoint is not implemented yet.")


class AsyncDrive(AsyncResource):
    """Async kDrive resource for drive endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.users = AsyncUsers(client)

    async def list(self) -> None:
        """List accessible drives."""
        raise NotImplementedError("kDrive drive.list endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get drive information."""
        raise NotImplementedError("kDrive drive.display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update drive details."""
        raise NotImplementedError("kDrive drive.update endpoint is not implemented yet.")

    async def wake(self) -> None:
        """Wake a sleeping drive."""
        raise NotImplementedError("kDrive drive.wake endpoint is not implemented yet.")


__all__ = ["Users", "AsyncUsers", "Drive", "AsyncDrive"]
