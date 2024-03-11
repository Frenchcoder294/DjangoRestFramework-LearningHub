import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"

username = input('username:\n')
password = getpass('password:\n')

auth_response = requests.post(auth_endpoint, json = {'username': username, 'password': password })
print('JSON:', auth_response.json())
# print('Status: ', auth_response.status_code)


if auth_response.status_code == 200:
    endpoint = "http://localhost:8000/products/phone/"
    token = auth_response.json()['token']

    headers = {
        'Authorization': f'Token {token}'
        }
    print(headers)

    response = requests.get(endpoint, headers=headers)

    print(response.json())
    print(response.status_code)
