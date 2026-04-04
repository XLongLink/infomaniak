from .fields import Fields, AsyncFields
from .groups import Groups, AsyncGroups
from .credits import Credits, AsyncCredits
from .domains import Domains, AsyncDomains
from .segments import Segments, AsyncSegments
from .webforms import Webforms, AsyncWebforms
from .campaigns import Campaigns, AsyncCampaigns
from .dashboard import Dashboard, AsyncDashboard
from .templates import Templates, AsyncTemplates
from .operations import Operations, AsyncOperations
from .subscribers import Subscribers, AsyncSubscribers
from infomaniak.resource import Resouce, AsyncResource


class Newsletter(Resouce):
    """Newsletter resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.campaigns = Campaigns(client)
        self.credits = Credits(client)
        self.dashboard = Dashboard(client)
        self.domains = Domains(client)
        self.fields = Fields(client)
        self.groups = Groups(client)
        self.operations = Operations(client)
        self.segments = Segments(client)
        self.subscribers = Subscribers(client)
        self.templates = Templates(client)
        self.webforms = Webforms(client)


class AsyncNewsletter(AsyncResource):
    """Async newsletter resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.campaigns = AsyncCampaigns(client)
        self.credits = AsyncCredits(client)
        self.dashboard = AsyncDashboard(client)
        self.domains = AsyncDomains(client)
        self.fields = AsyncFields(client)
        self.groups = AsyncGroups(client)
        self.operations = AsyncOperations(client)
        self.segments = AsyncSegments(client)
        self.subscribers = AsyncSubscribers(client)
        self.templates = AsyncTemplates(client)
        self.webforms = AsyncWebforms(client)
