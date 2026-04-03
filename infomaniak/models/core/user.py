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
