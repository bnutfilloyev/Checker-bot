from aiogram import types

from data import texts
from data.config import FACEBOOK_USERNAME
from keyboards.default.next_button import next

from loader import dp
from states.States import Form

from re import search

from utils.db_api.mongo import users_db

check = r'(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?'

@dp.message_handler(text='⏩next', state=Form.GetFacebook)
async def get_facebook(msg: types.Message):
    await msg.answer(text=texts.text['facebook_text'].format(msg.from_user.first_name, FACEBOOK_USERNAME), disable_web_page_preview=True)
    await Form.CheckFacebook.set()

@dp.message_handler(state=Form.CheckFacebook)
async def check_instagram(msg: types.Message):
    facebook_account = msg.text
    if search(check, facebook_account):
        users_db.update_one({'telegram_id': msg.from_user.id}, {
            "$set":{
                'invite_facebook': facebook_account
            }
        }, upsert=True)

        await msg.reply(text=texts.text['facebook_accept'], reply_markup=next)
        await Form.GetTwitter.set()
    else:
        await msg.reply(text=texts.text['facebook_repeat_text'])
