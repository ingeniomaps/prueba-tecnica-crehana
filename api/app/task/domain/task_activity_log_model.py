"""Modelo para el registro de actividades realizadas sobre una tarea."""

from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime
from sqlmodel import Field, Relationship, SQLModel

from .task_model import Task
from app.user.domain.user_model import User


class TaskActivityLog(SQLModel, table=True):
    """Representa un registro de actividad relacionada con una tarea específica.

    Esta tabla permite llevar un historial de acciones realizadas sobre las tareas, como:
    - Creación de la tarea.
    - Asignación de responsables.
    - Cambios de estado.
    - Actualizaciones generales.

    Atributos:
        id (UUID): Identificador único del registro de actividad.
        task_id (UUID): Identificador de la tarea afectada.
        performed_by_id (UUID): Identificador del usuario que ejecutó la acción.
        action (str): Tipo de acción realizada (ej. 'created', 'updated', 'assigned').
        performed_at (datetime): Fecha y hora (UTC) en que se realizó la acción.
        extra_metadata (str | None): Información adicional opcional sobre la acción.
    """

    id: UUID = Field(default_factory=uuid4, primary_key=True)  # noqa: A003
    task_id: UUID = Field(foreign_key="task.id")
    performed_by_id: UUID = Field(foreign_key="user.id")
    action: str  # Ej: 'created', 'updated', 'assigned', 'status_changed'
    performed_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True)),
    )
    extra_metadata: Optional[str] = Field(default=None, alias="metadata")

    task: Task = Relationship(back_populates="activity_logs")
    performed_by: User = Relationship()
