from dacite import from_dict

from infomaniak.models.dns.tld import Tld
from infomaniak.resource import AsyncResource, Resouce


class TLD(Resouce):
    """DNS TLD endpoints."""

    def list(
        self,
        *,
        with_: str | None = None,
        groups: list[int] | None = None,
    ) -> list[Tld]:
        """List all available TLDs."""
        url = "/2/tld"
        params: dict[str, str | list[int]] = {}
        if with_ is not None:
            params["with"] = with_
        if groups is not None:
            params["groups"] = groups
        response = self._client.get(url, params=params or None)
        return [from_dict(Tld, item) for item in response.json()["data"]]

    def show(
        self,
        tld: str,
        *,
        with_: str | None = None,
    ) -> Tld:
        """Show one TLD."""
        url = f"/2/tld/{tld}"
        params = {"with": with_} if with_ is not None else None
        response = self._client.get(url, params=params)
        return from_dict(Tld, response.json()["data"])


class AsyncTLD(AsyncResource):
    """Async DNS TLD endpoints."""

    async def list(
        self,
        *,
        with_: str | None = None,
        groups: list[int] | None = None,
    ) -> list[Tld]:
        """List all available TLDs."""
        url = "/2/tld"
        params: dict[str, str | list[int]] = {}
        if with_ is not None:
            params["with"] = with_
        if groups is not None:
            params["groups"] = groups
        response = await self._client.get(url, params=params or None)
        return [from_dict(Tld, item) for item in response.json()["data"]]

    async def show(
        self,
        tld: str,
        *,
        with_: str | None = None,
    ) -> Tld:
        """Show one TLD."""
        url = f"/2/tld/{tld}"
        params = {"with": with_} if with_ is not None else None
        response = await self._client.get(url, params=params)
        return from_dict(Tld, response.json()["data"])
