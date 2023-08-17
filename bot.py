import asyncio
import os
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from handlers.about_me_handlers import register_aboute_me_handlers
from handlers.photo_nandlers import register_photo_handlers
from handlers.start_handler import register_start_handlers
from handlers.unknown_mess_handler import register_unknown_mess_handler
from handlers.voices_handlers import register_voices_handler


load_dotenv()
logging.basicConfig(level=logging.INFO, filename="YaKusov.log",
                    format=":--> %(asctime)s %(levelname)s %(message)s")

def register_all_middlewares(dp):
    pass


def register_all_filters(dp):
    pass


def register_all_handlers(dp):
    register_start_handlers(dp)
    register_photo_handlers(dp)
    register_aboute_me_handlers(dp)
    register_voices_handler(dp)
    register_unknown_mess_handler(dp)

async def main():
    bot = Bot(token=os.getenv("TOKEN"), parse_mode='HTML')
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)
    # await dp.bot.send_message(354585871, 'YaBot')

    # start
    try:
        logging.info('Bot srarted')
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")