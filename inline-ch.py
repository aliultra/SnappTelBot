from email import message, message_from_string
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import os
import time
import datetime
import pytz
from datetime import datetime


bot = Bot(token='5250363255:AAEKZEiPzGySZpbntzdoDeaUxfxH50x9Jks')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, """خوش آمدید 🙂
برای درخواست اسنپ از گزینه (درخواست اسنپ) اقدام کنید!"""


executor.start_polling(dp)
