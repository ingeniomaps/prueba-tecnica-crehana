"""Algo."""

from httpx import AsyncClient
from main import app
import pytest
from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

from app.infrastructure.db.session import get_session


# Setup de prueba para la base de datos en memoria
DATABASE_URL = "sqlite+aiosqlite://"
engine = create_async_engine(DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(engine, class_=SQLAlchemyAsyncSession, expire_on_commit=False)


async def override_get_session():
    """Sobrescribimos el get_session con uno de prueba."""
    async with TestingSessionLocal() as session:
        yield session


app.dependency_overrides[get_session] = override_get_session


# @pytest.fixture(scope="module")
@pytest.mark.asyncio
async def client():
    """Algo."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
