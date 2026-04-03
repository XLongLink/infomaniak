import os
import httpx
from typing import Any
from infomaniak.constants import API


class RootClient:
    def __init__(
        self,
        token: str | None = None,
        base_url: str = API,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | httpx.AsyncBaseTransport | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self._token: str = token or os.environ.get("INFOMANIAK_API_TOKEN", "")
        if not self._token:
            raise ValueError(
                "No API token configured. Pass token=... or set INFOMANIAK_API_TOKEN."
            )

        self._base_url: str = base_url.rstrip("/")
        self._headers: dict[str, str] = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }

        if headers:
            self._headers.update(headers)

        self._timeout: float = timeout
        self._transport: httpx.BaseTransport | httpx.AsyncBaseTransport | None = transport


class BaseClient(RootClient):
    """Shared sync transport for all SDK resources."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str = API,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(token, base_url, timeout, transport, headers)

        self._client: httpx.Client = httpx.Client(
            base_url=self._base_url,
            headers=self._headers,
            timeout=self._timeout,
            transport=transport,
        )

    def _request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> httpx.Response:
        return self._client.request(method, path, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "BaseClient":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: Any,
    ) -> None:
        self.close()


class AsyncBaseClient(RootClient):
    """Shared async transport for all SDK resources."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str = API,
        timeout: float = 30.0,
        transport: httpx.AsyncBaseTransport | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(token, base_url, timeout, transport, headers)

        self._client: httpx.AsyncClient = httpx.AsyncClient(
            base_url=self._base_url,
            headers=self._headers,
            timeout=self._timeout,
            transport=transport,
        )

    async def _request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> httpx.Response:
        return await self._client.request(method, path, **kwargs)

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncBaseClient":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: Any,
    ) -> None:
        await self.aclose()