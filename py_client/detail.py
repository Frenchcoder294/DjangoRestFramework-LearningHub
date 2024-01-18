import requests

endpoint = "http://localhost:8000/api/products/phone/"

response = requests.get(endpoint)

print(response.json())