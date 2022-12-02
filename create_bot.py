import logging
import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=5768961788:AAFCh-6gvsfpMsUVhm3JHX7I_DvxKb6-3fM)
dp = Dispatcher(bot, storage=storage)