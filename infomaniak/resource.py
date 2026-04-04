from infomaniak.clients import AsyncBaseClient, BaseClient


class Resouce:
    def __init__(self, client: AsyncBaseClient):
        self._client = client


class AsyncResource:
    def __init__(self, client: AsyncBaseClient):
        self._client = client