"""Registro de usuario."""

from sqlmodel.ext.asyncio.session import AsyncSession

from app.auth.application.schemas import AuthCreate
from app.user.domain.user_model import User


async def register_user(db: AsyncSession, record_in: AuthCreate) -> User:
    """Crea un nuevo usuario a partir de los datos proporcionados.

    Parámetros:
        db_session (AsyncSession): Sesión de base de datos.
        record_in (AuthCreate): Datos proporcionados.

    Retorna:
        User: Objeto creado.
    """
    record = User(**record_in.model_dump())
    db.add(record)

    await db.commit()
    await db.refresh(record)

    return record
