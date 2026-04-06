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
            raise ValueError("No API token configured. Pass token=... or set INFOMANIAK_API_TOKEN.")

        self._base_url: str = base_url.rstrip("/")
        self._headers: dict[str, str] = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        }

        if headers:
            self._headers.update(headers)

        self._timeout: float = timeout
        self._transport: httpx.BaseTransport | httpx.AsyncBaseTransport | None = transport

    def _raise_for_api_error(self, response: httpx.Response) -> None:
        """
        Raise an exception when the API payload indicates an error.

        Args:
            response: The HTTP response returned by the API.

        Returns:
            None: This method returns nothing when no API error is detected.
        """
        try:
            payload = response.json()
        except ValueError:
            return

        if not isinstance(payload, dict):
            return

        if payload.get("result") != "error":
            return

        error_payload = payload.get("error", {})
        if isinstance(error_payload, dict):
            message = error_payload.get("description")
        else:
            message = None

        if not isinstance(message, str) or not message:
            message = "API request failed."

        raise ValueError(message)
