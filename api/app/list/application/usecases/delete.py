"""Eliminar registros."""

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel.ext.asyncio.session import AsyncSession

from app.list.domain.list_model import List


async def delete(db: AsyncSession, record: List) -> bool:
    """Eliminar un registro.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        record (List): Objeto a eliminar.

    Retorna:
        bool: True si fue eliminado exitosamente, False si hubo error.
    """
    try:
        await db.delete(record)
        await db.commit()
        return True
    except SQLAlchemyError:
        await db.rollback()
        return False
