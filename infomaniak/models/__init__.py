"""SDK models."""

from infomaniak.models.dns import DNSZone, DNSRecord
from infomaniak.models.cloud import (PublicCloudProject, PublicCloudProjectTag,
                                     PublicCloudProjectListResponse,
                                     CreatePublicCloudProjectResponse)
from infomaniak.models.backup import (BackupSlot, BackupProduct,
                                      BackupBillingPlan)
from infomaniak.models.domain import Domain, DomainListResponse
from infomaniak.models.core.user import (AccountInvitation,
                                         AccountInvitationTeam)
from infomaniak.models.newsletter import NewsletterBulkResponse
