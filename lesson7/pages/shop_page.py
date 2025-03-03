from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"

    def open(self):
        """Открывает сайт магазина."""
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        """Авторизуется как пользователь."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self, product_name: str):
        """Добавляет товар в корзину."""
        add_to_cart_button = self.driver.find_element(
            By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        )
        add_to_cart_button.click()

    def go_to_cart(self):
        """Переходит в корзину."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
        """Нажимает кнопку Checkout."""
        self.driver.find_element(By.ID, "checkout").click()

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        """Заполняет форму оформления заказа."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        """Возвращает итоговую стоимость."""
        total_price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_price.text