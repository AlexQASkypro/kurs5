from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure
import logging
from .base_page import BasePage
import time

logger = logging.getLogger(__name__)

class FormPage(BasePage):
    """Page Object для страницы с формой ввода данных"""

    def __init__(self, driver: WebDriver):
        super().__init__(driver, "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Ввести текст в поле {field_name}")
    def _enter_text(self, field_name: str, text: str) -> None:
        """Вводит текст в указанное поле"""
        try:
            locators = [
                (By.NAME, field_name),
                (By.CSS_SELECTOR, f'input[name="{field_name}"]'),
                (By.XPATH, f'//label[contains(text(), "{field_name.replace("-", " ")}")]/following-sibling::input')
            ]
            
            for locator in locators:
                try:
                    element = self.find_element(locator)
                    element.clear()
                    element.send_keys(text)
                    logger.info(f"В поле {field_name} введено: {text}")
                    return
                except:
                    continue
            
            raise Exception(f"Поле {field_name} не найдено")
        except Exception as e:
            logger.error(f"Ошибка при вводе в {field_name}: {str(e)}")
            self.take_screenshot(f"enter_text_error_{field_name}.png")
            raise

    @allure.step("Отправить форму")
    def submit(self) -> None:
        """Отправляет заполненную форму"""
        try:
            submit_button = self.find_element((By.CSS_SELECTOR, "button[type='submit']"))
            submit_button.click()
            logger.info("Форма отправлена")
            time.sleep(2)  # Ожидание обработки
        except Exception as e:
            logger.error(f"Ошибка отправки формы: {str(e)}")
            self.take_screenshot("submit_error.png")
            raise

    @allure.step("Проверить валидацию ZIP-кода")
    def check_zip_code_validation(self) -> str:
        """Проверяет состояние валидации ZIP-кода"""
        try:
            # Отладочная информация
            self.take_screenshot("before_validation_check.png")
            page_html = self.driver.find_element(By.TAG_NAME, "body").get_attribute("outerHTML")[:1000]
            logger.debug(f"HTML страницы (фрагмент):\n{page_html}")

            # Проверка блока ошибки
            error_div = self.find_element((By.ID, "zip-code"))
            classes = error_div.get_attribute("class")
            content = error_div.text
            
            logger.debug(f"Блок ошибки ZIP-кода. Классы: {classes}, Текст: {content}")

            if "alert-danger" in classes and error_div.is_displayed():
                logger.info("Найдена ошибка валидации ZIP-кода")
                return "invalid"

            # Дополнительная проверка поля ввода
            try:
                zip_input = self.find_element((By.NAME, "zip-code"))
                input_classes = zip_input.get_attribute("class")
                logger.debug(f"Поле ввода ZIP-кода. Классы: {input_classes}")
                
                if "is-invalid" in input_classes:
                    return "invalid"
            except Exception as e:
                logger.warning(f"Поле ввода ZIP-кода не найдено: {str(e)}")

            return "valid"
        except Exception as e:
            logger.error(f"Ошибка проверки валидации: {str(e)}")
            self.take_screenshot("validation_check_error.png")
            return "error"