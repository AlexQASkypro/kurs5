# API настройки
base_url_api = "https://api.kinopoisk.dev"
auth_token = "RRKRM0E-XNS4CW9-MYY9F2N-FR4XT65"
valid_id = 382906
invalid_id = 29999999
search_query_valid = "actor"
search_query_empty = ""  # используется в тесте пустого запроса
post_body = {"example_key": "example_value"}

# Параметры для универсального поиска
filter_params = {
    "page": 1,
    "limit": 10,
    "sortField": "name",
    "sortType": 1
}

# Ожидаемые статусы ответов API
expected_status_200 = 200
expected_status_404 = 404
expected_status_400 = 400  # не применяется в тесте пустого запроса
expected_status_401 = 401

# UI настройки
base_url_ui = "https://www.kinopoisk.ru/"

# Данные для тестирования UI
movie_name = "Терминатор"
movie_to_search = "Титаник"
movie_year = "1997"
country = "США"
actor = "Леонардо ДиКаприо"
genre = "Драма"

# Сообщения для проверки (UI)
expected_empty_search_message = "К сожалению, по вашему запросу ничего не найдено..."
