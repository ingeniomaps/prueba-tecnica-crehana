"""Modelo para representar listas de tareas dentro de un proyecto."""

from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:  # pragma: no cover
    from app.task.domain.task_model import Task


class List(SQLModel, table=True):
    """Representa una lista de tareas agrupadas por estado o etapa del proyecto.

    Ejemplos comunes de listas:
        - "Por hacer" (To Do)
        - "En progreso" (In Progress)
        - "Hecho" (Done)

    Atributos:
        id (UUID): Identificador único de la lista.
        name (str): Nombre descriptivo de la lista.
        tasks (List[Task]): Tareas asociadas a esta lista.
    """

    id: UUID = Field(default_factory=uuid4, primary_key=True)  # noqa: A003
    name: str
    is_active: bool = Field(default=True)

    tasks: list["Task"] = Relationship(back_populates="task_list")
