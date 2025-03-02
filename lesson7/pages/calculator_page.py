from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        """Открывает страницу с калькулятором."""
        self.driver.get(self.url)

    def set_delay(self, delay: int):
        """Устанавливает задержку вычислений."""
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, button_text: str):
        """Нажимает кнопку на калькуляторе."""
        button = self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def get_result(self):
        """Возвращает результат вычислений."""
        result = WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text