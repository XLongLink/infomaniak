# DNS TLD

Manage `client.dns.tld` endpoints.

## Methods

- `list(with_=None, groups=None) -> list[Tld]`
- `show(tld, with_=None) -> Tld`

## Request parameters

### `list`

- `with_`: include extra fields in the response (`length`, `periods`, `groups`, `transfer_method`, `is_idn`, `support`, `time`, `fields`, `idn`).
- `groups`: filter TLDs by TLD group IDs.

### `show`

- `tld`: TLD identifier (for example `com`, `ch`, `swiss`).
- `with_`: include extra fields in the response (`length`, `periods`, `groups`, `transfer_method`, `is_idn`, `support`, `time`, `fields`, `idn`).

## Returned models

- `Tld`
- `TldGroup`
- `TldPeriods`
- `TldSupport`
- `TldFields`

## Examples

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")

tlds = client.dns.tld.list(with_="groups")
for item in tlds:
    print(item.tld)
```

```py
tld = client.dns.tld.show("com", with_="periods,support")
print(tld.registration_periods)
print(tld.support)
```
