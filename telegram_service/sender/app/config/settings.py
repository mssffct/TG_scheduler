import os
import secrets

from pydantic.v1 import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = '/api_v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'

    PROJECT_NAME: str = 'tg-bot-service'

    TG_BOT_TOKEN: str = os.getenv('TG_BOT_TOKEN')
    TG_API_ID: str = os.getenv('TG_API_ID')
    TG_API_HASH: str = os.getenv('TG_API_HASH')
    TG_SESSION_NAME: str = os.getenv('TG_SESSION_NAME')

    TG_FILES_CHAT_ID: int = 0

    GW_ROOT_URL: str = ''
    GW_API_KEY: str = 'secret-api-key'

    LOGS_DIR: str = 'logs/'

    class Config:
        case_sensitive = True


settings = Settings()
