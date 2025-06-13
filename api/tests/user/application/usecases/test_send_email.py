"""Envió de correos."""

from app.user.application.usecases.send_email import send_email


async def test_send_email_success():
    """Caso: Emulación de envió de correos."""
    result = await send_email(
        to_email="user@example.com", subject="Bienvenido", body="Este es un correo de prueba."
    )

    assert result is True
