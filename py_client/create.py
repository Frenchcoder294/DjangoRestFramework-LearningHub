import requests
from getpass import getpass

auth_endpoint = "http://localhost:8080/api/auth/"
username = input('username:\n')
password = getpass('password:\n')

auth_response = requests.post(auth_endpoint, json = {'username': username, 'password': password })
print('JSON:', auth_response.json())

if auth_response.status_code == 200:
    endpoint = 'http://localhost:8080/products/tv/create/'
    token = auth_response.json()['token']

    headers = {
        'Authorization': f'Bearer {token}'
        }
    # print(headers)
    
    data = {
        "brand": "apple",
        "model": "3306",
        "price": 6959.97,
        "screen_size": 60,
    }

    response = requests.post(endpoint, json=data, headers=headers)

    print(response.json())
    print(response.status_code)