from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Начальная клавиатура
b = InlineKeyboardButton(text='Отправить фото', callback_data='send_photo')
b1 = InlineKeyboardButton(text='О боте', callback_data='about_bot')

kb_client_start = InlineKeyboardMarkup(row_width=2)
kb_client_start.add(b, b1)











