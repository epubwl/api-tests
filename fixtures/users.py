import pytest

from models import PasswordChange, UserCredentials


@pytest.fixture
def test_user_credentials():
    return UserCredentials("user", "weakpassword")


@pytest.fixture
def test_user_stronger_credentials():
    return UserCredentials("user", "$tr0ngerPassword")


@pytest.fixture
def test_user_password_change():
    return PasswordChange("weakpassword", "$tr0ngerPassword")


@pytest.fixture
def test_user_invalid_password_change():
    return PasswordChange("notapassword", "$tr0ngerPassword")


@pytest.fixture(scope="session")
def librarian_token(user_route):
    librarian_credentials = UserCredentials("librarian", "$EPUBwl3")
    token = user_route.register(librarian_credentials).json()["token"]
    yield token
    user_route.delete(librarian_credentials, librarian_credentials.username)
