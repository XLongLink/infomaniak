from typing import Literal
from dacite import from_dict
from infomaniak.models.core.user import AccountInvitation
from infomaniak.resource import Resouce, AsyncResource


class User(Resouce):
    """Core resources for Infomaniak services."""

    def invite(
        self,
        account: int,
        email: str,
        first_name: str,
        last_name: str,
        locale: Literal["de_DE", "en_GB", "es_ES", "fr_FR", "it_IT"],
        role_type: Literal["admin", "normal", "owner"],
        *,
        notifications_billing: bool | None = None,
        notifications_products: bool | None = None,
        permissions_billing: bool | None = None,
        silent: bool | None = None,
        strict: bool | None = None,
        teams: list[int] | None = None,
        with_: str | None = None,
    ) -> AccountInvitation:
        """
        Invite a User.

        Create and send an invitation for a new or existing User to join an
        Account using an email address.

        Args:
            account: Unique identifier of the Account.
            email: The email address of the user being invited.
            first_name: The first name of the user being invited.
            last_name: The last name of the user being invited.
            locale: The locale code for the language of the invitation the user
                will receive.
            role_type: The role to assign to the user upon invitation.
            notifications_billing: Whether or not the user will be able to
                receive billing notifications.
            notifications_products: Whether or not the user will be able to
                receive product notifications.
            permissions_billing: Whether or not the user will be able to manage
                the billing account.
            silent: Whether or not the user will receive the invitation email.
            strict: Whether or not the user should register with the same email
                address.
            teams: The teams the user should be added to upon invitation.
            with_: Optional related resources to include in the response.

        Returns:
            The created account invitation.

        Notes:
            API endpoint:
            https://developer.infomaniak.com/docs/api/post/1/accounts/{account}/invitations
        """
        url = f"/1/accounts/{account}/invitations"
        params = {"with": with_} if with_ is not None else None

        payload: dict[str, object] = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "locale": locale,
            "role_type": role_type,
        }

        notifications: dict[str, bool] = {}
        if notifications_billing is not None:
            notifications["billing"] = notifications_billing
        if notifications_products is not None:
            notifications["products"] = notifications_products
        if notifications:
            payload["notifications"] = notifications

        permissions: dict[str, bool] = {}
        if permissions_billing is not None:
            permissions["billing"] = permissions_billing
        if permissions:
            payload["permissions"] = permissions

        if silent is not None:
            payload["silent"] = silent
        if strict is not None:
            payload["strict"] = strict
        if teams is not None:
            payload["teams"] = teams

        response = self._client.post(url, json=payload, params=params)
        return from_dict(AccountInvitation, response.json()["data"])

    def revoke(self, account: int, invitation: int) -> bool:
        """
        Cancel an invitation to join an account.

        This operation deletes a previously created user invitation associated
        with a specific account. The request requires authentication and appropriate
        permissions.

        Args:
            account: Unique identifier of the account.
            invitation: Unique identifier of the user invitation.

        Returns:
            `True` when the invitation was successfully revoked.

        Raises:
            UnauthorizedError: If authentication is missing or invalid (HTTP 401).
            ForbiddenError: If the user does not have permission to cancel the invitation (HTTP 403).
            NotFoundError: If the account or invitation does not exist or is not accessible (HTTP 404).
            CannotDeleteError: If the invitation cannot be deleted due to a server-side issue (HTTP 500).

        Notes:
            API endpoint:
            https://developer.infomaniak.com/docs/api/delete/1/accounts/{account}/invitations/{invitation}
        """
        url = f"/1/accounts/{account}/invitations/{invitation}"
        response = self._client.delete(url)
        payload = response.json()
        return bool(payload.get("result") == "success")

    
class AsyncUser(AsyncResource):
    """Async core resources for Infomaniak services."""

    def __init__(self, client):
        self._client = client

    async def invite(
        self,
        account: int,
        email: str,
        first_name: str,
        last_name: str,
        locale: Literal["de_DE", "en_GB", "es_ES", "fr_FR", "it_IT"],
        role_type: Literal["admin", "normal", "owner"],
        *,
        notifications_billing: bool | None = None,
        notifications_products: bool | None = None,
        permissions_billing: bool | None = None,
        silent: bool | None = None,
        strict: bool | None = None,
        teams: list[int] | None = None,
        with_: str | None = None,
    ) -> AccountInvitation:
        """
        Invite a User.

        Create and send an invitation for a new or existing User to join an
        Account using an email address.

        Args:
            account: Unique identifier of the Account.
            email: The email address of the user being invited.
            first_name: The first name of the user being invited.
            last_name: The last name of the user being invited.
            locale: The locale code for the language of the invitation the user
                will receive.
            role_type: The role to assign to the user upon invitation.
            notifications_billing: Whether or not the user will be able to
                receive billing notifications.
            notifications_products: Whether or not the user will be able to
                receive product notifications.
            permissions_billing: Whether or not the user will be able to manage
                the billing account.
            silent: Whether or not the user will receive the invitation email.
            strict: Whether or not the user should register with the same email
                address.
            teams: The teams the user should be added to upon invitation.
            with_: Optional related resources to include in the response.

        Returns:
            The created account invitation.

        Notes:
            API endpoint:
            https://developer.infomaniak.com/docs/api/post/1/accounts/{account}/invitations
        """
        url = f"/1/accounts/{account}/invitations"
        params = {"with": with_} if with_ is not None else None

        payload: dict[str, object] = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "locale": locale,
            "role_type": role_type,
        }

        notifications: dict[str, bool] = {}
        if notifications_billing is not None:
            notifications["billing"] = notifications_billing
        if notifications_products is not None:
            notifications["products"] = notifications_products
        if notifications:
            payload["notifications"] = notifications

        permissions: dict[str, bool] = {}
        if permissions_billing is not None:
            permissions["billing"] = permissions_billing
        if permissions:
            payload["permissions"] = permissions

        if silent is not None:
            payload["silent"] = silent
        if strict is not None:
            payload["strict"] = strict
        if teams is not None:
            payload["teams"] = teams

        response = await self._client.post(url, json=payload, params=params)
        return from_dict(AccountInvitation, response.json()["data"])

    async def user(self):
        """Get the current authenticated user."""
        return await self._client._request("GET", "/user")

    async def revoke(self, account: int, invitation: int) -> bool:
        """
        Cancel an invitation to join an account.

        This operation deletes a previously created user invitation associated
        with a specific account. The request requires authentication and
        appropriate permissions.

        Args:
            account: Unique identifier of the account.
            invitation: Unique identifier of the user invitation.

        Returns:
            `True` when the invitation was successfully revoked.

        Notes:
            API endpoint:
            https://developer.infomaniak.com/docs/api/delete/1/accounts/{account}/invitations/{invitation}
        """
        url = f"/1/accounts/{account}/invitations/{invitation}"
        response = await self._client.delete(url)
        payload = response.json()
        return bool(payload.get("result") == "success")
    
