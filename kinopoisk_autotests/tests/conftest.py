import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from config.settings import settings

@pytest.fixture(scope="function")
def driver():
    """Фикстура инициализации FirefoxDriver."""
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webnotifications.enabled", False)
    options.set_preference("media.volume_scale", "0.0")
    if settings.HEADLESS:
        options.add_argument("--headless")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
