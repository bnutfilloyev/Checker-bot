from aiogram.dispatcher.filters.state import StatesGroup, State

class Form(StatesGroup):
    CheckTelegram = State()
    GetInstagram = State()
    CheckInstagram = State()
    GetFacebook = State()
    CheckFacebook = State()
    GetTwitter = State()
    CheckTwitter = State()
    GetDiscord = State()
    CheckDiscord = State()
    GetYoutube = State()
    CheckYoutube = State()