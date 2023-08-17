from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_voices_buttons():
    inline_voices_but = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton(text='💾 GPT это', callback_data='what_gpt')
    but2 = InlineKeyboardButton(text='📊 SQL vs NoSQL', callback_data='SQL_NOSQL')
    but3 = InlineKeyboardButton(text='❤️ История любви', callback_data='my_love')
    inline_voices_but.add(but1, but2, but3)
    return inline_voices_but