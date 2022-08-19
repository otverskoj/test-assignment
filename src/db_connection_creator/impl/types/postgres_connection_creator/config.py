from pydantic import BaseModel


class PostgresConnectionCreatorConfig(BaseModel):
    db_name: str = 'postgres'
    db_host: str = '127.0.0.1'
    db_port: str = '5432'
    db_user: str = 'postgres'
    db_password: str = 'postgres'
