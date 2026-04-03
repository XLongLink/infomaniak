"""Tests for configuration management."""

import os

import pytest

from infomaniak import config


class TestLoadEnvFile:
    def test_loads_env_vars(self, tmp_path, monkeypatch):
        env_file = tmp_path / ".env"
        env_file.write_text("TEST_VAR=hello\n")
        monkeypatch.chdir(tmp_path)
        monkeypatch.delenv("TEST_VAR", raising=False)

        config.load_env_file()
        assert os.environ.get("TEST_VAR") == "hello"

        monkeypatch.delenv("TEST_VAR", raising=False)

    def test_ignores_comments(self, tmp_path, monkeypatch):
        env_file = tmp_path / ".env"
        env_file.write_text("# comment\n\nVALID_VAR=yes\n")
        monkeypatch.chdir(tmp_path)
        monkeypatch.delenv("VALID_VAR", raising=False)

        config.load_env_file()
        assert os.environ.get("VALID_VAR") == "yes"

        monkeypatch.delenv("VALID_VAR", raising=False)


class TestGetToken:
    def test_from_env(self, mock_token):
        assert config.get_token() == "test-token-abc123"

    def test_missing_exits(self, monkeypatch):
        monkeypatch.delenv("INFOMANIAK_API_TOKEN", raising=False)

        with pytest.raises(SystemExit):
            config.get_token()


class TestGetAccountId:
    def test_from_env(self, mock_account_id):
        assert config.get_account_id("tok") == "12345"
