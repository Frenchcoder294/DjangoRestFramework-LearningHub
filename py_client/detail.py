import requests
import time

start = time.time()

endpoint = "http://localhost:8000/products/laptop/"

response = requests.get(endpoint)
end = time.time()

elapsed = end - start
print(response.json())
print('time: ', elapsed)