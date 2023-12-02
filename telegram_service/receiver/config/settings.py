import os

from pydantic.v1 import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = 'tg-bot-service-receiver'

    TG_BOT_TOKEN: str = os.getenv('TG_BOT_TOKEN')
    TG_API_ID: str = os.getenv('TG_API_ID')
    TG_API_HASH: str = os.getenv('TG_API_HASH')
    TG_SESSION_NAME: str = os.getenv('TG_SESSION_NAME')

    class Config:
        case_sensitive = True


settings = Settings()
