import asyncio

from contextlib import suppress
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from create_bot import dp, bot
from data_base import sqlite_db


a_inline = InlineKeyboardMarkup()
a_reply = ReplyKeyboardRemove()

group_admin = -886166071

#async def start


# Регистрация хэндрелов
#def register_handlers_admin(dp: Dispatcher):
