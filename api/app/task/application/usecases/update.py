"""Actualizar registros."""

from sqlmodel.ext.asyncio.session import AsyncSession

from app.task.domain.task_model import Task


async def update(db: AsyncSession, record: Task, updates: dict) -> Task:
    """Actualizar registro.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        record (Task): Objeto existente.
        updates (dict): Campos a actualizar.

    Retorna:
        Task: Objeto actualizado.
    """
    for field, value in updates.items():
        setattr(record, field, value)

    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record
