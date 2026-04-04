from __future__ import annotations

from typing import TypeVar, Iterable

T = TypeVar("T")


class PaginatedList(list[T]):
    def __init__(self, values: Iterable[T] = (), *, page: int = 1, pages: int = 1, items: int = 0,) -> None:
        super().__init__(values)
        self.page = page
        self.pages = pages
        self.items = items


def _with(**fields: bool) -> str | None:
    """
    Build a comma-separated value for API `with` query parameters.

    Args:
        **fields (bool): Mapping of field names to inclusion flags.

    Returns:
        str | None: Comma-separated field names for truthy flags, or None if empty.
    """
    values = [key for key, include in fields.items() if include]
    return ",".join(values) if values else None
