"""Envió de email."""

from pydantic import BaseModel, EmailStr


class EmailRequest(BaseModel):
    """Estructura para envió de emails."""

    email: EmailStr
    subject: str
    body: str
