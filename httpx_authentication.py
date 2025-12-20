import httpx
payload = {
    "email": "test@example.com",
    "password": "269269"
}
response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=payload)
login_response = response.json()
login_access_token = login_response["token"]["accessToken"]
print('login:', login_response)
print(response.status_code)

response = httpx.get('http://localhost:8000/api/v1/users/me', headers={'Authorization': f'Bearer {login_access_token}'})
print(response.json())
print(response.status_code)
# refresh_payload = {
#     "refreshToken": login_response['token']['refreshToken']
# }
#
# refresh_response = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json=refresh_payload)
# refresh_response_json = refresh_response.json()
# print('refresh:', refresh_response_json)
# print(response.status_code)