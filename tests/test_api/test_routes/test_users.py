from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder

from app.models.schemas.schemas import UserRequest, UserResponse


def test_create_user(
    user_request_for_test: UserRequest,
    test_client: TestClient
) -> None:
    response = test_client.post(
        url='/users/', 
        json=jsonable_encoder(user_request_for_test)
    )
    
    assert response.status_code == 201
    
    responsed_user = UserResponse(**response.json())

    try:
        id_ = UUID(str(responsed_user.id_), version=4)
    except ValueError:
        raise AssertionError('Not valid UUID')
    
    assert id_ == responsed_user.id_
    assert user_request_for_test.first_name == responsed_user.first_name
    assert user_request_for_test.last_name == responsed_user.last_name
    assert user_request_for_test.middle_name == responsed_user.middle_name


def test_get_existing_user_by_id(
    user_request_for_test: UserRequest, 
    test_client: TestClient
) -> None:
    post_response = test_client.post(
        url='/users/', 
        json=jsonable_encoder(user_request_for_test)
    )
    responsed_user = UserResponse(**post_response.json())

    response = test_client.get(url=f"/users/{responsed_user.id_}")

    assert response.status_code == 200
    assert UserResponse(**response.json()) == responsed_user


def test_get_not_existing_user_by_id(
    test_client: TestClient
) -> None:
    fake_id = uuid4()
    response = test_client.get(url=f"/users/{fake_id}")
    assert response.status_code == 404
    assert response.json() == {'detail': f"User with id {fake_id} does not exist."}


@pytest.mark.parametrize(
    'user_to_update',
    (
        UserRequest(**{
            'first_name': 'Not Ivan', 
            'last_name': 'Ivanov',
            'middle_name': 'Ivanovich'
        }),
        UserRequest(**{
            'first_name': 'Ivan', 
            'last_name': 'Not Ivanov',
            'middle_name': 'Ivanovich'
        }),
        UserRequest(**{
            'first_name': 'Ivan', 
            'last_name': 'Ivanov',
            'middle_name': 'Not Ivanovich'
        })
    )
)
def test_update_user(
    user_request_for_test: UserRequest,
    user_to_update: UserRequest,
    test_client: TestClient
) -> None:
    post_response = test_client.post(
        url='/users/', 
        json=jsonable_encoder(user_request_for_test)
    )
    responsed_user = UserResponse(**post_response.json())

    put_response = test_client.put(
        url=f"/users/{responsed_user.id_}",
        json=jsonable_encoder(user_to_update)
    )
    
    user_to_update_response = UserResponse(
        **user_to_update.dict() | {'id_': responsed_user.id_}
    )

    assert put_response.status_code == 200
    assert UserResponse(**put_response.json()) == user_to_update_response


def test_delete_user(
    user_request_for_test: UserRequest,
    test_client: TestClient
) -> None:
    post_response = test_client.post(
        url='/users/', 
        json=jsonable_encoder(user_request_for_test)
    )
    responsed_user = UserResponse(**post_response.json())

    response = test_client.delete(
        url=f"/users/{responsed_user.id_}"
    )

    assert response.status_code == 204
