"""Basic test coverage for the API."""

from fastapi.testclient import TestClient

from app.main import create_app


def test_health_check():
    client = TestClient(create_app())
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert isinstance(response.json()["uptime_seconds"], float)


def test_create_and_fetch_challenge():
    client = TestClient(create_app())
    payload = {
        "title": "Test challenge",
        "description": "A test challenge for the API.",
        "difficulty": "medium",
        "tags": ["test", "api"],
    }

    create_resp = client.post("/challenges", json=payload)
    assert create_resp.status_code == 201
    created = create_resp.json()
    assert created["title"] == payload["title"]
    assert created["difficulty"] == payload["difficulty"]

    get_resp = client.get(f"/challenges/{created['id']}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == created["id"]


def test_get_missing_challenge_returns_404():
    client = TestClient(create_app())
    response = client.get("/challenges/999999")
    assert response.status_code == 404
