from typing import Final

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import Executor

from configuration import EnvironmentKeys
from redis import Storage


class TelegramBot:
    bot: Final = Bot(token=EnvironmentKeys.TELEGRAM_BOT_TOKEN)
    dp: Final = Dispatcher(bot, storage=Storage.FSM_STORAGE)
    executor: Final = Executor(dp)
