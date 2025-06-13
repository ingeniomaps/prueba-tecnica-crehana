"""Validación de token."""

from datetime import timedelta

from app.auth.infrastructure.security.jwt_service import create_access_token, decode_token


def test_create_access_token_structure():
    """Caso: Token JWT válido como string."""
    data = {"sub": "usuario@example.com"}
    token = create_access_token(data)

    assert isinstance(token, str)
    assert token.count(".") == 2


def test_decode_token_valid_token():
    """Caso: Decodificar correctamente un token válido."""
    data = {"sub": "usuario@example.com"}
    token = create_access_token(data)
    decoded = decode_token(token)

    assert decoded is not None
    assert decoded["sub"] == "usuario@example.com"
    assert "exp" in decoded


def test_decode_token_expired(monkeypatch):
    """Caso: Token expiró."""
    data = {"sub": "usuario@example.com"}
    token = create_access_token(data, expires_delta=timedelta(seconds=-1))
    decoded = decode_token(token)

    assert decoded is None


def test_decode_token_invalid():
    """Caso: Token inválido (firmado con clave distinta)."""
    token = "ey.invalid.token"
    decoded = decode_token(token)

    assert decoded is None
