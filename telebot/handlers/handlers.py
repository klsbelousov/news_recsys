import aiogram, asyncio
from aiogram import types, Router
from aiogram.filters import CommandStart, Command


handler = Router()

#start command
@handler.message(CommandStart())                     
async def cmd_start(message: types.Message):
    await message.answer(
        text='''Привет, я – Хэдлайнер твоих новостей. 
Я помогу сэкономить тебе время и буду ограждать тебя от негативных новостей(если ты, конечно, хочешь)
'''
        )
@handler.message(Command('menu'))
async def cmd_menu(message: types.Message):
    await message.answer(text='Меню:')

@handler.message(Command('settings'))
async def cmd_menu(message: types.Message):
    await message.answer(text='Настройки бота:')

@handler.message(Command('feedback'))
async def cmd_menu(message: types.Message):
    await message.answer(text='Обратная связь:')

@handler.message(Command('about'))
async def cmd_menu(message: types.Message):
    await message.answer(text='О боте:')

#handling user id message.from_user.id
# @handler.message()                               
# async def greeting(message: types.Message):
#     text = message.text
#     if text in ['Привет', 'Здарова', 'Hi', 'Hello']:
#         await message.answer(text='И тебе привет!')
#     elif text in ['Пока', 'Покеда', 'До свидания']:
#         await message.answer(text='Всего доброго!')
#     else:
#         user_id = message.from_user.id
#         print('User ID:', user_id)
#         return user_id

