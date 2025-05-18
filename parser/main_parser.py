import logging

from parser.parser import get_wb_product_data, check_position
from utils.cache_decorator import cache


@cache
async def parser(wb_url):
    try:
        product_data = await get_wb_product_data(wb_url)

        if not product_data:
            return "Не нашли вашу ссылку в первой 1000 записей"


        nm_id = product_data["id"]
        data = []

        data.append(await check_position(nm_id=nm_id, keyword=product_data["name"], max_pages=30))
        logging.info(data)
        data.append(await check_position(nm_id=nm_id, keyword=product_data["subj_name"], max_pages=50))
        logging.info(data)
        data.append(await check_position(nm_id=nm_id, keyword=product_data["subj_root_name"], max_pages=70))

        data = "\n".join(data)
        return data

    except Exception as e:
        return f"Произошла ошибка {e}"