from uuid import uuid4

import pytest

from src.user.models.user import User
from src.user.models.user_in_db import UserInDB
from src.user.repositories.core.exceptions import UserDoesNotExist
from src.user.repositories.core.user_repository import IUserRepository
from src.user.service.impl.user_service_impl import UserServiceImpl


def test_user_service_can_create_user(
    mocker,
    fake_user_to_db: User,
    fake_user_from_db: UserInDB
) -> None:
    attrs = {
        'create.return_value': fake_user_from_db
    }
    mock_repo = mocker.Mock(IUserRepository, **attrs)
    service = UserServiceImpl(mock_repo)

    service_response = service.create_user(fake_user_to_db)

    mock_repo.create.assert_called_once_with(fake_user_to_db)
    assert service_response.json() == fake_user_from_db.json()


def test_get_user_by_id(
    mocker,
    fake_user_from_db: UserInDB
) -> None:
    attrs = {
        'get_by_id.return_value': fake_user_from_db
    }
    mock_repo = mocker.Mock(IUserRepository, **attrs)
    service = UserServiceImpl(mock_repo)

    service_response = service.get_user_by_id(fake_user_from_db.id_)

    mock_repo.get_by_id.assert_called_once_with(fake_user_from_db.id_)
    assert service_response.json() == fake_user_from_db.json()


def test_get_user_by_id_raises_exception(mocker) -> None:
    attrs = {
        'get_by_id.side_effect': UserDoesNotExist
    }
    mock_repo = mocker.Mock(IUserRepository, **attrs)
    service = UserServiceImpl(mock_repo)
    fake_id = uuid4()

    with pytest.raises(UserDoesNotExist):
        service.get_user_by_id(fake_id)


def test_update_user(
    mocker,
    fake_user_to_db: User,
    fake_user_from_db: UserInDB
) -> None:
    attrs = {
        'update.return_value': fake_user_from_db
    }
    mock_repo = mocker.Mock(IUserRepository, **attrs)
    service = UserServiceImpl(mock_repo)

    service_response = service.update_user(
        fake_user_from_db.id_,
        fake_user_to_db
    )

    mock_repo.update.assert_called_once_with(
        fake_user_from_db.id_,
        fake_user_to_db
    )
    assert service_response.json() == fake_user_from_db.json()


def test_delete_user(
    mocker,
    fake_user_from_db: UserInDB
) -> None:
    attrs = {
        'delete.return_value': fake_user_from_db
    }
    mock_repo = mocker.Mock(IUserRepository, **attrs)
    service = UserServiceImpl(mock_repo)

    service.delete_user(fake_user_from_db.id_)

    mock_repo.delete.assert_called_once_with(fake_user_from_db.id_)
