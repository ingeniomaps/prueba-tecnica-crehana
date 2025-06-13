"""Aplicación FastAPI con ciclo de vida y enrutadores."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.auth.api.router import router as auth_router
from app.infrastructure.db.session import create_database_and_tables
from app.list.api.router import router as list_router
from app.task.api.router import router as task_router
from app.user.api.router import router as user_router


@asynccontextmanager
async def startup_and_shutdown_events(app: FastAPI):
    """Función de contexto para manejar el ciclo de vida de la aplicación.

    Esta función se ejecuta al iniciar y detener la aplicación.
    Aquí se pueden realizar tareas de inicialización, como crear tablas en la base de datos.
    """
    await create_database_and_tables()
    yield


# Instancia principal
app = FastAPI(
    lifespan=startup_and_shutdown_events,
    title="Api de tareas",
    description="Prueba Técnica de un sistema de tareas.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Registro de los enrutadores
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(list_router, prefix="/list", tags=["List"])
app.include_router(task_router, prefix="/task", tags=["Task"])
app.include_router(user_router, prefix="/user", tags=["User"])
