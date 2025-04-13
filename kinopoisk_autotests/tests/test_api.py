import pytest
import allure
from utils.api_client import ApiClient
from config.test_data import TestData

@allure.feature("API Тесты Кинопоиска")
class TestKinopoiskApi:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api = ApiClient()

    @allure.story("Поиск студий")
    @allure.title("Поиск студий с корректными параметрами")
    def test_studio_search(self):
        response = self.api.get("v1.4/studio", params=TestData.STUDIO_SEARCH_PARAMS)
        with allure.step("Проверка, что в ответе есть поле 'docs' и оно не пустое"):
            assert "docs" in response, "Ответ не содержит список студий"
            assert len(response["docs"]) > 0, "Список студий пуст"
            assert "id" in response["docs"][0], "Отсутствует поле id"

    @allure.story("Поиск ключевых слов")
    @allure.title("Поиск ключевых слов по названию")
    def test_keyword_search(self):
        response = self.api.get("v1.4/keyword", params=TestData.KEYWORD_SEARCH_PARAMS)
        with allure.step("Проверка, что в ответе есть обязательные поля"):
            assert "docs" in response, "Ответ не содержит список ключевых слов"
            assert len(response["docs"]) > 0, "Список ключевых слов пуст"
            for field in ["id", "title"]:
                assert field in response["docs"][0], f"Поле {field} отсутствует в ответе"

    @allure.story("Обработка ошибок")
    @allure.title("Проверка ошибочного параметра ID")
    def test_invalid_id_parameter(self):
        response = self.api.get("v1.4/studio", params={"id": "!incorrect_id"})
        with allure.step("Проверка структуры ответа при ошибке"):
            assert "docs" in response, "Ответ должен содержать поле 'docs'"
            assert isinstance(response["docs"], list), "Поле 'docs' должно быть списком"
            invalid_ids = [studio["id"] for studio in response["docs"] if studio["id"] == "!incorrect_id"]
            assert not invalid_ids, f"Обнаружен некорректный ID: {invalid_ids}"

    @allure.story("Обработка ошибок")
    @allure.title("Проверка недопустимого значения page")
    def test_invalid_page_parameter(self):
        try:
            self.api.get("v1.4/studio", params={"page": -1, "limit": 10})
            pytest.fail("Ошибка не возникла для отрицательного номера страницы")
        except Exception as e:
            assert "400" in str(e), f"Ожидалась ошибка 400, получено: {e}"

    @allure.story("Обработка ошибок")
    @allure.title("Проверка превышения лимита")
    def test_exceeded_limit_parameter(self):
        try:
            self.api.get("v1.4/studio", params={"page": 1, "limit": 10000})
            pytest.fail("Ошибка не возникла при превышении лимита")
        except Exception as e:
            assert "400" in str(e), f"Ожидалась ошибка 400, получено: {e}"
