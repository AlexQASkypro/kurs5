import requests


class KinopoiskTestingAPI:
    def __init__(self, base_url, auth_token):
        """
        Инициализация клиента API с базовым URL и токеном авторизации.
        """
        self.base_url = base_url
        self.headers = {
            "X-API-KEY": auth_token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get_person_by_id(self, person_id):
        """
        Запрос для поиска персоны по ID.
        """
        url = f"{self.base_url}/v1.4/person/{person_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def search_person_by_name(self, query):
        """
        Поиск персон по имени.
        """
        url = f"{self.base_url}/v1.4/person/search?query={query}"
        response = requests.get(url, headers=self.headers)
        return response

    def universal_search_with_filters(self, params):
        """
        Универсальный поиск с фильтрами.
        """
        url = f"{self.base_url}/v1.4/person"
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def post_person_by_id(self, person_id, body):
        """
        POST-запрос для поиска персоны по ID.
        """
        url = f"{self.base_url}/v1.4/person/{person_id}"
        response = requests.post(url, headers=self.headers, json=body)
        return response

    def search_person_with_empty_query(self):
        """
        Поиск персон с пустым параметром `query`.
        """
        url = f"{self.base_url}/v1.4/person/search?query="
        response = requests.get(url, headers=self.headers)
        return response

    def get_person_without_token(self, person_id):
        """
        Запрос на поиск персоны по ID без токена авторизации.
        """
        url = f"{self.base_url}/v1.4/person/{person_id}"
        response = requests.get(url)
        return response
