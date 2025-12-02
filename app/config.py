from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Database
    db_connection: str
    db_host: str
    db_port: int
    db_database: str
    db_username: str
    db_password: str | None = None

    # JWT
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(
        # env_file=".env",  # প্রজেক্ট রুটে থাকলে
        env_file="app/.env",     # যদি app ফোল্ডারে থাকে তাহলে এটা
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

# Create settings instance
settings = Settings()
