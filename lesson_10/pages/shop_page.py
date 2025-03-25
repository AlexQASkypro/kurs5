import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу магазина")
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизоваться под пользователем {username}")
    def login(self, username: str, password: str):
        self.find_visible_element((By.ID, "user-name")).send_keys(username)
        self.find_visible_element((By.ID, "password")).send_keys(password)
        self.find_clickable_element((By.ID, "login-button")).click()

    @allure.step("Добавить товар {item_name} в корзину")
    def add_to_cart(self, item_name: str):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.find_clickable_element((By.XPATH, item_xpath)).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        self.find_clickable_element((By.CLASS_NAME, "shopping_cart_link")).click()

    @allure.step("Начать оформление заказа")
    def checkout(self):
        self.find_clickable_element((By.ID, "checkout")).click()

    @allure.step("Заполнить данные для оформления")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.find_visible_element((By.ID, "first-name")).send_keys(first_name)
        self.find_visible_element((By.ID, "last-name")).send_keys(last_name)
        self.find_visible_element((By.ID, "postal-code")).send_keys(postal_code)
        self.find_clickable_element((By.ID, "continue")).click()

    @allure.step("Получить итоговую сумму")
    def get_total_price(self):
        return self.find_visible_element((By.CLASS_NAME, "summary_total_label")).text

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))