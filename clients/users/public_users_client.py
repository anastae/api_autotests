from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict

class CreateUserDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(ApiClient):
    def create_user_api(self, request: CreateUserDict) -> Response:
        """метод создает нового юзера
:       :param request: Словарь с CreateUserDict.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)