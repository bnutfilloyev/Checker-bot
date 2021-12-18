from aiogram import types

from data import texts
from data.config import TWITTER_USERNAME
from keyboards.default.next_button import next

from loader import dp
from states.States import Form


@dp.message_handler(text='⏩next', state=Form.GetTwitter)
async def get_facebook(msg: types.Message):
    await msg.answer(text=texts.text['twitter_text'].format(msg.from_user.first_name, TWITTER_USERNAME), disable_web_page_preview=True)
    await Form.CheckTwitter.set()

@dp.message_handler(state=Form.CheckTwitter)
async def check_instagram(msg: types.Message):
    twitter_account = msg.text
    await msg.reply(text=twitter_account, reply_markup=next)
