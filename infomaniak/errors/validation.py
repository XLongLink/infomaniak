from typing import Any, Dict, Iterable, Optional, Sequence, Union

from infomaniak.errors.app import AppError


class ValidationErrorDetail:
    """ValidationError schema from OpenApi.json."""

    def __init__(self, loc: Sequence[Union[str, int]], msg: str, error_type: str) -> None:
        self.loc = tuple(loc)
        self.msg = msg
        self.type = error_type

    @classmethod
    def from_api(cls, payload: Dict[str, Any]) -> "ValidationErrorDetail":
        return cls(
            loc=payload.get("loc") or (),
            msg=payload.get("msg", ""),
            error_type=payload.get("type", ""),
        )


class ValidationError(AppError):
    """Application error carrying one or more validation details."""

    def __init__(
        self,
        message: str,
        *,
        errors: Optional[Iterable[ValidationErrorDetail]] = None,
        status_code: Optional[int] = None,
        error_id: Optional[str] = None,
        request_id: Optional[str] = None,
        payload: Optional[Any] = None,
    ) -> None:
        super().__init__(
            message,
            status_code=status_code,
            error_id=error_id,
            request_id=request_id,
            payload=payload,
        )
        self.errors = tuple(errors or ())

    @classmethod
    def from_payload(cls, status_code: int, payload: Optional[Dict[str, Any]]) -> "ValidationError":
        payload = payload or {}
        details = tuple(
            ValidationErrorDetail.from_api(item)
            for item in payload.get("detail") or payload.get("errors") or ()
            if isinstance(item, dict)
        )
        message = payload.get("message") or "Validation error"
        if details:
            message = "; ".join(detail.msg for detail in details if detail.msg) or message
        return cls(
            message,
            errors=details,
            status_code=payload.get("status_code", status_code),
            error_id=payload.get("id"),
            request_id=payload.get("request_id"),
            payload=payload,
        )
