from aiogram import Dispatcher, types
from keyboards.inline_get_photo import get_inline_photo

def register_photo_handlers(dp: Dispatcher):
    @dp.message_handler(text='🤠Посмотреть фотографии')
    async def get_first_photo(message: types.Message):
        await message.answer_photo(
            photo='AgACAgIAAxkBAAMiZNzHFcgAAccSRbaiQ-_w-Avdi7OfAAImzjEblIToSjDOORcBEZBlAQADAgADeQADMAQ', 
            caption='Вот так я выгляжу сейчас', reply_markup=get_inline_photo())

    @dp.callback_query_handler(text='get_photo_school')
    async def choose_task(call: types.CallbackQuery):
        await call.answer()
        await call.message.answer_photo(
            photo='AgACAgIAAxkBAAMoZNzHs3OEo3YD0LWyDa4QG6AIDyUAAifOMRuUhOhKYtodHn1dtJQBAAMCAAN4AAMwBA', 
            caption='А это школьная...')

