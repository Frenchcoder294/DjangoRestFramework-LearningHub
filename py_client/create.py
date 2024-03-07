import requests

endpoint = 'http://localhost:8000/products/laptop/create/'
#endpoint = 2


data = {
    'brand': 'apple',
    'model': 'x1eqe',
    'price': 1959.97,
    'screen_size': 15,
}

response = requests.post(endpoint, json=data)

print(response.json())
