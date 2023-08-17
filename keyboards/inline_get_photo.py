from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_inline_photo():
    inline_get_photo = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton(text='👽Фото со школы', callback_data='get_photo_school')
    inline_get_photo.add(but1)
    return inline_get_photo
