import aioredis


client_redis = aioredis.Redis(host='redis', port=6379, db=0)
