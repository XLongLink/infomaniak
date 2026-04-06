# Core Actions

The `core.actions` resource lets you list all available API action types.

## List Actions

- `search`: Optional search string used to filter action codes.

```py
from infomaniak import Client
from infomaniak.models import Action

client = Client()
actions: list[Action] = client.core.actions.list(search="example")
```

`list[Action]`:

- `id`: Unique identifier of the action.
- `code`: Action code.
- `description`: Action description.
