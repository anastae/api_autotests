from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class LoginRequestDict(TypedDict):
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    refreshToken: str  # Название ключа совпадает с API

class AuthenticationClient(ApiClient): #Клиент для работы с /api/v1/authentication, добавлять методы
    def login_api(self, request: LoginRequestDict) -> Response:
        """
               Метод выполняет аутентификацию пользователя.
               :return: Ответ от сервера в виде объекта httpx.Response
               """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)
