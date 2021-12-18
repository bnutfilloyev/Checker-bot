from aiogram import types

from data import texts
from data.config import FACEBOOK_USERNAME
from keyboards.default.next_button import next

from loader import dp
from states.States import Form


@dp.message_handler(text='⏩next', state=Form.GetFacebook)
async def get_facebook(msg: types.Message):
    await msg.answer(text=texts.text['facebook_text'].format(msg.from_user.first_name, FACEBOOK_USERNAME), disable_web_page_preview=True)
    await Form.CheckFacebook.set()

@dp.message_handler(state=Form.CheckFacebook)
async def check_instagram(msg: types.Message):
    facebook_account = msg.text
    await msg.reply(text=facebook_account, reply_markup=next)
    await Form.GetTwitter.set()
