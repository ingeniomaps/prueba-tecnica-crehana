"""Esquemas (schemas) de datos utilizados en operaciones relacionadas con usuarios."""

from uuid import UUID

from pydantic import BaseModel, EmailStr


class AuthBase(BaseModel):
    """Esquema base con los campos mínimos compartidos."""

    id: UUID  # noqa: A003
    email: EmailStr


class AuthCreate(BaseModel):
    """Esquema para la creación."""

    email: EmailStr
    password: str


class AuthLogin(BaseModel):
    """Esquema utilizado para iniciar sesión."""

    email: EmailStr
    password: str


class AuthRead(BaseModel):
    """Esquema para representar la información de un usuario."""

    id: UUID  # noqa: A003
    name: str
    email: EmailStr
