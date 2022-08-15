from uuid import UUID

from pydantic import BaseModel

from app.user.models.user import User


class UserInDB(User):
    id_: UUID
