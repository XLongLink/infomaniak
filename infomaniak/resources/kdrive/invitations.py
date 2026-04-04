from infomaniak.resource import AsyncResource, Resouce


class Invitations(Resouce):
    """kDrive resource for invitation endpoints."""

    def list(self) -> None:
        """List invitations for a drive."""
        raise NotImplementedError("kDrive invitations.list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a drive invitation."""
        raise NotImplementedError("kDrive invitations.create endpoint is not implemented yet.")

    def display(self) -> None:
        """Get invitation details."""
        raise NotImplementedError("kDrive invitations.display endpoint is not implemented yet.")

    def update(self) -> None:
        """Update an invitation."""
        raise NotImplementedError("kDrive invitations.update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Cancel an invitation."""
        raise NotImplementedError("kDrive invitations.delete endpoint is not implemented yet.")


class AsyncInvitations(AsyncResource):
    """Async kDrive resource for invitation endpoints."""

    async def list(self) -> None:
        """List invitations for a drive."""
        raise NotImplementedError("kDrive invitations.list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a drive invitation."""
        raise NotImplementedError("kDrive invitations.create endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get invitation details."""
        raise NotImplementedError("kDrive invitations.display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update an invitation."""
        raise NotImplementedError("kDrive invitations.update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Cancel an invitation."""
        raise NotImplementedError("kDrive invitations.delete endpoint is not implemented yet.")
