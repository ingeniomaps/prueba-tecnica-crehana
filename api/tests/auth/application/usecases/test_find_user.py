"""Buscar usuarios."""

from app.auth.application.usecases.find_user import find_user
from app.user.domain.user_model import User


async def test_find_user_exists(session, registered_user):
    """Caso: Usuario existe."""
    user = User(email=registered_user["email"], password=registered_user["password"])
    session.add(user)
    await session.commit()
    await session.refresh(user)

    result = await find_user(session, registered_user["email"])

    assert result is not None
    assert result.email == registered_user["email"]
    assert isinstance(result, User)


async def test_find_user_not_exists(session):
    """Caso: Usuario no existe."""
    result = await find_user(session, "no-existe@example.com")

    assert result is None
