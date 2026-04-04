from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

TldFieldType = Literal[
    "checkbox",
    "contact_id",
    "date",
    "email",
    "info",
    "phone",
    "radio",
    "select",
    "text",
    "warning",
]


@dataclass(slots=True)
class TldGroup:
    """TLD group payload."""

    id: int
    name: str


@dataclass(slots=True)
class TldLocalizedText:
    """Localized text payload used by TLD timing fields."""

    de_DE: str
    en_GB: str
    es_ES: str
    fr_FR: str
    it_IT: str


@dataclass(slots=True)
class TldPeriods:
    """Domain lifecycle periods for a TLD."""

    renew_grace: int | None = None
    redemption: int | None = None
    deletion: int | None = None


@dataclass(slots=True)
class TldSupport:
    """Supported features for a TLD."""

    dns_anycast: bool | None = None
    domain_privacy: bool | None = None
    transfer_lock: bool | None = None
    renew_on_transfer: bool | None = None
    preconfigured_dns: bool | None = None
    dnssec: bool | None = None


@dataclass(slots=True)
class TldOutgoingTransferNeed:
    """Outgoing transfer requirements for a TLD."""

    auth_code: bool | None = None
    auth_code_length: int | None = None
    ips_tag: bool | None = None


@dataclass(slots=True)
class TldFieldOption:
    """Possible value for a TLD field."""

    name: str
    value: str


@dataclass(slots=True)
class TldFieldCondition:
    """Conditional requirement for a TLD field."""

    field: str
    operator: str
    value: str
    contact: Literal["admin", "billing", "owner", "tech"] | None = None
    logic: Literal["AND", "OR"] | None = None


@dataclass(slots=True)
class TldField:
    """TLD registration or transfer field."""

    type: TldFieldType
    name: str
    required: bool
    description: str | None = None
    guideline: str | None = None
    min_length: int | None = None
    max_length: int | None = None
    pattern: str | None = None
    note: str | None = None
    default: str | None = None
    options: list[TldFieldOption] | None = None
    required_conditions: list[TldFieldCondition] | None = None


@dataclass(slots=True)
class TldContactField:
    """Contact field requirements for a TLD."""

    type: TldFieldType
    contact_type: dict[str, str]
    name: str
    required: bool
    transfer: bool
    trade: bool
    restricted_fields: list[TldField] | None = None


@dataclass(slots=True)
class TldFields:
    """Extra fields required by a TLD."""

    contacts: list[TldContactField] | None = None
    description: str | None = None
    registration: list[TldField] | None = None
    transfer: list[TldField] | None = None


@dataclass(slots=True)
class IDNTable:
    """Internationalized Domain Name table."""

    language: str
    characters: list[str]


@dataclass(slots=True)
class Tld:
    """Top-level domain payload."""

    id: int
    tld: str
    is_idn: bool | None = None
    groups: list[TldGroup] | None = None
    registration_time: TldLocalizedText | None = None
    transfer_time: int | None = None
    trade_time: TldLocalizedText | None = None
    outgoing_transfer_time: int | None = None
    domain_length: str | None = None
    periods: TldPeriods | None = None
    support: TldSupport | None = None
    renewal_periods: list[int] | None = None
    registration_periods: list[int] | None = None
    outgoing_transfer_need: TldOutgoingTransferNeed | None = None
    fields: TldFields | None = None
    idn: list[IDNTable] | None = None
