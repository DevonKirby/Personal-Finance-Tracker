from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    anthropic_api_key: str

    class Config:
        env_file = BASE_DIR / ".env"

settings = Settings()