from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
from config.database import database as connection
from routes.user_role import user_role_router
from routes.family import family_router
from routes.user import user_router
from helpers.apy_key_auth import get_api_key

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage database connection during the application's lifespan.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Runs the application.

    Finally:
        Closes the database connection when the application stops.
    """
    # Connect to DB if the connection is closed
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Run the application
    finally:
        # Close the connection when the application is stopped
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    """Redirect to the API documentation.

    Returns:
        RedirectResponse: Redirect response to the documentation URL.
    """
    return RedirectResponse(url="/docs")

# Include routers for different API endpoints
app.include_router(user_router, prefix="/api/users", tags=["users"], dependencies= [Depends(get_api_key)])
app.include_router(user_role_router, prefix="/api/user_roles", tags=["user_roles"], dependencies= [Depends(get_api_key)])
app.include_router(family_router, prefix="/api/families", tags=["families"], dependencies= [Depends(get_api_key)])
