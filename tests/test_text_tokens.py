import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_text_tokens():
    response = client.post(
        "/text_tokens",
        json={"text": "Hello, world!", "model_name": "gpt-3.5"},
        headers={"Authorization": "Bearer my_secure_token"},
    )
    assert response.status_code == 200
    assert "tokens" in response.json()


def test_text_tokens_invalid_model():
    response = client.post(
        "/text_tokens",
        json={"text": "Hello, world!", "model_name": "invalid-model"},
        headers={"Authorization": "Bearer my_secure_token"},
    )
    assert response.status_code == 422


def test_text_tokens_unauthorized():
    response = client.post(
        "/text_tokens",
        json={"text": "Hello, world!", "model_name": "gpt-3.5"},
    )
    assert response.status_code == 401