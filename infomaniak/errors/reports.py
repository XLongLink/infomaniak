from typing import Any, Dict, Optional


class MailingListSubscriberErrorReport:
    """Mailing List Subscriber Error Report schema from OpenApi.json."""

    def __init__(
        self,
        count: int,
        last_error: Optional[int],
        last_error_code: Optional[int],
    ) -> None:
        self.count = count
        self.last_error = last_error
        self.last_error_code = last_error_code

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]) -> "MailingListSubscriberErrorReport":
        payload = payload or {}
        return cls(
            count=payload.get("count", 0),
            last_error=payload.get("last_error"),
            last_error_code=payload.get("last_error_code"),
        )
