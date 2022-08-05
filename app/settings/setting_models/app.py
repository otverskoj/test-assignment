from pydantic import BaseSettings


class ApplicationSettings(BaseSettings):
    repository_type: str
    db_name: str
    db_host: str
    db_port: str
    db_user: str
    db_password: str

    class Config:
        anystr_strip_whitespace = True
