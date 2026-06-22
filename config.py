
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """" Application settings """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    # Application
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: int
    FACEBOOK_PAGE_ID: str
    FACEBOOK_PAGE_ACCESS_TOKEN: str