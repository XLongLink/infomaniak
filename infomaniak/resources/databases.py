from infomaniak.models.database import DatabaseInstance


class DatabaseResource:
    """Scaffold for future database resources."""

    def __init__(self, client):
        self._client = client

    def list(self, path, params=None):
        data = self._client._request("GET", path, params=params)
        if isinstance(data, list):
            return [DatabaseInstance.from_api(item) for item in data]
        return data

    def create(self, path, payload):
        data = self._client._request("POST", path, json=payload)
        if isinstance(data, dict):
            return DatabaseInstance.from_api(data)
        return data


class AsyncDatabaseResource:
    """Async scaffold for future database resources."""

    def __init__(self, client):
        self._client = client

    async def list(self, path, params=None):
        data = await self._client._request("GET", path, params=params)
        if isinstance(data, list):
            return [DatabaseInstance.from_api(item) for item in data]
        return data

    async def create(self, path, payload):
        data = await self._client._request("POST", path, json=payload)
        if isinstance(data, dict):
            return DatabaseInstance.from_api(data)
        return data
