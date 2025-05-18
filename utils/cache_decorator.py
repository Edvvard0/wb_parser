from utils.redis_dao import RedisDAO


def cache(func):
    async def wrapper(*args, **kwargs):
        wb_url = args[0]
        cache_data = await RedisDAO.get_data(wb_url)
        if cache_data:
            return cache_data

        data = await func(*args, **kwargs)

        await RedisDAO.add_data(wb_url, data)
        return data
    return wrapper