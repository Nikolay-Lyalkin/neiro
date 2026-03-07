from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # PostgreSQL
    postgres_db: str = "neiro"
    postgres_user: str = "postgres"
    postgres_password: str = "password"
    database_host: str = "db"
    database_port: int = 5432


settings = Settings()
