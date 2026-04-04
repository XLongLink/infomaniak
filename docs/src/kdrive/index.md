# kDrive Overview

The `kdrive` namespace groups all SDK resources related to Infomaniak kDrive.

## Resource tree

- [`drive`](/kdrive/drive)
  - [`drive.users`](/kdrive/drive/users)
- [`files`](/kdrive/files)
  - [`files.upload`](/kdrive/files/upload)
    - [`files.upload.session`](/kdrive/files/upload/session)
  - [`files.trash`](/kdrive/files/trash)
    - [`files.trash.directory`](/kdrive/files/trash/directory)
  - [`files.search`](/kdrive/files/search)
- [`invitations`](/kdrive/invitations)
- [`settings`](/kdrive/settings)
- [`statistics`](/kdrive/statistics)
- [`users`](/kdrive/users)
  - [`users.roles`](/kdrive/users/roles)

::: warning
kDrive resource methods are currently placeholders and raise `NotImplementedError`.
:::

## Usage

```py
from infomaniak import Client

client = Client(token="<access-token>")
kdrive = client.kdrive
```
