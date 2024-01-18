import requests

endpoint = 'http://localhost:8000/api/products/laptop/1/update/'

data = {
    'brand': 'apple',
    'model': 'macboock pro 1 ',
    'price': 1999.99,
    'size': 15,
}

response = requests.put(endpoint, json=data)

print(response.json())