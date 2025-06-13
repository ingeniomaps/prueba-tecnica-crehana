"""Modelo de relación muchos a muchos entre tareas y colaboradores."""

from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

from .task_model import Task
from app.user.domain.user_model import User


class TaskCollaborator(SQLModel, table=True):
    """Representa una relación muchos-a-muchos entre usuarios y tareas.

    Este modelo actúa como tabla intermedia para asociar múltiples usuarios
    como colaboradores en una tarea, y viceversa.

    Atributos:
        id (UUID): Identificador único de la relación.
        task_id (UUID): ID de la tarea en la que colabora el usuario.
        user_id (UUID): ID del usuario que colabora en la tarea.
    """

    id: UUID = Field(default_factory=uuid4, primary_key=True)  # noqa: A003
    task_id: UUID = Field(foreign_key="task.id")
    user_id: UUID = Field(foreign_key="user.id")

    task: Task = Relationship(back_populates="collaborators")
    user: User = Relationship(back_populates="collaborating_tasks")
