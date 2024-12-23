from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_audio_tokens():
    response = client.post(
        "/audio_tokens",
        files={"file": ("audio.wav", b"dummy audio data")},
        headers={"Authorization": "Bearer my_secure_token"},
    )
    assert response.status_code == 200
    assert response.json()["error"] == "Audio token calculation is not supported in this environment."
