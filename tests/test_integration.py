"""Integration tests for the minimal CLI entrypoint."""

import os
import subprocess
import sys


CLI = [sys.executable, "-m", "infomaniak"]


def run(*args):
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    return subprocess.run(
        [*CLI, *args],
        capture_output=True,
        text=True,
        env=env,
        timeout=10,
    )


class TestCliIntegration:
    def test_help_flag(self):
        result = run("--help")

        assert result.returncode == 0
        assert "Open the Infomaniak token creation page." in result.stdout

    def test_version_flag(self):
        result = run("--version")

        assert result.returncode == 0
        assert "infomaniak" in result.stdout

    def test_unknown_argument_fails(self):
        result = run("--unknown")

        assert result.returncode != 0
        assert "usage:" in result.stderr.lower()
