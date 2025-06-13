"""Configuración y creación de la base de datos con SQLModel y PostgreSQL."""

import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

"""Carga las variables de entorno desde un archivo `.env`."""
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "admin12345")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "local")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


"""Crea una instancia del motor asincrónico de SQLAlchemy."""
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)


async def create_database_and_tables():
    """Crea la base de datos y las tablas definidas en los modelos SQLModel."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


"""Se crean sesiones asíncronas utilizando `sessionmaker`."""
AsyncSessionLocal = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Obtiene la sesión de la base de datos."""
    async with AsyncSessionLocal() as session:
        yield session
