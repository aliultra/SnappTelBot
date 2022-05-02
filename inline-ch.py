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


bot = Bot(token='5281541980:AAEWZkVWFLAKyu_oy4ksb96thu3MA44TWfs')
dp = Dispatcher(bot)


button1 = InlineKeyboardButton(text="‌", callback_data="status")
button2 = InlineKeyboardButton(text="𝘋𝘪𝘳𝘦𝘤𝘵", url="tg://user?id=671062879")
button3 = InlineKeyboardButton(text="𝘉𝘰𝘵", url="tg://user?id=5281541980")
keyboard_inline = InlineKeyboardMarkup().add(button1).add(button2, button3)

channel='@aliultra'

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, "❗️")


@dp.message_handler(commands=['sendinline'])
async def welcome(message: types.Message):
    await bot.send_photo(chat_id=channel, photo='https://t.me/kobstesty/151', caption='- 𝘕𝘢𝘮𝘦: <b><i>AliUltra</i></b>\n- 𝘜𝘴𝘦𝘳𝘯𝘢𝘮𝘦: <b><i>{NULL}</i></b>\n- 𝘜𝘴𝘦𝘳𝘐𝘋: <b><i>671062879</i></b>\n- 𝘋𝘤𝘐𝘋: <b><i>AMS, NL (4)</i></b>' ,reply_markup=keyboard_inline, parse_mode='HTML')    
    await message.reply("( SENT TO : "+channel+" )")


@dp.callback_query_handler(text=["status"])
async def random_value(call: types.CallbackQuery):
    IR = pytz.timezone('Asia/Tehran')
    datetime_ist = datetime.now(IR)
    await bot.answer_callback_query(callback_query_id=call.id, text="t.me/aliultra"+"  -  "+datetime_ist.strftime('%H:%M'), show_alert=False)

executor.start_polling(dp)