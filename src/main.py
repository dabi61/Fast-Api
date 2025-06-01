from fastapi import FastAPI
from api.events import router as event_router
from contextlib import asynccontextmanager
from api.db.session import init_db


@asynccontextmanager
async def lifespan( app:FastAPI):
    #before app startup up
    init_db()
    yield
    #clean up

app = FastAPI(lifespan=lifespan)
app.include_router(event_router, prefix='/api/events') #/api/events


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
