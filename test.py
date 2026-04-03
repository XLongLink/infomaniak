"""Sample usage against the installed ``infomaniak`` SDK package."""

import json

import httpx
import infomaniak
from infomaniak.sdk import Client


def _mock_handler(request):
    if request.method == "GET" and request.url.path == "/2/zones/example.com/records":
        return httpx.Response(
            200,
            json={
                "result": "success",
                "data": [
                    {"id": 1, "type": "A", "source": "www", "target": "192.0.2.10", "ttl": 300},
                    {"id": 2, "type": "TXT", "source": "@", "target": "hello=world", "ttl": 600},
                ],
            },
        )

    if request.method == "POST" and request.url.path == "/2/zones/example.com/records":
        payload = json.loads(request.content.decode("utf-8"))
        return httpx.Response(
            200,
            json={
                "result": "success",
                "data": {"id": 3, **payload},
            },
        )

    return httpx.Response(404, json={"result": "error", "error": {"code": "not_found", "description": request.url.path}})


def run_sample():
    print(f"Loaded package: infomaniak {infomaniak.__version__}")
    print(f"API base: {infomaniak.API_BASE}")

    transport = httpx.MockTransport(_mock_handler)
    with Client(token="test-token", zone="example.com", transport=transport) as client:
        records = client.dns.records()
        created = client.dns.add(source="api", record_type="A", target="198.51.100.25", ttl=900)

        print(f"records(): {len(records)} records")
        print(f"first record: {records[0].source} {records[0].type} -> {records[0].target}")
        print(f"add(): created #{created.id} {created.source or '@'} {created.type} -> {created.target}")
        print(f"resource groups: {', '.join(sorted(['dns', 'vms', 'databases', 'kubernetes']))}")


if __name__ == "__main__":
    run_sample()
