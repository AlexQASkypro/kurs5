from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from allure import step
from pages.base_page import BasePage
from config.settings import settings
from config.test_data import TestData

class MainPage(BasePage):
    # Основные локаторы главной страницы
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="kp_query"]')
    USER_AVATAR = (By.CSS_SELECTOR, 'img.UserPic-Image')
    PROMO_CODE_FIELD = (By.NAME, "promo_code")
    APPLY_PROMO_BUTTON = (By.CSS_SELECTOR, "button.apply-promo")
    MOVIE_LINK = (By.XPATH, f"//a[contains(text(), '{TestData.TEST_MOVIE_NAME}')]")

    @step("Поиск фильма '{movie_name}'")
    def search_movie(self, movie_name):
        """Вводит название фильма в поисковой строке."""
        self.type(self.SEARCH_FIELD, movie_name)
        self.click_main_search_button()
        return self

    @step("Установка куки авторизации")
    def add_auth_cookie(self):
        """
        Добавляет cookie с токеном авторизации для обхода капчи.
        Имя и домен указаны согласно требованиям сайта.
        """
        cookie = {
            'name': 'auth_token',
            'value': settings.AUTH_TOKEN,
            'domain': 'kinopoisk.ru'
        }
        self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.wait_for_element((By.TAG_NAME, "body"))
        return self

    @step("Нажатие кнопки поиска")
    def click_main_search_button(self):
        """Нажимает на кнопку поиска на главной странице."""
        self.click((By.XPATH, '//button[contains(@class, "styles_submit__2AIpj") and @aria-label="Найти"]'))
        return self

    @step("Переход на страницу 'Онлайн-кинотеатр'")
    def open_online_cinema(self):
        """
        Переходит на страницу Онлайн-кинотеатра, используя уточнённый локатор.
        Ожидает появления уникального элемента (например, заголовка).
        """
        self.click((By.CSS_SELECTOR, "a[data-tid='acc26a70']"))
        unique_locator = (By.XPATH, "//h1[contains(text(), 'Онлайн-кинотеатр')]")
        self.wait_for_element(unique_locator)
        return self

    @step("Переход в раздел 'Спорт'")
    def open_sport(self):
        """Переходит в раздел 'Спорт' и ждёт появления соответствующего заголовка."""
        self.click((By.XPATH, "//a[contains(text(), 'Спорт')]"))
        unique_locator = (By.XPATH, "//h1[contains(text(), 'Спорт')]")
        self.wait_for_element(unique_locator)
        return self

    @step("Переход в раздел 'Телеканалы'")
    def open_tv_channels(self):
        """Переходит в раздел 'Телеканалы' и ждёт появления соответствующего заголовка."""
        self.click((By.XPATH, "//a[contains(text(), 'Телеканалы')]"))
        unique_locator = (By.XPATH, "//h1[contains(text(), 'Телеканалы')]")
        self.wait_for_element(unique_locator)
        return self

    @step("Переход в раздел 'Медиа'")
    def open_media(self):
        """Переходит в раздел 'Медиа' и ждёт появления соответствующего заголовка."""
        self.click((By.XPATH, "//a[contains(text(), 'Медиа')]"))
        unique_locator = (By.XPATH, "//h1[contains(text(), 'Медиа')]")
        self.wait_for_element(unique_locator)
        return self
