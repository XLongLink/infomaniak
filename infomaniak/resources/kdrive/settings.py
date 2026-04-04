from infomaniak.resource import Resouce, AsyncResource


class Settings(Resouce):
    """kDrive resource for settings endpoints."""

    def display(self) -> None:
        """Get drive settings."""
        raise NotImplementedError("kDrive settings.display endpoint is not implemented yet.")

    def update(self) -> None:
        """Update drive settings."""
        raise NotImplementedError("kDrive settings.update endpoint is not implemented yet.")


class AsyncSettings(AsyncResource):
    """Async kDrive resource for settings endpoints."""

    async def display(self) -> None:
        """Get drive settings."""
        raise NotImplementedError("kDrive settings.display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update drive settings."""
        raise NotImplementedError("kDrive settings.update endpoint is not implemented yet.")
