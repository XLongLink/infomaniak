"""DNS SDK resource."""

from infomaniak.models.dns import DNSRecord


class DNSResource:
    """Sync DNS resource backed by the documented /2/zones endpoints."""

    def __init__(self, client):
        self._client = client

    def records(self, zone=None, source=None, record_types=None, search=None):
        zone = self._client._require_zone(zone)
        params = {}
        if source:
            params["source"] = source
        if record_types:
            params["type"] = record_types
        if search:
            params["search"] = search
        data = self._client._request("GET", f"/2/zones/{zone}/records", params=params or None)
        return [DNSRecord.from_api(item) for item in data]

    def get(self, record_id, zone=None):
        zone = self._client._require_zone(zone)
        data = self._client._request("GET", f"/2/zones/{zone}/records/{record_id}")
        return DNSRecord.from_api(data)

    def add(self, source, record_type, target, ttl=3600, zone=None):
        zone = self._client._require_zone(zone)
        payload = {
            "source": "" if source == "@" else source,
            "type": record_type.upper(),
            "target": target,
            "ttl": ttl,
        }
        data = self._client._request("POST", f"/2/zones/{zone}/records", json=payload)
        return DNSRecord.from_api(data)

    def update(self, record_id, zone=None, target=None, ttl=None):
        zone = self._client._require_zone(zone)
        payload = {}
        if target is not None:
            payload["target"] = target
        if ttl is not None:
            payload["ttl"] = ttl
        if not payload:
            raise ValueError("Specify at least one of target=... or ttl=... when updating a DNS record.")
        data = self._client._request("PUT", f"/2/zones/{zone}/records/{record_id}", json=payload)
        return DNSRecord.from_api(data)

    def delete(self, record_id, zone=None):
        zone = self._client._require_zone(zone)
        return self._client._request("DELETE", f"/2/zones/{zone}/records/{record_id}")

    def check(self, record_id, zone=None):
        zone = self._client._require_zone(zone)
        return self._client._request("GET", f"/2/zones/{zone}/records/{record_id}/check")


class AsyncDNSResource:
    """Async DNS resource backed by the documented /2/zones endpoints."""

    def __init__(self, client):
        self._client = client

    async def records(self, zone=None, source=None, record_types=None, search=None):
        zone = self._client._require_zone(zone)
        params = {}
        if source:
            params["source"] = source
        if record_types:
            params["type"] = record_types
        if search:
            params["search"] = search
        data = await self._client._request("GET", f"/2/zones/{zone}/records", params=params or None)
        return [DNSRecord.from_api(item) for item in data]

    async def get(self, record_id, zone=None):
        zone = self._client._require_zone(zone)
        data = await self._client._request("GET", f"/2/zones/{zone}/records/{record_id}")
        return DNSRecord.from_api(data)

    async def add(self, source, record_type, target, ttl=3600, zone=None):
        zone = self._client._require_zone(zone)
        payload = {
            "source": "" if source == "@" else source,
            "type": record_type.upper(),
            "target": target,
            "ttl": ttl,
        }
        data = await self._client._request("POST", f"/2/zones/{zone}/records", json=payload)
        return DNSRecord.from_api(data)

    async def update(self, record_id, zone=None, target=None, ttl=None):
        zone = self._client._require_zone(zone)
        payload = {}
        if target is not None:
            payload["target"] = target
        if ttl is not None:
            payload["ttl"] = ttl
        if not payload:
            raise ValueError("Specify at least one of target=... or ttl=... when updating a DNS record.")
        data = await self._client._request("PUT", f"/2/zones/{zone}/records/{record_id}", json=payload)
        return DNSRecord.from_api(data)

    async def delete(self, record_id, zone=None):
        zone = self._client._require_zone(zone)
        return await self._client._request("DELETE", f"/2/zones/{zone}/records/{record_id}")

    async def check(self, record_id, zone=None):
        zone = self._client._require_zone(zone)
        return await self._client._request("GET", f"/2/zones/{zone}/records/{record_id}/check")
