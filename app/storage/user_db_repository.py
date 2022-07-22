from uuid import UUID

import psycopg2
from psycopg2.extras import DictCursor

from app.models.schemas.schemas import UserRequest, UserResponse
from app.errors.user_does_not_exist_error import UserDoesNotExist
from app.settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


class UserDBRepository:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserDBRepository, cls).__new__(cls)
            cls.instance.connection = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
        return cls.instance
        
    def create(self, user: UserRequest) -> UserResponse:
        with self.connection.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO users (first_name, last_name, middle_name) VALUES (%s, %s, %s)",
                    (user.first_name, user.last_name, user.middle_name)
                )
                self.connection.commit()
            except psycopg2.Error:
                self.connection.rollback()


    def get_by_id(self, user_id: UUID) -> UserResponse:
        with self.connection.cursor(cursor_factory=DictCursor) as cur:
            try:
                cur.execute(
                    "SELECT user_id AS id_, first_name, last_name, middle_name FROM users WHERE user_id = %s",
                    (user_id,)
                )
                self.connection.commit()
            except psycopg2.Error:
                self.connection.rollback()
            
            user = cur.fetchone()
            if not user:
                raise UserDoesNotExist
            
            return UserResponse(**user)

    def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
        with self.connection.cursor(cursor_factory=DictCursor) as cur:
            try:
                cur.execute(
                    "UPDATE users SET (first_name, last_name, middle_name) = (%s, %s, %s) WHERE user_id = %s",
                    (user.first_name, user.last_name, user.middle_name, user_id)
                )
                self.connection.commit()
            except psycopg2.Error:
                self.connection.rollback()
                raise UserDoesNotExist
            
            new_user_data = user.dict()
            new_user_data['id_'] = user_id
            return UserResponse(**new_user_data)
    
    def delete(self, user_id: UUID) -> None:
        with self.connection.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM users WHERE user_id = %s",
                    (user_id,)
                )
                self.connection.commit()
            except psycopg2.Error:
                self.connection.rollback()
                raise UserDoesNotExist
