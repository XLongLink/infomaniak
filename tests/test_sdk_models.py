import httpx

from infomaniak.client import DNSClient
from infomaniak.models import DatabaseInstance, DNSRecord, KubernetesService, KubernetesServicePack, VirtualMachine


def _transport(routes):
    def handler(request):
        payload = routes[(request.method, request.url.path)]
        return httpx.Response(200, json={"result": "success", "data": payload})

    return httpx.MockTransport(handler)


def test_dns_resource_returns_dns_record_models():
    transport = _transport(
        {
            (
                "GET",
                "/2/zones/example.com/records",
            ): [
                {
                    "id": 1,
                    "source": "@",
                    "source_idn": "example.com",
                    "target": "192.0.2.1",
                    "type": "A",
                    "ttl": 300,
                    "updated_at": 1710000000,
                    "description": {"priority": {"value": 10, "label": "10"}},
                }
            ]
        }
    )

    client = DNSClient(token="token", zone="example.com", transport=transport)
    records = client.dns.records()

    assert len(records) == 1
    assert isinstance(records[0], DNSRecord)
    assert records[0].description.priority.value == 10


def test_vm_resource_returns_virtual_machine_models():
    transport = _transport(
        {
            ("GET", "/vms"): [
                {
                    "id": "vm-1",
                    "hostname": "web-01",
                    "state": "ACTIVE",
                    "instance_type": "small",
                    "availability_zone": "dc-a",
                }
            ]
        }
    )

    client = DNSClient(token="token", transport=transport)
    vms = client.vms.list("/vms")

    assert len(vms) == 1
    assert isinstance(vms[0], VirtualMachine)
    assert vms[0].name == "web-01"
    assert vms[0].status == "ACTIVE"


def test_database_resource_returns_database_instance_models():
    transport = _transport(
        {
            ("POST", "/databases"): {
                "id": "db-1",
                "name": "app",
                "type": "postgresql",
                "version": "16",
                "status": "ready",
                "hostname": "db.internal",
                "port": 5432,
            }
        }
    )

    client = DNSClient(token="token", transport=transport)
    database = client.databases.create("/databases", {"name": "app"})

    assert isinstance(database, DatabaseInstance)
    assert database.engine == "postgresql"
    assert database.host == "db.internal"


def test_kubernetes_resource_returns_schema_models():
    transport = _transport(
        {
            ("GET", "/1/public_clouds/kaas"): [
                {
                    "kaas_id": 99,
                    "name": "cluster-a",
                    "open_stack_name": "pck-12345",
                    "region": "rc3-a",
                    "kubernetes_version": "1.30",
                    "status": "Active",
                    "pack": {
                        "kaas_pack_id": 1,
                        "name": "shared",
                        "description": "Shared pack",
                        "price_per_hour": [{"currency": "CHF", "amount": "0.10"}],
                        "limit_per_project": None,
                        "is_active": True,
                    },
                    "project": {
                        "id": 5,
                        "public_cloud_id": 3,
                        "name": "project-a",
                        "open_stack_name": "PCP-A",
                    },
                    "tags": [{"id": 7, "name": "prod", "color": 4, "product_count": 1}],
                    "instances": {
                        "total": 10,
                        "used": 4,
                        "fixed": 2,
                        "minimum_autoscaled": 1,
                        "maximum_autoscaled": 5,
                        "minimum_available_instances": 1,
                        "maximum_available_instances": 2,
                    },
                }
            ],
            ("GET", "/1/public_clouds/kaas/packs"): [
                {
                    "kaas_pack_id": 1,
                    "name": "shared",
                    "description": "Shared pack",
                    "price_per_hour": [],
                    "limit_per_project": None,
                    "is_active": "true",
                }
            ],
        }
    )

    client = DNSClient(token="token", transport=transport)
    services = client.kubernetes.list()
    packs = client.kubernetes.packs()

    assert len(services) == 1
    assert isinstance(services[0], KubernetesService)
    assert services[0].pack.name == "shared"
    assert services[0].project.name == "project-a"
    assert services[0].tags[0].name == "prod"
    assert isinstance(packs[0], KubernetesServicePack)


def test_scalar_kubernetes_endpoints_still_return_plain_lists():
    transport = _transport(
        {
            ("GET", "/1/public_clouds/kaas/versions"): ["1.29", "1.30"],
            ("GET", "/1/public_clouds/kaas/regions"): ["rc1-a", "rc3-a"],
            ("GET", "/1/public_clouds/kaas/availability_zones"): ["az-1", "az-2"],
        }
    )

    client = DNSClient(token="token", transport=transport)

    assert client.kubernetes.versions() == ["1.29", "1.30"]
    assert client.kubernetes.regions() == ["rc1-a", "rc3-a"]
    assert client.kubernetes.availability_zones() == ["az-1", "az-2"]
