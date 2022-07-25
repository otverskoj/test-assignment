from datetime import datetime
from uuid import UUID, uuid4

import psycopg2
from psycopg2.extras import DictCursor

from app.models.schemas.schemas import UserRequest, UserResponse
from app.errors.user_does_not_exist_error import UserDoesNotExist
from app.errors.db_cant_handle_query_error import DBCantHandleQuery
from app.settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from app.storage.base_repository import UserRepository


class UserDBRepository(UserRepository):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserDBRepository, cls).__new__(cls)
            cls.instance._connection = cls.instance._connect()
        return cls.instance

    def _connect(cls):
        if hasattr(cls.instance, '_connection') and cls.instance._connection:
            return cls.instance._connection
        
        return psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

    def close_connection(self) -> None:
        if self._connection:
            self._connection.close()
        
    def create(self, user: UserRequest) -> UserResponse:
        user_response = UserResponse(**user.dict(), id_=uuid4())

        cur = self._connection.cursor()
        to_insert = (
            str(user_response.id_), user_response.first_name,
            user_response.last_name, user_response.middle_name
        )

        with self._connection.cursor() as cur:
            to_insert = (
                str(user_response.id_), user_response.first_name,
                user_response.last_name, user_response.middle_name
            )
            try:
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
                self._connection.rollback()
                raise DBCantHandleQuery(str(err))
            else:
                self._connection.commit()
        
        return user_response


    def get_by_id(self, user_id: UUID) -> UserResponse:
        with self._connection.cursor(cursor_factory=DictCursor) as cur:
            try:
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
            except psycopg2.Error as err:
                self._connection.rollback()
                raise DBCantHandleQuery(str(err))
            else:
                if cur.rowcount == 0:
                    raise UserDoesNotExist
                user = cur.fetchone()
                self._connection.commit()
        return UserResponse(**user)

    def update(self, user_id: UUID, user: UserRequest) -> UserResponse:
        with self._connection.cursor(cursor_factory=DictCursor) as cur:
            to_update = (
                user.first_name, user.last_name, user.middle_name,
                datetime.now(), str(user_id)
            )
            try:
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
                self._connection.rollback()
                raise DBCantHandleQuery(str(err))
            else:
                self._connection.commit()
            
        new_user_data = user.dict() | {'id_': user_id}
        return UserResponse(**new_user_data)
    
    def delete(self, user_id: UUID) -> None:
        with self._connection.cursor() as cur:
            try:
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
                self._connection.rollback()
                raise DBCantHandleQuery(str(err))
            else:
                self._connection.commit()
