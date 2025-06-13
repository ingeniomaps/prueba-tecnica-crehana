"""Rutas de autenticación y usuario."""

from fastapi import APIRouter, Depends

from app.auth.infrastructure.security.current_user_provider import get_current_user
from app.user.application.schemas import EmailRequest
from app.user.application.usecases.send_email import send_email
from app.user.domain.user_model import User


router = APIRouter()


@router.post("/board/invite")
async def invite_user(
    email_in: EmailRequest,
    current_user: User = Depends(get_current_user),
):
    """Enviar un correo."""
    await send_email(email_in.email, email_in.subject, email_in.body)
    return {"code": "send_email"}
