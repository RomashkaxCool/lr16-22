from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Lab FastAPI Project"
    version: str = "0.1.0"
    sentry_dsn: str | None = None
    environment: str = "local"

    class Config:
        env_file = ".env"

settings = Settings()