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

# Тест для проверки формы
def test_form(driver):
    print("Запуск теста...")
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    print("Страница загружена.")

    # Заполнение формы
    print("Заполнение формы...")
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    # Поле Zip code оставляем пустым
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")
    print("Форма заполнена.")

    # Нажатие кнопки Submit
    print("Нажатие кнопки Submit...")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Ожидание применения стилей
    print("Ожидание применения стилей...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.alert'))
    )

    # Ожидание появления поля Zip code и его подсветки красным
    print("Ожидание появления поля Zip code и его подсветки красным...")
    zip_code_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="zip-code"].is-invalid'))
    )
    print("Поле Zip code найдено и подсвечено красным.")

    # Проверка, что поле Zip code подсвечено красным
    assert "is-invalid" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"
    print("Поле Zip code подсвечено красным.")

    # Проверка, что остальные поля подсвечены зеленым
    valid_fields = [
        'input[name="first-name"]',
        'input[name="last-name"]',
        'input[name="address"]',
        'input[name="e-mail"]',
        'input[name="phone"]',
        'input[name="city"]',
        'input[name="country"]',
        'input[name="job-position"]',
        'input[name="company"]'
    ]
    for field in valid_fields:
        element = driver.find_element(By.CSS_SELECTOR, field)
        assert "is-valid" in element.get_attribute("class"), f"Поле {field} не подсвечено зеленым"
    print("Все остальные поля подсвечены зеленым.")

    # Завершение теста
    print("Тест завершен.")