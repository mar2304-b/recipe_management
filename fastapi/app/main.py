from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from config.database import database as connection
from routes.user_role import user_role_router
from routes.family import family_router
from routes.user import user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Maneja la conexión a la base de datos durante el ciclo de vida de la aplicación.

    Args:
        app (FastAPI): La instancia de la aplicación FastAPI.

    Yields:
        None: Ejecuta la aplicación.

    Finally:
        Cierra la conexión a la base de datos cuando se detiene la aplicación.
    """
    # Connect to DB if the connection is closed
    if connection.is_closed():
        connection.connect()
    try:
        yield  # run the app
    finally:
        # Close the connection when the app is stopped
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    """
    Redirige a la documentación de la API.

    Returns:
        RedirectResponse: Respuesta de redirección a la URL de documentación.
    """
    return RedirectResponse(url="/docs")

app.include_router(user_router, prefix="/api/users", tags=["users"])
app.include_router(user_role_router, prefix="/api/user_roles", tags=["user_roles"])
app.include_router(family_router, prefix="/api/families", tags=["families"])