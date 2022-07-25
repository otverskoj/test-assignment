from abc import ABC
from uuid import UUID

from app.models.schemas.schemas import UserRequest, UserResponse


class UserRepository(ABC):
    def create(self, user: UserRequest) -> UserResponse:
        raise NotImplementedError
    
    def get_by_id(self, user_id: UUID) -> UserResponse:
        raise NotImplementedError

    def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
        raise NotImplementedError
    
    def delete(self, user_id: UUID) -> None:
        raise NotImplementedError
