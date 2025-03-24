import sys
from pathlib import Path
import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Добавляем папку проекта в PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера"""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении тестов"""
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        with allure.step("Сделать скриншот при ошибке"):
            allure.attach(
                item.funcargs['browser'].get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )