def test_register_delete(user_route, test_user_credentials):
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
