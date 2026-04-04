"""Top-level SDK resource groups."""

from infomaniak.resources.backup import AsyncBackup, Backup
from infomaniak.resources.cloud import AsyncCloud, Cloud
from infomaniak.resources.core import AsyncCore, Core
from infomaniak.resources.dns import AsyncDNS, DNS
from infomaniak.resources.domain import AsyncDomain, Domain
from infomaniak.resources.etickets import AsyncEtickets, Etickets
from infomaniak.resources.kchat import AsyncKchat, Kchat
from infomaniak.resources.kdrive import AsyncKdrive, Kdrive
from infomaniak.resources.kmeet import AsyncKmeet, Kmeet
from infomaniak.resources.mail import AsyncMail, Mail
from infomaniak.resources.newsletter import AsyncNewsletter, Newsletter
from infomaniak.resources.radio import AsyncRadio, Radio
from infomaniak.resources.url import AsyncUrl, Url
from infomaniak.resources.video import AsyncVideo, Video

__all__ = [
    "AsyncBackup",
    "Backup",
    "AsyncCloud",
    "Cloud",
    "AsyncCore",
    "Core",
    "AsyncDNS",
    "DNS",
    "AsyncDomain",
    "Domain",
    "AsyncEtickets",
    "Etickets",
    "AsyncKchat",
    "Kchat",
    "AsyncKdrive",
    "Kdrive",
    "AsyncKmeet",
    "Kmeet",
    "AsyncMail",
    "Mail",
    "AsyncNewsletter",
    "Newsletter",
    "AsyncRadio",
    "Radio",
    "AsyncUrl",
    "Url",
    "AsyncVideo",
    "Video",
]
