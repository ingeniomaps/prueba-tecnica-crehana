"""Buscar registros."""

from typing import Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.list.domain.list_model import List
from ..schemas import ListRead


async def read(db: AsyncSession, filters: ListRead, skip: int = 0, limit: int = 100) -> list[List]:
    """Leer registros con filtros opcionales.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        filters (List): Filtros aplicables.
        skip (int): Cantidad de registros a omitir.
        limit (int): Cantidad máxima de registros a devolver.

    Retorna:
        list[List]: Registros Encontrados.
    """
    conditions = [
        getattr(List, field) == value
        for field, value in filters.model_dump(exclude_unset=True).items()
        if getattr(List, field, None) is not None and value is not None
    ]

    query = select(List)
    if conditions:
        query = query.where(*conditions)

    query = query.offset(skip).limit(limit)
    result = await db.exec(query)
    return result.all()


async def read_by_id(db: AsyncSession, record_id: str) -> Optional[List]:
    """Leer un registro por su ID.

    Parámetros:
        db (AsyncSession): Sesión de base de datos.
        record_id (str): UUID.

    Retorna:
        List | None: Registro encontrado o None si no existe o es inválido.
    """
    try:
        uuid_obj = UUID(record_id)
    except ValueError:
        return None

    return await db.get(List, uuid_obj)
