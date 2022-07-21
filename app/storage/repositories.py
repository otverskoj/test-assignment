# from typing import Protocol
# from uuid import UUID, uuid4

# from app.models.schemas.schemas import UserRequest, UserResponse
# from app.api.errors.user_does_not_exist_error import UserDoesNotExist
# from app.settings import settings


# class UserRepository(Protocol):
#     def create(self, user: UserRequest) -> None:
#         raise NotImplementedError
    
#     def get_by_id(self, user_id: UUID) -> UserResponse:
#         raise NotImplementedError

#     def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
#         raise NotImplementedError
    
#     def delete(self, user_id: UUID) -> None:
#         raise NotImplementedError


# class UserInMemoryRepository:
#     def __new__(cls, config: dict = None):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(UserInMemoryRepository, cls).__new__(cls)
#             cls.instance.config = config or {}
#             cls.instance.storage: dict[UUID, UserResponse] = dict()
#         return cls.instance

#     def create(self, user: UserRequest) -> UserResponse:
#         user_response = UserResponse(**user.dict(), id_=uuid4())
#         self.storage[user_response.id_] = user_response
#         return self.storage[user_response.id_]

#     def get_by_id(self, user_id: UUID) -> UserResponse:
#         return self._get_user(user_id)
        
#     def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
#         new_user_data = self._get_user(user_id).dict() | user.dict()
#         self.storage[user_id] = UserResponse(**new_user_data)
#         return self.storage[user_id]
    
#     def delete(self, user_id: UUID) -> None:
#         self._get_user(user_id)
#         del self.storage[user_id]

#     def _get_user(self, user_id: UUID) -> UserResponse:
#         if user_id not in self.storage:
#             raise UserDoesNotExist
#         return self.storage[user_id]


# class UserDBRepository:
#     def __init__(self, config) -> None:
#         self.config = config
        
#     def create(self, user: UserRequest) -> UserResponse:
#         pass

#     def get_by_id(self, user_id: UUID) -> UserResponse:
#         pass

#     def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
#         pass
    
#     def delete(self, user_id: UUID) -> None:
#         pass

