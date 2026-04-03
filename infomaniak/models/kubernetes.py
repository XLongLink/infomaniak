from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class KubernetesTag:
    id: Optional[int] = None
    name: str = ""
    color: Optional[int] = None
    product_count: Optional[int] = None

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return None
        return cls(
            id=payload.get("id"),
            name=payload.get("name", ""),
            color=payload.get("color"),
            product_count=payload.get("product_count"),
        )


@dataclass
class ServiceProject:
    id: Optional[int] = None
    public_cloud_id: Optional[int] = None
    name: str = ""
    open_stack_name: str = ""

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return None
        return cls(
            id=payload.get("id"),
            public_cloud_id=payload.get("public_cloud_id"),
            name=payload.get("name", ""),
            open_stack_name=payload.get("open_stack_name", ""),
        )


@dataclass
class KubernetesServiceInstanceTotals:
    total: Optional[int] = None
    used: Optional[int] = None
    fixed: int = 0
    minimum_autoscaled: int = 0
    maximum_autoscaled: int = 0
    minimum_available_instances: int = 0
    maximum_available_instances: int = 0

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return None
        return cls(
            total=payload.get("total"),
            used=payload.get("used"),
            fixed=payload.get("fixed", 0),
            minimum_autoscaled=payload.get("minimum_autoscaled", 0),
            maximum_autoscaled=payload.get("maximum_autoscaled", 0),
            minimum_available_instances=payload.get("minimum_available_instances", 0),
            maximum_available_instances=payload.get("maximum_available_instances", 0),
        )


@dataclass
class KubernetesServicePack:
    kaas_pack_id: Optional[int] = None
    name: str = ""
    description: str = ""
    price_per_hour: List[Any] = field(default_factory=list)
    limit_per_project: Optional[int] = None
    is_active: str = ""
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return None
        return cls(
            kaas_pack_id=payload.get("kaas_pack_id"),
            name=payload.get("name", ""),
            description=payload.get("description", ""),
            price_per_hour=list(payload.get("price_per_hour") or []),
            limit_per_project=payload.get("limit_per_project"),
            is_active=str(payload.get("is_active", "")),
            raw=dict(payload),
        )


@dataclass
class KubernetesService:
    kaas_id: Optional[int] = None
    name: str = ""
    open_stack_name: str = ""
    region: str = ""
    kubernetes_version: str = ""
    status: str = ""
    pack: Optional[KubernetesServicePack] = None
    project: Optional[ServiceProject] = None
    tags: List[KubernetesTag] = field(default_factory=list)
    instances: Optional[KubernetesServiceInstanceTotals] = None
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_api(cls, payload: Optional[Dict[str, Any]]):
        if not isinstance(payload, dict):
            return None
        return cls(
            kaas_id=payload.get("kaas_id"),
            name=payload.get("name", ""),
            open_stack_name=payload.get("open_stack_name", ""),
            region=payload.get("region", ""),
            kubernetes_version=payload.get("kubernetes_version", ""),
            status=payload.get("status", ""),
            pack=KubernetesServicePack.from_api(payload.get("pack")),
            project=ServiceProject.from_api(payload.get("project")),
            tags=[
                tag
                for tag in (KubernetesTag.from_api(item) for item in payload.get("tags") or [])
                if tag is not None
            ],
            instances=KubernetesServiceInstanceTotals.from_api(payload.get("instances")),
            raw=dict(payload),
        )
