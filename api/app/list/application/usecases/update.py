"""Actualizar registros."""

from sqlmodel.ext.asyncio.session import AsyncSession

from app.list.domain.list_model import List


async def update(db: AsyncSession, record: List, updates: dict) -> List:
    """Actualizar registro.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        record (List): Objeto existente.
        updates (dict): Campos a actualizar.

    Retorna:
        List: Objeto actualizado.
    """
    for field, value in updates.items():
        setattr(record, field, value)

    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record
