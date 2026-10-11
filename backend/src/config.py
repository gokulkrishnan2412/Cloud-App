from pydantic import BaseSettings

class Settings(BaseSettings):
    STORAGE_BACKEND: str = "json"  # json, sql, sheets
    DATABASE_URL: str | None = None
    SHEETS_CREDENTIALS: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
