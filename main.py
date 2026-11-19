import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handler import setup_message_routers

API_TOKEN = BOT_TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def main():
    handler_router = setup_message_routers()
    dp.include_router(handler_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
