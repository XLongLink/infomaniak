from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Action:
    """Core action payload."""

    id: int
    code: str
    description: str


@dataclass(slots=True)
class Timezone:
    """Timezone payload."""

    id: int
    name: str
    gmt: str
