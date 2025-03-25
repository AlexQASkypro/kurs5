from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import logging

logger = logging.getLogger(__name__)

class BasePage:
    """Базовый класс для всех страниц проекта"""
    
    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу")
    def open(self) -> None:
        self.driver.get(self.url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator: tuple, timeout: int = 10):
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    @allure.step("Найти кликабельный элемент {locator}")
    def find_clickable_element(self, locator: tuple, timeout: int = 10):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )

    @allure.step("Сделать скриншот {filename}")
    def take_screenshot(self, filename: str = "screenshot.png") -> None:
        self.driver.save_screenshot(filename)
        allure.attach.file(filename, name=filename, attachment_type=allure.attachment_type.PNG)
        logger.info(f"Скриншот сохранён: {filename}")