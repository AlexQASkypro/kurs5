import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Настройки API
    API_BASE_URL = "https://api.kinopoisk.dev"
    API_KEY = os.getenv("API_KEY", "CQRC0C0-1KY42T1-HKGVPN6-M0613Z0")  # Резервный ключ
    
    # Настройки UI
    BASE_URL = "https://www.kinopoisk.ru"
    LOGIN = os.getenv("KP_LOGIN")
    PASSWORD = os.getenv("KP_PASSWORD")
    AUTH_TOKEN = os.getenv("KP_AUTH_TOKEN")  # Для подкладывания в куки
    
    # Настройки тестов
    WAIT_TIMEOUT = 20
    HEADLESS = os.getenv("HEADLESS", "False") == "True"


settings = Settings()