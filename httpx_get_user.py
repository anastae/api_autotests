import httpx

from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "269269",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

auth_payload = {
    "email": create_user_response_data['user']['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=auth_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get(
    f'http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}', headers=get_user_headers)
get_user_response_data = get_user_response.json()
print('Get user data:', get_user_response_data)

delete_user_response = httpx.delete(f'http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}', headers=get_user_headers)
delete_user_response_code = delete_user_response.status_code
print('Delete user data:', delete_user_response_code)