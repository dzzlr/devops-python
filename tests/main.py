from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_main_without_token():
    response = client.get("/")
    assert response.status_code == 422

def test_main_with_token():
    response = client.get("/?token=jessica")
    assert response.status_code == 200
    assert response.json() == {
        "code": 200, 
        "message": "Hello Bigger Applications!"
    }
