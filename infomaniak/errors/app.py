from typing import Any, Dict, Optional

from infomaniak.errors.base import InfomaniakError


class AppError(InfomaniakError):
    """Error schema used by some /api/v4 endpoints in OpenApi.json."""

    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        error_id: Optional[str] = None,
        request_id: Optional[str] = None,
        payload: Optional[Any] = None,
    ) -> None:
        super().__init__(
            message,
            status_code=status_code,
            payload=payload,
            request_id=request_id,
        )
        self.error_id = error_id

    @classmethod
    def from_payload(cls, status_code: int, payload: Optional[Dict[str, Any]]) -> "AppError":
        payload = payload or {}
        return cls(
            payload.get("message") or f"HTTP {status_code} application error",
            status_code=payload.get("status_code", status_code),
            error_id=payload.get("id"),
            request_id=payload.get("request_id"),
            payload=payload,
        )


class InternalServerError(AppError):
    """Named 500 error response from OpenApi.json."""

