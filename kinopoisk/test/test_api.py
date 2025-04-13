import pytest
import config
import allure
import requests


@pytest.fixture
def auth_api():
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
    session = requests.Session()
    return session


@allure.epic("API Testing")
@allure.feature("Person Search")
@allure.story("Search by valid ID")
@allure.severity("blocker")
@allure.title("Test search by valid ID")
@pytest.mark.api
def test_search_by_id(auth_api):
    url = f"{config.base_url_api}/v1.4/person/{config.valid_id}"
    with allure.step("Отправить запрос GET на поиск по ID."):
        response = auth_api.get(url)
        print(f"URL: {url}, Статус ответа: {response.status_code}, Тело ответа: {response.text}")
    with allure.step("Проверить, что возвращён статус 200."):
        assert response.status_code == config.expected_status_200, "Неверный статус ответа"


@allure.epic("API Testing")
@allure.feature("Person Search")
@allure.story("Universal Search with Filters")
@allure.severity("critical")
@allure.title("Test universal search with filters")
@pytest.mark.api
def test_filter_search(auth_api):
    url = f"{config.base_url_api}/v1.4/person?page=1&limit=10&sortField=name&sortType=1"
    with allure.step("Отправить запрос GET с параметрами фильтрации."):
        response = auth_api.get(url)
        print(f"URL: {url}, Статус ответа: {response.status_code}, Тело ответа: {response.text}")
    with allure.step("Проверить, что возвращён статус 200."):
        assert response.status_code == config.expected_status_200, "Неверный статус ответа"


@allure.epic("API Testing")
@allure.feature("Person Search")
@allure.story("Search by Name")
@allure.severity("critical")
@allure.title("Test search by name")
@pytest.mark.api
def test_search_by_name(auth_api):
    url = f"{config.base_url_api}/v1.4/person/search?query={config.search_query_valid}"
    with allure.step("Отправить запрос GET с параметром имени."):
        response = auth_api.get(url)
        print(f"URL: {url}, Статус ответа: {response.status_code}, Тело ответа: {response.text}")
    with allure.step("Проверить, что возвращён статус 200."):
        assert response.status_code == config.expected_status_200, "Неверный статус ответа"


@allure.epic("API Testing")
@allure.feature("Person Search")
@allure.story("Search by Invalid ID")
@allure.severity("medium")
@allure.title("Test search by invalid ID")
@pytest.mark.api
def test_search_invalid_id(auth_api):
    url = f"{config.base_url_api}/v1.4/person/{config.invalid_id}"
    with allure.step("Отправить запрос GET с невалидным ID."):
        response = auth_api.get(url)
        print(f"URL: {url}, Статус ответа: {response.status_code}, Тело ответа: {response.text}")
    with allure.step("Проверить, что возвращён статус 404."):
        assert response.status_code == config.expected_status_404, "Ожидался статус 404"


@allure.epic("API Testing")
@allure.feature("Person Search")
@allure.story("Search with Empty Query")
@allure.severity("medium")
@allure.title("Test search with empty query")
@pytest.mark.api
def test_search_empty_query(auth_api):
    url = f"{config.base_url_api}/v1.4/person/search?query="
    with allure.step("Отправить запрос GET с пустым query."):
        response = auth_api.get(url)
        print(f"URL: {url}, Статус ответа: {response.status_code}, Тело ответа: {response.text}")
    with allure.step("Проверить, что возвращён статус 200 и список результатов не пустой."):
        assert response.status_code == config.expected_status_200, (
            f"Ожидался статус 200 для пустого запроса, но был {response.status_code}"
        )
        data = response.json()
        # Здесь ожидаем, что API возвращает данные по умолчанию
        assert len(data.get("docs", [])) > 0, "Ожидались ненулевые результаты для пустого запроса"


@allure.epic("API Testing")
@allure.feature("Person Search")
@allure.story("Search by ID without Token")
@allure.severity("critical")
@allure.title("Test search by ID without authorization token")
@pytest.mark.api
def test_search_without_token(api_client):
    url = f"{config.base_url_api}/v1.4/person/{config.valid_id}"
    with allure.step("Отправить запрос GET без токена авторизации."):
        response = api_client.get(url)
        print(f"URL: {url}, Статус ответа: {response.status_code}, Тело ответа: {response.text}")
    with allure.step("Проверить, что возвращён статус 401."):
        assert response.status_code == config.expected_status_401, "Ожидался статус 401"


@allure.epic("API Testing")
@allure.feature("Person Search")
@allure.story("Search by POST Method")
@allure.severity("low")
@allure.title("Test search by ID using POST method instead of GET")
@pytest.mark.api
def test_search_with_post_method(auth_api):
    url = f"{config.base_url_api}/v1.4/person/{config.valid_id}"
    body = config.post_body
    with allure.step("Отправить POST-запрос на поиск по ID."):
        response = auth_api.post(url, json=body)
        print(f"URL: {url}, Статус ответа: {response.status_code}, Тело ответа: {response.text}")
    with allure.step("Проверить, что возвращён статус 404."):
        assert response.status_code == config.expected_status_404, "Ожидался статус 404"


@allure.epic("API Testing")
@allure.feature("Person Search")
@allure.story("Universal Search without Filters")
@allure.severity("medium")
@allure.title("Test universal search without parameters")
@pytest.mark.api
def test_search_without_params(auth_api):
    url = f"{config.base_url_api}/v1.4/person"
    with allure.step("Отправить запрос GET без параметров."):
        response = auth_api.get(url)
        print(f"URL: {url}, Статус ответа: {response.status_code}, Тело ответа: {response.text}")
    with allure.step("Проверить, что возвращён статус 200 и результаты присутствуют."):
        assert response.status_code == config.expected_status_200, "Неверный статус ответа"
        assert len(response.json().get("docs", [])) > 0, "Результаты поиска отсутствуют"
