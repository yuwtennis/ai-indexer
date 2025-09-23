import redis

if __name__ == "__main__":
    redis_client = redis.from_url("redis://localhost:6379")
    redis_client.ping()