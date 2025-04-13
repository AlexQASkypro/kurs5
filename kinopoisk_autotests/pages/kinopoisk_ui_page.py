from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from allure import step
from pages.base_page import BasePage

class KinopoiskUIPage(BasePage):
    def __init__(self, driver, test_config=None):
        super().__init__(driver)
        self.test_config = test_config

    @step("Поиск фильма '{movie_name}' на главной странице")
    def search_main_page_movie(self, movie_name: str):
        search_input = self.wait_for_element((By.CSS_SELECTOR, 'input[name="kp_query"]'))
        search_input.clear()
        search_input.send_keys(movie_name)
        self.click_main_search_button()
        return self

    # Добавляем метод-алиас, чтобы можно было вызывать search_movie
    search_movie = search_main_page_movie

    @step("Поиск актёра '{actor}' на главной странице")
    def search_main_page_actor(self, actor: str):
        search_input = self.wait_for_element((By.CSS_SELECTOR, 'input[name="kp_query"]'))
        search_input.clear()
        search_input.send_keys(actor)
        self.click_main_search_button()
        return self

    @step("Нажатие кнопки поиска на главной странице")
    def click_main_search_button(self):
        try:
            button = self.wait_for_element(
                (By.XPATH, '//button[contains(@class, "styles_submit__2AIpj") and @aria-label="Найти"]')
            )
            button.click()
        except Exception as e:
            print(f"Error clicking main search button: {e}")
        return self

    @step("Нажатие кнопки расширенного поиска")
    def click_extended_search_button(self):
        try:
            button = self.wait_for_element((By.CSS_SELECTOR, 'input.el_18.submit.nice_button'))
            button.click()
        except Exception as e:
            print(f"Error clicking extended search button: {e}")
        return self

    @step("Расширенный поиск: фильм='{movie_name}', год='{year}', страна='{country}', актер='{actor}', жанр='{genre}'")
    def extended_search_movie(self, movie_name: str = None, year: int = None, country: str = None,
                              actor: str = None, genre: str = None):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Расширенный поиск"]'))).click()

            input_movie_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#find_film')))
            input_movie_name.clear()
            input_movie_name.send_keys(movie_name)

            input_year = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#year')))
            input_year.clear()
            input_year.send_keys(year)

            input_country = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#country')))
            input_country.clear()
            input_country.send_keys(country)

            input_actor = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="m_act[actor]"]')))
            input_actor.clear()
            input_actor.send_keys(actor)

            genre_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select[id='m_act[genre]']")))
            genre_option = genre_dropdown.find_element(By.XPATH, f'.//option[@value="{genre}"]')
            genre_option.click()

        except Exception as e:
            print(f"Ошибка при выполнении расширенного поиска: {e}")
        return self

    @step("Открытие Rewiews для фильма '{movie_name}'")
    def open_reviews(self, movie_name: str):
        wait = WebDriverWait(self.driver, 10)
        self.search_main_page_movie(movie_name)
        self.click_main_search_button()
        movie_link = wait.until(EC.element_to_be_clickable((By.XPATH, f'//a[text()="{movie_name}"]')))
        movie_link.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.styles_reviewCountLight__XNZ9P.styles_reviewCount__w_RrM'))).click()
        reviews_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Рецензии зрителей")))
        reviews_link.click()
        return self

    @step("Открытие фильмографии для актёра '{actor}'")
    def open_filmography(self, actor: str):
        wait = WebDriverWait(self.driver, 10)
        self.search_main_page_actor(actor)
        self.click_main_search_button()
        actor_link = wait.until(EC.element_to_be_clickable((By.XPATH, f'//a[text()="{actor}"]')))
        actor_link.click()
        self.driver.execute_script("window.scrollBy(0, 2800)")
        filmography_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[data-tid="9fd92bab"] .styles_title__skJ4z')
        ))
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(self.driver).scroll_to_element(filmography_button).perform()
        filmography_button.click()
        return self
