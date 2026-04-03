"""OpenAPI-derived error types for the Infomaniak package."""

from infomaniak.errors.app import AppError, InternalServerError
from infomaniak.errors.base import APIError, ErrorDetail, InfomaniakError, NonJSONResponseError
from infomaniak.errors.reports import MailingListSubscriberErrorReport
from infomaniak.errors.validation import ValidationError, ValidationErrorDetail

__all__ = [
    "APIError",
    "AppError",
    "ErrorDetail",
    "InfomaniakError",
    "InternalServerError",
    "MailingListSubscriberErrorReport",
    "NonJSONResponseError",
    "ValidationError",
    "ValidationErrorDetail",
]
