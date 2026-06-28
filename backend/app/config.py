from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    BASE_URL: str
    ADMIN_API_KEY: str
    RATE_LIMIT_SHORTEN: str
    RATE_LIMIT_REDIRECT: str
    VITE_API_URL: str
    VITE_ADMIN_KEY: str


    model_config = SettingsConfigDict (
        env_file = "../.env",
        env_file_encoding = "utf-8",
    )


settings = Settings()
