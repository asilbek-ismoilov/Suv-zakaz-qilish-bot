from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
kv = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Lokatsi 📍', request_location=True)]
    ],
    resize_keyboard=True
)

