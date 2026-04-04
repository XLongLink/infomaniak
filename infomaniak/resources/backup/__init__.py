from .slots import Slots, AsyncSlots
from .billing import Billing, AsyncBilling
from .product import Product, AsyncProduct
from .passwords import Passwords, AsyncPasswords
from .administrator import Administrator, AsyncAdministrator
from infomaniak.resource import Resouce, AsyncResource


class Backup(Resouce):
    """Swiss Backup resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.product = Product(client)
        self.slots = Slots(client)
        self.administrator = Administrator(client)
        self.passwords = Passwords(client)
        self.billing = Billing(client)


class AsyncBackup(AsyncResource):
    """Async Swiss Backup resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.product = AsyncProduct(client)
        self.slots = AsyncSlots(client)
        self.administrator = AsyncAdministrator(client)
        self.passwords = AsyncPasswords(client)
        self.billing = AsyncBilling(client)


__all__ = [
    "Backup",
    "AsyncBackup",
    "Product",
    "AsyncProduct",
    "Slots",
    "AsyncSlots",
    "Administrator",
    "AsyncAdministrator",
    "Passwords",
    "AsyncPasswords",
    "Billing",
    "AsyncBilling",
]
