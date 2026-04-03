from infomaniak.resource import AsyncResource, Resouce


class Notifications(Resouce):
    """Radio notifications endpoints."""

    def get_station(self) -> None:
        """Get station-level notification settings."""
        raise NotImplementedError("Radio.notifications.get_station is not implemented yet.")

    def update_station(self) -> None:
        """Update station-level notification settings."""
        raise NotImplementedError("Radio.notifications.update_station is not implemented yet.")

    def get_product(self) -> None:
        """Get product-level notification settings."""
        raise NotImplementedError("Radio.notifications.get_product is not implemented yet.")

    def update_product(self) -> None:
        """Update product-level notification settings."""
        raise NotImplementedError("Radio.notifications.update_product is not implemented yet.")


class AsyncNotifications(AsyncResource):
    """Async radio notifications endpoints."""

    async def get_station(self) -> None:
        """Get station-level notification settings."""
        raise NotImplementedError("AsyncRadio.notifications.get_station is not implemented yet.")

    async def update_station(self) -> None:
        """Update station-level notification settings."""
        raise NotImplementedError("AsyncRadio.notifications.update_station is not implemented yet.")

    async def get_product(self) -> None:
        """Get product-level notification settings."""
        raise NotImplementedError("AsyncRadio.notifications.get_product is not implemented yet.")

    async def update_product(self) -> None:
        """Update product-level notification settings."""
        raise NotImplementedError("AsyncRadio.notifications.update_product is not implemented yet.")
