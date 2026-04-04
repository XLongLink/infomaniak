from infomaniak.resource import Resouce, AsyncResource


class Session(Resouce):
    """kDrive resource for chunked upload session endpoints."""

    def start(self) -> None:
        """Start an upload session."""
        raise NotImplementedError("kDrive files.upload.session.start endpoint is not implemented yet.")

    def batch_start(self) -> None:
        """Start multiple upload sessions in batch."""
        raise NotImplementedError("kDrive files.upload.session.batch_start endpoint is not implemented yet.")

    def append_chunk(self) -> None:
        """Append a chunk to an upload session."""
        raise NotImplementedError("kDrive files.upload.session.append_chunk endpoint is not implemented yet.")

    def finish(self) -> None:
        """Finish an upload session."""
        raise NotImplementedError("kDrive files.upload.session.finish endpoint is not implemented yet.")

    def batch_finish(self) -> None:
        """Finish multiple upload sessions in batch."""
        raise NotImplementedError("kDrive files.upload.session.batch_finish endpoint is not implemented yet.")

    def cancel(self) -> None:
        """Cancel an upload session."""
        raise NotImplementedError("kDrive files.upload.session.cancel endpoint is not implemented yet.")

    def batch_cancel(self) -> None:
        """Cancel multiple upload sessions in batch."""
        raise NotImplementedError("kDrive files.upload.session.batch_cancel endpoint is not implemented yet.")


class AsyncSession(AsyncResource):
    """Async kDrive resource for chunked upload session endpoints."""

    async def start(self) -> None:
        """Start an upload session."""
        raise NotImplementedError("kDrive files.upload.session.start endpoint is not implemented yet.")

    async def batch_start(self) -> None:
        """Start multiple upload sessions in batch."""
        raise NotImplementedError("kDrive files.upload.session.batch_start endpoint is not implemented yet.")

    async def append_chunk(self) -> None:
        """Append a chunk to an upload session."""
        raise NotImplementedError("kDrive files.upload.session.append_chunk endpoint is not implemented yet.")

    async def finish(self) -> None:
        """Finish an upload session."""
        raise NotImplementedError("kDrive files.upload.session.finish endpoint is not implemented yet.")

    async def batch_finish(self) -> None:
        """Finish multiple upload sessions in batch."""
        raise NotImplementedError("kDrive files.upload.session.batch_finish endpoint is not implemented yet.")

    async def cancel(self) -> None:
        """Cancel an upload session."""
        raise NotImplementedError("kDrive files.upload.session.cancel endpoint is not implemented yet.")

    async def batch_cancel(self) -> None:
        """Cancel multiple upload sessions in batch."""
        raise NotImplementedError("kDrive files.upload.session.batch_cancel endpoint is not implemented yet.")
