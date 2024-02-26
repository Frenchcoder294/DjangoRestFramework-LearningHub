import redis

# initiate redis
r = redis.Redis(
  host='redis-14042.c54.ap-northeast-1-2.ec2.cloud.redislabs.com',
  port=14042,
  password='Jrfwliaxc49EjovAcjKwPN79QdcSnEO0')

# create instances
r.set('new_key', 'new_value')