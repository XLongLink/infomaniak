from __future__ import annotations

from infomaniak.utils import parse, query_params
from infomaniak.models import Action
from infomaniak.resource import Resouce, AsyncResource


class Actions(Resouce):
    """Core actions endpoints."""

    def list(self, *, search: str | None = None) -> list[Action]:
        """
        Retrieve available core actions.

        Args:
            search: Optional search string used to filter action codes.

        Returns:
            list[Action]: The list of available action types.
        """
        response = self._client.get(
            "/1/actions",
            params=query_params(search=search),
        )
        return [parse(Action, item) for item in response.json()["data"]]


class AsyncActions(AsyncResource):
    """Async core actions endpoints."""

    async def list(self, *, search: str | None = None) -> list[Action]:
        """
        Retrieve available core actions.

        Args:
            search: Optional search string used to filter action codes.

        Returns:
            list[Action]: The list of available action types.
        """
        response = await self._client.get(
            "/1/actions",
            params=query_params(search=search),
        )
        return [parse(Action, item) for item in response.json()["data"]]
