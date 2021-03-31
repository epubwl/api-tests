import pytest

from models import UserCredentials


@pytest.fixture
def test_user_credentials():
    return UserCredentials("user", "weakpassword")


@pytest.fixture
def librarian_token():
    pass
