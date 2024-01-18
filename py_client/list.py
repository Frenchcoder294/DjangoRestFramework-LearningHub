import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"

username = input('username:\n')
password = getpass()

auth_response = requests.post(auth_endpoint, json = {'username': username, 'password': password })
print(auth_response.json())
print(auth_response.status_code)

# endpoint = "http://localhost:8000/api/products/tv/"

# response = requests.get(endpoint)

# print(response.json())
