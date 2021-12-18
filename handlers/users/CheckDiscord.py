from aiogram import types

from data import texts
from data.config import FACEBOOK_USERNAME, DISCORD_USERNAME
from keyboards.default.next_button import next

from loader import dp
from states.States import Form
from utils.db_api.mongo import users_db


@dp.message_handler(text='⏩next', state=Form.GetDiscord)
async def get_link(msg: types.Message):
    await msg.answer(text=texts.text['discord_text'].format(msg.from_user.first_name, DISCORD_USERNAME), disable_web_page_preview=True)
    await Form.CheckDiscord.set()

@dp.message_handler(state=Form.CheckDiscord)
async def check_link(msg: types.Message):
    discord_username = msg.text

    users_db.update_one({'telegram_id': msg.from_user.id}, {
        "$set": {
            'invite_discord': discord_username
        }
    }, upsert=True)

    await msg.reply(text=texts.text['discord_accept'], reply_markup=next)
    await Form.GetYoutube.set()
