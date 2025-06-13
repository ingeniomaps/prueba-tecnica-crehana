"""Nuevo registro."""

from sqlmodel.ext.asyncio.session import AsyncSession

from app.list.domain.list_model import List
from ..schemas import ListCreate


async def create(db: AsyncSession, record_in: ListCreate) -> List:
    """Crea un nuevo registro.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        record_in (ListCreate): Datos para crear un registro.

    Retorna:
        : Objeto creado.
    """
    record = List(**record_in.model_dump())
    db.add(record)

    await db.commit()
    await db.refresh(record)

    return record
