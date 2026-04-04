from infomaniak.resource import AsyncResource, Resouce


class Customers(Resouce):
    """eTickets customers endpoints."""

    def logs(self, customer_id: int) -> None:
        """List email logs for a specific customer (GET /2/etickets/customers/{customer_id}/logs)."""
        raise NotImplementedError("Etickets.customers.logs is not implemented yet.")


class AsyncCustomers(AsyncResource):
    """Async eTickets customers endpoints."""

    async def logs(self, customer_id: int) -> None:
        """List email logs for a specific customer (GET /2/etickets/customers/{customer_id}/logs)."""
        raise NotImplementedError("AsyncEtickets.customers.logs is not implemented yet.")
