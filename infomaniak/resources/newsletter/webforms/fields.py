from infomaniak.resource import Resouce, AsyncResource


class WebformsFields(Resouce):
    """Newsletter webforms fields endpoints."""

    def list(self) -> None:
        """List fields of a webform."""
        raise NotImplementedError("Newsletter webforms fields list endpoint is not implemented yet.")


class AsyncWebformsFields(AsyncResource):
    """Async newsletter webforms fields endpoints."""

    async def list(self) -> None:
        """List fields of a webform."""
        raise NotImplementedError("Newsletter webforms fields list endpoint is not implemented yet.")


__all__ = ["WebformsFields", "AsyncWebformsFields"]
