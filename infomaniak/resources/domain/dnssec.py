from infomaniak.resource import AsyncResource, Resouce


class DNSSEC(Resouce):
    """Domain DNSSEC endpoints."""

    def check(self) -> None:
        """Check DNSSEC status for a domain."""
        raise NotImplementedError("Domain.dnssec.check is not implemented yet.")

    def enable(self) -> None:
        """Enable DNSSEC for a domain."""
        raise NotImplementedError("Domain.dnssec.enable is not implemented yet.")

    def disable(self) -> None:
        """Disable DNSSEC for a domain."""
        raise NotImplementedError("Domain.dnssec.disable is not implemented yet.")


class AsyncDNSSEC(AsyncResource):
    """Async domain DNSSEC endpoints."""

    async def check(self) -> None:
        """Check DNSSEC status for a domain."""
        raise NotImplementedError("AsyncDomain.dnssec.check is not implemented yet.")

    async def enable(self) -> None:
        """Enable DNSSEC for a domain."""
        raise NotImplementedError("AsyncDomain.dnssec.enable is not implemented yet.")

    async def disable(self) -> None:
        """Disable DNSSEC for a domain."""
        raise NotImplementedError("AsyncDomain.dnssec.disable is not implemented yet.")
