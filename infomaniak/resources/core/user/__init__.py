class User:
    """Core resources for Infomaniak services."""

    def __init__(self, client):
        self._client = client

    def invite(self):
        """https://developer.infomaniak.com/docs/api/post/1/accounts/%7Baccount%7D/invitations"""
        pass

    def revoke(self, account: int, invitation: int):
        """https://developer.infomaniak.com/docs/api/delete/1/accounts/%7Baccount%7D/invitations/%7Binvitation%7D"""
        pass

    

class AsyncUser:
    """Async core resources for Infomaniak services."""

    def __init__(self, client):
        self._client = client

    async def user(self):
        """Get the current authenticated user."""
        return await self._client._request("GET", "/user")
    