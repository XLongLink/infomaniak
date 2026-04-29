from __future__ import annotations

from typing import Any, Callable

import httpx

from infomaniak import Client


def fetch(
    method: str,
    path: str,
    response: Any,
    call: Callable[[Client], Any],
) -> Any:
    """
    Create a mock API client, assert the request, and run a client call.

    Args:
        method: The expected HTTP method.
        path: The expected request path.
        response: The mocked JSON response body.
        call: A callable that executes the SDK method under test.

    Returns:
        Any: The value returned by the SDK call.
    """

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == method
        assert request.url.path == path
        return httpx.Response(200, json=response)

    transport = httpx.MockTransport(handler)
    client = Client(token="test-token", transport=transport)
    return call(client)
