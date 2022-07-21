from uuid import UUID

from app.models.schemas.schemas import UserRequest, UserResponse
from app.storage.base_repository import repository


def create_user(user: UserRequest) -> None:
    return repository.create(user)
    
def get_user_by_id(user_id: UUID) -> UserResponse:
    return repository.get_by_id(user_id)

def update_user(user_id: UUID, user: UserRequest) -> UserResponse:
    return repository.update(user_id, user)

def delete_user(user_id: UUID) -> None:
    repository.delete(user_id)
