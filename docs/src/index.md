# Overview

::: warning
This SDK and its documentation are currently in active development. Endpoints, method signatures, and coverage can change without notice.
:::

## How to install

```bash
pip install xinfomaniak
```

## Pagination example

Use the shared pagination helper to iterate through all pages for a list endpoint.

```py
from infomaniak import Client
from infomaniak.utils.pagination import paginate

client = Client(token="YOUR_API_TOKEN")

for item in paginate(client.mail.mailboxes.list, account_id=12345, per_page=50):
    print(item)
```

## Pagination with filtering (`functools.partial`)

You can pre-apply filters with `functools.partial` and still paginate with the same helper.

```py
from functools import partial

from infomaniak import Client
from infomaniak.utils.pagination import paginate

client = Client(token="YOUR_API_TOKEN")

active_domains = partial(
    client.domain.domains.list,
    account_id=12345,
    status="active",
)

for domain in paginate(active_domains, per_page=100):
    print(domain)
```

## API Resources

Infomaniak OpenAPI v3.1.0

| Resource                     | Infomaniak Reference                      | Documented methods | Status  |
| ---------------------------- | ----------------------------------------- | ------------------ | ------- |
| [`ai`](/ai/)                 | AI Tools                                  | 0                  | Low priority |
| [`backup`](/backup/)         | Swiss Backup                              | 17                 | Low priority |
| [`cloud`](/cloud/)           | Cloud Overview                            | 51                 | Planned |
| [`core`](/core/)             | Core Resources                            | 48                 | Low priority |
| [`dns`](/dns/)               | Domain and Zones                          | 24                 | In progress |
| [`domain`](/domain/)         | Domain Overview                           | 10                 | Low priority |
| [`etickets`](/etickets/)     | [ETickets](https://chk.me/kOM6ZoO)        | 11                 | Low priority |
| [`kchat`](/kchat/)           | [kChat](https://chk.me/sXgWvJp)           | 85                 | Low priority |
| [`kdrive`](/kdrive/)         | [kDrive](https://chk.me/qlJozmn)          | 64                 | Low priority |
| [`kmeet`](/kmeet/)           | [kMeet](https://chk.me/xgAjld6)           | 2                  | Low priority |
| [`mail`](/mail/)             | Mail Services                             | 71                 | Low priority |
| [`newsletter`](/newsletter/) | Newsletter Overview                       | 74                 | Low priority |
| [`radio`](/radio/)           | [Streaming Radio](https://chk.me/u4XqnUZ) | 85                 | Low priority |
| [`tickets`](/tickets/)       | Tickets Overview                          | 0                  | Low priority |
| [`url`](/url/)               | URL Overview                              | 4                  | Low priority |
| [`video`](/video/)           | [Streaming Video](https://chk.me/BWbluEg) | 77                 | Low priority |
| [`vod`](/vod/)               | [VOD](https://chk.me/MRAj6ne)             | 0                  | Low priority |
