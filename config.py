from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    app_name: str = "ResolveAI API"
    database_url: str

    class Config:
        env_file = ".env"
