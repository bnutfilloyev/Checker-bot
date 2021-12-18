from aiogram.dispatcher.filters.state import StatesGroup, State

class Form(StatesGroup):
    CheckTelegram = State()
    GetInstagram = State()
    CheckInstagram = State()