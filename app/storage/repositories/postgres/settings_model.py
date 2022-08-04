from pydantic import BaseModel


class UserPostgresRepositorySettings(BaseModel):
    db_name: str
    db_host: str
    db_port: str
    db_user: str
    db_password: str
