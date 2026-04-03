"""Configuration management for environment-backed auth."""

import os
import sys

from dotenv import find_dotenv, load_dotenv

from infomaniak.api import api_request


def load_env_file():
    """Load variables from the nearest .env file if it exists."""
    env_path = find_dotenv(usecwd=True)
    if not env_path:
        return
    load_dotenv(env_path, override=False)


def get_token():
    """Get API token from environment or .env file."""
    token = os.environ.get("INFOMANIAK_API_TOKEN")
    if token:
        return token

    print("\nNo API token found.\n")
    print("Set INFOMANIAK_API_TOKEN in your environment or .env file.\n")
    sys.exit(1)


def get_account_id(token):
    """Get account ID from environment or auto-discover it."""
    account_id = os.environ.get("INFOMANIAK_ACCOUNT_ID")
    if account_id:
        return account_id

    data = api_request("GET", "/1/accounts", token)
    accounts = data.get("data", [])
    if not accounts:
        print("No accounts found for this token.")
        sys.exit(1)
    if len(accounts) == 1:
        return accounts[0]["id"]

    print("Multiple accounts found:\n")
    for index, acc in enumerate(accounts, start=1):
        print(f"  [{index}] {acc['name']} (ID: {acc['id']})")
    print()
    choice = input(f"Select account [1-{len(accounts)}]: ")
    try:
        idx = int(choice) - 1
        return accounts[idx]["id"]
    except (ValueError, IndexError):
        print("Invalid choice.")
        sys.exit(1)
