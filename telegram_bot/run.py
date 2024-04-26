import os
import logging
import aiogram
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, педик!')



async def main():
    await dp.start_polling(bot)
    

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try: 
        asyncio.run(main())
    except KeyboardInterrupt:
        print('EXIT')