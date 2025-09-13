from fastapi import FastAPI

from app.api import router
from app.database import init_db, seed
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(fastapi: FastAPI):
    await init_db()
    await seed()
    yield

app = FastAPI(title="Async RAG Service", lifespan=lifespan)

app.include_router(router)

