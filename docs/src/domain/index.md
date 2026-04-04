# Domain Overview

Manage domains through `client.domain`.

## Methods

- `show(domain: str) -> Domain`
- `list(*, account_id=None, expires_after=None, expires_before=None, order_by=None, order_dir=None, search=None, tld=None, page=None, per_page=None) -> DomainListResponse`

## Request parameters

### `show`

- `domain: str` (required): domain name (example: `mydomain.ch`).

### `list`

- `account_id: int | None`
- `expires_after: int | None`
- `expires_before: int | None`
- `order_by: Literal["expiration", "name"] | None`
- `order_dir: Literal["asc", "desc"] | None`
- `search: str | None`
- `tld: str | None`
- `page: int | None`
- `per_page: int | None`

## Returned models

- `Domain` from `infomaniak.models.domain`
- `DomainListResponse` from `infomaniak.models.domain`

## Example

```py
from infomaniak import Client

client = Client(token="...")

item = client.domain.show("mydomain.ch")
print(item.name, item.expires_at)

result = client.domain.list(account_id=12345, page=1, per_page=20)
print(result.total, len(result.data))
```
