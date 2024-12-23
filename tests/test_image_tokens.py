from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_image_tokens():
    response = client.post(
        "/image_tokens",
        files={"file": ("image.png", b"dummy image data")},
        headers={"Authorization": "Bearer my_secure_token"},
    )
    assert response.status_code == 200
    assert response.json()["error"] == "Image token calculation is not supported in this environment."
