def test_register_delete(
    user_route,
    test_user_credentials
):
    # Register user
    response = user_route.register(test_user_credentials)
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, dict)
    assert "token" in json_content
    token = json_content["token"]

    # Register duplicate user
    response = user_route.register(test_user_credentials)
    assert response.status_code == 400

    # Delete registered user
    response = user_route.delete(token, test_user_credentials.username)
    assert response.status_code == 204

    # Delete non-existent user
    response = user_route.delete(token, test_user_credentials.username)
    assert response.status_code == 401


def test_login(
    user_route,
    test_user_credentials
):
    # Login non-existent user
    response = user_route.login(test_user_credentials)
    assert response.status_code == 400

    # Register user
    response = user_route.register(test_user_credentials)
    assert response.status_code == 200

    # Login user
    response = user_route.login(test_user_credentials)
    assert response.status_code == 200
    json_content = response.json()
    assert isinstance(json_content, dict)
    assert "token" in json_content
    token = json_content["token"]
    assert token

    # Delete registered user
    response = user_route.delete(token, test_user_credentials.username)
    assert response.status_code == 204

    # Login non-existent user
    response = user_route.login(test_user_credentials)
    assert response.status_code == 400


def test_change_password(
    user_route,
    test_user_credentials,
    test_user_stronger_credentials,
    test_user_password_change,
    test_user_invalid_password_change
):
    # Change password for non existent user
    response = user_route.change_password("", test_user_password_change)
    assert response.status_code == 401

    # Register user
    response = user_route.register(test_user_credentials)
    assert response.status_code == 200
    token = response.json()["token"]

    # Invalid current password
    response = user_route.change_password(
        token,
        test_user_invalid_password_change
    )
    assert response.status_code == 400

    # Change password
    response = user_route.change_password(token, test_user_password_change)
    assert response.status_code == 204

    # Try logging in with old password
    response = user_route.login(test_user_credentials)
    assert response.status_code == 400

    # Login with new password
    response = user_route.login(test_user_stronger_credentials)
    assert response.status_code == 200

    # Delete registered user
    response = user_route.delete(token, test_user_credentials.username)
    assert response.status_code == 204
