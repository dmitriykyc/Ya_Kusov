import logging
from aiogram import Dispatcher, types
from keyboards.reply_tasks import reply_main

def register_start_handlers(dp: Dispatcher):
    @dp.message_handler(commands='start')
    async def start_comm(message: types.Message):
        id_user = message.from_user.id
        first_name = message.from_user.first_name
        logging.info(f'{id_user} ({first_name}) --> Вошел в чат')
        await message.answer(f'Добро пожаловать!', reply_markup=reply_main)

    @dp.message_handler(text='🔗Ссылка на GitHub')
    async def get_url_github(message: types.Message):
        await message.answer('ссылка')
