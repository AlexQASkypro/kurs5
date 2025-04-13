import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from allure import step
from config.settings import settings

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.WAIT_TIMEOUT)
        self.base_url = settings.BASE_URL

    def human_pause(self, min_delay=0.5, max_delay=2.0):
        """Эмулирует естественную задержку между действиями пользователя."""
        pause_time = random.uniform(min_delay, max_delay)
        time.sleep(pause_time)

    @step("Открытие страницы {url}")
    def open(self, url=""):
        """Открывает страницу по базовому URL с относительным путём."""
        self.driver.get(f"{self.base_url}{url}")
        # Даем странице немного времени на загрузку
        self.human_pause(1, 2)
        # Проверяем, не показана ли капча
        self.check_for_captcha()
        return self

    @step("Проверка наличия капчи")
    def check_for_captcha(self):
        """
        Пытается определить, появилось ли окно капчи.
        Если капча обнаружена, ждет некоторое время и перезагружает страницу.
        """
        try:
            # Пример селектора капчи. Замените 'div.captcha-container' на актуальный селектор.
            captcha = self.driver.find_elements(By.CSS_SELECTOR, "div.captcha-container")
            if captcha:
                # Если капча обнаружена, выводим сообщение и ждем больше времени.
                print("Капча обнаружена! Ожидание 15 секунд для ручного решения или обхода...")
                time.sleep(15)  # можно увеличить или интегрировать сервис решения капчи
                self.driver.refresh()
                self.wait_for_element((By.TAG_NAME, "body"))
        except Exception as e:
            print(f"Ошибка при проверке капчи: {e}")

    @step("Поиск элемента {locator}")
    def find_element(self, locator):
        """Находит элемент с использованием WebDriverWait."""
        return self.wait.until(EC.presence_of_element_located(locator))

    @step("Клик по элементу {locator}")
    def click(self, locator):
        """
        Выполняет клик по элементу с эмуляцией движения мыши.
        Сначала перемещается к элементу, делает небольшое случайное смещение, затем кликает.
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.human_pause(0.5, 1.5)
        actions.move_by_offset(random.randint(-5, 5), random.randint(-5, 5)).perform()
        self.human_pause(0.3, 0.8)
        element.click()
        self.human_pause(0.5, 1.0)
        return self

    @step("Ввод текста '{text}' в элемент {locator}")
    def type(self, locator, text):
        """
        Очищает поле и вводит заданный текст по символам,
        имитируя естественный набор текста.
        """
        element = self.find_element(locator)
        element.clear()
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))
        self.human_pause(0.5, 1.0)
        return self

    @step("Проверка видимости элемента {locator}")
    def is_visible(self, locator, timeout=None):
        """Возвращает True, если элемент виден на странице."""
        try:
            wt = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
            return wt.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    @step("Ожидание появления элемента {locator}")
    def wait_for_element(self, locator):
        """Ожидает появления элемента с использованием WebDriverWait."""
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не появился"
        )
