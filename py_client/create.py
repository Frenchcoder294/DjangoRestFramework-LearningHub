import requests

endpoint = 'http://localhost:8000/api/products/laptop/create/'
#endpoint = 2


data = {
    'brand': 'asus',
    'model': 'x515',
    'price': 1959.97,
    #'has_lcd': False,
    'screen_size': 15,
    #'color': 'blue',
}

response = requests.post(endpoint, json=data)

print(response.json())
