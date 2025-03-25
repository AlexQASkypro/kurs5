# Инструкция по запуску тестов

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск тестов
```bash
pytest lesson_10/tests/ --alluredir=lesson_10/allure-results -v
```

## Просмотр отчета Allure
```bash
allure serve lesson_10/allure-results
```

## Структура проекта
- `pages/` - Page Object модели
- `tests/` - тесты
- `conftest.py` - фикстуры pytest
- `pytest.ini` - настройки pytest