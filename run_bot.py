from aiogram import Dispatcher

import logging

from bot import TelegramBot
from setup import setup_everything
from handlers import register_all_handlers


def main(dp: Dispatcher) -> None:

    logging.basicConfig(level=logging.INFO)
    setup_everything(TelegramBot.executor)
    register_all_handlers(dp)
    TelegramBot.executor.start_polling()


if __name__ == '__main__':
    main(TelegramBot.dp)
