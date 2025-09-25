import logging
import redis
from redis.exceptions import ResponseError


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class RedisOps(metaclass=SingletonMeta):

    LOGGER = logging.getLogger(__name__)

    def __init__(self, redis_url: str):
        self._redis_cli = redis.from_url(redis_url)

    def idx_exists(self, index_name) -> bool:
        """ """
        try:
            self._redis_cli.ft(index_name).info()
        except ResponseError:
            return False

        return True
