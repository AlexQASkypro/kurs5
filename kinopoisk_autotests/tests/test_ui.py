import pytest
import allure
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.kinopoisk_ui_page import KinopoiskUIPage
from config.test_data import TestData

@allure.feature("UI Тесты Кинopoиска")
class TestKinopoiskUI:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.ui_page = KinopoiskUIPage(driver)

    @allure.story("Навигация + обход капчи")
    @allure.title("Открытие страницы 'Онлайн-кинотеатр'")
    def test_open_online_cinema(self):
        with allure.step("Открытие главной страницы"):
            self.main_page.open()
        with allure.step("Установка куки авторизации"):
            self.main_page.add_auth_cookie()
        with allure.step("Переход на страницу 'Онлайн-кинотеатр'"):
            self.main_page.open_online_cinema()
        with allure.step("Проверка, что заголовок 'Онлайн-кинотеатр' виден"):
            unique_locator = (By.XPATH, "//h1[contains(text(), 'Онлайн-кинотеатр')]")
            assert self.main_page.is_visible(unique_locator), "Элемент 'Онлайн-кинотеатр' не найден"

    @allure.story("Навигация + обход капчи")
    @allure.title("Открытие раздела 'Спорт'")
    def test_open_sport(self):
        with allure.step("Открытие главной страницы"):
            self.main_page.open()
        with allure.step("Установка куки авторизации"):
            self.main_page.add_auth_cookie()
        with allure.step("Переход в раздел 'Спорт'"):
            self.main_page.open_sport()
        with allure.step("Проверка, что заголовок 'Спорт' виден"):
            unique_locator = (By.XPATH, "//h1[contains(text(), 'Спорт')]")
            assert self.main_page.is_visible(unique_locator), "Элемент 'Спорт' не найден"

    @allure.story("Навигация + обход капчи")
    @allure.title("Открытие раздела 'Телеканалы'")
    def test_open_tv_channels(self):
        with allure.step("Открытие главной страницы"):
            self.main_page.open()
        with allure.step("Установка куки авторизации"):
            self.main_page.add_auth_cookie()
        with allure.step("Переход в раздел 'Телеканалы'"):
            self.main_page.open_tv_channels()
        with allure.step("Проверка, что заголовок 'Телеканалы' виден"):
            unique_locator = (By.XPATH, "//h1[contains(text(), 'Телеканалы')]")
            assert self.main_page.is_visible(unique_locator), "Элемент 'Телеканалы' не найден"

    @allure.story("Навигация + обход капчи")
    @allure.title("Открытие раздела 'Медиа'")
    def test_open_media(self):
        with allure.step("Открытие главной страницы"):
            self.main_page.open()
        with allure.step("Установка куки авторизации"):
            self.main_page.add_auth_cookie()
        with allure.step("Переход в раздел 'Медиа'"):
            self.main_page.open_media()
        with allure.step("Проверка, что заголовок 'Медиа' виден"):
            unique_locator = (By.XPATH, "//h1[contains(text(), 'Медиа')]")
            assert self.main_page.is_visible(unique_locator), "Элемент 'Медиа' не найден"

    @allure.story("Расширенный поиск")
    @allure.title("Расширенный поиск фильма")
    def test_extended_search_movie(self):
        movie_name = "Интерстеллар"
        self.ui_page.search_movie(movie_name)
        # Дополнительные проверки могут быть добавлены здесь

    @allure.story("Навигация")
    @allure.title("Открытие рецензий для фильма")
    def test_open_reviews(self):
        movie_name = "Интерстеллар"
        self.ui_page.open_reviews(movie_name)

    @allure.story("Навигация")
    @allure.title("Открытие фильмографии для актера")
    def test_open_filmography(self):
        actor = "Мэттью МакКонахи"
        self.ui_page.open_filmography(actor)
