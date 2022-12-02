import logging
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5696309371:AAHqtZMJ0qukDUWcdJBttMtXDPhK9Wpz1d8')
dp = Dispatcher(bot, storage=storage)