from fastapi import FastAPI
from api.events import router as event_router
from contextlib import asynccontextmanager
from api.db.session import init_db

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan( app:FastAPI):
    #before app startup up
    init_db()
    yield
    #clean up

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_orgins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(event_router, prefix='/api/events') #/api/events


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
