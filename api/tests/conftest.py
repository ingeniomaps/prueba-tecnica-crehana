"""Configuración de pruebas con base de datos en memoria."""

from fastapi import FastAPI
from httpx import ASGITransport
from httpx import AsyncClient
from main import app as fastapi_app
import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from app.infrastructure.db.session import get_session


# URL de la base de datos en memoria (SQLite con soporte async)
DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def anyio_backend():
    """Define el backend que usará AnyIO para pruebas async."""
    return "asyncio"


@pytest.fixture(scope="session")
def app() -> FastAPI:
    """Retorna la aplicación FastAPI para usarla en las pruebas."""
    return fastapi_app


@pytest.fixture(scope="session")
async def engine() -> AsyncEngine:
    """Base de datos.

    Crea una base de datos en memoria y genera las tablas a partir de los modelos.
    Se utiliza durante toda la sesión de pruebas.
    """
    engine = create_async_engine(DATABASE_URL, echo=False)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    yield engine
    await engine.dispose()


@pytest.fixture
async def session(engine: AsyncEngine) -> AsyncSession:
    """Nueva sesión de base de datos. Asegura aislamiento entre pruebas individuales."""
    async with AsyncSession(engine) as session:
        yield session


@pytest.fixture
async def client(app: FastAPI, session: AsyncSession) -> AsyncClient:
    """Cliente HTTP.

    Crea un cliente HTTP asincrónico para hacer peticiones a la app durante las pruebas.
    Sobrescribe la dependencia de `get_session` para usar la sesión de prueba.
    """

    def _get_test_session():
        return session

    app.dependency_overrides[get_session] = _get_test_session

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()


@pytest.fixture
def test_user_data():
    """Diccionario con los datos de un usuario de prueba."""
    return {"email": "test@example.com", "password": "test1234"}


@pytest.fixture
async def registered_user(client, test_user_data):
    """Registra el usuario si no existe."""
    response = await client.post("/auth/register", json=test_user_data)

    if response.status_code not in (200, 400):
        pass

    return test_user_data


@pytest.fixture
async def authorization_user(client, registered_user):
    """Genera un token para la sesión."""
    response = await client.post("/auth/login", json=registered_user)

    return {"Authorization": f"Bearer {response.json()["access_token"]}"}
