from .user import User, AsyncUser
from .tasks import Tasks, AsyncTasks
from .events import Events, AsyncEvents
from .ksuite import Ksuite, AsyncKsuite
from .actions import Actions, AsyncActions
from .profile import Profile, AsyncProfile
from .products import Products, AsyncProducts
from .countries import Countries, AsyncCountries
from .languages import Languages, AsyncLanguages
from .timezones import Timezones, AsyncTimezones
from infomaniak.resource import Resouce, AsyncResource


class Core(Resouce):
    """Core resources for Infomaniak services."""

    def __init__(self, client):
        super().__init__(client)
        self.actions = Actions(client)
        self.countries = Countries(client)
        self.events = Events(client)
        self.ksuite = Ksuite(client)
        self.languages = Languages(client)
        self.products = Products(client)
        self.profile = Profile(client)
        self.tasks = Tasks(client)
        self.timezones = Timezones(client)
        self.user = User(client)


class AsyncCore(AsyncResource):
    """Async core resources for Infomaniak services."""

    def __init__(self, client):
        super().__init__(client)
        self.actions = AsyncActions(client)
        self.countries = AsyncCountries(client)
        self.events = AsyncEvents(client)
        self.ksuite = AsyncKsuite(client)
        self.languages = AsyncLanguages(client)
        self.products = AsyncProducts(client)
        self.profile = AsyncProfile(client)
        self.tasks = AsyncTasks(client)
        self.timezones = AsyncTimezones(client)
        self.user = AsyncUser(client)
