import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input('username:\n')
password = getpass('password:\n')

auth_response = requests.post(auth_endpoint, json = {'username': username, 'password': password })
print('JSON:', auth_response.json())

if auth_response.status_code == 200:
    endpoint = 'http://localhost:8000/products/tv/create/'
    token = auth_response.json()['token']

    headers = {
        'Authorization': f'Bearer {token}'
        }
    # print(headers)
    
    data = {
        "brand": "samsung",
        "model": "d254",
        "price": 1959.97,
        "screen_size": 55,
    }

    response = requests.post(endpoint, json=data, headers=headers)

    print(response.json())
    print(response.status_code)