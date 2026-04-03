from infomaniak._base import AsyncBaseClient, BaseClient
from infomaniak.resources.databases import AsyncDatabaseResource, DatabaseResource
from infomaniak.resources.dns import AsyncDNSResource, DNSResource
from infomaniak.resources.kubernetes import AsyncKubernetesResource, KubernetesResource
from infomaniak.resources.vms import AsyncVMResource, VMResource


class DNSClient(BaseClient):
    """Sync resource-based SDK client."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dns = DNSResource(self)
        self.vms = VMResource(self)
        self.databases = DatabaseResource(self)
        self.kubernetes = KubernetesResource(self)


class AsyncDNSClient(AsyncBaseClient):
    """Async resource-based SDK client."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dns = AsyncDNSResource(self)
        self.vms = AsyncVMResource(self)
        self.databases = AsyncDatabaseResource(self)
        self.kubernetes = AsyncKubernetesResource(self)


Client = DNSClient
AsyncClient = AsyncDNSClient
