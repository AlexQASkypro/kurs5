import pytest
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Search for a movie on the main page")
@allure.severity("blocker")
@pytest.mark.ui
def test_search_movie_main_page(setup_auth_and_driver, test_config):
    """Проверка поиска фильма на главной странице."""
    with allure.step("Открыть сайт, отметить чекбокс капчи"):
        auth_ui, driver = setup_auth_and_driver
    with allure.step("Ввести название фильма и нажать кнопку поиска."):
        auth_ui.search_main_page_movie(test_config.movie_to_search)
    with allure.step("Проверить, что результат поиска отображается корректно."):
        try:
            if driver.find_elements(By.CSS_SELECTOR, '.search_results'):
                film_name_element = driver.find_element(By.CSS_SELECTOR, '.search_results .name a')
                film_name = film_name_element.text.strip().lower()
                expected_name = test_config.movie_to_search.strip().lower()
                assert film_name == expected_name, f"Название фильма '{film_name}' не соответствует ожидаемому '{expected_name}'."
            elif driver.find_elements(By.CSS_SELECTOR, 'h2.textorangebig'):
                no_results_message = driver.find_element(By.CSS_SELECTOR, 'h2.textorangebig').text
                assert no_results_message == test_config.expected_empty_search_message, "Сообщение о ненайденном результате неожиданное."
            else:
                assert False, "Не найдены результаты поиска или сообщение об ошибке."
        except Exception as e:
            assert False, f"Поиск для '{test_config.movie_to_search}' завершился с ошибкой: {e}"


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Search for an actor on the main page")
@allure.severity("blocker")
@pytest.mark.ui
def test_search_actor_main_page(setup_auth_and_driver, test_config):
    with allure.step("Открыть сайт, отметить чекбокс капчи"):
        auth_ui, driver = setup_auth_and_driver
    with allure.step("Ввести имя актёра и нажать кнопку поиска."):
        auth_ui.search_main_page_actor(test_config.actor)
    with allure.step("Проверить отображение результата поиска актёра."):
        try:
            WebDriverWait(driver, 10).until(lambda d: d.find_elements(By.CSS_SELECTOR, '.search_results'))
            results_text = driver.find_element(By.CSS_SELECTOR, '.search_results_topText').text
            match = re.search(r'результаты: (\d+)', results_text)
            if match:
                count = int(match.group(1))
                assert count > 0, "По запросу актёра не найдено результатов."
                actor_name = driver.find_element(By.CSS_SELECTOR, '.search_results_topText b').text.strip().lower()
                expected_actor = test_config.actor.strip().lower()
                assert actor_name == expected_actor, f"Имя актёра '{actor_name}' не соответствует ожидаемому '{expected_actor}'."
            else:
                assert False, "Не удалось найти количество результатов в тексте поиска."
        except Exception as e:
            assert False, f"Поиск для '{test_config.actor}' завершился с ошибкой: {e}"


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Search for a movie using the extended search")
@allure.severity("blocker")
@pytest.mark.ui
def test_extended_search_movie(setup_auth_and_driver, test_config):
    with allure.step("Открыть сайт, отметить чекбокс капчи"):
        auth_ui, driver = setup_auth_and_driver
        expected_movie_text = f"{test_config.movie_to_search} ({test_config.movie_year})"
    with allure.step("Перейти на страницу расширенного поиска и ввести параметры поиска."):
        auth_ui.extended_search_movie(
            test_config.movie_to_search,
            test_config.movie_year,
            test_config.country,
            test_config.actor,
            test_config.genre
        )
    with allure.step("Нажать кнопку расширенного поиска."):
        auth_ui.click_extended_search_button()
    with allure.step("Проверить, что название и год фильма соответствуют ожидаемым."):
        try:
            h1_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1[data-tid="f22e0093"]'))
            )
            movie_element = h1_element.find_element(By.CSS_SELECTOR, 'span[data-tid="75209b22"]')
            movie_text = movie_element.text.strip()
            assert movie_text == expected_movie_text, f"Ожидалось '{expected_movie_text}', но получено '{movie_text}'."
        except Exception as e:
            assert False, f"Фильм '{expected_movie_text}' не найден в результатах поиска: {e}"


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Open the movie reviews")
@allure.severity("blocker")
@pytest.mark.ui
def test_search_and_open_movie_reviews(setup_auth_and_driver, test_config):
    with allure.step("Открыть сайт, отметить чекбокс капчи"):
        auth_ui, driver = setup_auth_and_driver
    with allure.step("Найти фильм по названию и перейти на страницу рецензий."):
        auth_ui.open_reviews(test_config.movie_name)
        reviews_label = driver.find_element(By.XPATH, '//span[text()="Все:"]')
    with allure.step("Найти и записать количество рецензий."):
        reviews_count = reviews_label.find_element(By.XPATH, 'following-sibling::b').text
        count = int(reviews_count)
    with allure.step("Проверить, что количество рецензий больше 0."):
        assert count > 0, f"Ожидалось минимум одна рецензия, найдено {count}."


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Open the actor's filmography")
@allure.severity("blocker")
@pytest.mark.ui
def test_search_and_open_actor_filmography(setup_auth_and_driver, test_config):
    with allure.step("Открыть сайт, отметить чекбокс капчи"):
        auth_ui, driver = setup_auth_and_driver
    with allure.step("Найти актёра по имени и открыть его фильмографию."):
        try:
            auth_ui.open_filmography(test_config.actor)
        except Exception as e:
            print(f"Warning: Ошибка при открытии фильмографии: {e}")
    with allure.step("Ожидать появления заголовка с именем актёра на странице фильмографии."):
        actor_header = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//h1[contains(text(), "{test_config.actor}")]')
            )
        )
    with allure.step("Проверить, что заголовок отображается."):
        assert actor_header.is_displayed(), f"Фильмография для актёра '{test_config.actor}' не открылась."
