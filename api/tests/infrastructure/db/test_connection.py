"""Validar conexión."""

import pytest
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, select, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from app.infrastructure.db.session import create_database_and_tables, get_session


class TestModel(SQLModel, table=True):
    """Modelo de pruebas."""

    id: int | None = Field(default=None, primary_key=True)
    name: str


async def test_database_connection():
    """Verifica que se puede abrir una sesión con la base de datos PostgreSQL."""
    try:
        async for session in get_session():
            assert isinstance(session, AsyncSession)
    except OperationalError as e:
        pytest.fail(f"No se pudo conectar a la base de datos: {e}")


async def test_create_database_and_tables(monkeypatch):
    """Verifica que se pueden crear tablas."""
    test_engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
    monkeypatch.setattr("app.infrastructure.db.session.engine", test_engine)

    # Agregar el modelo de prueba a la metadata
    TestModel.metadata = SQLModel.metadata

    await create_database_and_tables()

    TestSessionLocal = sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)
    async with TestSessionLocal() as session:
        dummy = TestModel(name="test")
        session.add(dummy)
        await session.commit()

        result = await session.exec(select(TestModel).where(TestModel.name == "test"))
        retrieved = result.first()

        assert retrieved is not None
        assert retrieved.name == "test"
