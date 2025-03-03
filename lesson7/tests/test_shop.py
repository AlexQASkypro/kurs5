import pytest
from selenium import webdriver
from lesson7.pages.shop_page import ShopPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shop(browser):
    """Тест для проверки работы интернет-магазина."""
    page = ShopPage(browser)
    page.open()

    # Авторизация
    page.login("standard_user", "secret_sauce")

    # Добавление товаров в корзину
    page.add_to_cart("Sauce Labs Backpack")
    page.add_to_cart("Sauce Labs Bolt T-Shirt")
    page.add_to_cart("Sauce Labs Onesie")

    # Переход в корзину
    page.go_to_cart()

    # Оформление заказа
    page.checkout()
    page.fill_checkout_form("Иван", "Иванов", "123456")

    # Проверка итоговой стоимости
    total_price = page.get_total_price()
    assert total_price == "Total: $58.29", f"Ожидаемая сумма: $58.29, Фактическая сумма: {total_price}"