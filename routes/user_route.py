import requests
from urllib.parse import urljoin

from .base_route import BaseRoute
from models import PasswordChange
from models import UserCredentials


class UserRoute(BaseRoute):
    def register(
        self,
        user_credentials: UserCredentials
    ) -> requests.Response:
        return requests.post(
            urljoin(self.hostname, "/api/users"),
            data=user_credentials.json_stringify(),
            headers=self.json_header
        )

    def delete(
        self,
        token: str,
        username: str
    ) -> requests.Response:
        return requests.delete(
            urljoin(self.hostname, f"/api/users/{username}"),
            headers=self.get_authorization_header(token)
        )

    def login(
        self,
        user_credentials: UserCredentials
    ) -> requests.Response:
        return requests.post(
            urljoin(self.hostname, "/api/users/login"),
            data=user_credentials.json_stringify(),
            headers=self.json_header
        )

    def change_password(
        self,
        token: str,
        password_change: PasswordChange
    ) -> requests.Response:
        return requests.post(
            urljoin(self.hostname, "/api/users/passwordchange"),
            data=password_change.json_stringify(),
            headers=self.json_header | self.get_authorization_header(token)
        )
