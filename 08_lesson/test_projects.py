import requests
import pytest
from project_api import ProjectAPI

# Фикстура для создания проекта
@pytest.fixture
def project_api():
    base_url = "https://ru.yougile.com/api-v2"
    headers = {
        "Authorization": "Bearer 85RdN29rDP90HKckUGHrgO4tyvs2JydVqMXFC7PkBCxuper09mzYURvyMnnYVNmF",
        "Content-Type": "application/json"
    }
    return ProjectAPI(base_url, headers)

@pytest.fixture
def create_project(project_api):
    # Создаем проект
    project_id = project_api.create_project("Test Project")
    yield project_id  # Возвращаем ID для использования в тестах
    # Удаляем проект после завершения теста
    project_api.delete_project(project_id)

# Позитивный тест для создания проекта
def test_create_project_positive(create_project, project_api):
    project_id = create_project
    assert project_id is not None  # Проверяем, что ID проекта получен

# Позитивный тест для получения проекта
def test_get_project_positive(create_project, project_api):
    project_id = create_project
    project = project_api.get_project(project_id)
    assert project["title"] == "Test Project"  # Проверяем данные проекта

# Позитивный тест для обновления проекта
def test_update_project_positive(create_project, project_api):
    project_id = create_project
    project_api.update_project(project_id, "Updated Test Project")
    project = project_api.get_project(project_id)
    assert project["title"] == "Updated Test Project"  # Проверяем обновленные данные

# Негативный тест для создания проекта (без обязательного поля title)
def test_create_project_negative(project_api):
    with pytest.raises(requests.exceptions.HTTPError):
        project_api.create_project("")  # Пустой title

# Негативный тест для получения проекта (несуществующий ID)
def test_get_project_negative(project_api):
    non_existent_id = "non-existent-id"
    with pytest.raises(requests.exceptions.HTTPError):
        project_api.get_project(non_existent_id)

# Негативный тест для обновления проекта (несуществующий ID)
def test_update_project_negative(project_api):
    non_existent_id = "non-existent-id"
    with pytest.raises(requests.exceptions.HTTPError):
        project_api.update_project(non_existent_id, "Updated Test Project")