import datetime
import time
from aiogram import Bot, Dispatcher, executor, types
import logging
from config import TOKEN, CHANNELID
from db import Sqlite
import requests

time1 = datetime.time(10, 00, 00)
time2 = datetime.time(19,00,00)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
db = Sqlite('db.db')

@dp.message_handler(commands='start')
async def start(message: types.Message):
    db.add_user(message.from_user.id)
    await message.answer('Вы успешно подписались на рассылку.')

@dp.message_handler(commands='stats')
async def stats(message: types.Message):
    await message.answer(f'{len(db.get_user())} - пользователей используют бота')    

if __name__ == '__main__':
    executor.start_polling(dp)

    
        

