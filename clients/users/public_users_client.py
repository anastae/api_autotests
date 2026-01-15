from clients.api_client import ApiClient
from httpx import Response
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema
from clients.public_http_builder import get_public_http_client
from tools.routes import APIRoutes

class PublicUsersClient(ApiClient):
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """метод создает нового юзера
:       :param request: Словарь с CreateUserRequestSchema.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(APIRoutes.USERS, json=request.model_dump(by_alias=True)) #model_dump(by_alias=True) приводит данные к формату API

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())