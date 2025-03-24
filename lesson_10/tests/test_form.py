import allure
import pytest
from selenium import webdriver
from pages.form_page import FormPage

@allure.feature("Тестирование формы")
@allure.severity(allure.severity_level.NORMAL)
class TestFormValidation:
    """Тесты для проверки валидации формы"""
    
    @pytest.fixture
    def browser(self):
        """Фикстура для инициализации браузера"""
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @allure.title("Проверка валидации обязательных полей")
    @allure.description("Тест проверяет подсветку невалидных полей формы")
    def test_form_validation(self, browser):
        """Тестирование валидации формы"""
        form = FormPage(browser)
        
        with allure.step("Открыть и заполнить форму (кроме ZIP-кода)"):
            form.open()
            form._enter_text("first-name", "Иван")
            form._enter_text("last-name", "Петров")
            form._enter_text("address", "ул. Ленина, 10")
            form._enter_text("e-mail", "test@example.com")
            form._enter_text("phone", "+79991234567")
            
        with allure.step("Отправить форму"):
            form.submit()
            
        with allure.step("Проверить валидацию полей"):
            assert form.get_validation_state("zip-code") == "valid", "ZIP-код должен быть валидным"
            assert form.get_validation_state("first-name") == "valid", "Имя должно быть валидным"