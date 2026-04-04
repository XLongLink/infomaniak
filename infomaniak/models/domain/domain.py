from __future__ import annotations

from typing import Literal
from dataclasses import dataclass


@dataclass(slots=True)
class DomainAssociatedDomain:
    """Domain associated with a contact."""

    id: int
    name: str
    roles: list[Literal["admin", "billing", "owner", "tech"]]


@dataclass(slots=True)
class DomainContact:
    """Domain contact payload."""

    address_type: Literal["int", "loc"]
    first_name: str
    last_name: str | None
    company: str
    street1: str
    street2: str
    street3: str | None
    postal_code: str
    city: str
    state: str
    country_code: str
    id: int
    type: Literal["Association", "Organization", "Other", "Person"]
    phone: str
    fax: str | None
    email: str
    is_validated: bool
    validated_at: int
    created_at: int
    associated_domains: list[DomainAssociatedDomain] | None = None


@dataclass(slots=True)
class DomainContacts:
    """Domain contacts grouped by role."""

    owner: DomainContact | None = None
    admin: DomainContact | None = None
    tech: DomainContact | None = None
    billing: DomainContact | None = None


@dataclass(slots=True)
class DomainOptions:
    """Domain options payload."""

    dns_anycast: bool
    renewal_warranty: bool
    domain_privacy: bool
    dnssec: bool


@dataclass(slots=True)
class Domain:
    """Domain payload.

    OpenAPI schema: `6a791d9b_api-domain_domain`.
    """

    name: str
    tld: str
    is_premium: bool
    created_at: int
    expires_at: int
    options: DomainOptions
    contacts: DomainContacts
    status: (
        list[
            Literal[
                "addPeriod",
                "autoRenewPeriod",
                "clientDeleteProhibited",
                "clientHold",
                "clientRenewProhibited",
                "clientTransferProhibited",
                "clientUpdateProhibited",
                "inactive",
                "ok",
                "pendingCreate",
                "pendingDelete",
                "pendingRenew",
                "pendingRestore",
                "pendingTransfer",
                "pendingUpdate",
                "redemptionPeriod",
                "renewPeriod",
                "serverDeleteProhibited",
                "serverHold",
                "serverRenewProhibited",
                "serverTransferProhibited",
                "serverUpdateProhibited",
                "transferPeriod",
            ]
        ]
        | None
    ) = None


@dataclass(slots=True)
class DomainListResponse:
    """List domains response payload with pagination metadata."""

    data: list[Domain]
    total: int | None = None
    page: int | None = None
    pages: int | None = None
    items_per_page: int | None = None
