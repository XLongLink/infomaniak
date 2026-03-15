"""
infomaniak — CLI for managing Infomaniak services.

Usage:
    infomaniak setup                                         # Configure your API token
    infomaniak dns domains                                   # List all domains
    infomaniak dns records <domain>                          # List DNS records
    infomaniak dns check <domain> <record_id>                # Check record health
    infomaniak dns add <domain> <type> <source> <target>     # Create record
    infomaniak dns update <domain> <record_id> --target X    # Update record
    infomaniak dns delete <domain> <record_id>               # Delete record
    infomaniak dns export <domain>                           # Export records as JSON
    infomaniak dns import <domain> <file>                    # Import records from JSON
    infomaniak dns diff <domain> <file>                       # Compare live vs file
    infomaniak dns clone <source> <target>                   # Clone records between domains
    infomaniak products [--type <name>]                      # List all products
    infomaniak mail list                                     # List mail hostings
    infomaniak status                                        # Service status overview
    infomaniak config show                                   # Show configuration
"""

__version__ = "0.5.0"
API_BASE = "https://api.infomaniak.com"
