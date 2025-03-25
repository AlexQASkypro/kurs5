import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.form_page import FormPage
import logging
import time

logger = logging.getLogger(__name__)

@allure.feature("Тестирование формы")
class TestFormValidation:
    """Тесты для проверки валидации формы"""

    @pytest.fixture
    def browser(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

    @allure.title("Проверка валидации ZIP-кода")
    def test_zip_code_validation(self, browser):
        form = FormPage(browser)
        
        with allure.step("1. Открыть страницу с формой"):
            form.open()
            WebDriverWait(browser, 15).until(
                EC.presence_of_element_located((By.NAME, "first-name"))
            )
            form.take_screenshot("page_loaded.png")

        with allure.step("2. Заполнить обязательные поля (кроме ZIP-кода)"):
            test_data = {
                "first-name": "Иван",
                "last-name": "Петров",
                "address": "ул. Ленина, 10",
                "e-mail": "test@example.com",
                "phone": "+79991234567"
            }
            
            for field, value in test_data.items():
                try:
                    form._enter_text(field, value)
                    time.sleep(0.3)  # Небольшая пауза между заполнением полей
                except Exception as e:
                    logger.error(f"Ошибка заполнения поля {field}: {str(e)}")
                    form.take_screenshot(f"field_{field}_error.png")
                    pytest.fail(f"Не удалось заполнить поле {field}: {str(e)}")

            form.take_screenshot("form_filled.png")

        with allure.step("3. Отправить форму"):
            form.submit()
            form.take_screenshot("form_submitted.png")
            
            # Ожидание появления блока ошибки
            try:
                WebDriverWait(browser, 10).until(
                    EC.visibility_of_element_located((By.ID, "zip-code"))
                )
                form.take_screenshot("error_visible.png")
            except Exception as e:
                logger.error(f"Блок ошибки не появился: {str(e)}")
                form.take_screenshot("error_not_found.png")
                pytest.fail("Блок ошибки валидации не появился после отправки формы")

        with allure.step("4. Проверить валидацию ZIP-кода"):
            validation_state = form.check_zip_code_validation()
            
            # Дополнительная отладочная информация
            if validation_state == "error":
                logger.error("Состояние валидации: error. Дополнительная информация:")
                logger.error(f"URL страницы: {browser.current_url}")
                logger.error(f"Заголовок страницы: {browser.title}")
                form.take_screenshot("validation_error_state.png")

            assert validation_state == "invalid", (
                f"Ожидалось состояние 'invalid', получено: {validation_state}\n"
                f"Проверьте скриншоты в отчёте Allure"
            )