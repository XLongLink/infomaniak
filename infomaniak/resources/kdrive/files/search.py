from infomaniak.resource import AsyncResource, Resouce


class Search(Resouce):
    """kDrive resource for file search endpoints."""

    def exists(self) -> None:
        """Check file existence."""
        raise NotImplementedError("kDrive files.search.exists endpoint is not implemented yet.")

    def largest(self) -> None:
        """Get largest files in drive."""
        raise NotImplementedError("kDrive files.search.largest endpoint is not implemented yet.")

    def last_modified(self) -> None:
        """Get last modified files."""
        raise NotImplementedError("kDrive files.search.last_modified endpoint is not implemented yet.")

    def most_versioned(self) -> None:
        """Get most versioned files."""
        raise NotImplementedError("kDrive files.search.most_versioned endpoint is not implemented yet.")

    def my_shared(self) -> None:
        """Get files shared by the current user."""
        raise NotImplementedError("kDrive files.search.my_shared endpoint is not implemented yet.")

    def shared(self) -> None:
        """Get files shared with the current user."""
        raise NotImplementedError("kDrive files.search.shared endpoint is not implemented yet.")

    def create_team_directory(self) -> None:
        """Create a team directory."""
        raise NotImplementedError("kDrive files.search.create_team_directory endpoint is not implemented yet.")

    def recent(self) -> None:
        """List recently used files and directories."""
        raise NotImplementedError("kDrive files.search.recent endpoint is not implemented yet.")


class AsyncSearch(AsyncResource):
    """Async kDrive resource for file search endpoints."""

    async def exists(self) -> None:
        """Check file existence."""
        raise NotImplementedError("kDrive files.search.exists endpoint is not implemented yet.")

    async def largest(self) -> None:
        """Get largest files in drive."""
        raise NotImplementedError("kDrive files.search.largest endpoint is not implemented yet.")

    async def last_modified(self) -> None:
        """Get last modified files."""
        raise NotImplementedError("kDrive files.search.last_modified endpoint is not implemented yet.")

    async def most_versioned(self) -> None:
        """Get most versioned files."""
        raise NotImplementedError("kDrive files.search.most_versioned endpoint is not implemented yet.")

    async def my_shared(self) -> None:
        """Get files shared by the current user."""
        raise NotImplementedError("kDrive files.search.my_shared endpoint is not implemented yet.")

    async def shared(self) -> None:
        """Get files shared with the current user."""
        raise NotImplementedError("kDrive files.search.shared endpoint is not implemented yet.")

    async def create_team_directory(self) -> None:
        """Create a team directory."""
        raise NotImplementedError("kDrive files.search.create_team_directory endpoint is not implemented yet.")

    async def recent(self) -> None:
        """List recently used files and directories."""
        raise NotImplementedError("kDrive files.search.recent endpoint is not implemented yet.")
