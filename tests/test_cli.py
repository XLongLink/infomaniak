"""Tests for the minimal token-page CLI."""

from unittest.mock import patch

import pytest

from infomaniak.cli import TOKEN_URL, main


class TestCli:
    def test_opens_token_page_by_default(self, capsys):
        with patch("infomaniak.cli.webbrowser.open") as open_browser:
            exit_code = main([])

        assert exit_code == 0
        open_browser.assert_called_once_with(TOKEN_URL)
        captured = capsys.readouterr()
        assert TOKEN_URL in captured.out

    def test_version_flag(self, capsys):
        with pytest.raises(SystemExit) as exc:
            main(["--version"])

        assert exc.value.code == 0
        captured = capsys.readouterr()
        assert "infomaniak" in captured.out
