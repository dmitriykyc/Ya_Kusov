import logging
from aiogram import Dispatcher, types

def register_unknown_mess_handler(dp: Dispatcher):
    @dp.message_handler(content_types=[types.ContentType.ANY])
    async def unknown_ness(message: types.Message):
        logging.info(f'Неизвестное сообщение: {message}')
        text = 'К сожалению, я не знаю такой команды🙂'
        await message.reply(text)

