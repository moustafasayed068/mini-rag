from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    FILE_MAX_SIZE: int
    FILE_EXTENSIONS: list
    DEFAULT_CHUNK_SIZE: int

    class config:
        env_file = ".env"

def get_settings():
    return Settings()