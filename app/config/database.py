# Database configuration
from __future__ import annotations
import threading
from contextlib import contextmanager
from typing import Generator
from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from app.config.logger import logger
from app.config.settings import settings
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(
    naming_convention=NAMING_CONVENTION
)
class Base(DeclarativeBase):

# Base class inherited by every ORM model.

    metadata = metadata
class DatabaseManager:
    """
    Centralized database lifecycle manager.
    Responsible only for:
        • Engine creation
        • Session creation
        • Connection lifecycle
        • Database initialization
    Does NOT perform any CRUD operations.
    """
    def __init__(self) -> None:
        self._engine: Engine | None = None
        self._session_factory: sessionmaker[Session] | None = None
        self._init_lock = threading.Lock()
    def initialize(self) -> None:
        """
        Initialize the database engine and session factory.
        Safe to call multiple times.
        Thread-safe.
        """
        with self._init_lock:
            if self._engine is not None:
                logger.warning(
                    "DatabaseManager is already initialized."
                )
                return
            database_url = str(
                settings.database.url or ""
            )
            if not database_url.strip():
                raise RuntimeError(
                    "Database URL is missing from application settings."
                )
            self._engine = create_engine(
                database_url,
                pool_size=settings.database.pool_size,
                max_overflow=settings.database.max_overflow,
                pool_recycle=settings.database.pool_recycle,
                echo=settings.database.echo,
                future=True,
                pool_pre_ping=True,
            )
            self._session_factory = sessionmaker(
                bind=self._engine,
                autocommit=False,
                autoflush=False,
                expire_on_commit=False,
            )
            self.__log_engine_info()
            logger.info(
                "DatabaseManager initialized successfully."
            )
    def __log_engine_info(self) -> None:
        """
        Log database connection information.
        Passwords are never logged.
        """
        engine = self.get_engine()
        url = engine.url
        logger.info(
            "Database Connection"
            f" | Dialect={url.get_backend_name()}"
            f" | Host={url.host}"
            f" | Database={url.database}"
            f" | Pool Size={settings.database.pool_size}"
            f" | Echo={settings.database.echo}"
        )
    def get_engine(self) -> Engine:
        """
        Return the active SQLAlchemy engine.
        Raises
        ------
        RuntimeError
            If the manager has not been initialized.
        """
        if self._engine is None:
            raise RuntimeError(
                "DatabaseManager has not been initialized."
            )

        return self._engine
    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        """
        Create a transactional database session.
        The session is automatically:

            • committed on success
            • rolled back on failure
            • closed in all cases
        """
        if self._session_factory is None:
            raise RuntimeError(
                "DatabaseManager has not been initialized."
            )
        session: Session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            logger.exception(
                "Database transaction rolled back."
            )
            raise
        finally:
            self.close_session(session)
    def close_session(self, session: Session) -> None:
        """
        Close a database session.
        """
        session.close()
    def check_connection(self) -> bool:
        """
        Verify that the database is reachable.
        Returns
        -------
        bool
            True if the connection succeeds.
        """
        try:
            with self.get_engine().connect() as connection:
                connection.execute(text("SELECT 1"))
            return True
        except Exception:
            logger.exception(
                "Database connection health check failed."
            )
            return False
    def ping(self) -> bool:
        """
        Lightweight database ping.
        Used by future health-check endpoints.
        """
        return self.check_connection()
    def create_tables(self) -> None:
        """
        Create all registered ORM tables.
        """
        Base.metadata.create_all(
            bind=self.get_engine()
        )
        logger.info(
            "Database tables created successfully."
        )
    def drop_tables(self) -> None:
        """
        Drop all registered ORM tables.
        Intended only for development or testing.
        """
        Base.metadata.drop_all(
            bind=self.get_engine()
        )
        logger.warning(
            "Database tables dropped."
        )
    def shutdown(self) -> None:
        """
        Dispose the SQLAlchemy engine and
        release the connection pool.
        """
        if self._engine is None:
            return
        self._engine.dispose()
        self._engine = None
        self._session_factory = None
        logger.info(
            "Database engine shutdown completed."
        )
database = DatabaseManager()
def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency.

    Example
    -------
    db: Session = Depends(get_db)
    """
    with database.get_session() as session:
        yield session
__all__ = (
    "Base",
    "database",
    "get_db",
)