from .users import Users, AsyncUsers
from .restrictions import Restrictions, AsyncRestrictions
from infomaniak.resource import Resouce, AsyncResource
from .conflict_restrictions import (ConflictRestrictions,
                                    AsyncConflictRestrictions)


class Products(Resouce):
    """Radio products endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.users = Users(client)
        self.conflict_restrictions = ConflictRestrictions(client)
        self.restrictions = Restrictions(client)

    def list(self) -> None:
        """List radio products."""
        raise NotImplementedError("Radio.products.list is not implemented yet.")

    def get(self) -> None:
        """Display a specific radio product."""
        raise NotImplementedError("Radio.products.get is not implemented yet.")

    def update(self) -> None:
        """Update a radio product."""
        raise NotImplementedError("Radio.products.update is not implemented yet.")


class AsyncProducts(AsyncResource):
    """Async radio products endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.users = AsyncUsers(client)
        self.conflict_restrictions = AsyncConflictRestrictions(client)
        self.restrictions = AsyncRestrictions(client)

    async def list(self) -> None:
        """List radio products."""
        raise NotImplementedError("AsyncRadio.products.list is not implemented yet.")

    async def get(self) -> None:
        """Display a specific radio product."""
        raise NotImplementedError("AsyncRadio.products.get is not implemented yet.")

    async def update(self) -> None:
        """Update a radio product."""
        raise NotImplementedError("AsyncRadio.products.update is not implemented yet.")


__all__ = [
    "Products",
    "AsyncProducts",
    "Users",
    "AsyncUsers",
    "ConflictRestrictions",
    "AsyncConflictRestrictions",
    "Restrictions",
    "AsyncRestrictions",
]
