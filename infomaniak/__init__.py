"""Library-first Infomaniak client package."""

__version__ = "0.7.0"
API_BASE = "https://api.infomaniak.com"

from infomaniak.client import AsyncClient, AsyncDNSClient, Client, DNSClient

__all__ = ["AsyncClient", "AsyncDNSClient", "Client", "DNSClient"]
