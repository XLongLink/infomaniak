# Cloud Projects

The `cloud.projects` resource manages Public Cloud projects.

## Create Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `project_name`: Name for the new project.
- `user_password`: Password for the default project user.
- `user_description`: Optional description for the default project user.
- `user_email`: Optional email for the default project user.

```py
from infomaniak import Client
from infomaniak.models.cloud import CreatePublicCloudProjectResponse

client = Client(token="<token>")
created: CreatePublicCloudProjectResponse = client.cloud.projects.create(
    public_cloud_id=64258,
    project_name="MyProject",
    user_password="Example123",
)
```

`CreatePublicCloudProjectResponse`:

- `data`: Created project action payload.
- `result`: API operation status.

## Create Project with Invitation

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `project_name`: Name for the new project.
- `user_email`: Email address that receives the invitation.
- `user_description`: Optional description for the invited user.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProjectInvitationResponse

client = Client(token="<token>")
invited: PublicCloudProjectInvitationResponse = client.cloud.projects.create_with_invitation(
    public_cloud_id=64258,
    project_name="MyProject",
    user_email="user@example.com",
)
```

`PublicCloudProjectInvitationResponse`:

- `data`: Invitation payload.
- `result`: API operation status.

## Update Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to update.
- `name`: New project name (maximum `250` characters).

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProjectAsyncActionResponse

client = Client(token="<token>")
updated: PublicCloudProjectAsyncActionResponse = client.cloud.projects.update(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
    name="RenamedProject",
)
```

`PublicCloudProjectAsyncActionResponse`:

- `data`: Asynchronous action payload.
- `result`: API operation status.

## Delete Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to delete.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProjectAsyncActionResponse

client = Client(token="<token>")
removed: PublicCloudProjectAsyncActionResponse = client.cloud.projects.delete(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
)
```

`PublicCloudProjectAsyncActionResponse`:

- `data`: Asynchronous action payload.
- `result`: API operation status.

## List Projects

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `with_`: Optional response expansions.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProjectListResponse

client = Client(token="<token>")
projects: PublicCloudProjectListResponse = client.cloud.projects.list(public_cloud_id=64258)
```

`PublicCloudProjectListResponse`:

- `data`: List of projects.
- `result`: API operation status.

## Get Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to retrieve.
- `with_`: Optional response expansions.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProject

client = Client(token="<token>")
project: PublicCloudProject = client.cloud.projects.get(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
)
```

`PublicCloudProject`:

- `id`: Project identifier.
- `name`: Project name.
- `status`: Project status.
- `region`: Project region.
