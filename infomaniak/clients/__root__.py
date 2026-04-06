import os
import httpx
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

        error_payload = payload.get("error")
        message: str = "API request failed."

        if isinstance(error_payload, dict):
            base_description = error_payload.get("description")
            details = error_payload.get("errors")

            if isinstance(base_description, str) and base_description.strip():
                message = base_description.strip()

            if isinstance(details, list):
                detail_messages: list[str] = []
                for item in details:
                    if not isinstance(item, dict):
                        continue

                    detail_description = item.get("description")
                    context = item.get("context")

                    if isinstance(detail_description, str) and detail_description.strip():
                        if isinstance(context, dict):
                            attribute = context.get("attribute")
                            if isinstance(attribute, str) and attribute.strip():
                                detail_messages.append(f"{detail_description} (attribute: {attribute})")
                            else:
                                detail_messages.append(detail_description)
                        else:
                            detail_messages.append(detail_description)

                if detail_messages:
                    message = f"{message}: {'; '.join(detail_messages)}"

        raise ValueError(message)
