from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Определение базы для моделей
Base = declarative_base()

# Определение класса Entity
class Entity(Base):
    __tablename__ = 'entities'
    __table_args__ = {'schema': 'myschema'}

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Entity(id={self.id}, name='{self.name}')"

def test_add_entity(session):
    # Создание новой сущности
    new_entity = Entity(name='New Entity')

    # Добавление сущности в базу данных
    session.add(new_entity)
    session.commit()

    # Проверка, что сущность была добавлена
    assert session.query(Entity).filter_by(name='New Entity').first() is not None

def test_update_entity(session):
    # Добавление тестовой сущности
    entity = Entity(name='Test Entity')
    session.add(entity)
    session.commit()

    # Изменение сущности
    entity.name = 'Updated Entity'
    session.commit()

    # Проверка, что сущность была изменена
    updated_entity = session.query(Entity).filter_by(id=entity.id).first()
    assert updated_entity.name == 'Updated Entity'

def test_delete_entity(session):
    # Добавление тестовой сущности
    entity = Entity(name='Test Entity')
    session.add(entity)
    session.commit()

    # Удаление сущности из базы данных
    session.delete(entity)
    session.commit()

    # Проверка, что сущность была удалена
    assert session.query(Entity).filter_by(id=entity.id).first() is None