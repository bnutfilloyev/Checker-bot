from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

accept_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👍 I'm ready to submit my details")
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)