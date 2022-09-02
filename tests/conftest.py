import json

import pytest
import requests

from src.user.views.models.request import UserRequest


@pytest.fixture
def fake_user() -> UserRequest:
    return UserRequest(
        first_name="Test",
        last_name="Test",
        middle_name="Test"
    )


@pytest.fixture
def id_of_fake_user(fake_user: UserRequest) -> str:
    url = "http://127.0.0.1:8000/users/"
    payload = json.dumps(fake_user.dict())
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        data=payload
    )

    return json.loads(response.text)['id_']


@pytest.fixture
def api_localhost_url() -> str:
    return "http://127.0.0.1:8000/users/"


# import pytest
# import psycopg2
# from fastapi.testclient import TestClient
#
# from app.main import app
# from app.user.models.user import User, UserResponse
# from app.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
# from app.storage.user_in_memory_repository import UserInMemoryRepository
#
#
# @pytest.fixture
# def test_client() -> TestClient:
#     client = TestClient(app)
#     yield client
#
#
# @pytest.fixture
# def user_request_for_test() -> User:
#     return User(**
#         {
#             'first_name': 'Ivan',
#             'last_name': 'Ivanov',
#             'middle_name': 'Ivanovich'
#         }
#                 )
#
#
# @pytest.fixture
# def user_response_for_test() -> UserResponse:
#     return UserResponse(**
#         {
#             'id_': '1930eadb-8c5f-488f-8084-3e445042917f',
#             'first_name': 'Ivan',
#             'last_name': 'Ivanov',
#             'middle_name': 'Ivanovich'
#         }
#     )
#
#
# @pytest.fixture(scope='module')
# def insert_values_db() -> None:
#     with psycopg2.connect(
#             dbname=DB_NAME,
#             user=DB_USER,
#             password=DB_PASSWORD,
#             host=DB_HOST,
#             port=DB_PORT
#     ) as conn:
#         with conn.cursor() as session:
#             session.execute(
#                 """
#                 INSERT INTO
#                     users (id, first_name, middle_name, last_name)
#                 VALUES
#                     ('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa', 'Jayden', 'Sebastian', 'Perez')
#                 """
#             )
#
#
# @pytest.fixture
# def insert_values_in_memory() -> None:
#     user = UserResponse(
#         id_='aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa',
#         first_name='Jayden',
#         middle_name='Sebastian',
#         last_name='Perez'
#     )
#     UserInMemoryRepository().storage = {user.id_: user}
