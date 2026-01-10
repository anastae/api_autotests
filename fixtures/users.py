import pytest
from pydantic import BaseModel, EmailStr

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.private_users_client import PrivateUsersClient, get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema

# Модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password

    def authentication_user(self) -> AuthenticationUserSchema: # для аутентификации API-клиентов
        return AuthenticationUserSchema(email=self.email, password=self.password)


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()

@pytest.fixture
def private_users_client(function_user) -> PrivateUsersClient:
    # Создаем новый API клиент для работы с приватным API пользователей
    return get_private_users_client(function_user.authentication_user())


# Фикстура для создания пользователя
@pytest.fixture
# Название строится по шаблону {scope фикстуры}_{название создаваемой сущности}
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)  # Возвращаем все нужные данные