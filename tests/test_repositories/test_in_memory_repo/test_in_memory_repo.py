from uuid import UUID
import pytest
from app._errors.user_does_not_exist_error import UserDoesNotExist
from app.user.models.user import User
from app.storage.user_in_memory_repository import UserInMemoryRepository


def test_in_memory_repo_create_and_get() -> None:
    after_create = UserInMemoryRepository().create(User(
        **{
            'first_name': 'Name',
            'last_name': 'Familievich',
            'middle_name': 'Patronymicievich'
        }
    ))

    after_get = UserInMemoryRepository().get_by_id(after_create.id_)

    assert after_create == after_get


@pytest.mark.usefixtures('insert_values_in_memory')
def test_in_memory_repo_update() -> None:
    id_ = UUID('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa')
    after_update = UserInMemoryRepository().update(
        id_,
        User(
            first_name='Test',
            last_name='Testoviy',
            middle_name='Testovich'
        )
    )

    after_get = UserInMemoryRepository().get_by_id(id_)
    assert after_update == after_get


@pytest.mark.usefixtures('insert_values_in_memory')
def test_in_memory_repo_delete() -> None:
    id_ = UUID('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa')
    UserInMemoryRepository().delete(id_)

    with pytest.raises(UserDoesNotExist):
        UserInMemoryRepository().get_by_id(id_)
