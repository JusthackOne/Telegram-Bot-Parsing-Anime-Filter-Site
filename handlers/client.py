import asyncio

from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, File, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BotBlocked

from create_bot import dp, bot
from data_base import sqlite_db


a_inline = InlineKeyboardMarkup()
a_reply = ReplyKeyboardRemove()





# Регистрация хэндрелов
#ef register_handlers_client(dp: Dispatcher):




