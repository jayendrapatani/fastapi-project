import json 
import redis 
from app.core.config import settings

redis_client=redis.Redis.from_url(settings.REDIS_URL)


def get_sached_prediction(key: str):
    value = redis_client.get(key)
    return eval(value) if value else None


def set_cached_prediction(key: str, value: dict):
    redis_client.set(key, str(value))