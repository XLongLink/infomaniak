from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class DNSRecordAttribute:
    value: Any = None
    label: str = ""

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return None
        return cls(value=payload.get("value"), label=payload.get("label", ""))


@dataclass
class DNSRecordDescription:
    priority: Optional[DNSRecordAttribute] = None
    port: Optional[DNSRecordAttribute] = None
    weight: Optional[DNSRecordAttribute] = None
    protocol: Optional[DNSRecordAttribute] = None
    flags: Optional[DNSRecordAttribute] = None
    tag: Optional[DNSRecordAttribute] = None
    usage: Optional[DNSRecordAttribute] = None
    selector: Optional[DNSRecordAttribute] = None
    matching_type: Optional[DNSRecordAttribute] = None
    algorithm: Optional[DNSRecordAttribute] = None
    key_tag: Optional[DNSRecordAttribute] = None
    digest_type: Optional[DNSRecordAttribute] = None
    digest: Optional[DNSRecordAttribute] = None
    mname: Optional[DNSRecordAttribute] = None
    rname: Optional[DNSRecordAttribute] = None
    serial: Optional[DNSRecordAttribute] = None
    refresh: Optional[DNSRecordAttribute] = None
    retry: Optional[DNSRecordAttribute] = None
    expire: Optional[DNSRecordAttribute] = None
    minimum: Optional[DNSRecordAttribute] = None

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return None
        fields = {name: DNSRecordAttribute.from_api(payload.get(name)) for name in cls.__dataclass_fields__}
        return cls(**fields)


@dataclass
class DNSRecord:
    id: Any = None
    source: str = ""
    source_idn: str = ""
    target: str = ""
    type: str = ""
    ttl: int = 3600
    updated_at: Optional[int] = None
    dyndns_id: Optional[int] = None
    delegated_zone: Dict[str, Any] = field(default_factory=dict)
    description: Optional[DNSRecordDescription] = None
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return cls()
        return cls(
            id=payload.get("id"),
            source=payload.get("source", ""),
            source_idn=payload.get("source_idn", ""),
            target=payload.get("target", ""),
            type=payload.get("type", ""),
            ttl=payload.get("ttl", 3600),
            updated_at=payload.get("updated_at"),
            dyndns_id=payload.get("dyndns_id"),
            delegated_zone=payload.get("delegated_zone") or {},
            description=DNSRecordDescription.from_api(payload.get("description")),
            raw=dict(payload),
        )
