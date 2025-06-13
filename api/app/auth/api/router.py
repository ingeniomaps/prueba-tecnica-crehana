"""Rutas de autenticación y usuario."""

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession

from app.auth.application.schemas import AuthBase, AuthCreate, AuthLogin
from app.auth.application.usecases.find_user import find_user
from app.auth.application.usecases.register_user import register_user
from app.auth.infrastructure.security.current_user_provider import get_current_user
from app.auth.infrastructure.security.jwt_service import create_access_token
from app.auth.infrastructure.security.password_hasher import hash_password, verify_password
from app.infrastructure.db.session import get_session
from app.user.domain.user_model import User


router = APIRouter()


@router.post("/register", response_model=AuthBase)
async def register(
    user_in: AuthCreate,
    db: AsyncSession = Depends(get_session),  # noqa: B008
):
    """Registra un nuevo usuario.

    - Verifica si ya existe un usuario con el mismo correo.
    - Hashea la contraseña antes de guardarla.
    """
    user = await find_user(db, user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="user_exist")

    user_in.password = hash_password(user_in.password)
    return await register_user(db, user_in)


@router.post("/login")
async def login(
    login_in: AuthLogin,
    db: AsyncSession = Depends(get_session),  # noqa: B008
):
    """Autentica al usuario y genera un token JWT.

    - Verifica credenciales.
    - Retorna token si son válidas.
    """
    user = await find_user(db, login_in.email)
    if not user or not verify_password(login_in.password, user.password):
        raise HTTPException(status_code=401, detail="incorrect_credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout")
async def logout_user():
    """Simula un cierre de sesión.

    Nota: no invalida token JWT (debe hacerse en frontend o con blacklist en backend).
    """
    return {"detail": "logout"}


@router.get("/me", response_model=AuthBase)
async def get_current_authenticated_user(
    current_user: User = Depends(get_current_user),  # noqa: B008
):
    """Retorna los datos del usuario actualmente autenticado."""
    return current_user
