import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# Подключение к базе данных
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Определение базы для моделей
Base = declarative_base()

# Фикстура для создания сессии
@pytest.fixture
def session():
    """Фикстура для создания сессии."""
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    # Создание схемы (если она ещё не существует)
    connection.execute(text("CREATE SCHEMA IF NOT EXISTS myschema"))

    # Создание таблицы в базе данных
    Base.metadata.create_all(connection)

    yield session

    # Откат транзакции и закрытие сессии
    transaction.rollback()
    connection.close()