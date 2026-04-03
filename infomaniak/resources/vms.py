"""VM resource scaffolding for the SDK."""

from infomaniak.models.vm import VirtualMachine


class VMResource:
    """Scaffold for VM APIs.

    Public cloud VM endpoints are project-scoped in the Infomaniak API, so this
    resource intentionally accepts explicit paths until the project model is
    implemented.
    """

    def __init__(self, client):
        self._client = client

    def list(self, path, params=None):
        data = self._client._request("GET", path, params=params)
        if isinstance(data, list):
            return [VirtualMachine.from_api(item) for item in data]
        return data

    def create(self, path, payload):
        data = self._client._request("POST", path, json=payload)
        if isinstance(data, dict):
            return VirtualMachine.from_api(data)
        return data


class AsyncVMResource:
    """Async VM scaffold with the same path-based contract as VMResource."""

    def __init__(self, client):
        self._client = client

    async def list(self, path, params=None):
        data = await self._client._request("GET", path, params=params)
        if isinstance(data, list):
            return [VirtualMachine.from_api(item) for item in data]
        return data

    async def create(self, path, payload):
        data = await self._client._request("POST", path, json=payload)
        if isinstance(data, dict):
            return VirtualMachine.from_api(data)
        return data
