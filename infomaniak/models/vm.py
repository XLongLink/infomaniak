from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class VirtualMachine:
    id: Any = None
    name: str = ""
    status: str = ""
    flavor: str = ""
    image: str = ""
    region: str = ""
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return cls()
        return cls(
            id=payload.get("id"),
            name=payload.get("name") or payload.get("hostname") or payload.get("label", ""),
            status=payload.get("status") or payload.get("state", ""),
            flavor=payload.get("flavor") or payload.get("instance_type", ""),
            image=payload.get("image", ""),
            region=payload.get("region") or payload.get("availability_zone", ""),
            raw=dict(payload),
        )
