import asyncio

from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, File, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BotBlocked

from keyboards import kb_client_start
from create_bot import dp, bot
from data_base import sqlite_db


a_inline = InlineKeyboardMarkup()
a_reply = ReplyKeyboardRemove()

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
            await bot.send_message(message.from_user.id, 'Приветствую вас в боте ANIMA!')
    except :
        await message.reply('Общение с ботом через ЛС, напишите ему:\n www...')




# Регистрация хэндрелов
#ef register_handlers_client(dp: Dispatcher):




