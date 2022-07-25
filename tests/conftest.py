from uuid import uuid4

from fastapi.testclient import TestClient
import pytest

from app.main import app
from app.models.schemas.schemas import UserRequest, UserResponse


@pytest.fixture
def test_client() -> TestClient:
    client = TestClient(app)
    yield client


@pytest.fixture
def user_request_for_test() -> UserRequest:
    return UserRequest(**
        {
            'first_name': 'Ivan', 
            'last_name': 'Ivanov',
            'middle_name': 'Ivanovich'
        }
    )


@pytest.fixture
def user_response_for_test() -> UserResponse:
    return UserResponse(**
        {
            'id_': '1930eadb-8c5f-488f-8084-3e445042917f',
            'first_name': 'Ivan', 
            'last_name': 'Ivanov',
            'middle_name': 'Ivanovich'
        }
    )
