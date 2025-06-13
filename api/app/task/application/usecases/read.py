"""Buscar registros."""

from typing import Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.task.domain.task_model import Task
from ..schemas import TaskRead


async def read(db: AsyncSession, filters: TaskRead, skip: int = 0, limit: int = 100) -> list[Task]:
    """Leer registros con filtros opcionales.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        filters (Task): Filtros aplicables.
        skip (int): Cantidad de registros a omitir.
        limit (int): Cantidad máxima de registros a devolver.

    Retorna:
        list[Task]: Registros Encontrados.
    """
    conditions = [
        getattr(Task, field) == value
        for field, value in filters.model_dump(exclude_unset=True).items()
        if getattr(Task, field, None) is not None and value is not None
    ]

    query = select(Task)
    if conditions:
        query = query.where(*conditions)

    query = query.offset(skip).limit(limit)
    result = await db.exec(query)
    return result.all()


async def read_by_id(db: AsyncSession, record_id: str) -> Optional[Task]:
    """Leer un registro por su ID.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        record_id (str): UUID.

    Retorna:
        Task | None: Registro encontrado o None si no existe o es inválido.
    """
    try:
        uuid_obj = UUID(record_id)
    except ValueError:
        return None

    return await db.get(Task, uuid_obj)
