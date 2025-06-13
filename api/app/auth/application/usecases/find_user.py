"""Buscar un usuario."""

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.user.domain.user_model import User


async def find_user(db: AsyncSession, email: str) -> list[User]:
    """Busca un usuario por su correo electrónico.

    Parámetros:
        db_session (AsyncSession): Sesión de base de datos.
        email (str): Correo electrónico.

    Retorna:
        User | None: Objeto de usuario si se encuentra, o None si no existe.
    """
    result = await db.exec(select(User).where(User.email == email))
    return result.first()
