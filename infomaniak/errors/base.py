from typing import Any, Dict, Iterable, Optional


class InfomaniakError(RuntimeError):
    """Base exception for package-level Infomaniak errors."""

    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        payload: Optional[Any] = None,
        request_id: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.payload = payload
        self.request_id = request_id


class NonJSONResponseError(InfomaniakError):
    """Raised when the API returns a non-JSON response."""


class ErrorDetail:
    """Legacy API error object described inline in OpenAPI responses."""

    def __init__(
        self,
        code: Optional[Any] = None,
        description: str = "",
        errors: Optional[Iterable[Any]] = None,
    ) -> None:
        self.code = code
        self.description = description
        self.errors = tuple(errors or ())

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]) -> "ErrorDetail":
        payload = payload or {}
        return cls(
            code=payload.get("code"),
            description=payload.get("description", ""),
            errors=payload.get("errors") or (),
        )

    def __str__(self) -> str:
        if self.code is None:
            return self.description
        return f"[{self.code}] {self.description}"


class APIError(InfomaniakError):
    """Legacy API error for envelopes shaped like {'result': 'error', 'error': {...}}."""

    def __init__(
        self,
        *,
        status_code: Optional[int] = None,
        detail: Optional[ErrorDetail] = None,
        payload: Optional[Any] = None,
    ) -> None:
        self.detail = detail or ErrorDetail()
        code = self.detail.code if self.detail.code is not None else status_code
        description = self.detail.description or "Unknown API error"
        super().__init__(
            f"API error [{code}]: {description}",
            status_code=status_code,
            payload=payload,
        )

    @classmethod
    def from_payload(cls, status_code: int, payload: Optional[Dict[str, Any]]) -> "APIError":
        payload = payload or {}
        return cls(
            status_code=status_code,
            detail=ErrorDetail.from_api(payload.get("error")),
            payload=payload,
        )
