import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"

username = input('username:\n')
password = getpass()

auth_response = requests.post(auth_endpoint, json = {'username': username, 'password': password })
# print('JSON:', auth_response.json())
# print('Status: ', auth_response.status_code)

endpoint = "http://localhost:8000/products/phone/"
token = auth_response.json()['token']

headers = {
    'Authorization': f'Token {token}'
    }

response = requests.get(endpoint, headers=headers)

print(response.json())
