from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class DatabaseInstance:
    id: Any = None
    name: str = ""
    engine: str = ""
    version: str = ""
    status: str = ""
    host: str = ""
    port: Optional[int] = None
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return cls()
        return cls(
            id=payload.get("id"),
            name=payload.get("name", ""),
            engine=payload.get("engine") or payload.get("type", ""),
            version=payload.get("version", ""),
            status=payload.get("status", ""),
            host=payload.get("host") or payload.get("hostname", ""),
            port=payload.get("port"),
            raw=dict(payload),
        )
