"""Endpoints para manejar listas de tareas."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.auth.infrastructure.security.current_user_provider import get_current_user
from app.infrastructure.db.session import get_session
from app.user.domain.user_model import User
from ..application.schemas import (
    ListBase,
    ListCreate,
    ListRead,
    ListUpdate,
)
from ..application.usecases.create import create
from ..application.usecases.delete import delete
from ..application.usecases.read import read, read_by_id
from ..application.usecases.update import update

router = APIRouter()


@router.post("/", response_model=ListBase, status_code=201)
async def create_service(
    record_in: ListCreate,
    db: AsyncSession = Depends(get_session),  # noqa: B008
    current_user: User = Depends(get_current_user),
):
    """Crea un nuevo registro."""
    return await create(db, record_in)


@router.get("/", response_model=List[ListBase])
async def read_service(
    filters: ListRead = Depends(),  # noqa: B008
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_session),  # noqa: B008
    current_user: User = Depends(get_current_user),
):
    """Obtiene una lista de registros con filtros, paginación y límites."""
    return await read(db, filters, skip, limit)


@router.get("/{record_id}", response_model=ListBase)
async def read_by_id_service(
    record_id: str,
    db: AsyncSession = Depends(get_session),  # noqa: B008
    current_user: User = Depends(get_current_user),
):
    """Obtiene un registro por su ID."""
    if not record_id:
        raise HTTPException(status_code=404, detail="required_id")

    record = await read_by_id(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="record_not_found")

    return record


@router.patch("/{record_id}", response_model=ListBase)
async def update_service(
    record_id: str,
    record_update: ListUpdate,
    db: AsyncSession = Depends(get_session),  # noqa: B008
    current_user: User = Depends(get_current_user),
):
    """Actualiza una lista por su ID."""
    record = await read_by_id(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="record_not_found")

    return await update(db, record, record_update.model_dump(exclude_unset=True))


@router.delete("/{record_id}", status_code=200)
async def delete_service(
    record_id: str,
    db: AsyncSession = Depends(get_session),  # noqa: B008
    current_user: User = Depends(get_current_user),
):
    """Elimina por su ID."""
    record = await read_by_id(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="record_not_found")

    is_deleted = await delete(db, record)
    if not is_deleted:
        raise HTTPException(status_code=500, detail="record_not_deleted")

    return {"detail": "record_deleted"}
