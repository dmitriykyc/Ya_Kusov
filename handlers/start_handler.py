import logging
from aiogram import Dispatcher, types
from keyboards.reply_tasks import reply_main
from handlers.texts.start_texts import start_message

def register_start_handlers(dp: Dispatcher):
    @dp.message_handler(commands='start')
    async def start_comm(message: types.Message):
        id_user = message.from_user.id
        first_name = message.from_user.first_name
        logging.info(f'{id_user} ({first_name}) --> Вошел в чат')
        await message.answer(start_message, reply_markup=reply_main)

    @dp.message_handler(text='🔗Ссылка на GitHub')
    async def get_url_github(message: types.Message):
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton('🔗Ссылка на GitHub', 
            url="https://github.com/dmitriykyc/Ya_Kusov")
        keyboard.add(but1)
        await message.answer('Чтобы перейти на GitHub, нажмите ' \
            '<a href="https://github.com/dmitriykyc/Ya_Kusov">сюда</a>\n\n' \
            'Или на кнопку ниже👇', reply_markup=keyboard)
