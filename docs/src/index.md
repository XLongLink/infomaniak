# Overview

Welcome to the **Infomaniak SDK for Python** documentation.

Use the sidebar to navigate by API domain. Each section mirrors the SDK resource tree under `infomaniak/resources` so you can quickly map documentation pages to SDK entry points.

## Getting started

```py
from infomaniak import Client

client = Client(token="<your-api-token>")
core = client.core
```

## Available API domains

- AI
- Backup
- Cloud
- Core
- DNS
- kChat
- kDrive
- kMeet
- Mail
- Newsletter
- Radio
- Tickets
- URL
- Video
- VOD

::: tip
Looking for a specific endpoint? Open the related domain in the sidebar and start from its **Overview** page.
:::


## SDK function coverage

| Resource methods | Api Reference | Implemented |
|---|---|---|
| [`backup.administrator.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/administrator.py) |  | ❌ |
| [`backup.administrator.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/administrator.py) |  | ❌ |
| [`backup.billing.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/billing.py) |  | ❌ |
| [`backup.passwords.administrator`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/passwords.py) |  | ❌ |
| [`backup.passwords.slot`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/passwords.py) |  | ❌ |
| [`backup.product.acronis`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/product.py) |  | ❌ |
| [`backup.product.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/product.py) |  | ❌ |
| [`backup.product.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/product.py) |  | ❌ |
| [`backup.product.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/product.py) |  | ❌ |
| [`backup.slots.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/slots.py) |  | ❌ |
| [`backup.slots.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/slots.py) |  | ❌ |
| [`backup.slots.disable`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/slots.py) |  | ❌ |
| [`backup.slots.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/slots.py) |  | ❌ |
| [`backup.slots.enable`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/slots.py) |  | ❌ |
| [`backup.slots.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/slots.py) |  | ❌ |
| [`backup.slots.rclone`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/slots.py) |  | ❌ |
| [`backup.slots.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/backup/slots.py) |  | ❌ |
| [`cloud.database.backups.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py) |  | ❌ |
| [`cloud.database.backups.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py) |  | ❌ |
| [`cloud.database.backups.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py) |  | ❌ |
| [`cloud.database.config.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.config.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.config.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.config.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.config.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.data.packs`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py) |  | ❌ |
| [`cloud.database.data.regions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py) |  | ❌ |
| [`cloud.database.data.types`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py) |  | ❌ |
| [`cloud.database.ip.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py) |  | ❌ |
| [`cloud.database.ip.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py) |  | ❌ |
| [`cloud.database.ip.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py) |  | ❌ |
| [`cloud.database.restore.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/restore.py) |  | ❌ |
| [`cloud.database.restore.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/restore.py) |  | ❌ |
| [`cloud.database.scheduled.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.database.scheduled.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.database.scheduled.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.database.scheduled.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.database.scheduled.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.kubernetes.data.flavors`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.data.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.data.reagions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ✅ |
| [`cloud.kubernetes.data.regions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.data.versions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.data.zones`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.ip.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py) |  | ❌ |
| [`cloud.kubernetes.ip.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py) |  | ❌ |
| [`cloud.kubernetes.ip.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py) |  | ❌ |
| [`cloud.kubernetes.ip.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py) |  | ❌ |
| [`cloud.kubernetes.pools.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`cloud.kubernetes.pools.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`cloud.kubernetes.pools.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`cloud.kubernetes.pools.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`cloud.kubernetes.pools.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`core.actions.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/actions.py) |  | ❌ |
| [`core.countries.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/countries.py) |  | ❌ |
| [`core.countries.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/countries.py) |  | ❌ |
| [`core.events.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/events.py) |  | ❌ |
| [`core.events.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/events.py) |  | ❌ |
| [`core.ksuite.mailbox.attach`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.ksuite.mailbox.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.ksuite.mailbox.password`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.ksuite.mailbox.primary`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.ksuite.mailbox.unlink`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.languages.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/languages.py) |  | ❌ |
| [`core.languages.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/languages.py) |  | ❌ |
| [`core.products.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/products.py) |  | ❌ |
| [`core.profile.avatar.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/avatar.py) |  | ❌ |
| [`core.profile.avatar.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/avatar.py) |  | ❌ |
| [`core.profile.email.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py) |  | ❌ |
| [`core.profile.email.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py) |  | ❌ |
| [`core.profile.email.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py) |  | ❌ |
| [`core.profile.info.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/info.py) |  | ❌ |
| [`core.profile.info.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/info.py) |  | ❌ |
| [`core.profile.password.add`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py) |  | ❌ |
| [`core.profile.password.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py) |  | ❌ |
| [`core.profile.password.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py) |  | ❌ |
| [`core.profile.phone.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py) |  | ❌ |
| [`core.profile.phone.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py) |  | ❌ |
| [`core.profile.phone.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py) |  | ❌ |
| [`core.tasks.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/tasks.py) |  | ❌ |
| [`core.tasks.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/tasks.py) |  | ❌ |
| [`core.timezones.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/timezones.py) |  | ❌ |
| [`core.timezones.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/timezones.py) |  | ❌ |
| [`core.user.accounts.apps`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.products`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.services`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.tags`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.teams`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.users`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.teams.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`core.user.teams.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`core.user.teams.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`core.user.teams.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`core.user.teams.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`domain.dnssec.check`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/dnssec.py) |  | ❌ |
| [`domain.dnssec.disable`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/dnssec.py) |  | ❌ |
| [`domain.dnssec.enable`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/dnssec.py) |  | ❌ |
| [`domain.nameservers.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/nameservers.py) |  | ❌ |
| [`domain.order.check`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/order.py) |  | ❌ |
| [`domain.order.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/order.py) |  | ❌ |
| [`domain.order.transfer`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/order.py) |  | ❌ |
| [`domain.zone.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/zone.py) |  | ❌ |
| [`kchat.bots.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/bots.py) |  | ❌ |
| [`kchat.bots.disable`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/bots.py) |  | ❌ |
| [`kchat.bots.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/bots.py) |  | ❌ |
| [`kchat.bots.enable`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/bots.py) |  | ❌ |
| [`kchat.bots.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/bots.py) |  | ❌ |
| [`kchat.bots.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/bots.py) |  | ❌ |
| [`kchat.channels.add`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.all`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.autocomplete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.autocomplete_search`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.by_ids`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.by_name`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.by_name_and_team_name`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.create_direct_message`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.create_group_message`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.deleted`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.for_user`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.memberships_and_roles`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.move`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.patch`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.pinned_posts`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.private`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.public`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.restore`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.search`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.search_all`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.search_archived`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.search_group`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.set`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.stats`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.unread_messages`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.channels.view`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.commands.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/commands.py) |  | ❌ |
| [`kchat.emoji.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/emoji.py) |  | ❌ |
| [`kchat.files.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/files.py) |  | ❌ |
| [`kchat.files.metadata`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/files.py) |  | ❌ |
| [`kchat.files.preview`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/files.py) |  | ❌ |
| [`kchat.files.thumbnail`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/files.py) |  | ❌ |
| [`kchat.files.upload`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/files.py) |  | ❌ |
| [`kchat.groups.channel_groups`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/groups.py) |  | ❌ |
| [`kchat.groups.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/groups.py) |  | ❌ |
| [`kchat.groups.team_channel_groups`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/groups.py) |  | ❌ |
| [`kchat.groups.team_groups`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/groups.py) |  | ❌ |
| [`kchat.groups.user_groups`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/groups.py) |  | ❌ |
| [`kchat.insights.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/insights.py) |  | ❌ |
| [`kchat.posts.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/posts.py) |  | ❌ |
| [`kchat.preferences.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/preferences.py) |  | ❌ |
| [`kchat.reactions.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/reactions.py) |  | ❌ |
| [`kchat.roles.by_name`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/roles.py) |  | ❌ |
| [`kchat.roles.by_names`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/roles.py) |  | ❌ |
| [`kchat.roles.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/roles.py) |  | ❌ |
| [`kchat.roles.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/roles.py) |  | ❌ |
| [`kchat.status.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/status.py) |  | ❌ |
| [`kchat.system.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/system.py) |  | ❌ |
| [`kchat.teams.by_ids`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.by_name`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.for_user`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.invite_guests`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.search`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.stats`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.teams.user_teams`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.threads.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/threads.py) |  | ❌ |
| [`kchat.users.autocomplete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.by_group_channels_ids`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.by_ids`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.by_usernames`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.default`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.patch`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.publish`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.search`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.users.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.webhooks.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/webhooks.py) |  | ❌ |
| [`kmeet.plan.plan_a_conference`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kmeet/plan.py) |  | ❌ |
| [`kmeet.room.get_room_settings`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kmeet/room.py) |  | ❌ |
| [`newsletter.campaigns.template.test`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/campaigns/template.py) |  | ❌ |
| [`newsletter.credits.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/credits.py) |  | ❌ |
| [`newsletter.credits.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/credits.py) |  | ❌ |
| [`newsletter.dashboard.campaigns_statistics`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/dashboard.py) |  | ❌ |
| [`newsletter.dashboard.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/dashboard.py) |  | ❌ |
| [`newsletter.dashboard.latest_campaigns`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/dashboard.py) |  | ❌ |
| [`newsletter.dashboard.monthly_campaigns_statistics`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/dashboard.py) |  | ❌ |
| [`newsletter.dashboard.subscribers_statistics`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/dashboard.py) |  | ❌ |
| [`newsletter.domains.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/domains.py) |  | ❌ |
| [`newsletter.domains.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/domains.py) |  | ❌ |
| [`newsletter.fields.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/fields.py) |  | ❌ |
| [`newsletter.fields.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/fields.py) |  | ❌ |
| [`newsletter.fields.delete_bulk`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/fields.py) |  | ❌ |
| [`newsletter.fields.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/fields.py) |  | ❌ |
| [`newsletter.fields.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/fields.py) |  | ❌ |
| [`newsletter.groups.subscribers.assign`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/groups/subscribers.py) |  | ❌ |
| [`newsletter.groups.subscribers.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/groups/subscribers.py) |  | ❌ |
| [`newsletter.groups.subscribers.unassign`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/groups/subscribers.py) |  | ❌ |
| [`newsletter.operations.cancel`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/operations.py) |  | ❌ |
| [`newsletter.segments.subscribers.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/segments/subscribers.py) |  | ❌ |
| [`newsletter.subscribers.addressbooks.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/subscribers/addressbooks.py) |  | ❌ |
| [`newsletter.subscribers.addressbooks.select`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/subscribers/addressbooks.py) |  | ❌ |
| [`newsletter.templates.thumbnail.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/templates/thumbnail.py) |  | ❌ |
| [`newsletter.webforms.fields.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/webforms/fields.py) |  | ❌ |
| [`newsletter.webforms.themes.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/newsletter/webforms/themes.py) |  | ❌ |
| [`radio.autodj.events.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/events.py) |  | ❌ |
| [`radio.autodj.events.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/events.py) |  | ❌ |
| [`radio.autodj.events.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/events.py) |  | ❌ |
| [`radio.autodj.events.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/events.py) |  | ❌ |
| [`radio.autodj.events.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/events.py) |  | ❌ |
| [`radio.autodj.media.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/media.py) |  | ❌ |
| [`radio.autodj.media.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/media.py) |  | ❌ |
| [`radio.autodj.media.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/media.py) |  | ❌ |
| [`radio.autodj.media.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/media.py) |  | ❌ |
| [`radio.autodj.media.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/media.py) |  | ❌ |
| [`radio.autodj.playing_playlist.generate`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playing_playlist.py) |  | ❌ |
| [`radio.autodj.playing_playlist.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playing_playlist.py) |  | ❌ |
| [`radio.autodj.playing_playlist.insert`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playing_playlist.py) |  | ❌ |
| [`radio.autodj.playing_playlist.move`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playing_playlist.py) |  | ❌ |
| [`radio.autodj.playing_playlist.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playing_playlist.py) |  | ❌ |
| [`radio.autodj.playlists.attach_media`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playlists.py) |  | ❌ |
| [`radio.autodj.playlists.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playlists.py) |  | ❌ |
| [`radio.autodj.playlists.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playlists.py) |  | ❌ |
| [`radio.autodj.playlists.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playlists.py) |  | ❌ |
| [`radio.autodj.playlists.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playlists.py) |  | ❌ |
| [`radio.autodj.playlists.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/autodj/playlists.py) |  | ❌ |
| [`radio.encoder_events.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/encoder_events.py) |  | ❌ |
| [`radio.hls_stream.add`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/hls_stream.py) |  | ❌ |
| [`radio.hls_stream.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/hls_stream.py) |  | ❌ |
| [`radio.hls_stream.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/hls_stream.py) |  | ❌ |
| [`radio.hls_stream.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/hls_stream.py) |  | ❌ |
| [`radio.mediapulse.export_log`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/mediapulse.py) |  | ❌ |
| [`radio.mediapulse.is_export_log_available`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/mediapulse.py) |  | ❌ |
| [`radio.mediapulse.report`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/mediapulse.py) |  | ❌ |
| [`radio.mediapulse.report_station`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/mediapulse.py) |  | ❌ |
| [`radio.notifications.get_product`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/notifications.py) |  | ❌ |
| [`radio.notifications.get_station`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/notifications.py) |  | ❌ |
| [`radio.notifications.update_product`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/notifications.py) |  | ❌ |
| [`radio.notifications.update_station`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/notifications.py) |  | ❌ |
| [`radio.options.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/options.py) |  | ❌ |
| [`radio.packs.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/packs.py) |  | ❌ |
| [`radio.players.config.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/players/config.py) |  | ❌ |
| [`radio.players.config.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/players/config.py) |  | ❌ |
| [`radio.players.thumbnail.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/players/thumbnail.py) |  | ❌ |
| [`radio.players.thumbnail.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/players/thumbnail.py) |  | ❌ |
| [`radio.product_options.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/product_options.py) |  | ❌ |
| [`radio.products.conflict_restrictions.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/products/conflict_restrictions.py) |  | ❌ |
| [`radio.products.restrictions.set`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/products/restrictions.py) |  | ❌ |
| [`radio.products.users.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/products/users.py) |  | ❌ |
| [`radio.server_events.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/server_events.py) |  | ❌ |
| [`radio.stats.hls_stream.consumption`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.hls_stream.countries`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.hls_stream.countries_continent`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.hls_stream.export_csv`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.hls_stream.listeners`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.hls_stream.listeners_per_minute`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.hls_stream.players`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.hls_stream.total_consumption`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.hls_stream.total_players`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/hls_stream.py) |  | ❌ |
| [`radio.stats.product.consumption`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.countries`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.countries_continent`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.export_csv`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.export_csv_by_station`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.listeners`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.listeners_per_minute`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.listeners_per_minute_grouped`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.players`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.station_consumption`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.station_listeners`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.stats_by_station`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.total_consumption`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`radio.stats.product.total_players`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/radio/stats/product.py) |  | ❌ |
| [`url.short.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/url/short.py) |  | ❌ |
| [`url.short.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/url/short.py) |  | ❌ |
| [`url.short.quota`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/url/short.py) |  | ❌ |
| [`url.short.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/url/short.py) |  | ❌ |