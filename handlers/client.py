import asyncio

from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, ContentType, File, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BotBlocked

from Parsing.main import Driver
from keyboards import kb_client_start
from create_bot import dp, bot
from data_base import sqlite_db


a_inline = InlineKeyboardMarkup()
a_reply = ReplyKeyboardRemove()

class FMSSendPhoto(StatesGroup):
    sendphoto = State()
    parsingphoto = State()

# -------------Старт бота---------------------
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
            await bot.send_message(message.from_user.id, 'Приветствую вас в боте ANIMA!', reply_markup=kb_client_start)
    except :
        await message.reply('Общение с ботом через ЛС, напишите ему:\n www...')


# -------------Отправка фото---------------
@dp.callback_query_handler(lambda x: 'send_photo' == x.data)
async def send_photo_to_parsing(callback: types.CallbackQuery):
    await FMSSendPhoto.sendphoto.set()

    try: await callback.message.edit_text('Отправьте фото', reply_markup=a_inline)
    except: await callback.message.answer('Отправьте фото', reply_markup=a_inline)
    finally: await callback.answer()
# Парсинг
@dp.message_handler(content_types=['photo'], state = FMSSendPhoto.sendphoto)
async def parsing_photo(message: types.Message, state: FSMContext):
    await FMSSendPhoto.next()

    try:
        await message.answer('Начинаю парсинг, ждите')

        photoSize: PhotoSize = message.photo[-1]
        file_info = await bot.get_file(photoSize.file_id)
        fileExt = file_info.file_path.split(".")[-1]
        url_photo = "photo_original/" + photoSize.file_unique_id + '.' + fileExt
        await message.photo[-1].download(url_photo)
    except: return

    r = Driver()
    Parsing =  r.start_parsing(url_photo)

    if Parsing == True:
        url_photo_parsing = 'photo_parsing/' + url_photo.replace('photo_original/', '').replace('jpg', 'png')
        await bot.send_photo(message.from_user.id, types.InputFile(url_photo_parsing))
    else:
        await message.answer('Ой, что то произошло не так, попробуйте ещё раз')

    await state.finish()






# Регистрация хэндрелов
#ef register_handlers_client(dp: Dispatcher):




