"""Nuevo registro."""

from sqlmodel.ext.asyncio.session import AsyncSession

from app.task.domain.task_model import Task
from ..schemas import TaskCreate


async def create(db: AsyncSession, record_in: TaskCreate) -> Task:
    """Crea un nuevo registro.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        record_in (TaskCreate): Datos para crear un registro.

    Retorna:
        : Objeto creado.
    """
    record = Task(**record_in.model_dump())
    db.add(record)

    await db.commit()
    await db.refresh(record)

    return record
