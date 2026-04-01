from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    jwt_secret: str
    jwt_algorithm: str
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()