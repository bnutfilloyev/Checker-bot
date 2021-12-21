from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from utils.db_api.mongo import users_db
import datetime
import pandas as pd


@dp.message_handler(commands='get_excel')
async def bot_echo(message: types.Message):
    with open('handlers/users/load.csv', 'r+') as f:
        name = list(users_db.find_one().keys())
        # print(','.join(name))
        f.write(','.join(name))
        f.write('\n')
        for i in users_db.find():
            name = list(i.values())
            text = []

            for j in name:
                text.append(str(j))

            # print(','.join(text))
            f.write(','.join(text))
            f.write('\n')

    read_file = pd.read_csv(r'handlers/users/load.csv')
    read_file.to_excel(r'handlers/users/load.xlsx', index=None, header=True)

    with open('handlers/users/load.xlsx', 'rb') as f:
        await message.answer_document(f)
