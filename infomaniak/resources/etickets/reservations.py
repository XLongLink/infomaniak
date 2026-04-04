from infomaniak.resource import AsyncResource, Resouce


class Reservations(Resouce):
    """eTickets reservation endpoints."""

    def display_by_id(self, reservation_id: int) -> None:
        """Get a reservation by numeric ID (GET /2/etickets/reservation/{reservation_id})."""
        raise NotImplementedError("Etickets.reservations.display_by_id is not implemented yet.")

    def display_by_uuid(self, reservation_uuid: str) -> None:
        """Get a reservation by UUID (GET /2/etickets/reservation/{reservation_uuid})."""
        raise NotImplementedError("Etickets.reservations.display_by_uuid is not implemented yet.")


class AsyncReservations(AsyncResource):
    """Async eTickets reservation endpoints."""

    async def display_by_id(self, reservation_id: int) -> None:
        """Get a reservation by numeric ID (GET /2/etickets/reservation/{reservation_id})."""
        raise NotImplementedError("AsyncEtickets.reservations.display_by_id is not implemented yet.")

    async def display_by_uuid(self, reservation_uuid: str) -> None:
        """Get a reservation by UUID (GET /2/etickets/reservation/{reservation_uuid})."""
        raise NotImplementedError("AsyncEtickets.reservations.display_by_uuid is not implemented yet.")
