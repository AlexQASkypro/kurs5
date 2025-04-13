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

# Тест для проверки калькулятора
def test_calculator(driver):
    print("Запуск теста...")
    # Переход на страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    print("Страница загружена.")

    # Ввод значения задержки
    print("Установка задержки...")
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    print("Задержка установлена на 45 секунд.")

    # Нажатие кнопок: 7 + 8 =
    print("Выполнение вычислений...")
    driver.find_element(By.XPATH, "//span[text()='7']").click()  # Кнопка 7
    driver.find_element(By.XPATH, "//span[text()='+']").click()  # Кнопка +
    driver.find_element(By.XPATH, "//span[text()='8']").click()  # Кнопка 8
    driver.find_element(By.XPATH, "//span[text()='=']").click()  # Кнопка =
    print("Вычисления выполнены.")

    # Ожидание результата
    print("Ожидание результата...")
    result = WebDriverWait(driver, 46).until(  # Ожидание 46 секунд (45 + запас)
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    print("Результат отобразился.")

    # Проверка результата
    result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result_text == "15", f"Ожидаемый результат: 15, Фактический результат: {result_text}"
    print("Результат корректен.")

    # Завершение теста
    print("Тест завершен.")
    