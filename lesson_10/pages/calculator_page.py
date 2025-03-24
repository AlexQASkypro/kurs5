from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from .base_page import BasePage

class CalculatorPage(BasePage):
    """Page Object для страницы калькулятора с задержкой"""
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку {delay} сек")
    def set_delay(self, delay: int) -> None:
        """
        Устанавливает задержку вычислений
        
        :param delay: Задержка в секундах
        :type delay: int
        """
        delay_input = self.find_element((By.CSS_SELECTOR, "#delay"))
        delay_input.clear()
        delay_input.send_keys(str(delay))

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает указанную кнопку калькулятора
        
        :param button_text: Текст на кнопке
        :type button_text: str
        """
        self.find_clickable_element(
            (By.XPATH, f"//span[text()='{button_text}']")
        ).click()

    @allure.step("Получить результат вычислений")
    def get_result(self) -> str:
        """
        Возвращает результат вычислений
        
        :return: Текст результата
        :rtype: str
        """
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), 
                "15"
            )
        )
        return self.find_element((By.CSS_SELECTOR, ".screen")).text