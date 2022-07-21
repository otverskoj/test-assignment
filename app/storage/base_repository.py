from typing import Protocol
from uuid import UUID

from app.models.schemas.schemas import UserRequest, UserResponse
from app.storage.user_in_memory_repository import UserInMemoryRepository
from app.storage.user_db_repository import UserDBRepository
from app.settings import settings


class UserRepository(Protocol):
    def create(self, user: UserRequest) -> None:
        raise NotImplementedError
    
    def get_by_id(self, user_id: UUID) -> UserResponse:
        raise NotImplementedError

    def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
        raise NotImplementedError
    
    def delete(self, user_id: UUID) -> None:
        raise NotImplementedError


_repositories = {
    'in_memory': UserInMemoryRepository,
    'db': UserDBRepository
}


repository = _repositories[settings['repository_type']](settings['repository_config'])
