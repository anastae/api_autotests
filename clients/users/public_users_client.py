from clients.api_client import ApiClient
from httpx import Response
from typing import TypedDict
from clients.public_http_builder import get_public_http_client

class CreateUserDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User


class PublicUsersClient(ApiClient):
    def create_user_api(self, request: CreateUserDict) -> Response:
        """метод создает нового юзера
:       :param request: Словарь с CreateUserDict.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)

    # Добавили новый метод
    def create_user(self, request: CreateUserDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())