import requests

class ProjectAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, title):
        """Создает проект с указанным заголовком."""
        payload = {
            "title": title
        }
        response = requests.post(f"{self.base_url}/projects", json=payload, headers=self.headers)
        response.raise_for_status()  # Проверяем, что запрос успешен
        return response.json()["id"]  # Возвращаем ID созданного проекта

    def get_project(self, project_id):
        """Получает проект по ID."""
        response = requests.get(f"{self.base_url}/projects/{project_id}", headers=self.headers)
        response.raise_for_status()  # Проверяем, что запрос успешен
        return response.json()  # Возвращаем данные проекта

    def update_project(self, project_id, title):
        """Обновляет проект с указанным ID."""
        payload = {
            "title": title
        }
        response = requests.put(f"{self.base_url}/projects/{project_id}", json=payload, headers=self.headers)
        response.raise_for_status()  # Проверяем, что запрос успешен
        return response.json()  # Возвращаем ответ сервера

    def delete_project(self, project_id):
        """Удаляет проект с указанным ID."""
        response = requests.delete(f"{self.base_url}/projects/{project_id}", headers=self.headers)
        if response.status_code != 404:  # Проверяем, что проект не был удален ранее
            response.raise_for_status()  # Проверяем, что запрос успешен