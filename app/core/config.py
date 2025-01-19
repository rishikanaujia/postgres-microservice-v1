# app/core/config.py
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str = "Item Management Service"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        case_sensitive = True


settings = Settings()