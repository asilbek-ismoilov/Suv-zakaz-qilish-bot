from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Zakas qilish 🛎")],
    ],
    resize_keyboard=True,
)

num_water = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3"), KeyboardButton(text="4")],
        [KeyboardButton(text="5"), KeyboardButton(text="6"), KeyboardButton(text="7"), KeyboardButton(text="8")],
        [KeyboardButton(text="9"), KeyboardButton(text="10"), KeyboardButton(text="12"), KeyboardButton(text="15")],
    ],
    resize_keyboard=True,
)
