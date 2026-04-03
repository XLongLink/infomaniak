import os
import httpx
from infomaniak import API_BASE
from infomaniak.errors import APIError, AppError, InternalServerError, NonJSONResponseError, ValidationError


def _default_headers(token, extra_headers=None):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    if extra_headers:
        headers.update(extra_headers)
    return headers


def _resolve_token(token):
    resolved = token or os.environ.get("INFOMANIAK_API_TOKEN")
    if not resolved:
        raise ValueError("No API token configured. Pass token=... or set INFOMANIAK_API_TOKEN.")
    return resolved


def _unwrap_response(response):
    if response.status_code == 204:
        return None

    try:
        payload = response.json()
    except ValueError as exc:
        raise NonJSONResponseError(
            f"Non-JSON response (HTTP {response.status_code}): {response.text[:300]}",
            status_code=response.status_code,
            payload=response.text,
        ) from exc

    if response.is_error or payload.get("result") == "error":
        if payload.get("result") == "error":
            raise APIError.from_payload(response.status_code, payload)
        if isinstance(payload.get("detail"), list) or isinstance(payload.get("errors"), list):
            raise ValidationError.from_payload(response.status_code, payload)
        if all(key in payload for key in ("status_code", "message")):
            error_cls = InternalServerError if response.status_code >= 500 else AppError
            raise error_cls.from_payload(response.status_code, payload)
        raise AppError(
            f"HTTP {response.status_code}: {response.text[:300]}",
            status_code=response.status_code,
            payload=payload,
        )

    return payload.get("data", payload)


class BaseClient:
    """Shared sync transport for all SDK resources."""

    def __init__(self, token=None, zone=None, base_url=API_BASE, timeout=30.0, transport=None, headers=None):
        self._token = _resolve_token(token)
        self._zone = zone or os.environ.get("INFOMANIAK_DNS_ZONE")
        self._client = httpx.Client(
            base_url=base_url.rstrip("/"),
            headers=_default_headers(self._token, headers),
            timeout=timeout,
            transport=transport,
        )

    def _request(self, method, path, **kwargs):
        response = self._client.request(method, path, **kwargs)
        return _unwrap_response(response)

    def _require_zone(self, zone=None):
        resolved = zone or self._zone
        if not resolved:
            raise ValueError("No DNS zone configured. Pass zone=... or set INFOMANIAK_DNS_ZONE.")
        return resolved

    def close(self):
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()


class AsyncBaseClient:
    """Shared async transport for all SDK resources."""

    def __init__(self, token=None, zone=None, base_url=API_BASE, timeout=30.0, transport=None, headers=None):
        self._token = _resolve_token(token)
        self._zone = zone or os.environ.get("INFOMANIAK_DNS_ZONE")
        self._client = httpx.AsyncClient(
            base_url=base_url.rstrip("/"),
            headers=_default_headers(self._token, headers),
            timeout=timeout,
            transport=transport,
        )

    async def _request(self, method, path, **kwargs):
        response = await self._client.request(method, path, **kwargs)
        return _unwrap_response(response)

    def _require_zone(self, zone=None):
        resolved = zone or self._zone
        if not resolved:
            raise ValueError("No DNS zone configured. Pass zone=... or set INFOMANIAK_DNS_ZONE.")
        return resolved

    async def aclose(self):
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.aclose()
