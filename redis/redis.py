from typing import Final

from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from configuration import EnvironmentKeys


class Storage:

    FSM_STORAGE: Final = RedisStorage2(**EnvironmentKeys.REDIS_SETTINGS)

    @staticmethod
    async def redis_shutdown(dispatcher: Dispatcher) -> None:

        await dispatcher.storage.close()
        await dispatcher.storage.wait_closed()
