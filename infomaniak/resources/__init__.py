"""SDK resource groups."""

from infomaniak.resources.core import AsyncUserResource, UserResource
from infomaniak.resources.databases import AsyncDatabaseResource, DatabaseResource
from infomaniak.resources.dns import AsyncDNSResource, DNSResource
from infomaniak.resources.groups import AsyncCoreResources, CoreResources
from infomaniak.resources.kubernetes import AsyncKubernetesResource, KubernetesResource
from infomaniak.resources.vms import AsyncVMResource, VMResource

__all__ = [
    "AsyncCoreResources",
    "AsyncDNSResource",
    "DNSResource",
    "AsyncVMResource",
    "VMResource",
    "AsyncDatabaseResource",
    "DatabaseResource",
    "AsyncKubernetesResource",
    "KubernetesResource",
    "AsyncUserResource",
    "UserResource",
    "CoreResources",
]
