import requests
from allure import step
from config.settings import settings

class ApiClient:
    def __init__(self):
        self.base_url = settings.API_BASE_URL
        self.headers = {
            "accept": "application/json",
            "X-API-KEY": settings.API_KEY
        }

    @step("Отправка GET запроса к {endpoint}")
    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    @step("Проверка статус кода ответа")
    def check_status_code(self, response, expected_code):
        assert response.status_code == expected_code, \
            f"Ожидался статус код {expected_code}, получен {response.status_code}"
