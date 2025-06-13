"""Validación de usuario."""

from fastapi import HTTPException
import pytest

from app.auth.infrastructure.security.current_user_provider import get_current_user
from app.auth.infrastructure.security.jwt_service import create_access_token
from app.user.domain.user_model import User


async def test_get_current_user_valid_token(session, registered_user):
    """Caso: Si el token es válido y el usuario existe."""
    user = User(email=registered_user["email"], password=registered_user["password"])
    session.add(user)
    await session.commit()
    await session.refresh(user)

    token = create_access_token({"sub": user.email})
    result = await get_current_user(token=token, db=session)

    assert result is not None
    assert result.email == user.email


async def test_get_current_user_invalid_token(session):
    """Caso: Si el token es inválido o no tiene 'sub'."""
    invalid_token = "invalid_token"

    with pytest.raises(HTTPException) as exc_info:
        await get_current_user(token=invalid_token, db=session)

    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "invalid_token"


async def test_get_current_user_user_not_found(session):
    """Caso: Si el token es válido pero el usuario no existe."""
    token = create_access_token({"sub": "no_exist@example.com"})

    with pytest.raises(HTTPException) as exc_info:
        await get_current_user(token=token, db=session)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "user_not_found"
