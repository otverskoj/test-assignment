import json
from uuid import uuid4

import requests

from src.user.views.models.request import UserRequest


def test_create_user_view_returns_right_data(
    api_localhost_url: str,
    fake_user: UserRequest
) -> None:
    payload = json.dumps(fake_user.dict())
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(
        method='POST',
        url=api_localhost_url,
        headers=headers,
        data=payload
    )

    response_data = json.loads(response.text)

    assert response.status_code == 201
    assert fake_user.first_name == response_data['first_name']
    assert fake_user.last_name == response_data['last_name']
    assert fake_user.middle_name == response_data['middle_name']


def test_get_user_by_id_view_returns_correct_user(
    api_localhost_url: str,
    id_of_fake_user: str,
    fake_user: UserRequest
) -> None:
    response = requests.request(
        method='GET',
        url=api_localhost_url + id_of_fake_user,
    )

    user_in_response = json.loads(response.text)
    assert response.status_code == 200
    assert user_in_response['id_'] == id_of_fake_user
    assert user_in_response['first_name'] == fake_user.first_name
    assert user_in_response['middle_name'] == fake_user.middle_name
    assert user_in_response['last_name'] == fake_user.last_name


def test_get_user_by_id_view_return_404_if_user_dont_exist(
    api_localhost_url: str
) -> None:
    fake_id = uuid4()

    response = requests.request(
        method='GET',
        url=api_localhost_url + str(fake_id),
    )

    assert response.status_code == 404


def test_update_user_view_changes_user(
    api_localhost_url: str,
    id_of_fake_user: str,
    fake_user: UserRequest
) -> None:
    headers = {
        'Content-Type': 'application/json'
    }
    fake_user.first_name = "Ivan"
    payload = json.dumps(fake_user.dict())

    response = requests.request(
        method='PUT',
        url=api_localhost_url + id_of_fake_user,
        headers=headers,
        data=payload
    )

    response_data = json.loads(response.text)

    assert response.status_code == 200
    assert fake_user.first_name == response_data['first_name']
    assert fake_user.last_name == response_data['last_name']
    assert fake_user.middle_name == response_data['middle_name']


def test_delete_user_view_returns_204(
    api_localhost_url: str,
    id_of_fake_user: str
) -> None:
    response = requests.request(
        method='DELETE',
        url=api_localhost_url + str(id_of_fake_user),
    )

    assert response.status_code == 204
