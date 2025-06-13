"""Algo."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.auth.infrastructure.security.jwt_service import decode_token
from app.infrastructure.db.session import get_session
from app.user.domain.user_model import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_session)  # noqa: B008
):
    """Obtiene el usuario autenticado a partir del token JWT.

    :param token: Token JWT obtenido del encabezado Authorization.
    :param db: Sesión de base de datos asíncrona.
    :return: Instancia del usuario autenticado.
    :raises HTTPException: Si el token es inválido o el usuario no existe.
    """
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid_token")

    user = await db.exec(select(User).where(User.email == payload["sub"]))
    user = user.first()
    if not user:
        raise HTTPException(status_code=404, detail="user_not_found")

    return user
