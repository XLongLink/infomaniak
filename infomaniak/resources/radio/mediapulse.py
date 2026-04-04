from infomaniak.resource import Resouce, AsyncResource


class Mediapulse(Resouce):
    """Radio Mediapulse endpoints."""

    def export_log(self) -> None:
        """Export a log file in Mediapulse format."""
        raise NotImplementedError("Radio.mediapulse.export_log is not implemented yet.")

    def is_export_log_available(self) -> None:
        """Check whether an export log is available."""
        raise NotImplementedError("Radio.mediapulse.is_export_log_available is not implemented yet.")

    def report_station(self) -> None:
        """Generate a Mediapulse report for a specific station."""
        raise NotImplementedError("Radio.mediapulse.report_station is not implemented yet.")

    def report(self) -> None:
        """Generate a Mediapulse report for all stations in a product."""
        raise NotImplementedError("Radio.mediapulse.report is not implemented yet.")


class AsyncMediapulse(AsyncResource):
    """Async radio Mediapulse endpoints."""

    async def export_log(self) -> None:
        """Export a log file in Mediapulse format."""
        raise NotImplementedError("AsyncRadio.mediapulse.export_log is not implemented yet.")

    async def is_export_log_available(self) -> None:
        """Check whether an export log is available."""
        raise NotImplementedError("AsyncRadio.mediapulse.is_export_log_available is not implemented yet.")

    async def report_station(self) -> None:
        """Generate a Mediapulse report for a specific station."""
        raise NotImplementedError("AsyncRadio.mediapulse.report_station is not implemented yet.")

    async def report(self) -> None:
        """Generate a Mediapulse report for all stations in a product."""
        raise NotImplementedError("AsyncRadio.mediapulse.report is not implemented yet.")
