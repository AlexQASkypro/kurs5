import allure
import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage

@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    """Тесты для проверки работы калькулятора"""
    
    @pytest.fixture
    def browser(self):
        """Фикстура для инициализации браузера"""
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    @allure.title("Проверка сложения с задержкой")
    @allure.description("Тест проверяет корректность работы калькулятора с установленной задержкой")
    def test_addition(self, browser):
        """Тестирование операции сложения"""
        calculator = CalculatorPage(browser)
        
        with allure.step("Открыть страницу калькулятора"):
            calculator.open()
            
        with allure.step("Установить задержку вычислений"):
            calculator.set_delay(5)
            
        with allure.step("Выполнить операцию 7 + 8"):
            calculator.click_button("7")
            calculator.click_button("+")
            calculator.click_button("8")
            calculator.click_button("=")
            
        with allure.step("Проверить результат вычисления"):
            assert calculator.get_result() == "15", "Неверный результат вычисления"