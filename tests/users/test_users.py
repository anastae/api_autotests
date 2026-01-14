from http import HTTPStatus
import pytest
import allure

from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake
from tools.allure.tags import AllureTag

@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
class TestUsers:
    @pytest.mark.parametrize('email', ['mail.ru', 'gmail.com', 'example.com'])
    @allure.title("Create user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    def test_create_user(self, email: str, public_users_client: PublicUsersClient):
        # генерируем почту с доменами из параметризации
        email = fake.email(domain=email)
        # Формируем тело запроса на создание пользователя
        request = CreateUserRequestSchema(email=email)
        # Отправляем запрос на создание пользователя
        response = public_users_client.create_user_api(request)
        # Инициализируем модель ответа на основе полученного JSON в ответе
        # Также благодаря встроенной валидации в Pydantic дополнительно убеждаемся, что ответ корректный
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        # Проверяем статус-код ответа
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Проверяем, что данные ответа совпадают с данными запроса
        assert_create_user_response(request, response_data)

        # Проверяет, что ответ сервера полностью соответствует ожидаемой JSON-схеме.
        # Предотвращает случайные приведения типов и скрытые ошибки.
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get user me")
    @allure.tag(AllureTag.GET_ENTITY)
    def test_get_user_me(self, private_users_client, function_user):
        # Отправляем запрос на получение данных пользователя
        response = private_users_client.get_user_me_api()
        # Валидируем тело ответа и проверяем на соответствие запросу по созданию пользователя
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)
        validate_json_schema(response.json(), response_data.model_json_schema())