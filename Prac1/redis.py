import redis
r = redis.Redis()
r.mset({'Croatia': 'Zagreb'})
print(r.get('Croatia'))
