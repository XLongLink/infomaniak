class Core:
    """Core resources for Infomaniak services."""

    def __init__(self, client):
        self._client = client

    def user(self):
        """Get the current authenticated user."""
        return self._client._request("GET", "/user")
    

class AsyncCore:
    """Async core resources for Infomaniak services."""

    def __init__(self, client):
        self._client = client

    async def user(self):
        """Get the current authenticated user."""
        return await self._client._request("GET", "/user")
    