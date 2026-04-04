from infomaniak.resource import Resouce, AsyncResource


class Restore(Resouce):
    """Cloud database restore resources."""

    def get(self) -> None:
        """Retrieve cloud database restore operations."""
        raise NotImplementedError("Cloud database restore get endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a cloud database restore operation."""
        raise NotImplementedError("Cloud database restore create endpoint is not implemented yet.")


class AsyncRestore(AsyncResource):
    """Async cloud database restore resources."""

    async def get(self) -> None:
        """Retrieve cloud database restore operations."""
        raise NotImplementedError("Cloud database restore get endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a cloud database restore operation."""
        raise NotImplementedError("Cloud database restore create endpoint is not implemented yet.")
