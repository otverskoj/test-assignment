from uuid import UUID

from app.models.schemas.schemas import UserRequest, UserResponse
from app.api.errors.user_does_not_exist_error import UserDoesNotExist


class UserDBRepository:
    def __init__(self, config) -> None:
        self.config = config
        
    def create(self, user: UserRequest) -> UserResponse:
        pass

    def get_by_id(self, user_id: UUID) -> UserResponse:
        pass

    def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
        pass
    
    def delete(self, user_id: UUID) -> None:
        pass

