from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure

class BasePage:
    """Базовый класс для всех страниц проекта"""
    
    def __init__(self, driver: WebDriver, url: str):
        """
        Инициализация базовой страницы
        
        :param driver: Экземпляр WebDriver
        :type driver: WebDriver
        :param url: URL страницы
        :type url: str
        """
        self.driver = driver
        self.url = url

    @allure.step("Открыть страницу")
    def open(self) -> None:
        """Открывает страницу по указанному URL"""
        self.driver.get(self.url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator: tuple, timeout: int = 10):
        """
        Находит элемент с ожиданием
        
        :param locator: Кортеж (By, локатор)
        :type locator: tuple
        :param timeout: Время ожидания в секундах
        :type timeout: int
        :return: Найденный элемент
        :rtype: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} не найден"
        )

    @allure.step("Найти кликабельный элемент {locator}")
    def find_clickable_element(self, locator: tuple, timeout: int = 10):
        """
        Находит кликабельный элемент с ожиданием
        
        :param locator: Кортеж (By, локатор)
        :type locator: tuple
        :param timeout: Время ожидания в секундах
        :type timeout: int
        :return: Найденный элемент
        :rtype: WebElement
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )