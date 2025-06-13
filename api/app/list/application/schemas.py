"""Esquemas Pydantic para la entidad List."""

from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ListBase(BaseModel):
    """Esquema base."""

    id: UUID  # noqa: A003
    name: str
    is_active: bool


class ListCreate(BaseModel):
    """Esquema utilizado al crear un nuevo registro."""

    name: str


class ListRead(BaseModel):
    """Esquema de entrada para aplicar filtros."""

    name: Optional[str] = None
    is_active: Optional[bool] = None


class ListUpdate(BaseModel):
    """Esquema utilizado para actualizar."""

    name: str
