from infomaniak.resource import AsyncResource, Resouce


class ProductOptions(Resouce):
    """Radio product options endpoints."""

    def list(self) -> None:
        """List options specific to a radio product."""
        raise NotImplementedError("Radio.product_options.list is not implemented yet.")


class AsyncProductOptions(AsyncResource):
    """Async radio product options endpoints."""

    async def list(self) -> None:
        """List options specific to a radio product."""
        raise NotImplementedError("AsyncRadio.product_options.list is not implemented yet.")
