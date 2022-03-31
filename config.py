import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    telebot_token: str
    url: str

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env")


settings = Settings()
