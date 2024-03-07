import sys
import os
import django

sys.path.append('D:/DRF-training/walmart')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'walmart.settings')

django.setup()


import pickle
from django.core.cache import cache

# Retrieve data from Redis
redis_data = cache.get(":1:product_queryset_laptop")

# Deserialize the data
if redis_data:
    actual_data = pickle.loads(redis_data)
    print(actual_data)
else:
    print("No data found in Redis")
