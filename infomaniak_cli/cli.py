"""CLI argument parsing and entry point."""

import argparse
import sys

from infomaniak_cli import __version__
from infomaniak_cli.commands.dns import (
    cmd_dns_add,
    cmd_dns_check,
    cmd_dns_delete,
    cmd_dns_domains,
    cmd_dns_export,
    cmd_dns_import,
    cmd_dns_records,
    cmd_dns_update,
)
from infomaniak_cli.commands.mail import cmd_mail_list
from infomaniak_cli.commands.products import cmd_products
from infomaniak_cli.commands.setup import cmd_setup
from infomaniak_cli.commands.status import cmd_status
from infomaniak_cli.config import load_env_file
from infomaniak_cli.output import bold


def main():
    load_env_file()

    parser = argparse.ArgumentParser(
        prog="infomaniak",
        description="Manage Infomaniak services from the command line.",
        epilog=f"Get started: {bold('infomaniak setup')}",
    )
    parser.add_argument("--version", "-V", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(dest="service", help="Service to manage")

    # ── setup ──────────────────────────────────────────────────────────────
    sp_setup = subparsers.add_parser("setup", help="Configure your API token")
    sp_setup.set_defaults(func=cmd_setup)

    # ── dns ────────────────────────────────────────────────────────────────
    dns_parser = subparsers.add_parser("dns", help="Manage DNS records and domains")
    dns_sub = dns_parser.add_subparsers(dest="command")

    # dns domains
    sp = dns_sub.add_parser("domains", help="List all domains on your account")
    sp.add_argument("--json", action="store_true", help="Output as JSON")
    sp.set_defaults(func=cmd_dns_domains)

    # dns records
    sp = dns_sub.add_parser("records", help="List DNS records for a domain")
    sp.add_argument("domain", help="Domain name (e.g. example.com)")
    sp.add_argument("--type", "-t", help="Filter by record type (A, AAAA, CNAME, MX, TXT, etc.)")
    sp.add_argument("--json", action="store_true", help="Output as JSON")
    sp.set_defaults(func=cmd_dns_records)

    # dns check
    sp = dns_sub.add_parser("check", help="Check if a DNS record resolves correctly")
    sp.add_argument("domain", help="Domain name")
    sp.add_argument("record_id", help="Record ID to check")
    sp.add_argument("--json", action="store_true", help="Output as JSON")
    sp.set_defaults(func=cmd_dns_check)

    # dns add
    sp = dns_sub.add_parser("add", help="Create a DNS record")
    sp.add_argument("domain", help="Domain name (e.g. example.com)")
    sp.add_argument("type", help="Record type (A, AAAA, CNAME, MX, TXT, SRV, NS)")
    sp.add_argument("source", help="Record name (e.g. 'www', 'api', '@' for root)")
    sp.add_argument("target", help="Record value (e.g. IP address, hostname)")
    sp.add_argument("--ttl", type=int, default=3600, help="TTL in seconds (default: 3600)")
    sp.add_argument("--json", action="store_true", help="Output as JSON")
    sp.set_defaults(func=cmd_dns_add)

    # dns update
    sp = dns_sub.add_parser("update", help="Update a DNS record")
    sp.add_argument("domain", help="Domain name")
    sp.add_argument("record_id", help="Record ID to update")
    sp.add_argument("--target", help="New target value")
    sp.add_argument("--ttl", type=int, help="New TTL in seconds")
    sp.set_defaults(func=cmd_dns_update)

    # dns delete
    sp = dns_sub.add_parser("delete", help="Delete a DNS record")
    sp.add_argument("domain", help="Domain name")
    sp.add_argument("record_id", help="Record ID to delete")
    sp.add_argument("--yes", "-y", action="store_true", help="Skip confirmation")
    sp.set_defaults(func=cmd_dns_delete)

    # dns export
    sp = dns_sub.add_parser("export", help="Export DNS records as JSON or CSV")
    sp.add_argument("domain", help="Domain name")
    sp.add_argument("--format", "-f", choices=["json", "csv"], default="json", help="Output format (default: json)")
    sp.add_argument("--output", "-o", help="Output file path (default: stdout)")
    sp.set_defaults(func=cmd_dns_export)

    # dns import
    sp = dns_sub.add_parser("import", help="Import DNS records from JSON or CSV file")
    sp.add_argument("domain", help="Domain name")
    sp.add_argument("file", help="Path to JSON or CSV file")
    sp.add_argument("--yes", "-y", action="store_true", help="Skip confirmation")
    sp.set_defaults(func=cmd_dns_import)

    # ── products ───────────────────────────────────────────────────────────
    sp_products = subparsers.add_parser("products", help="List all products on your account")
    sp_products.add_argument("--type", "-t", dest="service_filter", help="Filter by service type (e.g. domain, email_hosting)")
    sp_products.add_argument("--json", action="store_true", help="Output as JSON")
    sp_products.set_defaults(func=cmd_products)

    # ── mail ───────────────────────────────────────────────────────────────
    mail_parser = subparsers.add_parser("mail", help="Manage mail services")
    mail_sub = mail_parser.add_subparsers(dest="command")

    sp = mail_sub.add_parser("list", help="List mail hosting services")
    sp.add_argument("--json", action="store_true", help="Output as JSON")
    sp.set_defaults(func=cmd_mail_list)

    # ── status ─────────────────────────────────────────────────────────────
    sp_status = subparsers.add_parser("status", help="Service status overview")
    sp_status.add_argument("--json", action="store_true", help="Output as JSON")
    sp_status.set_defaults(func=cmd_status)

    args = parser.parse_args()

    if not args.service:
        parser.print_help()
        sys.exit(1)

    if args.service == "dns" and not getattr(args, "command", None):
        dns_parser.print_help()
        sys.exit(1)

    if args.service == "mail" and not getattr(args, "command", None):
        mail_parser.print_help()
        sys.exit(1)

    args.func(args)
