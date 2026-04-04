from infomaniak.resource import Resouce, AsyncResource


class ConflictRestrictions(Resouce):
    """Radio products conflict restrictions endpoints."""

    def list(self) -> None:
        """List streams in conflict when updating restrictions."""
        raise NotImplementedError("Radio.products.conflict_restrictions.list is not implemented yet.")


class AsyncConflictRestrictions(AsyncResource):
    """Async radio products conflict restrictions endpoints."""

    async def list(self) -> None:
        """List streams in conflict when updating restrictions."""
        raise NotImplementedError("AsyncRadio.products.conflict_restrictions.list is not implemented yet.")
