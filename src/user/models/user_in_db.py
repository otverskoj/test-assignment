from uuid import UUID

from src.user.models.user import User


class UserInDB(User):
    id_: UUID
