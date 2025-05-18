import asyncio
import logging
import os

import redis
from dotenv import load_dotenv
from redis.asyncio import Redis

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL")

redis_url = REDIS_URL

async def connection() -> Redis:
    redis_client = redis.Redis.from_url(redis_url, decode_responses=True)

    try:
        response = redis_client.ping()
        if response:
            logging.debug("Подключение успешно!")
        else:
            logging.error("Не удалось подключиться к Redis.")
            return None
    except redis.exceptions.RedisError as e:
        logging.error(f"Ошибка: {e}")

    # redis_client.set("1", 123)
    # print(redis_client.get("1"))
    return redis_client

asyncio.run(connection())
