from aiogram import types

from data import texts
from data.config import YOUTUBE_USERNAME
from aiogram.dispatcher import FSMContext
from loader import dp
from states.States import Form
from re import search

from utils.db_api.mongo import users_db

check = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
wallet = r'^0x[a-fA-F0-9]{40}$'

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
                'invite_youtube': youtube
            }
        }, upsert=True)

        walletcheck = users_db.find_one({'telegram_id': msg.from_user.id})
        try:
            print(walletcheck['wallet'])
            await msg.reply(text=texts.text['bye_text'])
            await state.finish()
        except:
            await msg.reply(text=texts.text['final_text'])
            await Form.GetWallet.set()
    else:
        await msg.reply(text=texts.text['youtube_repeat'])


@dp.message_handler(state=Form.GetWallet)
async def get_wallet(msg: types.Message, state: FSMContext):
    wallet_text = msg.text
    if search(wallet, wallet_text):
        users_db.update_one({'telegram_id': msg.from_user.id}, {
            "$set": {
                'wallet': wallet_text,
                'all_check': True
            }
        }, upsert=True)
        await msg.reply(text=texts.text['bye_text'])
        await state.finish()
    else:
        await msg.reply(text=texts.text['final_text'])