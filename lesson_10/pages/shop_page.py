from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from .base_page import BasePage


class ShopPage(BasePage):
    """Page Object для интернет-магазина"""
    
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы магазина
        
        :param driver: Экземпляр WebDriver
        :type driver: WebDriver
        """
        super().__init__(driver, "https://www.saucedemo.com")

    @allure.step("Авторизоваться под пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию в магазине
        
        :param username: Логин пользователя
        :type username: str
        :param password: Пароль пользователя
        :type password: str
        """
        self.find_element((By.ID, "user-name")).send_keys(username)
        self.find_element((By.ID, "password")).send_keys(password)
        self.find_clickable_element((By.ID, "login-button")).click()

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину
        
        :param product_name: Название товара
        :type product_name: str
        """
        self.find_clickable_element(
            (By.XPATH, f"//div[contains(text(),'{product_name}')]/ancestor::div[@class='inventory_item']//button")
        ).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины"""
        self.find_clickable_element(
            (By.CLASS_NAME, "shopping_cart_link")
        ).click()

    @allure.step("Начать оформление заказа")
    def checkout(self) -> None:
        """Начинает процесс оформления заказа"""
        self.find_clickable_element((By.ID, "checkout")).click()

    @allure.step("Заполнить данные для заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет форму оформления заказа
        
        :param first_name: Имя
        :type first_name: str
        :param last_name: Фамилия
        :type last_name: str
        :param postal_code: Почтовый индекс
        :type postal_code: str
        """
        self.find_element((By.ID, "first-name")).send_keys(first_name)
        self.find_element((By.ID, "last-name")).send_keys(last_name)
        self.find_element((By.ID, "postal-code")).send_keys(postal_code)
        self.find_clickable_element((By.ID, "continue")).click()

    @allure.step("Получить итоговую сумму")
    def get_total_price(self) -> str:
        """
        Возвращает итоговую сумму заказа
        
        :return: Сумма заказа
        :rtype: str
        """
        return self.find_element((By.CLASS_NAME, "summary_total_label")).text