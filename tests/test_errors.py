from unittest.mock import MagicMock

import pytest

from infomaniak._base import _unwrap_response
from infomaniak.errors import (
    APIError,
    AppError,
    InternalServerError,
    MailingListSubscriberErrorReport,
    NonJSONResponseError,
    ValidationError,
    ValidationErrorDetail,
)


def make_response(*, status_code=200, payload=None, text="", is_error=False, json_error=None):
    response = MagicMock()
    response.status_code = status_code
    response.text = text
    response.is_error = is_error
    if json_error is not None:
        response.json.side_effect = json_error
    else:
        response.json.return_value = payload
    return response


def test_unwrap_response_raises_api_error_for_legacy_error_payload():
    response = make_response(
        payload={
            "result": "error",
            "error": {"code": "forbidden", "description": "No access", "errors": []},
        }
    )

    with pytest.raises(APIError) as exc_info:
        _unwrap_response(response)

    assert exc_info.value.status_code == 200
    assert exc_info.value.detail.code == "forbidden"
    assert "No access" in str(exc_info.value)


def test_unwrap_response_raises_non_json_response_error():
    response = make_response(status_code=502, text="Bad Gateway", json_error=ValueError("No JSON"))

    with pytest.raises(NonJSONResponseError) as exc_info:
        _unwrap_response(response)

    assert exc_info.value.status_code == 502
    assert "Bad Gateway" in str(exc_info.value)


def test_unwrap_response_raises_app_error_from_openapi_shape():
    response = make_response(
        status_code=403,
        is_error=True,
        payload={
            "status_code": 403,
            "id": "forbidden_file",
            "message": "Do not have appropriate permissions",
            "request_id": "req-123",
        },
    )

    with pytest.raises(AppError) as exc_info:
        _unwrap_response(response)

    assert exc_info.value.status_code == 403
    assert exc_info.value.error_id == "forbidden_file"
    assert exc_info.value.request_id == "req-123"


def test_unwrap_response_raises_internal_server_error_for_500_app_error():
    response = make_response(
        status_code=500,
        is_error=True,
        payload={"status_code": 500, "message": "Something went wrong", "request_id": "req-500"},
    )

    with pytest.raises(InternalServerError):
        _unwrap_response(response)


def test_unwrap_response_raises_validation_error_for_detail_list():
    response = make_response(
        status_code=422,
        is_error=True,
        payload={
            "message": "Validation failed",
            "detail": [{"loc": ["body", "email"], "msg": "field required", "type": "missing"}],
        },
    )

    with pytest.raises(ValidationError) as exc_info:
        _unwrap_response(response)

    assert len(exc_info.value.errors) == 1
    assert isinstance(exc_info.value.errors[0], ValidationErrorDetail)
    assert exc_info.value.errors[0].loc == ("body", "email")


def test_mailing_list_subscriber_error_report_from_api():
    report = MailingListSubscriberErrorReport.from_api(
        {"count": 3, "last_error": 1712000000, "last_error_code": 42}
    )

    assert report.count == 3
    assert report.last_error_code == 42
