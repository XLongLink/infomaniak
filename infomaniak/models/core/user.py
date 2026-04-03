from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class AccountInvitationTeam:
    """
    Team attached to an account invitation.

    OpenAPI schema: `087adaad_Team_7471c6bd`.
    """

    id: int
    name: str
    color_id: int
    created_at: int
    updated_at: int
    user_count: int | None = None

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AccountInvitationTeam":
        return cls(
            id=int(data["id"]),
            name=str(data["name"]),
            color_id=int(data["color_id"]),
            created_at=int(data["created_at"]),
            updated_at=int(data["updated_at"]),
            user_count=int(data["user_count"]) if data.get("user_count") is not None else None,
        )


@dataclass(slots=True)
class AccountInvitation:
    """
    Account invitation payload.

    OpenAPI schema: `087adaad_AccountInvitation`.
    """

    id: int
    first_name: str
    last_name: str
    email: str
    strict: bool
    status: Literal["accepted", "cancelled", "pending", "rejected"]
    role_type: Literal["admin", "normal", "owner"]
    language_id: int
    locale: str
    account_id: int
    has_ksuite: bool
    has_billing: bool
    has_billing_mailing: bool
    has_mailing: bool
    sent_at: int | None
    created_at: int
    updated_at: int
    expired_at: int | None
    url_accept: str
    teams: list[AccountInvitationTeam]
    ksuite: list[object] | None = None
    app_accesses: str | None = None
    permissions: list[object] | None = None
    service_permissions: list[object] | None = None
    qr_code: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AccountInvitation":
        return cls(
            id=int(data["id"]),
            first_name=str(data["first_name"]),
            last_name=str(data["last_name"]),
            email=str(data["email"]),
            strict=bool(data["strict"]),
            status=data["status"],  # type: ignore[assignment]
            role_type=data["role_type"],  # type: ignore[assignment]
            language_id=int(data["language_id"]),
            locale=str(data["locale"]),
            account_id=int(data["account_id"]),
            has_ksuite=bool(data["has_ksuite"]),
            has_billing=bool(data["has_billing"]),
            has_billing_mailing=bool(data["has_billing_mailing"]),
            has_mailing=bool(data["has_mailing"]),
            sent_at=int(data["sent_at"]) if data.get("sent_at") is not None else None,
            created_at=int(data["created_at"]),
            updated_at=int(data["updated_at"]),
            expired_at=int(data["expired_at"]) if data.get("expired_at") is not None else None,
            url_accept=str(data["url_accept"]),
            teams=[
                AccountInvitationTeam.from_dict(item)
                for item in data.get("teams", [])
                if isinstance(item, dict)
            ],
            ksuite=list(data["ksuite"]) if isinstance(data.get("ksuite"), list) else None,
            app_accesses=str(data["app_accesses"]) if data.get("app_accesses") is not None else None,
            permissions=list(data["permissions"]) if isinstance(data.get("permissions"), list) else None,
            service_permissions=(
                list(data["service_permissions"])
                if isinstance(data.get("service_permissions"), list)
                else None
            ),
            qr_code=str(data["qr_code"]) if data.get("qr_code") is not None else None,
        )


@dataclass(slots=True)
class AccountInvitationResponse:
    """
    Generic response for account invitation endpoints.

    OpenAPI response shape: `Response` + `data: 087adaad_AccountInvitation`.
    """

    result: Literal["success", "error", "asynchronous"]
    data: AccountInvitation

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "AccountInvitationResponse":
        payload = data.get("data")
        if not isinstance(payload, dict):
            raise ValueError("Missing or invalid 'data' field in account invitation response.")

        result = data.get("result")
        if result not in {"success", "error", "asynchronous"}:
            raise ValueError("Missing or invalid 'result' field in account invitation response.")

        return cls(
            result=result,
            data=AccountInvitation.from_dict(payload),
        )
