from aiogram import Dispatcher, types

from keyboards.inline_voices import get_voices_buttons

def register_voices_handler(dp: Dispatcher):
    @dp.message_handler(text='🔉Мои войсы')
    async def my_voice(message: types.Message):
        await message.answer('Какой воис вы хотите послушать?', 
            reply_markup=get_voices_buttons())

    @dp.callback_query_handler(text='what_gpt')
    async def gpt_answer(call: types.CallbackQuery):
        await call.answer()
        await call.message.answer_voice('AwACAgIAAxkBAANMZN4jKfrrojByHBBNaQT5Ayq4z_0AAt81AALYmPlKSmKNZn2zP8swBA')

    @dp.callback_query_handler(text='SQL_NOSQL')
    async def gpt_answer(call: types.CallbackQuery):
        await call.answer()
        await call.message.answer_voice('AwACAgIAAxkBAANOZN4j0RGmHikW7k7QMbuHhwgMIY8AAu41AALYmPlKrcxK8GWzn38wBA')

    @dp.callback_query_handler(text='my_love')
    async def gpt_answer(call: types.CallbackQuery):
        await call.answer()
        await call.message.answer_voice('AwACAgIAAxkBAANRZN4j9hir_BC_rMhm0pAm30OHe0oAAvQ1AALYmPlKabF_AAG7ZMChMAQ')



