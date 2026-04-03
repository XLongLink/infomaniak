"""Kubernetes resource group for the SDK."""

from infomaniak.models.kubernetes import KubernetesService, KubernetesServicePack


class KubernetesResource:
    """Sync Kubernetes resource.

    This starts with the static KaaS discovery endpoints found in OpenApi.json,
    plus a generic deploy hook for future cluster-scoped operations.
    """

    def __init__(self, client):
        self._client = client

    def list(self):
        data = self._client._request("GET", "/1/public_clouds/kaas")
        return [KubernetesService.from_api(item) for item in data]

    def packs(self):
        data = self._client._request("GET", "/1/public_clouds/kaas/packs")
        return [KubernetesServicePack.from_api(item) for item in data]

    def versions(self):
        return self._client._request("GET", "/1/public_clouds/kaas/versions")

    def regions(self):
        return self._client._request("GET", "/1/public_clouds/kaas/regions")

    def availability_zones(self):
        return self._client._request("GET", "/1/public_clouds/kaas/availability_zones")

    def deploy(self, path, payload):
        return self._client._request("POST", path, json=payload)


class AsyncKubernetesResource:
    """Async Kubernetes resource."""

    def __init__(self, client):
        self._client = client

    async def list(self):
        data = await self._client._request("GET", "/1/public_clouds/kaas")
        return [KubernetesService.from_api(item) for item in data]

    async def packs(self):
        data = await self._client._request("GET", "/1/public_clouds/kaas/packs")
        return [KubernetesServicePack.from_api(item) for item in data]

    async def versions(self):
        return await self._client._request("GET", "/1/public_clouds/kaas/versions")

    async def regions(self):
        return await self._client._request("GET", "/1/public_clouds/kaas/regions")

    async def availability_zones(self):
        return await self._client._request("GET", "/1/public_clouds/kaas/availability_zones")

    async def deploy(self, path, payload):
        return await self._client._request("POST", path, json=payload)
