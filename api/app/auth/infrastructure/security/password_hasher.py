"""Hasheo de password."""

from passlib.context import CryptContext

# Funciones de utilidades para contraseñas
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hashea una contraseña usando bcrypt.

    :param password: Contraseña en texto plano.
    :return: Contraseña hasheada.
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """Verifica si la contraseña ingresada coincide con el hash.

    :param plain_password: Contraseña en texto plano.
    :param hashed_password: Contraseña previamente hasheada.
    :return: True si coinciden, False en caso contrario.
    """
    return pwd_context.verify(plain_password, hashed_password)
