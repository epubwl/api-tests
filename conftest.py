import pytest

from routes import (
    UserRoute
)


pytest_plugins = [
    "fixtures.users"
]


@pytest.fixture(scope="session")
def user_route():
    return UserRoute()
