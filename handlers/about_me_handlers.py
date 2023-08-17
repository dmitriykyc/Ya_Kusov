from aiogram import Dispatcher, types
from handlers.texts.about_me_texts import about_me

def register_aboute_me_handlers(dp: Dispatcher):
    @dp.message_handler(text='🎯Моё увлечение')
    async def about_me_func(message: types.Message):
        await message.answer(about_me)