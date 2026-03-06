from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.config.settings import settings

sync_dsn = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.database_host}:{settings.database_port}/{settings.postgres_db}"
sync_engine = create_engine(sync_dsn, echo=False, pool_pre_ping=True)
sync_session = sessionmaker(bind=sync_engine, autocommit=False, autoflush=False)


@contextmanager
def get_session_for_cli() -> Session:
    """Контекстный менеджер для сессии CLI"""
    session = sync_session()  # Создаем сессию
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
