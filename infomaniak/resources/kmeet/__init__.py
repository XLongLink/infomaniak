from .plan import Plan, AsyncPlan
from .room import Room, AsyncRoom
from infomaniak.resource import Resouce, AsyncResource


class Kmeet(Resouce):
    """kMeet resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.plan = Plan(client)
        self.room = Room(client)


class AsyncKmeet(AsyncResource):
    """Async kMeet resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.plan = AsyncPlan(client)
        self.room = AsyncRoom(client)
