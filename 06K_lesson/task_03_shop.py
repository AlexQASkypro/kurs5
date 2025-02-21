import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Фикстура для инициализации и завершения работы драйвера
@pytest.fixture
def driver():
    # Настройка опций Chrome
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")  # Убедитесь, что эта строка закомментирована
    chrome_options.add_argument("--window-size=1920,1080")  # Размер окна

    # Инициализация драйвера с опциями
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    yield driver
    # Закрытие драйвера после завершения теста
    driver.quit()

# Тест для проверки магазина
def test_shop(driver):
    print("Запуск теста...")
    # Переход на страницу магазина
    driver.get("https://www.saucedemo.com/")
    print("Страница магазина загружена.")

    # Авторизация
    print("Авторизация...")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Авторизация успешна.")

    # Добавление товаров в корзину
    print("Добавление товаров в корзину...")
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()  # Sauce Labs Backpack
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()  # Sauce Labs Bolt T-Shirt
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()  # Sauce Labs Onesie
    print("Товары добавлены в корзину.")

    # Переход в корзину
    print("Переход в корзину...")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    print("Корзина открыта.")

    # Нажатие кнопки Checkout
    print("Нажатие кнопки Checkout...")
    driver.find_element(By.ID, "checkout").click()
    print("Форма оформления заказа открыта.")

    # Заполнение формы
    print("Заполнение формы...")
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    print("Форма заполнена.")

    # Нажатие кнопки Continue
    print("Нажатие кнопки Continue...")
    driver.find_element(By.ID, "continue").click()
    print("Переход на страницу подтверждения заказа.")

    # Получение итоговой стоимости
    print("Получение итоговой стоимости...")
    total_price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    ).text
    print(f"Итоговая стоимость: {total_price}")

    # Проверка итоговой стоимости
    assert total_price == "Total: $58.29", f"Ожидаемая стоимость: $58.29, Фактическая стоимость: {total_price}"
    print("Итоговая стоимость корректна.")

    # Завершение теста
    print("Тест завершен.")
    