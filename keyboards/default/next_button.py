from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

next = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⏩NEXT')
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)