from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

confirmation = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "📝 O'zgartirish", callback_data="edit")]
    ]
)

deliver = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "Yetgazib beringdi ✅", callback_data="deliver")]
    ]
)