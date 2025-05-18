import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from parser.main_parser import parser


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    logging.info("Start message")
    await message.reply("Привет! Я бот, который находит текущие позиции товара в выдаче по ключевым словам.\nЕсли хочешь попробовать пришли ссылку на товар")


@dp.message()
async def handler_wb_url(message: types.Message):
    msg = await message.answer("Парсим ваши данные, подождите немного ....")
    wb_url = message.text
    data = await parser(wb_url)

    await msg.delete()
    await message.answer(data)


if __name__ == '__main__':
    logging.info("Start Bot")
    asyncio.run(dp.start_polling(bot))