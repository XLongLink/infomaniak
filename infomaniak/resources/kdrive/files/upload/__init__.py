from .session import Session, AsyncSession
from infomaniak.resource import Resouce, AsyncResource


class Upload(Resouce):
    """kDrive resource for file upload endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.session = Session(client)

    def upload(self) -> None:
        """Upload a file directly."""
        raise NotImplementedError("kDrive files.upload.upload endpoint is not implemented yet.")

    def cancel_by_path(self) -> None:
        """Cancel an upload by path."""
        raise NotImplementedError("kDrive files.upload.cancel_by_path endpoint is not implemented yet.")


class AsyncUpload(AsyncResource):
    """Async kDrive resource for file upload endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.session = AsyncSession(client)

    async def upload(self) -> None:
        """Upload a file directly."""
        raise NotImplementedError("kDrive files.upload.upload endpoint is not implemented yet.")

    async def cancel_by_path(self) -> None:
        """Cancel an upload by path."""
        raise NotImplementedError("kDrive files.upload.cancel_by_path endpoint is not implemented yet.")
