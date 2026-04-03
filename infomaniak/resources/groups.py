"""Grouped client resource namespaces."""

from infomaniak.resources.core import AsyncUserResource, UserResource


class CoreResources:
    """Sync grouped resources mounted under client.resources."""

    def __init__(self, client):
        self.user = UserResource(client)


class AsyncCoreResources:
    """Async grouped resources mounted under client.resources."""

    def __init__(self, client):
        self.user = AsyncUserResource(client)


__all__ = ["AsyncCoreResources", "CoreResources"]
