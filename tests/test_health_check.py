from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health", headers={"Authorization": "Bearer my_secure_token"})
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_health_check_unauthorized():
    response = client.get("/health")
    assert response.status_code == 401
