from datetime import datetime
from uuid import UUID, uuid4

import psycopg2
from psycopg2.extras import DictCursor

from app.models.schemas.schemas import UserRequest, UserResponse
from app.errors.user_does_not_exist_error import UserDoesNotExist
from app.errors.db_cant_handle_query_error import DBCantHandleQuery
from app.storage.repositories.user_repository import IUserRepository


class UserPostgresRepository(IUserRepository):
    # def __new__(cls, connection: psycopg2.extensions.connection):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(UserPostgresRepository, cls).__new__(cls)
    #         cls.instance._connection = connection
    #     return cls.instance

    __slots__ = ('__connection',)

    def __init__(self, connection: psycopg2.extensions.connection) -> None:
        self.__connection = connection
        
    def create(self, user: UserRequest) -> UserResponse:
        user_response = UserResponse(**user.dict(), id_=uuid4())

        to_insert = (
            str(user_response.id_), user_response.first_name,
            user_response.last_name, user_response.middle_name
        )
        try:
            with self.__connection:
                with self.__connection.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO 
                            users (id, first_name, last_name, middle_name)
                        VALUES
                            (%s, %s, %s, %s);
                        """,
                        to_insert
                    )
        except psycopg2.Error as err:
            raise DBCantHandleQuery(str(err))
        return user_response

    def get_by_id(self, user_id: UUID) -> UserResponse:
        try:
            with self.__connection:
                with self.__connection.cursor(cursor_factory=DictCursor) as cur:
                    cur.execute(
                        """
                        SELECT
                            id AS id_, first_name, last_name, middle_name
                        FROM
                            users
                        WHERE
                            id = %s;
                        """,
                        (str(user_id),)
                    )
                    if cur.rowcount == 0:
                        raise UserDoesNotExist
                    user = cur.fetchone()
        except psycopg2.Error as err:
            raise DBCantHandleQuery(str(err))
        return UserResponse(**user)

    def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
        to_update = (
            user.first_name, user.last_name, user.middle_name,
            datetime.now(), str(user_id)
        )

        try:
            with self.__connection:
                with self.__connection.cursor(cursor_factory=DictCursor) as cur:
                    cur.execute(
                        """
                        UPDATE 
                            users 
                        SET 
                            (first_name, last_name, middle_name, updated_at) = (%s, %s, %s, %s) 
                        WHERE 
                            id = %s;
                        """,
                        to_update
                    )
        except psycopg2.Error as err:
            raise DBCantHandleQuery(str(err))
            
        new_user_data = user.dict() | {'id_': user_id}
        return UserResponse(**new_user_data)
    
    def delete(self, user_id: UUID) -> None:
        try:
            with self.__connection:
                with self.__connection.cursor() as cur:
                    cur.execute(
                        """
                        DELETE FROM 
                            users 
                        WHERE
                            id = %s;
                        """,
                        (str(user_id),)
                    )
        except psycopg2.Error as err:
            raise DBCantHandleQuery(str(err))
