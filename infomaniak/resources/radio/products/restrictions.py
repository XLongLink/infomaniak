from infomaniak.resource import AsyncResource, Resouce


class Restrictions(Resouce):
    """Radio products restrictions endpoints."""

    def set(self) -> None:
        """Apply restrictions to all streams in a product."""
        raise NotImplementedError("Radio.products.restrictions.set is not implemented yet.")


class AsyncRestrictions(AsyncResource):
    """Async radio products restrictions endpoints."""

    async def set(self) -> None:
        """Apply restrictions to all streams in a product."""
        raise NotImplementedError("AsyncRadio.products.restrictions.set is not implemented yet.")
