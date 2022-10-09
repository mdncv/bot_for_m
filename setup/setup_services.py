from aiogram import Dispatcher
from aiogram.utils.executor import Executor

from auxiliary_logic.quiz_supply import cheers_table_add_default_entries
from orm import ORM
from redis import Storage


async def services_startup(dispatcher: Dispatcher) -> None:

    await ORM.orm_init()
    await cheers_table_add_default_entries()


async def services_shutdown(dispatcher: Dispatcher) -> None:

    await ORM.orm_shutdown()
    await Storage.redis_shutdown(dispatcher)


def setup_everything(executor: Executor) -> None:

    executor.on_startup(services_startup)
    executor.on_shutdown(services_shutdown)
