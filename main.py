import logging
from unicodedata import name
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from aiogram.types import ParseMode
from datetime import datetime, timedelta

import config as cfg
import SchoolScript as school
import markups as env 
logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет", reply_markup=env.Menu)

@dp.message_handler()
async def start(message: types.Message):
    text = message.text

    if text == 'Расписание на сегодня':
        await bot.send_message(message.from_user.id, school.TimeTable(0))
    
    if text == 'Расписание на завтра':
        await bot.send_message(message.from_user.id, school.TimeTable(1))
    
    elif text == 'Расписание звонков':
        await bot.send_message(message.from_user.id, school.Calls())
    
    elif text == 'Когда звонок?':
        await bot.send_message(message.from_user.id, school.WhenCall())

    elif message.from_user.id == cfg.ADMIN_ID:
        if text.split(' ')[0] == ',,':
            ID = text.split(' ')[1]
            TEXT = text[text.find(' ',len(ID))+1:]
            print(ID, TEXT)
            await bot.send_message(ID, TEXT, reply_markup=env.Menu)
    else:
        await bot.send_message(cfg.ADMIN_ID, f',, {message.from_user.id}')
        await bot.send_message(cfg.ADMIN_ID, f'name: {message.from_user.full_name}\ntext: {text}', reply_markup=env.Menu)


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates = True)
    except:
        pass
