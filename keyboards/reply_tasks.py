from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_main = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🤠Посмотреть фотографии')],
            [KeyboardButton(text='🎯Моё увлечение')],
            [KeyboardButton(text='🔉Мои войсы')],
            [KeyboardButton(text='🔗Ссылка на GitHub')]
        ], resize_keyboard=True
    )