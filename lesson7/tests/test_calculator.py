import pytest
from selenium import webdriver
from lesson7.pages.calculator_page import CalculatorPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(browser):
    """Тест для проверки работы калькулятора с задержкой."""
    page = CalculatorPage(browser)
    page.open()

    # Устанавливаем задержку 45 секунд
    page.set_delay(45)

    # Нажимаем кнопки: 7 + 8 =
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    # Проверяем результат через 45 секунд
    result = page.get_result()
    assert result == "15", f"Ожидаемый результат: 15, Фактический результат: {result}"