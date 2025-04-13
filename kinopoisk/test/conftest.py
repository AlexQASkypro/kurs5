import pytest
import os
import pickle
import config
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.Kinopoisk_testing_ui import Kinopoisk_testing_ui

def captcha_solved(driver):
    """
    Функция-предикат для WebDriverWait.
    Возвращает True, если элемент капчи отсутствует или скрыт.
    Здесь предполагается, что капча отображается в элементе с селектором "div.captcha-container".
    Если селектор другой, замените его на корректный.
    """
    try:
        captcha_elem = driver.find_element(By.CSS_SELECTOR, "div.captcha-container")
        return not captcha_elem.is_displayed()
    except Exception:
        # Если элемент не найден, считаем, что капча не отображается
        return True

@pytest.fixture
def auth_api():
    """
    Фикстура для авторизованного API-клиента.
    """
    import requests
    session = requests.Session()
    session.headers.update({
        "X-API-KEY": config.auth_token,
        "Accept": "application/json",
        "Content-Type": "application/json"
    })
    print(f"Токен авторизации (из config): {config.auth_token}")
    return session

@pytest.fixture
def api_client():
    """
    Фикстура для API-клиента без авторизации.
    """
    import requests
    session = requests.Session()
    return session

@pytest.fixture(scope="function")
def setup_auth_and_driver():
    """
    Фикстура для настройки Firefox WebDriver, ожидания решения капчи,
    сохранения и загрузки cookies (с помощью pickle) для обхода капчи
    и выполнения авторизации UI.
    """
    options = FFOptions()
    # Для прохождения капчи рекомендуется запускать браузер в режиме с визуальным отображением
    # (headless-параметр можно отключить). В headless-режиме капча может не отображаться корректно.
    options.headless = False

    try:
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке geckodriver: {e}")

    try:
        driver.get(config.base_url_ui)
        driver.implicitly_wait(5)
    except Exception as e:
        driver.quit()
        raise RuntimeError(f"Ошибка при открытии страницы {config.base_url_ui}: {e}")

    cookies_file = os.path.join(os.getcwd(), "cookies.pkl")
    if os.path.exists(cookies_file):
        # Если файл с cookie существует, загружаем их из pickle
        with open(cookies_file, "rb") as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"Не удалось добавить cookie {cookie}: {e}")
        driver.refresh()
        print("Cookies загружены из pickle файла, капча пропущена.")
    else:
        # Ожидаем решения капчи (до 180 секунд)
        try:
            WebDriverWait(driver, 180).until(captcha_solved)
            print("Captcha решена или отсутствует.")
        except Exception as e:
            driver.quit()
            raise RuntimeError("Captcha не была решена в течение отведённого времени.")
        # Сохраняем cookies в pickle файл для будущих запусков
        cookies = driver.get_cookies()
        with open(cookies_file, "wb") as f:
            pickle.dump(cookies, f)
        print("Cookies сохранены в pickle файл для следующих запусков.")

    auth_ui = Kinopoisk_testing_ui(config)
    auth_ui.set_driver(driver)
    yield auth_ui, driver
    driver.quit()

@pytest.fixture
def test_config():
    """
    Фикстура для доступа к конфигурации проекта.
    """
    return config
