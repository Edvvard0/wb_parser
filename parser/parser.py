import logging
import re

import aiohttp

from parser.raiting import get_wb_search_results, find_product_position


async def get_wb_product_data(url):
    # Извлекаем ID товара из ссылки
    match = re.search(r'/catalog/(\d+)/detail.aspx', url)
    if not match:
        logging.warning("No correct url")
        raise ValueError("Невозможно извлечь ID товара из URL")

    product_id = match.group(1)

    async with aiohttp.ClientSession() as session:
        for i in range(1, 100):
            try:
                if i < 10:
                    basket = f"0{i}"
                else:
                    basket = str(i)
                api_url = f"https://basket-{basket}.wbbasket.ru/vol{product_id[:4]}/part{product_id[:6]}/{product_id}/info/ru/card.json"

                headers = {
                    "User-Agent": "Mozilla/5.0"
                }

                async with session.get(api_url, headers=headers, timeout=10, ) as response:
                    if response.status == 200:
                        data = await response.json()
                        # print(data)
                        return transform_data(data)
            except:
                continue

    return False


def transform_data(product):
    result = {
        'id': product.get('nm_id'),
        'name': product.get('imt_name'),
        'subj_name': product.get('subj_name'),
        'subj_root_name': product.get('subj_root_name'),
    }

    return result


async def check_position(nm_id, keyword, max_pages=10):
    products = await get_wb_search_results(keyword, max_pages=max_pages)
    position = find_product_position(products, nm_id)

    if position != -1:
        return f"{keyword}: {position}"
    else:
        return f"Товар не найден в выдаче. {keyword}"
