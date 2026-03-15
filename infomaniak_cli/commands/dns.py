"""DNS management commands."""

import csv
import io
import json
import sys
from pathlib import Path

from infomaniak_cli.api import api_request
from infomaniak_cli.config import get_account_id, get_token
from infomaniak_cli.output import bold, cyan, dim, green, output_json, print_table, red, yellow


def cmd_dns_domains(args):
    """List all domains on the account."""
    token = get_token()
    account_id = get_account_id(token)

    data = api_request("GET", f"/1/domain/account/{account_id}", token)
    domains = data.get("data", [])

    if getattr(args, "json", False):
        output_json(domains)

    if not domains:
        print(f"  {dim('No domains found.')}")
        return

    headers = ["ID", "Domain", "DNSSEC", "DNS@IK"]
    rows = []
    for d in domains:
        dnssec = green("yes") if d.get("has_dnssec") else dim("no")
        dns_ik = green("yes") if d.get("is_dns_managed_by_infomaniak") else dim("no")
        rows.append([
            d.get("id", "?"),
            d.get("customer_name", "?"),
            dnssec,
            dns_ik,
        ])

    print(f"\n  {bold(f'Domains ({len(rows)})')}\n")
    print_table(headers, rows)
    print()


def cmd_dns_records(args):
    """List DNS records for a domain."""
    token = get_token()
    domain = args.domain

    data = api_request("GET", f"/2/zones/{domain}/records", token)
    records = data.get("data", [])

    if args.type:
        filter_type = args.type.upper()
        records = [r for r in records if r.get("type") == filter_type]

    if getattr(args, "json", False):
        output_json(records)

    if not records:
        print(f"  {dim(f'No DNS records found for {domain}.')}")
        return

    records.sort(key=lambda r: (r.get("type", ""), r.get("source", "")))

    headers = ["ID", "Type", "Name", "Target", "TTL"]
    rows = []
    for r in records:
        source = r.get("source", "@")
        if source == ".":
            source = "@"
        target = r.get("target", "?")
        if len(str(target)) > 60:
            target = str(target)[:57] + "..."
        rows.append([
            r.get("id", "?"),
            cyan(r.get("type", "?")),
            source,
            target,
            r.get("ttl", "?"),
        ])

    type_note = f" type={args.type.upper()}" if args.type else ""
    print(f"\n  {bold(f'DNS records for {domain}')}{dim(type_note)} — {len(rows)} records\n")
    print_table(headers, rows)
    print()


def cmd_dns_check(args):
    """Check if a DNS record resolves correctly."""
    token = get_token()
    data = api_request("GET", f"/2/zones/{args.domain}/records/{args.record_id}/check", token)
    result = data.get("data", {})

    if getattr(args, "json", False):
        output_json(result)

    print(f"\n  {bold(f'DNS check for record {args.record_id} in {args.domain}')}\n")
    print(json.dumps(result, indent=2))
    print()


def cmd_dns_add(args):
    """Create a new DNS record."""
    token = get_token()

    source = args.source
    if source == "@":
        source = ""

    body = {
        "type": args.type.upper(),
        "source": source,
        "target": args.target,
        "ttl": args.ttl,
    }

    display_name = args.source if args.source != "@" else args.domain
    print(f"\n  Creating {cyan(body['type'])} record: {display_name}.{args.domain} → {body['target']} (TTL: {body['ttl']})")
    data = api_request("POST", f"/2/zones/{args.domain}/records", token, json_data=body)

    record = data.get("data", {})

    if getattr(args, "json", False):
        output_json(record)

    print(f"  {green('✓')} Created record ID: {bold(str(record.get('id')))}\n")


def cmd_dns_update(args):
    """Update an existing DNS record."""
    token = get_token()

    body = {}
    if args.target:
        body["target"] = args.target
    if args.ttl:
        body["ttl"] = args.ttl

    if not body:
        print(f"  {red('✗')} Specify at least one of --target or --ttl to update.")
        sys.exit(1)

    changes = ", ".join(f"{k}={v}" for k, v in body.items())
    print(f"\n  Updating record {args.record_id} in {args.domain}: {changes}")
    api_request("PUT", f"/2/zones/{args.domain}/records/{args.record_id}", token, json_data=body)
    print(f"  {green('✓')} Record {bold(str(args.record_id))} updated.\n")


def cmd_dns_delete(args):
    """Delete a DNS record."""
    token = get_token()

    if not args.yes:
        data = api_request("GET", f"/2/zones/{args.domain}/records", token)
        records = data.get("data", [])
        target_rec = next((r for r in records if str(r.get("id")) == str(args.record_id)), None)
        if target_rec:
            source = target_rec.get("source", "@")
            if source == ".":
                source = "@"
            print(f"\n  Record: {cyan(target_rec.get('type'))} {source} → {target_rec.get('target')}")

        confirm = input(f"  Delete record {args.record_id} from {args.domain}? [y/N] ")
        if confirm.lower() not in ("y", "yes"):
            print(f"  {dim('Aborted.')}")
            return

    api_request("DELETE", f"/2/zones/{args.domain}/records/{args.record_id}", token)
    print(f"  {green('✓')} Record {bold(str(args.record_id))} deleted from {args.domain}.\n")


def cmd_dns_export(args):
    """Export all DNS records for a domain."""
    token = get_token()
    domain = args.domain

    data = api_request("GET", f"/2/zones/{domain}/records", token)
    records = data.get("data", [])

    if not records:
        print(f"  {dim(f'No DNS records found for {domain}.')}")
        return

    export_data = []
    for r in records:
        source = r.get("source", "@")
        if source == ".":
            source = "@"
        export_data.append({
            "type": r.get("type"),
            "source": source,
            "target": r.get("target"),
            "ttl": r.get("ttl"),
            "priority": r.get("priority"),
        })

    if args.format == "csv":
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=["type", "source", "target", "ttl", "priority"])
        writer.writeheader()
        writer.writerows(export_data)
        content = output.getvalue()
    else:
        content = json.dumps(export_data, indent=2, ensure_ascii=False)

    if args.output:
        outpath = Path(args.output)
        outpath.write_text(content)
        print(f"\n  {green('✓')} Exported {len(export_data)} records to {bold(str(outpath))}\n")
    else:
        print(content)


def cmd_dns_import(args):
    """Import DNS records from a JSON or CSV file."""
    token = get_token()
    domain = args.domain
    filepath = Path(args.file)

    if not filepath.exists():
        print(f"  {red('✗')} File not found: {filepath}")
        sys.exit(1)

    content = filepath.read_text()

    # Detect format
    if filepath.suffix == ".csv":
        reader = csv.DictReader(io.StringIO(content))
        records = list(reader)
    else:
        try:
            records = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"  {red('✗')} Invalid JSON: {e}")
            sys.exit(1)

    if not records:
        print(f"  {dim('No records found in file.')}")
        return

    print(f"\n  Importing {bold(str(len(records)))} records into {bold(domain)}:\n")

    # Preview
    for r in records[:10]:
        rtype = r.get("type", "?")
        source = r.get("source", "@")
        target = r.get("target", "?")
        print(f"    {cyan(rtype):>8}  {source} → {target}")
    if len(records) > 10:
        print(f"    {dim(f'... and {len(records) - 10} more')}")

    if not args.yes:
        print()
        confirm = input(f"  Proceed? [y/N] ")
        if confirm.lower() not in ("y", "yes"):
            print(f"  {dim('Aborted.')}")
            return

    print()
    created = 0
    failed = 0
    for r in records:
        source = r.get("source", "")
        if source == "@":
            source = ""

        body = {
            "type": r.get("type", "A").upper(),
            "source": source,
            "target": r.get("target", ""),
            "ttl": int(r.get("ttl", 3600)),
        }
        priority = r.get("priority")
        if priority is not None and priority != "":
            body["priority"] = int(priority)

        try:
            api_request("POST", f"/2/zones/{domain}/records", token, json_data=body)
            print(f"  {green('✓')} {body['type']} {r.get('source', '@')} → {body['target']}")
            created += 1
        except SystemExit:
            print(f"  {red('✗')} {body['type']} {r.get('source', '@')} → {body['target']}")
            failed += 1

    print(f"\n  Done: {green(str(created))} created, {red(str(failed)) if failed else dim('0')} failed.\n")


def _normalize_record(r):
    """Normalize a record dict for comparison."""
    source = r.get("source", "@")
    if source == ".":
        source = "@"
    return {
        "type": r.get("type", "").upper(),
        "source": source,
        "target": r.get("target", ""),
        "ttl": int(r.get("ttl", 3600)),
    }


def _record_key(r):
    """Create a unique key for matching records."""
    return (r["type"], r["source"], r["target"])


def cmd_dns_diff(args):
    """Compare current DNS records against a local file."""
    token = get_token()
    domain = args.domain
    filepath = Path(args.file)

    if not filepath.exists():
        print(f"  {red('✗')} File not found: {filepath}")
        sys.exit(1)

    # Load file records
    content = filepath.read_text()
    if filepath.suffix == ".csv":
        reader = csv.DictReader(io.StringIO(content))
        file_records = [_normalize_record(r) for r in reader]
    else:
        try:
            raw = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"  {red('✗')} Invalid JSON: {e}")
            sys.exit(1)
        file_records = [_normalize_record(r) for r in raw]

    # Load live records
    data = api_request("GET", f"/2/zones/{domain}/records", token)
    live_raw = data.get("data", [])
    live_records = [_normalize_record(r) for r in live_raw]

    if getattr(args, "json", False):
        file_keys = {_record_key(r) for r in file_records}
        live_keys = {_record_key(r) for r in live_records}
        output_json({
            "only_in_file": [r for r in file_records if _record_key(r) not in live_keys],
            "only_live": [r for r in live_records if _record_key(r) not in file_keys],
            "common": len(file_keys & live_keys),
        })

    file_keys = {_record_key(r) for r in file_records}
    live_keys = {_record_key(r) for r in live_records}

    only_in_file = [r for r in file_records if _record_key(r) not in live_keys]
    only_live = [r for r in live_records if _record_key(r) not in file_keys]
    common = file_keys & live_keys

    print(f"\n  {bold(f'DNS diff for {domain}')}\n")
    print(f"  File: {filepath}")
    print(f"  Live: {len(live_records)} records, File: {len(file_records)} records\n")

    if not only_in_file and not only_live:
        print(f"  {green('✓')} No differences found ({len(common)} records match).\n")
        return

    if only_in_file:
        print(f"  {bold('In file but not live')} ({len(only_in_file)}):\n")
        for r in only_in_file:
            print(f"    {green('+')} {cyan(r['type'])}  {r['source']} → {r['target']}  (TTL: {r['ttl']})")
        print()

    if only_live:
        print(f"  {bold('Live but not in file')} ({len(only_live)}):\n")
        for r in only_live:
            print(f"    {red('-')} {cyan(r['type'])}  {r['source']} → {r['target']}  (TTL: {r['ttl']})")
        print()

    if common:
        print(f"  {dim(f'{len(common)} records match.')}\n")


def cmd_dns_clone(args):
    """Clone DNS records from one domain to another."""
    token = get_token()
    source_domain = args.source_domain
    target_domain = args.target_domain

    # Fetch source records
    data = api_request("GET", f"/2/zones/{source_domain}/records", token)
    source_records = data.get("data", [])

    if not source_records:
        print(f"  {dim(f'No DNS records found for {source_domain}.')}")
        return

    # Filter out NS and SOA records (shouldn't be cloned)
    skip_types = {"NS", "SOA"}
    records_to_clone = []
    for r in source_records:
        rtype = r.get("type", "").upper()
        if rtype in skip_types:
            continue
        source = r.get("source", "@")
        if source == ".":
            source = "@"
        records_to_clone.append({
            "type": rtype,
            "source": source,
            "target": r.get("target", ""),
            "ttl": r.get("ttl", 3600),
            "priority": r.get("priority"),
        })

    print(f"\n  Cloning {bold(str(len(records_to_clone)))} records from {bold(source_domain)} → {bold(target_domain)}")
    print(f"  {dim(f'Skipping NS/SOA records')}\n")

    for r in records_to_clone[:10]:
        print(f"    {cyan(r['type'])}  {r['source']} → {r['target']}")
    if len(records_to_clone) > 10:
        print(f"    {dim(f'... and {len(records_to_clone) - 10} more')}")

    if not args.yes:
        print()
        confirm = input(f"  Proceed? [y/N] ")
        if confirm.lower() not in ("y", "yes"):
            print(f"  {dim('Aborted.')}")
            return

    print()
    created = 0
    failed = 0
    for r in records_to_clone:
        source = r["source"]
        if source == "@":
            source = ""

        body = {
            "type": r["type"],
            "source": source,
            "target": r["target"],
            "ttl": r["ttl"],
        }
        if r.get("priority") is not None:
            body["priority"] = r["priority"]

        try:
            api_request("POST", f"/2/zones/{target_domain}/records", token, json_data=body)
            print(f"  {green('✓')} {r['type']} {r.get('source', '@')} → {r['target']}")
            created += 1
        except SystemExit:
            print(f"  {red('✗')} {r['type']} {r.get('source', '@')} → {r['target']}")
            failed += 1

    print(f"\n  Done: {green(str(created))} created, {red(str(failed)) if failed else dim('0')} failed.\n")
