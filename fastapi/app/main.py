from fastapi import FastAPI
from fastapi.responses import RedirectResponse 

from contextlib import asynccontextmanager
from config.database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect to db if the connection is closed 
    if connection.is_closed():
        connection.connect()
    try:
        yield # run the app
    finally:
        # close the connection when the app is stopped
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")