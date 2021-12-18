import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data import texts
from data.config import CHANNELS
from keyboards.default.start_button import accept_button
from keyboards.inline.subscription import check_button
from keyboards.default.next_button import next
from states.States import Form
from utils.misc import subscription

from loader import dp, bot

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(texts.text['start_text'].format(message.from_user.full_name), reply_markup=accept_button)


@dp.message_handler(text="👍 I'm ready to submit my details")
async def check_telegram(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
    await message.answer(f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)
    await Form.CheckTelegram.set()

@dp.callback_query_handler(text="check_subs", state=Form.CheckTelegram)
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    next_check = True
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅ <b>{channel.title}</b> You have subscribed to the channel!\n\n"
            await Form.GetInstagram.set()
        else:
            next_check = False
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> You are not subscribed to the channel."
                       f"<a href='{invite_link}'>Subscribe</a>\n\n")
    if next_check:
        await call.message.answer(result, reply_markup=next, disable_web_page_preview=True)
    else:
        await call.message.answer(result, reply_markup=check_button, disable_web_page_preview=True)

