from http import HTTPStatus
import pytest

from clients.users.public_users_client import get_public_users_client
from clients.authentication.authentication_client import get_authentication_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from tools.assertions.base import assert_status_code
from tools.assertions.authentification import assert_login_response
from tools.assertions.schema import validate_json_schema

@pytest.mark.authentication
@pytest.mark.regression
def test_login():
    public_users_client = get_public_users_client()
    authentification_client = get_authentication_client()

    request_user = CreateUserRequestSchema()
    public_users_client.create_user(request_user)

    request = LoginRequestSchema(email=request_user.email, password=request_user.password)
    response = authentification_client.login_api(request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_login_response(response_data)
    validate_json_schema(response.json(), response_data.model_json_schema())







