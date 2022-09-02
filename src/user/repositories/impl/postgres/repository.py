from datetime import datetime
from uuid import UUID, uuid4

import psycopg2
from psycopg2.extras import DictCursor

from src.user.models.user import User
from src.user.models.user_in_db import UserInDB
from src.user.repositories.core.exceptions import DBCantHandleQuery, UserDoesNotExist
from src.user.repositories.core.user_repository import IUserRepository
from src.user.repositories.impl.postgres.connection.creator import PostgresConnection


class UserPostgresRepository(IUserRepository):
    __slots__ = ('__connection',)

    def __init__(self, connection: PostgresConnection) -> None:
        self.__connection = connection
        
    def create(self, user: User) -> UserInDB:
        user_response = UserInDB(**user.dict(), id_=uuid4())

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

    def get_by_id(self, user_id: UUID) -> UserInDB:
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
                        raise UserDoesNotExist()
                    user = cur.fetchone()
        except psycopg2.Error as err:
            raise DBCantHandleQuery(str(err))
        return UserInDB(**user)

    def update(self, user_id: UUID, user: User) -> UserInDB:
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
            
        new_user_data = user.dict()
        new_user_data.update({'id_': user_id})
        return UserInDB(**new_user_data)
    
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
