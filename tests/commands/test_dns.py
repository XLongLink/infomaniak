"""Tests for DNS commands."""

import json

import pytest
from unittest.mock import patch

from infomaniak_cli.commands.dns import (
    cmd_dns_add,
    cmd_dns_domains,
    cmd_dns_export,
    cmd_dns_import,
    cmd_dns_records,
    cmd_dns_update,
)


class TestDnsDomains:
    def test_displays_table(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"id": 1, "customer_name": "example.com", "has_dnssec": True, "is_dns_managed_by_infomaniak": True},
                {"id": 2, "customer_name": "test.org", "has_dnssec": False, "is_dns_managed_by_infomaniak": False},
            ],
        }

        cmd_dns_domains(fake_args())
        captured = capsys.readouterr()
        assert "example.com" in captured.out
        assert "test.org" in captured.out
        assert "Domains (2)" in captured.out

    def test_json_output(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [{"id": 1, "customer_name": "example.com"}],
        }

        with pytest.raises(SystemExit) as exc:
            cmd_dns_domains(fake_args(json=True))
        assert exc.value.code == 0
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data[0]["customer_name"] == "example.com"

    def test_empty(self, capsys, mock_token, mock_account_id, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {"result": "success", "data": []}

        cmd_dns_domains(fake_args())
        captured = capsys.readouterr()
        assert "No domains" in captured.out


class TestDnsRecords:
    def test_lists_records(self, capsys, mock_token, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"id": 100, "type": "A", "source": "www", "target": "1.2.3.4", "ttl": 3600},
                {"id": 101, "type": "CNAME", "source": "app", "target": "cdn.example.com", "ttl": 300},
            ],
        }

        cmd_dns_records(fake_args(domain="example.com", type=None))
        captured = capsys.readouterr()
        assert "1.2.3.4" in captured.out
        assert "cdn.example.com" in captured.out

    def test_filter_by_type(self, capsys, mock_token, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"id": 100, "type": "A", "source": "www", "target": "1.2.3.4", "ttl": 3600},
                {"id": 101, "type": "CNAME", "source": "app", "target": "cdn.example.com", "ttl": 300},
            ],
        }

        cmd_dns_records(fake_args(domain="example.com", type="A"))
        captured = capsys.readouterr()
        assert "1.2.3.4" in captured.out
        assert "cdn.example.com" not in captured.out

    def test_dot_source_becomes_at(self, capsys, mock_token, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [{"id": 100, "type": "A", "source": ".", "target": "1.2.3.4", "ttl": 3600}],
        }

        cmd_dns_records(fake_args(domain="example.com", type=None))
        captured = capsys.readouterr()
        assert "@" in captured.out


class TestDnsAdd:
    def test_sends_correct_payload(self, capsys, mock_token, mock_api, fake_args):
        mock_req, response = mock_api
        response.json.return_value = {"result": "success", "data": {"id": 999}}

        cmd_dns_add(fake_args(domain="example.com", type="A", source="www", target="1.2.3.4", ttl=3600))

        call_kwargs = mock_req.call_args[1]
        assert call_kwargs["json"]["type"] == "A"
        assert call_kwargs["json"]["source"] == "www"
        assert call_kwargs["json"]["target"] == "1.2.3.4"

    def test_at_source_becomes_empty(self, capsys, mock_token, mock_api, fake_args):
        mock_req, response = mock_api
        response.json.return_value = {"result": "success", "data": {"id": 999}}

        cmd_dns_add(fake_args(domain="example.com", type="A", source="@", target="1.2.3.4", ttl=3600))

        call_kwargs = mock_req.call_args[1]
        assert call_kwargs["json"]["source"] == ""


class TestDnsUpdate:
    def test_requires_target_or_ttl(self, fake_args, mock_token):
        with pytest.raises(SystemExit):
            cmd_dns_update(fake_args(domain="example.com", record_id="123", target=None, ttl=None))


class TestDnsExport:
    def test_json_export(self, capsys, mock_token, mock_api, fake_args):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [
                {"type": "A", "source": "www", "target": "1.2.3.4", "ttl": 3600, "priority": None},
            ],
        }

        cmd_dns_export(fake_args(domain="example.com", format="json", output=None))
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data[0]["type"] == "A"

    def test_export_to_file(self, tmp_path, mock_token, mock_api, fake_args, capsys):
        _, response = mock_api
        response.json.return_value = {
            "result": "success",
            "data": [{"type": "A", "source": "www", "target": "1.2.3.4", "ttl": 3600, "priority": None}],
        }

        outfile = str(tmp_path / "out.json")
        cmd_dns_export(fake_args(domain="example.com", format="json", output=outfile))

        content = (tmp_path / "out.json").read_text()
        data = json.loads(content)
        assert data[0]["target"] == "1.2.3.4"


class TestDnsImport:
    def test_imports_from_json(self, tmp_path, capsys, mock_token, mock_api, fake_args):
        mock_req, response = mock_api
        response.json.return_value = {"result": "success", "data": {"id": 1}}

        import_file = tmp_path / "records.json"
        import_file.write_text('[{"type":"A","source":"www","target":"1.2.3.4","ttl":3600}]')

        cmd_dns_import(fake_args(domain="example.com", file=str(import_file), yes=True))
        captured = capsys.readouterr()
        assert "1 created" in captured.out

    def test_missing_file_exits(self, fake_args, mock_token):
        with pytest.raises(SystemExit):
            cmd_dns_import(fake_args(domain="example.com", file="/nonexistent.json", yes=True))
