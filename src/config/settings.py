from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # PostgreSQL
    postgres_db: str = "neiro"
    postgres_user: str = "postgres"
    postgres_password: str = "9998441653Qq"
    database_host: str = "localhost"
    database_port: int = 5432


settings = Settings()
