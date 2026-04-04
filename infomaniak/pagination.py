from typing import TypeVar
from collections.abc import Callable, Iterator

TPage = TypeVar("TPage")
TCursor = TypeVar("TCursor")


def pages(
    fetch_page: Callable[[TCursor | None], tuple[TPage, TCursor | None]],
    cursor: TCursor | None = None,
) -> Iterator[TPage]:
    """Iterate over API pages until no data or cursor is returned.

    Args:
        fetch_page: Function receiving the current cursor and returning
            ``(data, next_cursor)``.
        cursor: Optional starting cursor.

    Yields:
        Each page payload returned by ``fetch_page``.
    """
    while True:
        data, cursor = fetch_page(cursor)
        if not data:
            break

        yield data

        if cursor is None:
            break
