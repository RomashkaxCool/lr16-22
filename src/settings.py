from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = "Lab FastAPI Project"
    version: str = "0.1.0"

    debug: bool = False
    environment: str = "local"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/lab_db"
    redis_url: str = "redis://localhost:6379/0"
    secret_key: str = "secret"

    sentry_dsn: str | None = None

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
