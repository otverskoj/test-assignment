from uuid import uuid4

import pytest
from app._errors.user_does_not_exist_error import UserDoesNotExist
from app.user.models.user import User, UserResponse
from app.user.service.impl.user_service_impl import (
    create_user, get_user_by_id, update_user, delete_user
)
from app.user.service.impl.user_service_impl import repository


def test_create_user(
    mocker,
    user_request_for_test: User,
    user_response_for_test: UserResponse
) -> None:
    attrs = {
        'create.return_value': user_response_for_test
    }
    mock_repo = mocker.Mock(repository, **attrs)
    
    mocker.patch('app.service.user_service.repository', mock_repo)
    service_response = create_user(user_request_for_test)

    mock_repo.create.assert_called_once_with(user_request_for_test)
    assert service_response.json() == user_response_for_test.json()


def test_get_user_by_id(
    mocker,
    user_response_for_test: UserResponse
) -> None:
    attrs = {
        'get_by_id.return_value': user_response_for_test
    }
    mock_repo = mocker.Mock(repository, **attrs)
    
    mocker.patch('app.service.user_service.repository', mock_repo)
    service_response = get_user_by_id(user_response_for_test.id_)

    mock_repo.get_by_id.assert_called_once_with(user_response_for_test.id_)
    assert service_response.json() == user_response_for_test.json()


def test_get_user_by_id_raises_exception(
    mocker
) -> None:
    attrs = {
        'get_by_id.side_effect': UserDoesNotExist
    }
    mock_repo = mocker.Mock(repository, **attrs)
    
    mocker.patch('app.service.user_service.repository', mock_repo)
    fake_id = uuid4()
    with pytest.raises(UserDoesNotExist):
        get_user_by_id(fake_id)


def test_update_user(
    mocker,
    user_request_for_test: User,
    user_response_for_test: UserResponse
) -> None:
    attrs = {
        'update.return_value': user_response_for_test        
    }
    mock_repo = mocker.Mock(repository, **attrs)
    
    mocker.patch('app.service.user_service.repository', mock_repo)
    service_response = update_user(
        user_response_for_test.id_,    
        user_request_for_test
    )

    mock_repo.update.assert_called_once_with(
        user_response_for_test.id_,    
        user_request_for_test
    )
    assert service_response.json() == user_response_for_test.json()


def test_delete_user(
    mocker,
    user_response_for_test: UserResponse
) -> None:
    attrs = {
        'delete.return_value': user_response_for_test
    }
    mock_repo = mocker.Mock(repository, **attrs)
    
    mocker.patch('app.service.user_service.repository', mock_repo)
    delete_user(user_response_for_test.id_)

    mock_repo.delete.assert_called_once_with(user_response_for_test.id_)
