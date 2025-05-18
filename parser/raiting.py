import json

import aiohttp


async def get_wb_search_results(keyword: str, max_pages: int = 10):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }


    found_items = []

    async with aiohttp.ClientSession() as session:
        for page in range(max_pages):
                url = f"https://search.wb.ru/exactmatch/ru/common/v4/search?TestGroup=control&TestID=0&appType=1&curr=rub&dest=-1257786&page={page + 1}&query={keyword}&resultset=catalog&sort=popular&spp=30"
                async with session.get(url, headers=headers, timeout=10, ) as response:
                    if response.status != 200:
                        break

                    text = await response.text()
                    data = json.loads(text)
                    if "data" not in data or "products" not in data["data"]:
                        break

                    products = data["data"]["products"]
                    if not products:
                        break

                    found_items.extend(products)

        return found_items


def find_product_position(products, target_nmid: int):
    for idx, product in enumerate(products, start=1):
        if product.get("id") == target_nmid:
            return idx
    return -1
