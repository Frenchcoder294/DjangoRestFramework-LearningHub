import requests

endpoint = 'http://localhost:8080/products/tv/create/'
#endpoint = 2


data = {
    "brand": "samsung",
    "model": "d254",
    "price": 1959.97,
    "screen_size": 55,
}

response = requests.post(endpoint, json=data)

print(response.json())
