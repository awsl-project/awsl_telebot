import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    telebot_token: str
    api_url: str
    api_token: str
    uomg_url: str
    chatgpt_prefix: str

    class Config:
        env_file = os.environ.get("ENV_FILE", ".env")


settings = Settings()
