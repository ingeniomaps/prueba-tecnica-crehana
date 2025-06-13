"""Validar conexión."""

import pytest
from sqlalchemy.exc import OperationalError
from sqlmodel.ext.asyncio.session import AsyncSession

from app.infrastructure.db.session import get_session


async def test_database_connection():
    """Verifica que se puede abrir una sesión con la base de datos PostgreSQL."""
    try:
        async for session in get_session():
            assert isinstance(session, AsyncSession)
    except OperationalError as e:
        pytest.fail(f"No se pudo conectar a la base de datos: {e}")
