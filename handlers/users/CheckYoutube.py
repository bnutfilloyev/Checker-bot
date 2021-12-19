from aiogram import types

from data import texts
from data.config import FACEBOOK_USERNAME, DISCORD_USERNAME, YOUTUBE_USERNAME
from keyboards.default.next_button import next

from aiogram.dispatcher import FSMContext
from loader import dp
from states.States import Form
from re import search

from utils.db_api.mongo import users_db

check = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

@dp.message_handler(text='⏩next', state=Form.GetYoutube)
async def get_link(msg: types.Message):
    await msg.answer(text=texts.text['youtube_text'].format(msg.from_user.first_name, YOUTUBE_USERNAME), disable_web_page_preview=True)
    await Form.CheckYoutube.set()

@dp.message_handler(state=Form.CheckYoutube)
async def check_link(msg: types.Message, state: FSMContext):
    youtube = msg.text
    if search(check, youtube):
        users_db.update_one({'telegram_id': msg.from_user.id}, {
            "$set":{
                'invite_youtube': youtube,
                'all_check': True
            }
        }, upsert=True)
        await msg.reply(text=texts.text['final_text'])
        await state.finish()
    else:
        await msg.reply(text=texts.text['youtube_repeat'])
