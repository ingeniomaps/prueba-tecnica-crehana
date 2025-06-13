"""Creación y decodificación de tokens."""

from datetime import datetime, timedelta, timezone
import os

from jose import jwt, JWTError


# Configuración de JWT y Seguridad
SECRET_KEY = os.getenv("SECRET_KEY", "0123456789")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Crea un token JWT firmado con los datos especificados.

    :param data: Información que se codificará en el token.
    :param expires_delta: Tiempo de expiración personalizado (opcional).
    :return: Token JWT como string.
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str):
    """Decodifica un token JWT.

    :param token: Token JWT codificado.
    :return: Diccionario con el contenido del token o None si es inválido.
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
