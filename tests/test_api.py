import time
from pathlib import Path

import jwt
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from fastapi.testclient import TestClient
from starlette.requests import Request

from app.main import create_app, legacy_identity


@pytest.fixture
def auth_context(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key_path = tmp_path / "jwt-public-key.pem"
    public_key_path.write_bytes(
        private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )
    monkeypatch.setenv("AUTH_TOKEN_PUBLIC_KEY_LOCATION", str(public_key_path))
    app = create_app(str(tmp_path / "workshop.db"), str(tmp_path / "uploads"))
    with TestClient(app) as client:
        yield client, private_key, app


def token(
    private_key: rsa.RSAPrivateKey,
    username: str = "student",
    roles: tuple[str, ...] = ("STUDENT",),
    expires_in: int = 3600,
) -> str:
    now = int(time.time())
    return jwt.encode(
        {"sub": username, "groups": list(roles), "iat": now, "exp": now + expires_in},
        private_key,
        algorithm="RS256",
    )


def headers(private_key: rsa.RSAPrivateKey, roles: tuple[str, ...] = ("STUDENT",)) -> dict[str, str]:
    return {"Authorization": f"Bearer {token(private_key, roles=roles)}"}


def test_lists_seeded_tasks(auth_context) -> None:
    client, private_key, _ = auth_context
    response = client.get("/api/tasks", headers=headers(private_key))
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_creates_task_and_summary(auth_context) -> None:
    client, private_key, _ = auth_context
    created = client.post(
        "/api/tasks",
        headers=headers(private_key),
        json={"title": "Add tests", "description": "Improve coverage", "status": "TODO", "priority": "HIGH"},
    )
    summary = client.get("/api/summary", headers=headers(private_key))
    assert created.status_code == 201
    assert created.json()["owner"] == "student"
    assert summary.json()["total"] == 3


def test_uploads_requirement(auth_context, tmp_path: Path) -> None:
    client, private_key, _ = auth_context
    response = client.post(
        "/api/requirements",
        headers=headers(private_key),
        files={"file": ("requirements.txt", b"Login must be accessible", "text/plain")},
    )
    assert response.status_code == 201
    assert (tmp_path / "uploads" / "requirements.txt").exists()


def test_accepts_jwt_with_multiple_roles(auth_context) -> None:
    client, private_key, app = auth_context
    authorization = headers(private_key, ("STUDENT", "TRAINER"))["Authorization"]
    request = Request({"type": "http", "app": app, "headers": []})
    identity = legacy_identity(request, authorization)

    response = client.get("/api/tasks", headers={"Authorization": authorization})

    assert response.status_code == 200
    assert identity == {"username": "student", "roles": ["STUDENT", "TRAINER"]}


def test_rejects_invalid_token(auth_context) -> None:
    client, _, _ = auth_context
    response = client.get("/api/tasks", headers={"Authorization": "Bearer invalid"})
    assert response.status_code == 401


def test_rejects_token_signed_by_another_key(auth_context) -> None:
    client, _, _ = auth_context
    other_private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    response = client.get("/api/tasks", headers=headers(other_private_key))
    assert response.status_code == 401


def test_rejects_expired_token(auth_context) -> None:
    client, private_key, _ = auth_context
    expired_token = token(private_key, expires_in=-1)
    response = client.get("/api/tasks", headers={"Authorization": f"Bearer {expired_token}"})
    assert response.status_code == 401
