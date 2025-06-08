# from pydantic import BaseSettings
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_url: str
    model_config = SettingsConfigDict(env_file=".env")
    # class Config:
    #     env_file = ".env"

settings = Settings()