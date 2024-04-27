import os
import dotenv
import logging

import asyncio
from aiogram import Bot, Dispatcher

from handlers.handlers import handler
from common.commands import commands_list
dotenv.load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()
ALLOWED_UPDATES = ['message', 'edited_message']

dp.include_routers(handler)

async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=commands_list)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
