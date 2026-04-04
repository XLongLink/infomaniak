# DNS TLD

Manage `client.dns.tld` endpoints.

## Methods

- `list(length=False, periods=False, group=False, transfer_method=False, is_idn=False, support=False, time=False, groups=None) -> list[Tld]`
- `show(tld, length=False, periods=False, group=False, transfer_method=False, is_idn=False, support=False, time=False) -> Tld`

## Request parameters

### `list`

- `length`: include the `domain_length` field.
- `periods`: include period fields (`periods`, `renewal_periods`, `registration_periods`).
- `group`: include TLD groups.
- `transfer_method`: include outgoing transfer method requirements.
- `is_idn`: include IDN support information.
- `support`: include supported features.
- `time`: include registration, transfer, trade and outgoing transfer time fields.
- `groups`: filter TLDs by TLD group IDs.

### `show`

- `tld`: TLD identifier (for example `com`, `ch`, `swiss`).
- `length`: include the `domain_length` field.
- `periods`: include period fields (`periods`, `renewal_periods`, `registration_periods`).
- `group`: include TLD groups.
- `transfer_method`: include outgoing transfer method requirements.
- `is_idn`: include IDN support information.
- `support`: include supported features.
- `time`: include registration, transfer, trade and outgoing transfer time fields.

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

tlds = client.dns.tld.list(group=True, periods=True)
for item in tlds:
    print(item.tld)
```

```py
tld = client.dns.tld.show("com", periods=True, support=True)
print(tld.registration_periods)
print(tld.support)
```
