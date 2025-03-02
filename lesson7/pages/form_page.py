from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class FormPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        """Открывает страницу с формой."""
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "first-name"))
        )

    def enter_first_name(self, text: str):
        """Вводит имя."""
        self._enter_text("first-name", text)

    def enter_last_name(self, text: str):
        """Вводит фамилию."""
        self._enter_text("last-name", text)

    def enter_address(self, text: str):
        """Вводит адрес."""
        self._enter_text("address", text)

    def enter_email(self, text: str):
        """Вводит email."""
        self._enter_text("e-mail", text)

    def enter_phone(self, text: str):
        """Вводит номер телефона."""
        self._enter_text("phone", text)

    def enter_zip_code(self, text: str):
        """Вводит ZIP-код."""
        self._enter_text("zip-code", text)

    def enter_city(self, text: str):
        """Вводит город."""
        self._enter_text("city", text)

    def enter_country(self, text: str):
        """Вводит страну."""
        self._enter_text("country", text)

    def enter_job_position(self, text: str):
        """Вводит должность."""
        self._enter_text("job-position", text)

    def enter_company(self, text: str):
        """Вводит компанию."""
        self._enter_text("company", text)

    def submit(self):
        """Нажимает кнопку Submit."""
        submit_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3"))
        )
        submit_button.click()
        
        # Ожидаем, что поле "zip-code" станет невалидным
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.is-invalid"))
        )

    def get_validation_state(self, field_name: str) -> str:
        """
        Возвращает состояние валидации поля.
        :param field_name: Имя поля (например, "first-name").
        :return: "valid", "invalid" или пустая строка, если состояние не определено.
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.NAME, field_name))
            )
            classes = element.get_attribute("class")
            logger.info(f"Состояние валидации для {field_name}: {classes}")
            if "is-valid" in classes:
                return "valid"
            elif "is-invalid" in classes:
                return "invalid"
            return ""
        except Exception as e:
            logger.error(f"Ошибка: {e}")
            return ""

    def _enter_text(self, field_name: str, text: str):
        """
        Вспомогательный метод для ввода текста в поле.
        :param field_name: Имя поля (например, "first-name").
        :param text: Текст для ввода.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, field_name))
        )
        element.clear()
        element.send_keys(text)