import pytest
from selenium import webdriver
from lesson7.pages.form_page import FormPage
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form_validation(browser):
    """Тест для проверки заполнения формы и валидации полей."""
    page = FormPage(browser)
    page.open()
    
    # Заполняем форму
    page.enter_first_name("Иван")
    page.enter_last_name("Петров")
    page.enter_address("Ленина, 55-3")
    page.enter_email("test@skypro.com")
    page.enter_phone("+7985899998787")
    # Поле "Zip code" оставляем пустым
    page.enter_city("Москва")
    page.enter_country("Россия")
    page.enter_job_position("QA")
    page.enter_company("SkyPro")

    # Нажимаем кнопку Submit
    page.submit()
    
    # Проверяем, что поле "Zip code" подсвечено красным
    assert page.get_validation_state("zip-code") == "invalid", "Поле 'Zip code' должно быть невалидным"

    # Проверяем, что остальные поля подсвечены зеленым
    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]
    for field in valid_fields:
        assert page.get_validation_state(field) == "valid", f"Поле {field} должно быть валидным"