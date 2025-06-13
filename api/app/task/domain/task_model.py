"""Modelo de tarea."""

from datetime import datetime, timezone
from typing import Any, Optional, TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime, JSON
from sqlmodel import Field, Relationship, SQLModel

from app.list.domain.list_model import List
from app.user.domain.user_model import User

if TYPE_CHECKING:
    from .task_activity_log_model import TaskActivityLog
    from .task_collaborator_model import TaskCollaborator


class Task(SQLModel, table=True):
    """Representa una tarea dentro de un sistema de gestión de proyectos.

    Atributos:
        id (UUID): Identificador único de la tarea.
        title (str): Título descriptivo de la tarea.
        description (Optional[str]): Detalle adicional de la tarea.
        status (str): Estado actual de la tarea ('pending', 'in_progress', 'completed').
        priority (str): Nivel de prioridad ('low', 'medium', 'high', 'urgent').
        progress (int): Porcentaje de avance (0 a 100).
        due_date (Optional[datetime]): Fecha límite para completar la tarea.
        created_at (datetime): Fecha de creación de la tarea.
        created_by_id (UUID): Usuario que creó la tarea.
        responsible_user_id (UUID): Usuario responsable de ejecutar la tarea.
        task_list_id (UUID): Lista de tareas a la que pertenece.

    Relaciones:
        created_by (User): Usuario creador.
        responsible_user (User): Usuario responsable.
        task_list (List): Lista a la que pertenece la tarea.
        collaborators (List[TaskCollaborator]): Colaboradores asignados.
        activity_logs (List[TaskActivityLog]): Registro de actividades.
    """

    id: UUID = Field(default_factory=uuid4, primary_key=True)  # noqa: A003
    title: str
    description: Optional[str] = None
    status: str  # Ej: 'pending', 'in_progress', 'completed'
    priority: str  # Ej: 'low', 'medium', 'high', 'urgent'
    progress: int = Field(default=0, ge=0, le=100)
    due_date: Optional[datetime] = None

    extra_metadata: Optional[dict[str, Any]] = Field(
        sa_column=Column(JSON), default=None, alias="metadata"
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True)),
    )

    created_by_id: UUID = Field(foreign_key="user.id")
    responsible_user_id: UUID = Field(foreign_key="user.id", nullable=True)
    task_list_id: UUID = Field(foreign_key="list.id")

    created_by: User = Relationship(
        back_populates="created_tasks",
        sa_relationship_kwargs={"foreign_keys": "[Task.created_by_id]"},
    )

    responsible_user: User = Relationship(
        back_populates="responsible_tasks",
        sa_relationship_kwargs={"foreign_keys": "[Task.responsible_user_id]"},
    )

    task_list: List = Relationship(back_populates="tasks")
    collaborators: list["TaskCollaborator"] = Relationship(back_populates="task")
    activity_logs: list["TaskActivityLog"] = Relationship(back_populates="task")
