from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    telegram_bot_api_key: str


config = Config()


def get_config() -> Config:
    return config
