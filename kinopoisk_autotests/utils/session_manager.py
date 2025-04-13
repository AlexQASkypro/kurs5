import pickle
import os
import allure
from selenium.webdriver.remote.webdriver import WebDriver
from config.settings import settings

class SessionManager:
    SESSION_FILE = "kp_session.pkl"

    @classmethod
    def save_session(cls, driver: WebDriver):
        """Сохраняет сессию (cookie) в файл."""
        cookies = driver.get_cookies()
        with open(cls.SESSION_FILE, 'wb') as file:
            pickle.dump(cookies, file)

    @classmethod
    def load_session(cls, driver: WebDriver):
        """Восстанавливает сессию из файла."""
        if not os.path.exists(cls.SESSION_FILE):
            return False
        with open(cls.SESSION_FILE, 'rb') as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except Exception as e:
                    print(f"Ошибка добавления cookie: {e}")
        return True
