from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.cache.router import router as cache_router
from src.core.logging.logging_config import setup_logging
from src.core.logging.sentry import init_sentry
from src.core.router import router as core_router
from src.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ініціалізація при старті
    init_sentry()
    setup_logging()
    yield
    # Дії при вимкненні (якщо потрібно)


app = FastAPI(title=settings.project_name, version=settings.version, lifespan=lifespan)

app.include_router(core_router)
app.include_router(cache_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
