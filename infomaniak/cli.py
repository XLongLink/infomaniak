"""Minimal CLI for opening the Infomaniak API token page."""

import argparse
import webbrowser

from infomaniak import __version__
from infomaniak.config import load_env_file


TOKEN_URL = "https://manager.infomaniak.com/v3/infomaniak-api"


def build_parser():
    parser = argparse.ArgumentParser(
        prog="infomaniak",
        description="Open the Infomaniak token creation page.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv=None):
    load_env_file()
    parser = build_parser()
    parser.parse_args(argv)
    webbrowser.open(TOKEN_URL)
    print(f"Opened {TOKEN_URL}")
    return 0
