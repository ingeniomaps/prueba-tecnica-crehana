"""Usuarios."""

from datetime import datetime, timezone
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Column, DateTime
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:  # pragma: no cover
    from app.task.domain.task_collaborator_model import TaskCollaborator
    from app.task.domain.task_model import Task


class User(SQLModel, table=True):
    """Mantiene la información de un usuario."""

    id: UUID = Field(default_factory=uuid4, primary_key=True)  # noqa: A003
    name: str = Field(nullable=True)
    email: str
    password: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True)),
    )

    # Relaciones
    created_tasks: list["Task"] = Relationship(
        back_populates="created_by", sa_relationship_kwargs={"foreign_keys": "[Task.created_by_id]"}
    )
    responsible_tasks: list["Task"] = Relationship(
        back_populates="responsible_user",
        sa_relationship_kwargs={"foreign_keys": "[Task.responsible_user_id]"},
    )

    collaborating_tasks: list["TaskCollaborator"] = Relationship(back_populates="user")
