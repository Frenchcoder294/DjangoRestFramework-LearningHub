import requests

endpoint = 'http://localhost:8000/api/products/phone/4/delete/'

response = requests.delete(endpoint)

print(response.content, response.status_code)