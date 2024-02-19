import requests

endpoint = 'http://localhost:8000/products/earbud/7/delete/'

response = requests.delete(endpoint)

print(response.content, response.status_code)