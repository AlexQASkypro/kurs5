from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure
import logging
from .base_page import BasePage

logger = logging.getLogger(__name__)

class FormPage(BasePage):
    """Page Object для страницы с формой ввода данных"""
    
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы формы
        
        :param driver: Экземпляр WebDriver
        :type driver: WebDriver
        """
        super().__init__(driver, "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Ввести текст в поле {field_name}")
    def _enter_text(self, field_name: str, text: str) -> None:
        """
        Вводит текст в указанное поле
        
        :param field_name: Имя поля
        :type field_name: str
        :param text: Текст для ввода
        :type text: str
        """
        element = self.find_element((By.NAME, field_name))
        element.clear()
        element.send_keys(text)

    @allure.step("Отправить форму")
    def submit(self) -> None:
        """Отправляет заполненную форму"""
        self.find_clickable_element(
            (By.CSS_SELECTOR, "button[type='submit']")
        ).click()

    @allure.step("Проверить валидацию поля {field_name}")
    def get_validation_state(self, field_name: str) -> str:
        """
        Проверяет состояние валидации поля
        
        :param field_name: Имя поля
        :type field_name: str
        :return: Состояние валидации ('valid' или 'invalid')
        :rtype: str
        """
        try:
            element = self.find_element((By.ID, field_name))
            classes = element.get_attribute("class")
            return "invalid" if "is-invalid" in classes else "valid"
        except Exception as e:
            logger.error(f"Ошибка проверки валидации: {e}")
            return "error"