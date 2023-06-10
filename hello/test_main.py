import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_item():
    response = client.post("/items/", json={"name": "Foo", "price": 45.2})
    assert response.status_code == 200
    assert response.json() == {"name": "Foo", "price": 45.2, "is_offer": None}
