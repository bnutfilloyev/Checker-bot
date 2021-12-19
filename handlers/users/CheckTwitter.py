from re import search

from aiogram import types

from data import texts
from data.config import TWITTER_USERNAME
from keyboards.default.next_button import next

from loader import dp
from states.States import Form
from utils.db_api.mongo import users_db

check = r'^@?(\w){1,15}$'

@dp.message_handler(text='⏩next', state=Form.GetTwitter)
async def get_facebook(msg: types.Message):
    await msg.answer(text=texts.text['twitter_text'].format(msg.from_user.first_name, TWITTER_USERNAME), disable_web_page_preview=True)
    await Form.CheckTwitter.set()

@dp.message_handler(state=Form.CheckTwitter)
async def check_instagram(msg: types.Message):
    twitter_account = msg.text
    if search(check, twitter_account):
        users_db.update_one({'telegram_id': msg.from_user.id}, {
            "$set": {
                'invite_twitter': twitter_account
            }
        }, upsert=True)

        await msg.reply(text=texts.text['twitter_accept'], reply_markup=next)
        await Form.GetDiscord.set()
    else:
        await msg.reply(text=texts.text['discord_repeat'])