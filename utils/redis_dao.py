import asyncio

from utils.redis_connect import connection


class RedisDAO:
    @classmethod
    async def get_data(cls, url: str) -> str:
        redis_client = await connection()
        return redis_client.get(url)

    @classmethod
    async def add_data(cls, url: str, data: str):
        redis_client = await connection()
        if redis_client is None:
            return

        redis_client.set(url, data, ex=3600)
        # print(f"Данные сохранены для {url} с TTL {3600} секунд")



# async def main():
#     await RedisDAO.add_data("http://1", "fadgbvdfg \ndfbgdfab")
#     print(await RedisDAO.get_data("http://1"))
#
# asyncio.run(main())