from __future__ import annotations

from typing import Literal
from dataclasses import dataclass


@dataclass(slots=True)
class UpdateNameserversRequest:
    """Request payload for updating a domain nameserver configuration."""

    nameservers: list[str] | None = None
    use_infomaniak_ns: bool | None = None
    verify_ns_availability: bool = False


@dataclass(slots=True)
class UpdateNameserversResponse:
    """Response payload returned by nameserver update operations."""

    result: Literal["success", "error", "asynchronous"]
    data: bool
