from dacite import from_dict

from infomaniak.models.dns.tld import Tld
from infomaniak.resource import AsyncResource, Resouce


def _build_with_values(
    *,
    length: bool,
    periods: bool,
    group: bool,
    transfer_method: bool,
    is_idn: bool,
    support: bool,
    time: bool,
) -> str | None:
    with_values: list[str] = []
    if length:
        with_values.append("length")
    if periods:
        with_values.append("periods")
    if group:
        with_values.append("groups")
    if transfer_method:
        with_values.append("transfer_method")
    if is_idn:
        with_values.append("is_idn")
    if support:
        with_values.append("support")
    if time:
        with_values.append("time")

    return ",".join(with_values) if with_values else None


class TLD(Resouce):
    """DNS TLD endpoints."""

    def list(
        self,
        *,
        length: bool = False,
        periods: bool = False,
        group: bool = False,
        transfer_method: bool = False,
        is_idn: bool = False,
        support: bool = False,
        time: bool = False,
        groups: list[int] | None = None,
    ) -> list[Tld]:
        """List all available TLDs."""
        url = "/2/tld"
        params: dict[str, str | list[int]] = {}
        with_values = _build_with_values(
            length=length,
            periods=periods,
            group=group,
            transfer_method=transfer_method,
            is_idn=is_idn,
            support=support,
            time=time,
        )
        if with_values is not None:
            params["with"] = with_values
        if groups is not None:
            params["groups"] = groups
        response = self._client.get(url, params=params or None)
        return [from_dict(Tld, item) for item in response.json()["data"]]

    def show(
        self,
        tld: str,
        *,
        length: bool = False,
        periods: bool = False,
        group: bool = False,
        transfer_method: bool = False,
        is_idn: bool = False,
        support: bool = False,
        time: bool = False,
    ) -> Tld:
        """Show one TLD."""
        url = f"/2/tld/{tld}"
        with_values = _build_with_values(
            length=length,
            periods=periods,
            group=group,
            transfer_method=transfer_method,
            is_idn=is_idn,
            support=support,
            time=time,
        )
        params = {"with": with_values} if with_values is not None else None
        response = self._client.get(url, params=params)
        return from_dict(Tld, response.json()["data"])


class AsyncTLD(AsyncResource):
    """Async DNS TLD endpoints."""

    async def list(
        self,
        *,
        length: bool = False,
        periods: bool = False,
        group: bool = False,
        transfer_method: bool = False,
        is_idn: bool = False,
        support: bool = False,
        time: bool = False,
        groups: list[int] | None = None,
    ) -> list[Tld]:
        """List all available TLDs."""
        url = "/2/tld"
        params: dict[str, str | list[int]] = {}
        with_values = _build_with_values(
            length=length,
            periods=periods,
            group=group,
            transfer_method=transfer_method,
            is_idn=is_idn,
            support=support,
            time=time,
        )
        if with_values is not None:
            params["with"] = with_values
        if groups is not None:
            params["groups"] = groups
        response = await self._client.get(url, params=params or None)
        return [from_dict(Tld, item) for item in response.json()["data"]]

    async def show(
        self,
        tld: str,
        *,
        length: bool = False,
        periods: bool = False,
        group: bool = False,
        transfer_method: bool = False,
        is_idn: bool = False,
        support: bool = False,
        time: bool = False,
    ) -> Tld:
        """Show one TLD."""
        url = f"/2/tld/{tld}"
        with_values = _build_with_values(
            length=length,
            periods=periods,
            group=group,
            transfer_method=transfer_method,
            is_idn=is_idn,
            support=support,
            time=time,
        )
        params = {"with": with_values} if with_values is not None else None
        response = await self._client.get(url, params=params)
        return from_dict(Tld, response.json()["data"])
