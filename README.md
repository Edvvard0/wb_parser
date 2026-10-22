<div align="center">

# 🔎 Wildberries Position Bot

**Telegram-бот, который находит позиции товара Wildberries в поисковой выдаче по ключевым словам**

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-3.20-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![aiohttp](https://img.shields.io/badge/aiohttp-2C5BB4?style=for-the-badge&logo=aiohttp&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

</div>

---

## 📖 О проекте

Бот для селлеров и аналитиков маркетплейса Wildberries: пришлите ссылку на карточку товара — в ответ получите его позиции в поисковой выдаче по трём ключевым словам: названию товара, его категории и родительской категории. Повторные запросы по той же ссылке отдаются из Redis-кэша, чтобы не нагружать API Wildberries.

<!-- TODO: скриншот -->

## ✨ Возможности

- 🔗 Приём ссылки вида `.../catalog/<id>/detail.aspx` и извлечение ID товара
- 📦 Получение данных карточки: название, категория, родительская категория
- 📈 Позиция товара в выдаче по трём ключевым словам (просматривается до 30 / 50 / 70 страниц выдачи соответственно)
- ⚡ Кэширование ответа в Redis на 1 час (ключ — URL товара)
- 🪵 Асинхронная работа (aiogram + aiohttp) и логирование в консоль

## 🧱 Стек

| Технология | Роль |
|---|---|
| Python 3.12+ | Язык |
| aiogram 3.20 | Telegram Bot API |
| aiohttp | Асинхронные запросы к публичным эндпоинтам Wildberries |
| Redis (`redis` 6.1) | Кэш результатов (TTL 3600 с) |
| python-dotenv | Загрузка переменных окружения |

## 🗂 Структура проекта

```text
.
├── bot/
│   └── bot.py               # запуск бота, /start и обработка ссылок
├── parser/
│   ├── main_parser.py       # сценарий: данные товара → позиции по 3 запросам
│   ├── parser.py            # данные карточки и проверка позиции
│   └── raiting.py           # поиск по выдаче и определение позиции
├── utils/
│   ├── cache_decorator.py   # декоратор @cache
│   ├── redis_connect.py     # подключение к Redis
│   └── redis_dao.py         # чтение/запись кэша
├── pyproject.toml
└── requirements.txt
```

## 🚀 Быстрый старт

```bash
git clone https://github.com/Edvvard0/wb_parser.git
cd wb_parser

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Создайте `.env` в корне проекта (см. «Конфигурацию») и запустите бота:

```bash
python -m bot.bot
```

Нужны токен бота от [@BotFather](https://t.me/BotFather) и доступ к Redis (облачный или локальный).

## ⚙️ Конфигурация

| Переменная | Назначение |
|---|---|
| `BOT_TOKEN` | Токен Telegram-бота от @BotFather |
| `REDIS_URL` | URL подключения к Redis (для кэша) |

## 🔌 Команды бота

| Команда / сообщение | Действие |
|---|---|
| `/start` | Приветствие и инструкция |
| Ссылка на товар Wildberries | Позиции товара по названию, категории и родительской категории |

## 📄 Лицензия

MIT — см. файл [LICENSE](LICENSE).

## 👤 Автор

**Эдвард Осипчук** · GitHub: [@Edvvard0](https://github.com/Edvvard0) · Telegram: [@Edward0076](https://t.me/Edward0076)
