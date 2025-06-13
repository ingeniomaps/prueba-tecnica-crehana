"""Registro de usuario."""

from sqlmodel import select

from app.auth.application.schemas import AuthCreate
from app.auth.application.usecases.register_user import register_user
from app.user.domain.user_model import User


async def test_register_user_success(session):
    """Caso: Nuevo usuario."""
    user_data = AuthCreate(email="new@example.com", password="test123")
    user = await register_user(session, user_data)

    assert user.id is not None
    assert user.email == user_data.email
    assert isinstance(user, User)


async def test_register_user_persists_in_db(session, registered_user):
    """Caso: Usuario registrado."""
    user_data = AuthCreate(email=registered_user["email"], password=registered_user["password"])
    await register_user(session, user_data)

    result = await session.exec(select(User).where(User.email == user_data.email))
    user = result.first()

    assert user is not None
    assert user.email == user_data.email
