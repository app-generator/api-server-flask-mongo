# -*- encoding: utf-8 -*-

"""
Copyright (c) 2019 - present AppSeed.us
"""

import pytest
import json

from api import app, db
from api.models import Users


"""
   Sample test data
"""

DUMMY_USERNAME = "apple"
DUMMY_USERNAME_NEW = "new new apple"
DUMMY_EMAIL = "apple@apple.com"
DUMMY_PASS = "newpassword"


@pytest.fixture
def client():

    with app.test_client() as client:
        yield client


def test_user_signup(client):
    """
       Tests /users/register API
    """
    response = client.post(
        "api/users/register",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME,
                "email": DUMMY_EMAIL,
                "password": DUMMY_PASS
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert "The user was successfully registered" in data["msg"]


def test_user_signup_invalid_data(client):
    """
       Tests /users/register API: invalid data like email field empty
    """
    response = client.post(
        "api/users/register",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME,
                "email": "",
                "password": DUMMY_PASS
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "'' is too short" in data["msg"]


def test_user_login_correct(client):
    """
       Tests /users/signup API: Correct credentials
    """
    response = client.post(
        "api/users/login",
        data=json.dumps(
            {
                "email": DUMMY_EMAIL,
                "password": DUMMY_PASS
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data["token"] != ""


def test_user_login_error(client):
    """
       Tests /users/signup API: Wrong credentials
    """
    response = client.post(
        "api/users/login",
        data=json.dumps(
            {
                "email": DUMMY_EMAIL,
                "password": DUMMY_EMAIL
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Wrong credentials." in data["msg"]


def test_user_edit_correct_token(client):
    """
       Tests /users/edit API: Correct token
       First get token by logging in, and then pass token to edit API
    """

    response = client.post(
        "api/users/login",
        data=json.dumps(
            {
                "email": DUMMY_EMAIL,
                "password": DUMMY_PASS
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())

    _DUMMY_TOKEN = data["token"]

    response = client.post(
        "api/users/edit",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME_NEW
            }
        ),
        content_type="application/json",
        headers={'authorization': _DUMMY_TOKEN})

    data = json.loads(response.data.decode())
    assert response.status_code == 200


def test_user_edit_wrong_token(client):
    """
       Tests /users/edit API: Wrong token
    """
    response = client.post(
        "api/users/edit",
        data=json.dumps(
            {
                "username": DUMMY_USERNAME_NEW
            }
        ),
        content_type="application/json",
        headers={'authorization': "fake-token"})

    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Token is invalid" in data["msg"]


def test_check_session_correct_token(client):
    """
       Tests /users/checkSession API: Correct token
       First get token by logging in, and then pass token to checkSession API
    """

    response = client.post(
        "api/users/login",
        data=json.dumps(
            {
                "email": DUMMY_EMAIL,
                "password": DUMMY_PASS
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())

    _DUMMY_TOKEN = data["token"]

    response = client.post(
        "api/users/checkSession",
        data=json.dumps(
            {}
        ),
        content_type="application/json",
        headers={'authorization': _DUMMY_TOKEN})

    data = json.loads(response.data.decode())
    assert response.status_code == 200


def test_check_session_wrong_token(client):
    """
       Tests /users/checkSession API: Wrong token
    """
    response = client.post(
        "api/users/checkSession",
        data=json.dumps(
            {}
        ),
        content_type="application/json",
        headers={'authorization': "fake-token"})

    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Token is invalid" in data["msg"]


def test_logout_correct_token(client):
    """
       Tests /users/logout API: Correct token
       First get token by logging in, and then pass token to logout API
    """

    response = client.post(
        "api/users/login",
        data=json.dumps(
            {
                "email": DUMMY_EMAIL,
                "password": DUMMY_PASS
            }
        ),
        content_type="application/json")

    data = json.loads(response.data.decode())

    _DUMMY_TOKEN = data["token"]

    response = client.post(
        "api/users/logout",
        data=json.dumps(
            {}
        ),
        content_type="application/json",
        headers={'authorization': _DUMMY_TOKEN})

    data = json.loads(response.data.decode())
    assert response.status_code == 200


def test_logout_wrong_token(client):
    """
       Tests /users/logout API: Wrong token
    """
    response = client.post(
        "api/users/logout",
        data=json.dumps(
            {}
        ),
        content_type="application/json",
        headers={'authorization': "fake-token"})

    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Token is invalid" in data["msg"]


def test_drop_db(client):
    """
       Drop test database at end
    """

    with app.app_context():
        user = Users.get_by_email(DUMMY_EMAIL)
        user.delete()
