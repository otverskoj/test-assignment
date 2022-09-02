from uuid import UUID
import pytest

from src.user.models.user import User
from src.user.repositories.core.exceptions import UserDoesNotExist
from src.user.repositories.impl.in_memory.repository import UserInMemoryRepository


def test_in_memory_repo_can_create() -> None:
    repo = UserInMemoryRepository()

    after_create = repo.create(User(
        **{
            'first_name': 'Name',
            'last_name': 'Familievich',
            'middle_name': 'Patronymicievich'
        }
    ))

    after_get = repo.get_by_id(after_create.id_)

    assert after_create == after_get


def test_in_memory_repo_update(
    fake_in_memory_user_id: UUID,
    not_empty_in_memory_repo: UserInMemoryRepository
) -> None:
    after_update = not_empty_in_memory_repo.update(
        fake_in_memory_user_id,
        User(
            first_name='Test',
            last_name='Testoviy',
            middle_name='Testovich'
        )
    )

    after_get = not_empty_in_memory_repo.get_by_id(fake_in_memory_user_id)
    assert after_update == after_get


def test_in_memory_repo_delete(
    fake_in_memory_user_id: UUID,
    not_empty_in_memory_repo: UserInMemoryRepository
) -> None:
    not_empty_in_memory_repo.delete(fake_in_memory_user_id)

    with pytest.raises(UserDoesNotExist):
        not_empty_in_memory_repo.get_by_id(fake_in_memory_user_id)
