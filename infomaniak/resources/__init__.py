"""SDK resource groups."""

from infomaniak.resources.databases import AsyncDatabaseResource, DatabaseResource
from infomaniak.resources.dns import AsyncDNSResource, DNSResource
from infomaniak.resources.kubernetes import AsyncKubernetesResource, KubernetesResource
from infomaniak.resources.vms import AsyncVMResource, VMResource

__all__ = [
    "AsyncDNSResource",
    "DNSResource",
    "AsyncVMResource",
    "VMResource",
    "AsyncDatabaseResource",
    "DatabaseResource",
    "AsyncKubernetesResource",
    "KubernetesResource",
]
