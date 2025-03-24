import allure
import pytest
from selenium import webdriver
from pages.shop_page import ShopPage


@allure.feature("Тестирование магазина")
@allure.severity(allure.severity_level.CRITICAL)
class TestShop:
    """Тесты для проверки работы интернет-магазина"""

    @pytest.fixture
    def browser(self):
        """Фикстура для инициализации браузера"""
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @allure.title("Полный цикл оформления заказа")
    @allure.description("Тестирование всего процесса покупки от авторизации до подтверждения заказа")
    def test_complete_order(self, browser):
        """Тестирование оформления заказа"""
        shop = ShopPage(browser)

        with allure.step("1. Авторизация под тестовым пользователем"):
            shop.open()
            shop.login("standard_user", "secret_sauce")

        with allure.step("2. Добавление товаров в корзину"):
            shop.add_to_cart("Sauce Labs Backpack")
            shop.add_to_cart("Sauce Labs Bolt T-Shirt")

        with allure.step("3. Оформление заказа"):
            shop.go_to_cart()
            shop.checkout()
            shop.fill_checkout_form("Иван", "Иванов", "123456")

        with allure.step("4. Проверка итоговой суммы"):
            total = shop.get_total_price()
            assert "Total: $" in total, f"Некорректный формат суммы. Ожидалось 'Total: $', получено: '{total}'"