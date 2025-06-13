"""Esquemas Pydantic para la entidad Task."""

from datetime import datetime
from typing import Any, Literal, Optional
from uuid import UUID

from pydantic import BaseModel
from sqlmodel import Field


class TaskBase(BaseModel):
    """Esquema base."""

    id: UUID  # noqa: A003
    title: str
    description: str
    status: str  # Literal["pending", "in_progress", "completed"]
    priority: str  # Ej: 'low', 'medium', 'high', 'urgent'
    progress: int
    due_date: datetime
    created_at: datetime
    created_by_id: UUID
    responsible_user_id: UUID | None = None
    task_list_id: UUID
    extra_metadata: Optional[dict[str, Any]] = Field(default=None, alias="metadata")

    class Config:
        """Configuración."""

        allow_population_by_field_name = True


class TaskCreate(BaseModel):
    """Esquema utilizado al crear un nuevo registro."""

    title: str
    description: str
    status: Literal["pending", "in_progress", "completed"]
    priority: Literal["low", "medium", "high", "urgent"]
    due_date: datetime
    created_by_id: UUID
    task_list_id: UUID
    extra_metadata: Optional[dict[str, Any]] = Field(default=None, alias="metadata")

    class Config:
        """Configuración."""

        allow_population_by_field_name = True


class TaskRead(BaseModel):
    """Esquema de entrada para aplicar filtros."""

    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    progress: Optional[int] = None
    due_date: Optional[datetime] = None
    responsible_user_id: Optional[UUID] = None
    task_list_id: Optional[UUID] = None

    created_at: Optional[datetime] = None
    created_by_id: Optional[UUID] = None


class TaskUpdate(BaseModel):
    """Esquema utilizado para actualizar."""

    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    progress: Optional[int] = None
    due_date: Optional[datetime] = None
    responsible_user_id: Optional[UUID] = None
    task_list_id: Optional[UUID] = None
