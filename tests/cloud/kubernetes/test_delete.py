import pytest
from collections.abc import Callable
from typing import Any

from tests.__init__ import fetch


@pytest.fixture
def api_fetch() -> Callable[..., Any]:
    return fetch


def test_delete_kubernetes_cluster_returns_true(
    api_fetch: Callable[..., Any],
) -> None:
    deleted = api_fetch(
        method="DELETE",
        path="/1/public_clouds/1234/projects/5678/kaas/9012",
        response={"result": "success", "data": True},
        call=lambda client: client.cloud.kubernetes.delete(
            public_cloud_id=1234,
            public_cloud_project_id=5678,
            kaas_id=9012,
        ),
    )

    assert deleted is True


def test_delete_kubernetes_cluster_raises_when_data_is_false(
    api_fetch: Callable[..., Any],
) -> None:
    with pytest.raises(ValueError, match="delete operation failed"):
        api_fetch(
            method="DELETE",
            path="/1/public_clouds/1234/projects/5678/kaas/9012",
            response={"result": "success", "data": False},
            call=lambda client: client.cloud.kubernetes.delete(
                public_cloud_id=1234,
                public_cloud_project_id=5678,
                kaas_id=9012,
            ),
        )
